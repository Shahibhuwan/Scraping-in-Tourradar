import scrapy
from ..items import TourItem
import w3lib.html
class NepalTour(scrapy.Spider):
    name ="nepatour"
    pages_number=2
    start_urls=['https://www.tourradar.com/i/nepal-hiking-trekking?page=1']

    def parse(self, response):
        products =response.xpath('//div[@class="js-serp-tour-list list"]/ul/li')
        item=TourItem()
        for product in products:
            url_inside =product.xpath('div/a/@href').get()
            
            item['url'] =response.urljoin(url_inside)
            
            yield response.follow(url = item['url'], meta = {'item': item}, callback=self.parse_additional_info) 
        next_page= 'https://www.tourradar.com/i/nepal-hiking-trekking?page='+str(NepalTour.pages_number)        
        if NepalTour.pages_number<=30 :
            NepalTour.pages_number=NepalTour.pages_number+1
            print(NepalTour.pages_number)
            yield response.follow(next_page, callback=self.parse)

    def parse_additional_info(self, response):
  
        filename = response.url.split("/")[-1][:6] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        item = response.meta['item']
        item['duration']=response.xpath('//div[@class="ao-tour-above-fold__main"]/div[1]/text()').extract_first()
        item['rating']=w3lib.html.remove_tags(str(response.xpath('//div[@class="ao-tour-above-fold__main"]/div[2]/div/div/text()').extract_first()) +'('+ str(response.xpath('//div[@class="ao-tour-above-fold__main"]/div[2]/div/div[3]/text()').extract_first()))
    
        item['price'] =w3lib.html.remove_tags(response.xpath('//div[@class="ao-tour-above-fold__main-price"]').extract_first()).strip()
        
        item['citi'] = str(response.xpath('//li[@class="ao-common-carousel__item  "][1]/div/div/text()').extract_first()) +','+ str(response.xpath('//li[@class="ao-common-carousel__item  "][2]/div/div/text()').extract_first())+','+ str(response.xpath('//li[@class="ao-common-carousel__item  "][3]/div/div/text()').extract_first())+ ','+str(response.xpath('//li[@class="ao-common-carousel__item  "][4]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][5]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][6]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][7]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][8]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][9]/div/div/text()').extract_first())
        
        
            
        touroperator =response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[1]/dd/text()').extract_first()
        item['touroperator']=touroperator
        
        maxgroupsize=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[2]/dd/text()').extract_first()
        item['maxgroupsize'] = maxgroupsize
        physicalrating=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[3]/dd/text()').extract_first()
        item['physicalrating']=physicalrating
        age=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[4]/dd/text()').extract_first()
        item['age']=age
        operatedin=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[5]/dd/text()').extract_first()
        item['operatedin']=operatedin
        tourid=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[6]/dd/text()').extract_first()
        item['tourid'] = tourid

        name = response.xpath('//div[@class="ao-tour-above-fold__main"]/h1/text()').extract_first()
        item['name'] = name
        # if name is not None:
        #     item['name'] = name.strip()
        # else:
        #     item['name']=None

        
        item['day1']=response.xpath('//ol[@class="det"]/li[1]/span/text()').extract_first()
        item['day2']=response.xpath('//ol[@class="det"]/li[2]/span/text()').extract_first()
        item['day3']=response.xpath('//ol[@class="det"]/li[3]/span/text()').extract_first()
        item['day4']=response.xpath('//ol[@class="det"]/li[4]/span/text()').extract_first()
        item['day5']=response.xpath('//ol[@class="det"]/li[5]/span/text()').extract_first()
        item['day6']=response.xpath('//ol[@class="det"]/li[6]/span/text()').extract_first()
        item['day7']=response.xpath('//ol[@class="det"]/li[7]/span/text()').extract_first()
        item['day8']=response.xpath('//ol[@class="det"]/li[8]/span/text()').extract_first()
        item['day9']=response.xpath('//ol[@class="det"]/li[9]/span/text()').extract_first()
        item['day10']=response.xpath('//ol[@class="det"]/li[10]/span/text()').extract_first()
        item['day11']=response.xpath('//ol[@class="det"]/li[11]/span/text()').extract_first()
        item['day12']=response.xpath('//ol[@class="det"]/li[12]/span/text()').extract_first()
        item['day13']=response.xpath('//ol[@class="det"]/li[13]/span/text()').extract_first()
        item['day14']=response.xpath('//ol[@class="det"]/li[14]/span/text()').extract_first()
        
       
        yield item


         

#  duration = response.xpath('//div[@class="ao-tour-above-fold__main"]/div[1]/text()').extract_first()
        
#         if duration is not None:
#             item['duration']=duration.strip()
#         else:
#             item['duration']=None
#         rating = w3lib.html.remove_tags(str(response.xpath('//div[@class="ao-tour-above-fold__main"]/div[2]/div/div/text()').extract_first()) +'('+ str(response.xpath('//div[@class="ao-tour-above-fold__main"]/div[2]/div/div[3]/text()').extract_first()))
        
#         if rating is not None:
#             item['rating']=rating.strip()
#         else:
#             item['rating']=None
 
#         price =w3lib.html.remove_tags(response.xpath('//div[@class="ao-tour-above-fold__main-price"]').extract_first()).strip()
#         if price is not None:
#             item['price']=price.strip()
#         else:
#             item['price']=None

#         citi = str(response.xpath('//li[@class="ao-common-carousel__item  "][1]/div/div/text()').extract_first()) +','+ str(response.xpath('//li[@class="ao-common-carousel__item  "][2]/div/div/text()').extract_first())+','+ str(response.xpath('//li[@class="ao-common-carousel__item  "][3]/div/div/text()').extract_first())+ ','+str(response.xpath('//li[@class="ao-common-carousel__item  "][4]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][5]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][6]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][7]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][8]/div/div/text()').extract_first())+','+str(response.xpath('//li[@class="ao-common-carousel__item  "][9]/div/div/text()').extract_first())
        
#         if citi is not None:
#             item['citi'] = citi.strip()
#         else:
#             item['citi']=None

            
#         touroperator =response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[1]/dd/text()').extract_first()
       
#         if touroperator is not None:
#              item['touroperator']=touroperator.strip()
#         else:
#             item['name']=None

#         maxgroupsize=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[2]/dd/text()').extract_first()
        
#         if maxgroupsize is not None:
#             item['maxgroupsize'] = maxgroupsize.strip()
#         else:
#             item['maxgroupsize'] =None

#         physicalrating=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[3]/dd/text()').extract_first()
#         if physicalrating is not None:
#             item['physicalrating'] = physicalrating.strip()
#         else:
#             item['physicalrating']=None



#         age=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[4]/dd/text()').extract_first()
#         if age is not None:
#             item['age'] = age.strip()
#         else:
#             item['age']=None

    

#         operatedin=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[5]/dd/text()').extract_first()
#         if operatedin is not None:
#             item['operatedin'] = operatedin.strip()
#         else:
#             item['operatedin']=None

       
#         tourid=response.xpath('//dl[@class="ao-tour-above-fold__properties-list ao-tour-above-fold__properties-list--count-5"]/div[6]/dd/text()').extract_first()
#         if tourid is not None:
#             item['tourid'] = tourid.strip()
#         else:
#             item['tourid']=None

        
#         name = response.xpath('//div[@class="ao-tour-above-fold__main"]/h1/text()').extract_first()
#         if name is not None:
#             item['name'] = name.strip()
#         else:
#             item['name']=None
