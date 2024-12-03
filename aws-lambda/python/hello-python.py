def lambda_handler(event, context):
   message = 'Hello {} !'.format(event['key1'])
   print("Hi")
   return {
       'message' : message
   }

   
