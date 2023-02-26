
import requests
import sys

apikey = 'api_key=RGAPI-c19d28c7-653a-4536-a7a5-524ba4e8ef5a'
urlSummoner = 'https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name'
# summonerName = 'MONTHASI'


def main() -> int:
    print("¿Cual es tu nombre de invocador HERMANO?")
    summonerName = input()
    resp = requests.get(
        urlSummoner + '/' + summonerName + '?' + apikey)
    objeto = resp.json()
    print(f"Tu nivel es : {objeto['summonerLevel']}")
    return 0


def summonerLevel(summonerName):
    resp = requests.get(
        urlSummoner + '/' + summonerName + '?' + apikey)
    objeto = resp.json()
    print(f"Tu nivel es : {objeto['summonerLevel']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
