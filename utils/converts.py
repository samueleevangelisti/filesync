'''
converts.py
This module is from samueva97.
Do not modify it
'''
import base64
import pyzstd



def byte_to_base64(byte):
    '''
    Converts bytes in base64

    Parameters
    ----------
    byte : b-str
        Bytes

    Returns
    -------
    str
    '''
    return base64.b64encode(byte).decode()



def base64_to_byte(text):
    '''
    Converts base64 to bytes

    Parameters
    ----------
    text : str
        Text in base64

    Returns
    -------
    b-str
    '''
    return base64.b64decode(text.encode())



def byte_to_zstd(byte):
    '''
    Converts bytes to zstd

    Parameters
    ----------
    byte : b-str
        Bytes

    Returns
    -------
    b-str
    '''
    return pyzstd.compress(byte)



def zstd_to_byte(byte):
    '''
    Converts zstd to bytes

    Parameters
    ----------
    byte : b-str
        Bytest representing a zst file

    Returns
    -------
    b-str
    '''
    return pyzstd.decompress(byte)
