import telebot
import subprocess

API_TOKEN = '7856951971:AAHhnHq_LTdvjC-cBrIuonXeJSzOfLNC7so'
bot = telebot.TeleBot(API_TOKEN)

RADIO_STATION = {
    "Air Bilaspur": "https://nl4.mystreaming.net/uber/bollywoodlove/icecast.audio",
    "Air Raipur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio118/playlist.m3u8",
    "Capital FM": "http://media-ice.musicradio.com/CapitalMP3?.mp3&listening-from-radio-garden=1616312105154",
    "English": "https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8",
    "Mirchi": "http://peridot.streamguys.com:7150/Mirchi",
    "Radio Today": "http://stream.zenolive.com/8wv4d8g4344tv",
    "YouTube": "https://www.youtube.com/live/eu191hR_LEc?si=T-9QYD548jd0Mogp",
    "Zee News": "https://www.youtube.com/live/TPcmrPrygDc?si=hiHBkIidgurQAd1P",
    "Aaj Tak": "https://www.youtube.com/live/Nq2wYlWFucg?si=usY4UYiSBInKA0S1",
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the FM Radio Bot! Use /play <station_name> to play a radio station.")

@bot.message_handler(commands=['play'])
def play_radio(message):
    try:
        station_name = message.text.split(' ', 1)[1]
        if station_name in RADIO_STATION:
            url = RADIO_STATION[station_name]
            chat_id = message.chat.id
            bot.send_message(chat_id, f"Playing {station_name}...")
            subprocess.Popen(['ffmpeg', '-i', url, '-f', 's16le', '-ar', '48000', '-ac', '2', 'pipe:1'], stdout=subprocess.PIPE)
        else:
            bot.send_message(message.chat.id, "Station not found. Please check the station name.")
    except IndexError:
        bot.send_message(message.chat.id, "Please provide a station name.")

bot.polling()

