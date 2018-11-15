tweeter_date = 'created_at'
tweeter_text = 'text'
tweeter_user = 'user'
tweeter_user_followers_count = 'followers_count'
tweeter_user_friends_count = 'friends_count'
tweeter_user_current_post_retweet_number = 'retweet_count'
tweeter_user_current_post_like_number = 'favorite_count'


class ParseTweet():
    tweets = ""

    def __init__(self, tweets):
        self.tweets = tweets

    def parse_tweets(self):
        d = {}
        for data in self.tweets:
            d['user'] = data[tweeter_user]
            d['date'] = data[tweeter_date]
            d['text'] = data[tweeter_text]
            d['retweets_count'] = data[tweeter_user_current_post_retweet_number]
        return d
