import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl

def reading_webpage(tin_number=""):
    """
    This function will be responsible to read the webpage and it will 
    tin_number : a 10 digit number that is called a tin number eg: 0041038077
    """
    # Specify SSL/TLS version and cipher suite
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')

    # Create a custom HTTPAdapter with the custom SSL context
    class CustomHTTPAdapter(HTTPAdapter):
        def init_poolmanager(self, connections, maxsize, block=False):
            self.poolmanager = PoolManager(num_pools=connections,
                                        maxsize=maxsize,
                                        block=block,
                                        ssl_context=ssl_context)

    # Create a session and mount the custom HTTPAdapter
    session = requests.Session()
    session.mount('https://', CustomHTTPAdapter())

    # Make the request
    url = 'https://etrade.gov.et/business-license-checker?tin={tin_number}'
    response = session.get(url, stream=True)

    # Check the response
    if response.status_code == 200:
        # Read the response content in chunks
        content = ''
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                content += chunk.decode('utf-8', errors='ignore')
        return content
    else:
        return "Request failed with status code:", {response.status_code}