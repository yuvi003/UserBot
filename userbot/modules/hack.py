@register(outgoing=True, pattern="^.hack$")
async def hacking (hacked):
    """ Dont Hack Too much -_-"""
    if not hacked.text[0].isalpha() and hacked.text[0] not in ("/", "#", "@", "!"):
        if await hacked.get_reply_message():
            await hacked.edit(
                "Targeted Account Hacked successfully ??......\n"
                "Pay 6969$ to @yuviking To Remove This Hack...\n"
            )
