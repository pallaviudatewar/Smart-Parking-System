import urllib,json
import urllib.request
import time
READ_API_KEY = '2UK1KWQOCN7YMJ2O'
CHANNEL_ID = 1150867
def main():
    conn = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print("http status code=%s" % (conn.getcode()))
    data =json.loads(response)
    print(data['field1'],data['created_at'])
    print(data['field2'],data['created_at'])
    print(data['field3'],data['created_at'])
    print(data['field4'],data['created_at'])

    if(data['field1'] == '1'):
        print("Parking 1 is unavailable")
    else:
        print("Parking 1 is available")
    time.sleep(15)

    if(data['field2'] == '1'):
        print("Parking 2 is unavailable")
    else:
        print("Parking 2 is available")
    time.sleep(15)

    if(data['field3'] == '1'):
        print("Parking 3 is unavailable")
    else:
        print("Parking 3 is available")
    time.sleep(15)

    if(data['field4'] == '1'):
        print("Parking 4 is unavailable")
    else:
        print("Parking 4 is available")
    time.sleep(15)
    conn.close()


if __name__ == '__main__':
    main()
