#!/usr/bin/env python3
import argparse, os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from _common import save_raw, clean_slug

load_dotenv()
p=argparse.ArgumentParser(description='Scrape a public/authorized web page using Firecrawl.')
p.add_argument('--coach', required=True)
p.add_argument('url')
a=p.parse_args()
key=os.getenv('FIRECRAWL_API_KEY')
if not key:
    raise SystemExit('Set FIRECRAWL_API_KEY in .env')
app=FirecrawlApp(api_key=key)
try:
    result=app.scrape_url(a.url, formats=['markdown'])
except TypeError:
    result=app.scrape_url(a.url, params={'formats':['markdown']})
markdown=getattr(result, 'markdown', None)
if markdown is None and isinstance(result, dict):
    markdown=result.get('markdown') or (result.get('data') or {}).get('markdown')
if not markdown:
    raise SystemExit('No markdown returned. Check your Firecrawl SDK/API version.')
filename='web-'+str(abs(hash(a.url)))+'.md'
save_raw(clean_slug(a.coach), filename, markdown, {'source':a.url,'type':'web'})
print('saved', a.url)
