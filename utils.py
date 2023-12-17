from kavenegar import *


def send_otp_code(phone, code):
    try:
        api = KavenegarAPI(
            '')
        params = {
            'sender': '',
            'receptor': phone,
            'message': f'کد تایید شما {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
