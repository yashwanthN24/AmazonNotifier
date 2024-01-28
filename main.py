import sys
import requests
import smtplib


url = "https://amazon-product-data6.p.rapidapi.com/product-by-text"
def process():

    search_url = "Vivo book 15 15.6' i3 1220p"

    querystring = {"keyword": f"{search_url}","page":"1","country":"IN"}

    headers = {
        "X-RapidAPI-Key": "7db4353802msh9d09f4b026c63b7p1de3e5jsn6bf9d4474d8c",
        "X-RapidAPI-Host": "amazon-product-data6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers , params=querystring)
    print(response.status_code)
    print(response.json())
    if response.status_code != 200:
        print("Error in the url u entered please check it again")
        while True :
            choice = input("Do you want to try with differenct product link  (y/n): ")
            if choice in ['y','yes','Y','YES']:
                process()
            else:
                print("Thank you for using our service")
                sys.exit(0)

    elif response.status_code == 200:
        first_result = response.json()['data'][0]

        title = first_result['title']
        price = first_result['price']

        pricefinal = ''
        for num in price:
	        if num not in [',' , '.' , '₹']:
		        pricefinal += num
        pricefinal = int(pricefinal)

        print(f"The current price of the product {title} is {pricefinal}")

    while True:
        try:
            BUY_PRICE = int(input("Enter the buy price here: "))
            break
        except ValueError:
            pass




    while True:
        send_mail = input("Enter your gmail to get the alert: ")
    # validate email
        if send_mail and send_mail.endswith("@gmail.com"):
            break


    if pricefinal < BUY_PRICE:
        message = f"{title} is now {price}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login("yashwanthnaddana2002@gmail.com", "nydv qexs jsxy cxai")
            connection.sendmail(
                from_addr="yashwanthnaddana2002@gmail.com",
                to_addrs=send_mail,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{first_result['url']}".encode("utf-8")
            )
            print("Email sent successfully")
    else:
        print("The price is not less than your buy price")


if __name__ == "__main__":
    process()
