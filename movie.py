current_movies = { 'Frozen 2' : '11:00am',
                                 ' Raya and the last dragon' : '1:00pm',
                                 'Mulan' : '3:00pm',
                                 'Moana' : '5:00 pm '}

print('We are showing the following movies:')


for key in current_movies:
    print(key)
movie = input('what movie would you like the showtime for?\n')
showtime = current_movies.get(movie)

if showtime == None:
    print('This movie is not playing')
else:
    print(movie,'is playing at', showtime)

