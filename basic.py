
from brutal.core.plugin import BotPlugin, cmd, event, match, threaded


@cmd
def ping(event):
    """Responds 'pong' to your 'ping'."""

    return 'pong'


@cmd
def echo(event):
    """Echoes back the message it recieves."""
    return ' '.join(event.args)


welcomes = {
    'LordPotato_': "All praise the mighty LordPotato_!",
    'pepol': "Nazimod sighted, take cover!",
    'mrshu': "Nazireviewer is here, hide your code!",
    'jn_': "Swiggidy swooty, he's comin' for dat booty!"
}

@event
def auto_welcome(event):
    if event.event_type == 'join':
    	if event.meta['nick'] in welcomes:
            return welcomes[event.meta['nick']]
        else:
            return event.meta['nick'] + ': hi!'
