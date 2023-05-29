string1string1 = "This is a test"
string_one = 'I am a string'
string_two= 'I am a test'

if( string_one.endswith('test') or string_two.endswith('test')):
    print('found test')
else:
     print('no test')

     nums = [1, 10, 100,1000, 2, 20, 200, 2000]
for num in nums:
     if(num>100):
          print('large', num)
     else:
          print('Not Large:', num)

          client  = {
               'username': 'user_one',
               'age' : 22,
               'friends' : ['friend one', 'frind two', 'friend three']
          }

          print (client ['username'])
          print(client['age'])
          for friend in client['friends']:
             print(friend)

