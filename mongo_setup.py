from pymongo import MongoClient

client = MongoClient('mongodb+srv://ishaanvijaywargia:YU1WqZT2tVkkCP47@cluster0.twbtwun.mongodb.net/crop_recommendation?retryWrites=true&w=majority&appName=Cluster0') 

db = client['crop_recommendation']
forum_posts_collection = db['forum_posts']

post = {
    'title': 'Best crop for this season?',
    'content': 'I would like to know the best crop to grow in this season based on the weather and soil.',
    'comments': [],
    'created_at': '2024-11-17T10:00:00'
}

forum_posts_collection.insert_one(post) 
retrieved_post = forum_posts_collection.find_one({'title': 'Best crop for this season?'})
print(retrieved_post)
