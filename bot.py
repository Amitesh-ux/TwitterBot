# bot.py - Your Twitter Bot
import tweepy
import time
import random
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class TwitterBot:
    def __init__(self):
        """Initialize the bot with API credentials"""
        self.client = tweepy.Client(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
        print("🤖 Bot initialized!")
    
    def test_connection(self):
        """Test if the bot can connect to Twitter"""
        try:
            me = self.client.get_me()
            print(f"✅ Connected successfully as: {me.data.name}")
            print(f"Username: @{me.data.username}")
            return True
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            return False
    
    def post_tweet(self, message):
        """Post a single tweet"""
        try:
            response = self.client.create_tweet(text=message)
            print(f"✅ Tweet posted: {message}")
            return response
        except Exception as e:
            print(f"❌ Failed to post tweet: {e}")
            return None
    
    def search_and_like(self, keyword, count=5):
        """Search for tweets with keyword and like them"""
        try:
            # Search for tweets
            tweets = self.client.search_recent_tweets(
                query=keyword,
                max_results=count
            )
            
            if not tweets.data:
                print(f"No tweets found for '{keyword}'")
                return
            
            # Like each tweet
            for tweet in tweets.data:
                try:
                    self.client.like(tweet.id)
                    print(f"❤️ Liked tweet: {tweet.text[:50]}...")
                    time.sleep(1)  # Be nice to the API
                except Exception as e:
                    print(f"❌ Failed to like tweet: {e}")
                    
        except Exception as e:
            print(f"❌ Search failed: {e}")
    
    def search_and_retweet(self, keyword, count=3):
        """Search for tweets with keyword and retweet them"""
        try:
            tweets = self.client.search_recent_tweets(
                query=keyword,
                max_results=count
            )
            
            if not tweets.data:
                print(f"No tweets found for '{keyword}'")
                return
            
            for tweet in tweets.data:
                try:
                    self.client.retweet(tweet.id)
                    print(f"🔄 Retweeted: {tweet.text[:50]}...")
                    time.sleep(2)  # Be nice to the API
                except Exception as e:
                    print(f"❌ Failed to retweet: {e}")
                    
        except Exception as e:
            print(f"❌ Search failed: {e}")

# Main execution
if __name__ == "__main__":
    # Create bot instance
    bot = TwitterBot()
    
    # Test connection
    if bot.test_connection():
        print("\n🚀 Bot is ready! Choose an action:")
        print("1. Post a tweet")
        print("2. Like tweets about programming")
        print("3. Retweet Python content")
        
        # Example usage - uncomment what you want to try:
        
        # Post a tweet
        # bot.post_tweet("Hello World! My first Python bot is working! 🐍🤖 #coding")
        
        # Like tweets about programming
        # bot.search_and_like("python programming", count=3)
        
        # Retweet content about Python
        # bot.search_and_retweet("python tutorial", count=2)
        
        print("\n✨ Uncomment the actions you want to try in bot.py!")
    else:
        print("❌ Bot setup failed. Check your API keys.")