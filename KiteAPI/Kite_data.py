from kiteconnect import KiteConnect

kite = KiteConnect(api_key="j8rcs7kpkdhenlv3")
print(kite.login_url())
data = kite.generate_session("8hz0pvO9kC0QGwpgrnDkR34kAjHsvLXS", api_secret="1nuxe5dnhxotk6ch330lqqaegd1pe9q5")
kite.set_access_token(data["request_token"])


print(kite.ltp("NSE:INFY"))   # Example: get live price of Infosys

#https://kite.zerodha.com/connect/login?v=3&api_key=j8rcs7kpkdhenlv3&redirect_params=redirect_url=https://kite.zerodha.com