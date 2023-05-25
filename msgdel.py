from telegram.ext import Updater, MessageHandler, filters

from telegram import Update

from telegram.ext import ApplicationBuilder
async def delete_join_message(update, context):
	#print("\n".join(dir(update.message)))
	if update.message.new_chat_members:
		print("Removed Join Msg")
		await context.bot.delete_message(update.message.chat.id, update.message.message_id) #.delete()
 
async def log(update, context):
	print("log")
	
def main():
	app = ApplicationBuilder().token("Bot Token").build()
	app.add_handler(MessageHandler(filters.ALL, delete_join_message))
	app.run_polling()
	
if __name__ == '__main__':
    main()
