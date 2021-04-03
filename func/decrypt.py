from apps.Messaging_App.lib.keys_system import the_keys, save_keys

from apps.Messaging_App.func.save_new_message import save_new_message


def decrypt_text(text_data,pubkey):

    nums = []

    for line in text_data.splitlines():
        nums.append(int(line))
    l = len(nums)
    n = nums[l-2]
    e = nums[l-1]

    print("\n\n\n e: "+str(e))
    

    temp_keys = the_keys()

    print(temp_keys)

    message_publickey = pubkey.replace("\n","").replace(" ","")


    for keys in temp_keys:
      if "fromUser" in temp_keys[keys]:
        key_publickey = temp_keys[keys]["fromUser"].replace("\n","").replace(" ","")
        if message_publickey == key_publickey or message_publickey in key_publickey or key_publickey in message_publickey:
            d = temp_keys["1"]["d"]
            print("d: "+str(d))
            i = 0
            decrypted_Mess = ""
            #with open("decryptText.txt") as newFile:
            while i < l -2:
                x = decrypt(nums[i], int(d), int(n))
                y = chr(x)
                #print(chr(x).encode('utf-8'), file=decrypted_Mess)
                decrypted_Mess += y
                i+=1
            message = {"from":"user","message":decrypted_Mess}
            save_new_message(message,temp_keys[keys]["n"],temp_keys[keys]["e"])
            return decrypted_Mess


def decrypt(c,d,n):
    x = pow(c,d,n)
    return x
