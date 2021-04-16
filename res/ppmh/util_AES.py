from Crypto.Cipher import AES
import base64


BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def aesEncrypt(key, data):
    '''
    AES的ECB模式加密方法
    :param key: 密钥
    :param data:被加密字符串（明文）
    :return:密文
    '''
    key = key.encode('utf8')
    # 字符串补位
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    print(enctext)
    return enctext

def aesDecrypt(key, data):
    '''

    :param key: 密钥
    :param data: 加密后的数据（密文）
    :return:明文
    '''
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    # 去补位
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    # print(text_decrypted)
    # print('\n')
    return text_decrypted


if __name__ == '__main__':
    key = 'YhG78Plkl56Htrqw'
    data = 'hello 你好'
    ecdata ='hxswZjVTDM3JIVEJ0JQ7MVXykSDE0C0oUFf0AOU1Ll9W49Wk5BUVj5AZZtqMMxfI'
    # 加密
    # ecdata = aesEncrypt(key, data)
    # 解密
    txt = aesDecrypt(key, ecdata)
    print(txt)
    # with open('test.png', 'wb') as f:
    #     f.write(base64.b64decode(txt))
