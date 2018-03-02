 # -*- coding: utf-8 -*
import fresh_tomatoes
import media

# spider_man,redemption,blade是调用Movie生成的实例
spider_man=media.Movie('Spider-Man','https://i.ytimg.com/vi/K4zm30yeHHE/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCZOvOupXYdQQVMQuIwHCnGSlk8yQ','https://www.youtube.com/watch?v=K4zm30yeHHE')
redemption=media.Movie('The Shawshank Redemption','https://i.ytimg.com/vi/qQIQVPNcB_Q/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLDH4nB7kVo0gqu2eSDira2ANfVqVg','https://www.youtube.com/watch?v=accOHNw_qX8')
blade=media.Movie('Blade The Series','https://i.ytimg.com/vi/uMNL4h8hZEs/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCtw8MR-BV89BtMIwB3QJe77I71Iw','https://www.youtube.com/watch?v=uMNL4h8hZEs')

# 将生成的实例放到movies列表中
movies=[spider_man,redemption,blade]

# 调用fresh_tomatoes模块的open_movies_page，传入movies列表，生成可以浏览的网页
fresh_tomatoes.open_movies_page(movies)

