import json

from django.test       import TestCase
from django.test       import Client
from django.db.models  import Avg

from user.models       import User, Review, Review_Star
from restaurant.models import(
    Top_List, 
    Topic,
    Topic_Top_list,
    Restaurant_image,
    Restaurant,
    Location_city,
    Location_state,
    Location_road,
    Price,
    Holiday,
    Food
    )

class MainTopList(TestCase):
    def setUp(self):
        client = Client()
        
        Topic.objects.create(
            id = 1,
            title = '믿고 보는 맛집 리스트'
        )
        Top_List.objects.create(
            id = 1,
            title = '2020 제주 인기 맛집 TOP 60',
            description = '제주의 인기 맛집만 쏙쏙 골라 모았다!!!',
            image = 'https://mp-seoul-image-production-s3.mangoplate.com/keyword_search/meta/pictures/7zsdxmpu4kauzpk7.jpg'
        )
        Topic_Top_list.objects.create(
            id = 1,
            top_list_id = 1,
            topic_id = 1
        )
        Food.objects.create(
            id = 1,
            category = '한식'
        )
        Location_city.objects.create(
            id = 1,
            city = '서울'
        )
        Location_state.objects.create(
            id = 1,
            state = '은평구'
        )
        Location_road.objects.create(
            id = 1,
            road = '녹번동'
        )
        Holiday.objects.create(
            id = 1,
            holiday = '월'
        )
        Price.objects.create(
            id = 1,
            price_range = '만원 미만'
        )
        Restaurant.objects.create(
            id = 1,
            name              = '테스트 레스토랑',
            price_range_id    = 1,
            food_id           = 1,
            location_city_id  = 1,
            location_state_id = 1,
            location_road_id  = 1,
            location_detail   = '12-1번지',
            holiday_id        = 1
        )
        Restaurant_image.objects.create(
            id = 1,
            restaurant_id = 1,
            images        = 'https://mp-seoul-image-production-s3.mangoplate.com/10226_1439659099246'
        )
        Topic_Restaurant.objects.create(
            id = 1,
            topic_id      = 1,
            restaurant_id = 1
        )
        User.objects.create(
            id = 1,
            nick_name = 'test',
            email     = 'test@naver.com',
            password  = 'test1234'
        )
        Review_Star.objects.create(
            id = 1,
            star    = 5,
            content = '맛있다' 
        )
        Review.objects.create(
            id = 1,
            user_id = 1,
            restaurant_id = 1,
            content = '맛있습니다',
            review_star_id = 1
        )
 

    def tearDown(self):
        Topic.objects.all().delete()
        Top_List.objects.all().delete()
        Topic_Top_list.objects.all().delete()
        Topic_Restaurant.objects.all().delete()
        Review.objects.all().delete()
        Review_Star.objects.all().delete()
        User.objects.all().delete()
        Restaurant_image.objects.all().delete()
        Restaurant.objects.all().delete()
        Food.objects.all().delete()
        Location_road.objects.all().delete()
        Location_state.objects.all().delete()
        Location_city.objects.all().delete()
        Holiday.objects.all().delete()
        


    def test_TopTopic(self):
        client = Client()

        response = client.get('/restaurant/topic/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                'title' : '믿고 보는 맛집 리스트',
                'top_list' : [
                    {
                        'id' : 1,
                        'title' : '2020 제주 인기 맛집 TOP 60',
                        'description' : '제주의 인기 맛집만 쏙쏙 골라 모았다!!!',
                        'image' : 'https://mp-seoul-image-production-s3.mangoplate.com/keyword_search/meta/pictures/7zsdxmpu4kauzpk7.jpg'
                    }
                ]
            }
        )

    def test_restaurant(self):
        client = Client()
        response = client.get('/restaurant/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'title':'믿고 보는 맛집 리스트',
            'restaurant_list':[{
                'id'    : 1,
                'name'  : '테스트 레스토랑',
                'state' : '은평구',
                'food'  : '한식',
                'image' : 'https://mp-seoul-image-production-s3.mangoplate.com/10226_1439659099246',
                'grade' : 5.0
            }]
        })

    def test_restaurant_not_exists(self):
        client = Client()
        response = client.get('/restaurant/3')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message":"DOES_NOT_EXIST_TOPIC"})

class DetailTopImageBar(TestCase):
    def setUp(self):
        client = Client()

        Location_city.objects.create(
            id = 1,
            city = '서울시'
        )

        Location_state.objects.create(
            id = 1,
            state = '동작구',
            city_id = 1
        )
        
        Location_road.objects.create(
            id = 1,
            road = '상도로',
            state_id = 1
        )

        Food.objects.create(
            id = 1,
            category = '치킨'
        )

        Price.objects.create(
            id = 1,
            price_range = '1만원'
        )

        Holiday.objects.create(
            id = 1,
            holiday = '일'
        )

        Restaurant.objects.create(
            id = 1,
            price_range_id = 1,
            food_id = 1,
            location_city_id = 1,
            location_state_id = 1,
            location_road_id = 1,
            location_detail = '14',
            holiday_id = 1
        )

        Restaurant_image.objects.create(
            id = 1,
            images ='https://mp-seoul-image-production-s3.mangoplate.com/keyword_search/meta/pictures/7zsdxmpu4kauzpk7.jpg',
            restaurant_id = 1
        )

    def test_detail_top_image(self):
        client = Client()

        response = client.get('/restaurant/1/topimage')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                'image' : [
                     'https://mp-seoul-image-production-s3.mangoplate.com/keyword_search/meta/pictures/7zsdxmpu4kauzpk7.jpg'   
                ]     
            }
        )

        def tearDown(self):
            Restaurant_image.objects.all().delete()
            Restaurant.objects.all().delete()
            Holiday.objects.all().delete()
            Location_road.objects.all().delete()
            Location_state.objects.all().delete()
            Location_city.objects.all().delete()
            Food.objects.all().delete()
            Price.objects.all().delete()

