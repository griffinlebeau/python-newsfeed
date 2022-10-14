def format_date(date):
  return date.strftime('%m/%d/%y')
#expects to receive a datetime object and then 
#use the strftime() method to convert it to a string
#the %m/%d/%y format code will result in '01/01/20'

def format_url(url):
#removes all extraneous info from a URL string, leaving only the domain name
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word