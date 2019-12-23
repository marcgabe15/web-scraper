# -*- coding: utf-8 -*-
import scrapy


class Popular_Songs(scrapy.Spider):
    name = 'reviews'
    start_urls = ['https://www.amazon.com/CuteKing-Weighted-Blanket-Individual-Weighing/product-reviews/B07GQZ4ZZ1/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    def parse(self, response):
        for review in response.xpath('//div[@data-hook="review"]'):
            yield {
                'author': review.xpath('.//div/div/div/a/div/span/text()').extract(),
                'rating': review.xpath('.//div/div/div[2]/a/i/span/text()').extract(),
                'review_date': review.xpath('.//div/div/span[@data-hook="review-date"]/text()').extract(),
                'review_title': review.xpath('.//div/div/div[2]/a[@data-hook="review-title"]/span/text()').extract(),
                'review': review.xpath('.//div/div/div/span[@data-hook="review-body"]/span/text()').extract(),
                'support_number': review.xpath('.//div/div/div[5]/div/span/div/span/text()').get()
            }
        next_page = response.xpath('//div[@data-hook="pagination-bar"]/ul/li[@class="a-last"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
