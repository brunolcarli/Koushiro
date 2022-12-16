import requests
from koushiro.settings import API_URL


class Query:

    @staticmethod
    def query_message_avg_polarity():
        payload = '''
        query{
            messageAveragePolarity {
                positive
                negative
                neutral
            }
        }
        '''
        return requests.post(API_URL, json={'query': payload}).json()

    @staticmethod
    def query_top_ten():
        payload = '''
        query{
            topTen {
                username
                messagesCount
            }
        }
        '''
        return requests.post(API_URL, json={'query': payload}).json()

    @staticmethod
    def query_chat_messages():
        payload = '''
        query{
            chatMessages {
                messageDatetime
                username
                message
                messageSentiment
                messageOffenseLevel
            }
        }
        '''
        return requests.post(API_URL, json={'query': payload}).json()
