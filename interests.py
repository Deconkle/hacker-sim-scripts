interests = {
    "Family and Relationships": ['Dating','Family','Fatherhood','Friendship','Marriage','Motherhood','Parenting','Weddings'],
    "Shopping and Fashion": ['Clothing','Cosmetics','Coupons','Dresses','Fragrances','Handbags','Jewelry','Malls','Shoes','Sunglasses','Tattoos','Toys'],
    'Food and Drink': ['Baking','Barbecue','Beer','Chocolate','Coffee','Coffeehouses','Desserts','Juice','Pizza','Recipes','Tea','Veganism','Wine'],
    "Business": ['Advertising','Agriculture','Architecture','Aviation','Banking','Business','Construction','Design','Economics','Engineering','Design','Entrepreneurship','Finance','Investment','Insurance','Management','Marketing','Online','Retail','Sales','Science'],
    "Entertainment": ['Bars','Books','Comics','Concerts','Dancehalls','Documentary','Festivals','Games','Literature','Magazines','Manga','Movies','Music','Newspapers','Nightclubs','Parties','Plays','Poker','Talkshows','Theatre']
}
# interest_list = [Marketing,Documentary,Engineering,Aviation,Literature,Business,Manga,Online,Construction,Plays]
def get_working_account_type(interest_list):
    interest_count = {}
    for interest_type in interests:
        interest_count[interest_type] = 0
        for interest in interests[interest_type]:
            if interest in interest_list:
                interest_count[interest_type] += 1
    largest_interest = [interest for interest in sorted(interest_count, key=interest_count.get, reverse=True)][0]
    print("You need a "+largest_interest+" account.")
    #return interest_count
