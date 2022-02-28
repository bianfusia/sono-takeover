from soco import SoCo
from soco import discover

# Audio track
# 0. Rick Roll - https://ia802307.us.archive.org/15/items/Sz39_39/rick-astley-never-gonna-give-you-up-official-music-video.mp3
# 1. India Song - https://ia800904.us.archive.org/8/items/tvtunes_12538/Psych%20-%20Bollywood%20Version.mp3
# 2. China National Anthem - https://ia804503.us.archive.org/23/items/20210523_20210523_1714/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9B%BD%E6%AD%8C%20side%201.mp3
# 3. Bella Ciao - https://ia801805.us.archive.org/22/items/bella-ciao-musica-original-de-la-serie-la-casa-de-papel-money-heist-gratis-mp-3-s.-net/Bella%20Ciao%20%28Musica%20Original%20de%20la%20Serie%20la%20Casa%20de%20Papel%20Money%20Heist%29%20%28GRATIS-MP3S.NET%29.mp3
def takeover():
    songs = ["https://ia802307.us.archive.org/15/items/Sz39_39/rick-astley-never-gonna-give-you-up-official-music-video.mp3","https://ia800904.us.archive.org/8/items/tvtunes_12538/Psych%20-%20Bollywood%20Version.mp3","https://ia804503.us.archive.org/23/items/20210523_20210523_1714/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9B%BD%E6%AD%8C%20side%201.mp3", "https://ia801805.us.archive.org/22/items/bella-ciao-musica-original-de-la-serie-la-casa-de-papel-money-heist-gratis-mp-3-s.-net/Bella%20Ciao%20%28Musica%20Original%20de%20la%20Serie%20la%20Casa%20de%20Papel%20Money%20Heist%29%20%28GRATIS-MP3S.NET%29.mp3"]
    listings = discover()
    if listings == None:
        print("No Sono detected in your WiFi. Exiting Program.")
        return
    else:
        available_devices = list(discover())
        print("-----------TAKEOVER SONOS LIST-------------")
        for index, zone in enumerate(available_devices):
            print(f"{index} - {zone} - {zone.player_name} - Current Vol: {zone.volume}")
        print("999 - Takeover everything!")

    device = int(input("Please select an option: "))
    song = int(input("Please choose a song:\n0. Rick Roll\n1. India Song\n2. China National Anthem\n3. Bella Ciao\nChoose: "))
    song = songs[song]
    volume = int(input("Please choose a volume between 0 - 100: "))

    if device == 999:
        for zone in available_devices:
            zone.volume = 0
        for zone in available_devices:
            zone.play_uri(song)
        for zone in available_devices:
            device.volume = volume
    else:
        device = available_devices[device]
        device.volume = 0
        device.play_uri(song)
        device.volume = volume


    while True:
        adj_vol = int(input("adjust the volume? 999 to destroy"))
        if adj_vol == 999 and device == 999:
            for zone in available_devices:
                zone.volume = 0
            i = 0
            while i < 100:
                for zone in available_devices:
                    zone.volume += 1
                i += 1

        elif device == 999:
            for zone in available_devices:
                zone.volume = adj_vol
        else:
            device.volume = adj_vol
                

if __name__ == "__main__":
    takeover()
        
