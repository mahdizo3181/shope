from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6E4A674739497466673237534A376E76744D713955586554556A31727270385177504C592F57796A684A6B3D')
        # params = {'sender': '10008663', 'receptor': '09184999263', 'message': f'Your code is {code}'}
        # response = api.sms_send(params)
        # print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
