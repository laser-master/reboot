#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import os

def fetch_and_parse(url, filename):
    """Fetch URL and parse with proper encoding"""
    try:
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        response = requests.get(url, headers=headers, timeout=30, verify=False)
        response.raise_for_status()
        
        # Try to detect encoding
        response.encoding = response.apparent_encoding or 'utf-8'
        
        # Save raw content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Successfully fetched {url}")
        print(f"Saved to {filename}")
        print(f"Content length: {len(response.text)} characters")
        
        return response.text
        
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_product_categories(html_content):
    """Parse product categories from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    categories = []
    
    # Look for product category links and info
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href and ('product' in href.lower() or 'category' in href.lower() or 'laser' in href.lower()):
            text = link.get_text(strip=True)
            if text and len(text) > 2:  # Filter out very short text
                categories.append({
                    'text': text,
                    'href': href,
                    'full_url': href if href.startswith('http') else f"https://www.redsail-laser.com{href}"
                })
    
    return categories

def extract_product_links(sitemap_content):
    """Extract product links from sitemap"""
    products = []
    
    # Use regex to find product URLs
    pattern = r'<loc>(https://www\.redsail-laser\.com/products[^<]+)</loc>'
    matches = re.findall(pattern, sitemap_content)
    
    for url in matches:
        products.append(url)
    
    return products

def main():
    base_url = "https://www.redsail-laser.com"
    
    # URLs to fetch
    urls_to_fetch = [
        (f"{base_url}/productcategory.html", "productcategory.html"),
        (f"{base_url}/products.html", "products.html"),
        (f"{base_url}/products/Laser-Engraver.html", "laser-engraver.html"),
        (f"{base_url}/products/Laser-Cutter.html", "laser-cutter.html"),
        (f"{base_url}/products/Laser-Cutter-and-Engraver.html", "laser-cutter-engraver.html"),
    ]
    
    # Create products directory
    os.makedirs("cnc-laser-cn/products", exist_ok=True)
    
    # Fetch main pages
    all_content = {}
    for url, filename in urls_to_fetch:
        content = fetch_and_parse(url, filename)
        if content:
            all_content[filename] = content
    
    # Parse sitemap
    print("\n=== PARSING SITEMAP ===")
    try:
        with open("sitemap.xml", 'r', encoding='utf-8') as f:
            sitemap_content = f.read()
        
        product_links = extract_product_links(sitemap_content)
        print(f"Found {len(product_links)} product URLs in sitemap:")
        for link in product_links[:10]:  # Show first 10
            print(f"  - {link}")
        if len(product_links) > 10:
            print(f"  ... and {len(product_links) - 10} more")
            
        # Save product links
        with open("cnc-laser-cn/products/product_urls.json", 'w', encoding='utf-8') as f:
            json.dump(product_links, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
    
    # Parse categories
    print("\n=== PARSING PRODUCT CATEGORIES ===")
    if "productcategory.html" in all_content:
        categories = parse_product_categories(all_content["productcategory.html"])
        print(f"Found {len(categories)} potential categories:")
        for cat in categories[:10]:  # Show first 10
            print(f"  - {cat['text']} -> {cat['href']}")
        if len(categories) > 10:
            print(f"  ... and {len(categories) - 10} more")
            
        # Save categories
        with open("cnc-laser-cn/products/categories.json", 'w', encoding='utf-8') as f:
            json.dump(categories, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()