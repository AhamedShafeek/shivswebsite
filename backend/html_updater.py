import os
from bs4 import BeautifulSoup

class HTMLUpdater:
    def __init__(self):
        self.html_file = os.path.join(os.path.dirname(__file__), '..', 'index.html')
    
    def read_html(self):
        """Read the HTML file"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_html(self, content):
        """Write to the HTML file"""
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def update_reviews(self, reviews):
        """Update reviews section in HTML"""
        html_content = self.read_html()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the reviews container
        review_section = soup.find('section', class_='py-20 bg-gradient-to-b from-gray-50 to-white')
        if not review_section:
            return
        
        # Find the grid container for reviews
        grid_container = review_section.find('div', class_='grid grid-cols-1 md:grid-cols-3 gap-8')
        if not grid_container:
            return
        
        # Clear existing reviews
        grid_container.clear()
        
        # Add new reviews (max 3 for the main section)
        for review in reviews[:3]:
            review_card = self._create_review_card(review, soup)
            grid_container.append(review_card)
        
        # Update the "More Customer Reviews" section if it exists
        more_reviews_section = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6')
        if more_reviews_section and len(reviews) > 3:
            more_reviews_section.clear()
            for review in reviews[3:]:
                review_card = self._create_small_review_card(review, soup)
                more_reviews_section.append(review_card)
        
        self.write_html(str(soup))
    
    def _create_review_card(self, review, soup):
        """Create a review card element"""
        card_html = f'''
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl hover:-translate-y-1 border border-gray-100">
          <div class="p-8">
            <div class="flex justify-between items-start mb-6">
              <div class="flex items-center space-x-4">
                <div class="w-14 h-14 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white text-xl font-bold shadow-lg">
                  {review.get('initial', 'A')}
                </div>
                <div>
                  <h3 class="font-bold text-lg text-gray-900">{review.get('name', 'Anonymous')}</h3>
                  <p class="text-sm text-gray-500">{review.get('time', '3 months ago')}</p>
                </div>
              </div>
              <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" class="h-6">
            </div>
            <div class="flex mb-4">
              {''.join(['<span class="text-yellow-400 text-xl">★</span>' for _ in range(review.get('rating', 5))])}
            </div>
            <h4 class="font-bold text-lg mb-3 text-gray-900">"{review.get('title', '')}"</h4>
            <p class="text-gray-600 leading-relaxed mb-4">{review.get('content', '')}</p>
            {f'<span class="inline-block bg-green-100 text-green-700 px-4 py-2 rounded-full text-sm font-semibold"><span class="mr-2">✓</span>{review.get("badge", "")}</span>' if review.get('badge') else ''}
          </div>
        </div>
        '''
        return BeautifulSoup(card_html, 'html.parser')
    
    def _create_small_review_card(self, review, soup):
        """Create a small review card for the more reviews section"""
        card_html = f'''
        <div class="bg-white rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-lg hover:-translate-y-1 border border-gray-100">
          <div class="p-6">
            <div class="flex items-center space-x-3 mb-4">
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center text-white font-bold shadow">
                {review.get('initial', 'V')}
              </div>
              <div class="flex-1">
                <h4 class="font-bold text-gray-900">{review.get('name', 'Anonymous')}</h4>
                <div class="flex items-center space-x-2">
                  <div class="flex">
                    {''.join(['<span class="text-yellow-400 text-sm">★</span>' for _ in range(review.get('rating', 5))])}
                  </div>
                  <span class="text-xs text-gray-500">{review.get('time', '4 months ago')}</span>
                </div>
              </div>
              <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" class="h-4">
            </div>
            <p class="text-gray-600 text-sm leading-relaxed">"{review.get('content', '')}"</p>
          </div>
        </div>
        '''
        return BeautifulSoup(card_html, 'html.parser')
    
    def update_faqs(self, faqs):
        """Update FAQs section in HTML"""
        html_content = self.read_html()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find FAQ section - looking for the "Why Shiv's?" section
        faq_section = soup.find('section', class_='bg-white')
        if not faq_section:
            return
        
        # Find the container with FAQ items
        faq_container = faq_section.find('div', class_='space-y-4')
        if not faq_container:
            return
        
        # Clear existing FAQs
        faq_container.clear()
        
        # Add new FAQs
        for faq in faqs:
            faq_item = self._create_faq_item(faq, soup)
            faq_container.append(faq_item)
        
        self.write_html(str(soup))
    
    def _create_faq_item(self, faq, soup):
        """Create an FAQ item element"""
        faq_html = f'''
        <div class="border-b border-gray-200 pb-4">
          <button class="flex justify-between items-center w-full text-left py-4 focus:outline-none faq-question">
            <h3 class="text-xl font-semibold text-gray-900">{faq.get('question', '')}</h3>
            <svg class="w-6 h-6 transform transition-transform duration-200 faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
            </svg>
          </button>
          <div class="faq-answer hidden mt-2">
            <p class="text-gray-600 leading-relaxed">{faq.get('answer', '')}</p>
          </div>
        </div>
        '''
        return BeautifulSoup(faq_html, 'html.parser')
    
    def update_gallery(self, gallery_images):
        """Update gallery section in HTML"""
        html_content = self.read_html()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find gallery grid
        gallery_grid = soup.find('div', id='gallery-grid')
        if not gallery_grid:
            return
        
        # Clear existing images
        gallery_grid.clear()
        
        # Add new images
        for image in gallery_images:
            img_item = self._create_gallery_item(image, soup)
            gallery_grid.append(img_item)
        
        self.write_html(str(soup))
    
    def _create_gallery_item(self, image, soup):
        """Create a gallery image item"""
        img_html = f'''
        <div class="break-inside-avoid overflow-hidden shadow-md" data-category="{image.get('category', 'weddings')}">
            <img src="{image.get('url', '')}" alt="{image.get('alt', 'Gallery image')}" class="w-full h-auto transition-transform duration-300 ease-in-out hover:scale-105">
        </div>
        '''
        return BeautifulSoup(img_html, 'html.parser')
    
    def update_reels(self, reels):
        """Update reels/Instagram section in HTML"""
        html_content = self.read_html()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the Instagram embed section
        # Looking for section with embedded Instagram posts
        instagram_section = soup.find('section', id='instagram-posts')
        if not instagram_section:
            # Try to find by class or other identifier
            instagram_section = soup.find('section', class_='elfsight-app-')
            if not instagram_section:
                return
        
        # This depends on how Instagram embeds are structured in your HTML
        # For now, we'll create a simple embed container
        # You may need to adjust this based on your actual HTML structure
        
        self.write_html(str(soup))
    
    def _create_reel_embed(self, reel, soup):
        """Create an Instagram reel embed"""
        embed_html = f'''
        <div class="instagram-embed">
            <blockquote class="instagram-media" data-instgrm-permalink="{reel.get('embed_url', '')}" data-instgrm-version="14">
            </blockquote>
        </div>
        '''
        return BeautifulSoup(embed_html, 'html.parser')
