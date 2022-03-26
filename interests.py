interests = {
    "Family and Relationships": ['Dating','Family','Fatherhood','Friendship','Marriage','Motherhood','Parenting','Weddings'],
    "Shopping and Fashion": ['Clothing','Cosmetics','Coupons','Dresses','Fragrances','Handbags','Jewelry','Malls','Shoes','Sunglasses','Tattoos','Toys'],
    'Food and Drink': ['Baking','Barbecue','Beer','Chocolate','Coffee','Coffeehouses','Desserts','Juice','Pizza','Recipes','Tea','Veganism','Wine'],
    "Business": ['Advertising','Agriculture','Architecture','Aviation','Banking','Business','Construction','Design','Economics','Engineering','Design','Entrepreneurship','Finance','Investment','Insurance','Management','Marketing','Online','Retail','Sales','Science'],
    "Entertainment": ['Bars','Books','Comics','Concerts','Dancehalls','Documentary','Festivals','Games','Literature','Magazines','Manga','Movies','Music','Newspapers','Nightclubs','Parties','Plays','Poker','Talkshows','Theatre']
} # this list was compiled by the community and posted to a steam guide.
# https://steamcommunity.com/sharedfiles/filedetails/?id=2645422003

# interest_list = ['Marketing','Documentary','Engineering','Aviation','Literature','Business','Manga','Online','Construction','Plays']
def get_working_account_type(interest_list):
    interest_count = {} # by the end this will look something like {"Family and Realtionships": 0, "Shopping and Fashion": 6, "Food and Drink": 4, "Business": 0, "Entertainment": 0}
    for interest_type in interests: # ['Family and Relationshiops', 'Shopping and Fashion', ETC]
        interest_count[interest_type] = 0 # init with zero
        for interest in interests[interest_type]: # loop through the values (['Dating', 'Family', 'Fatherhood', ETC])
            if interest in interest_list:
                interest_count[interest_type] += 1 # so that we can up when we match one.
    largest_interest = [interest for interest in sorted(interest_count, key=interest_count.get, reverse=True)][0] # Sort this dict by keys, set largest_interest to the key with the highest value.
    print("You need a "+largest_interest+" account.")
    #return interest_count
  
# ======= TODO / NOTICE =======
# At time of writing I only have 8.5 hours, but this script has never output a wrong result, this means I haven't bothered to add any error handling
# If OCR reads the text incorrectly, the line that was misread is simply ignored. If errors do start occuring, this lack of logging could cause frustration.
