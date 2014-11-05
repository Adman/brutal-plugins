
from brutal.core.plugin import BotPlugin, cmd, event, match, threaded


@cmd
def ping(event):
    """Responds 'pong' to your 'ping'."""

    return 'pong'


@cmd
def echo(event):
    """Echoes back the message it recieves."""
    return ' '.join(event.args)


@event
def auto_welcome(event):
    if event.event_type == 'join':
        # TODO: Generalise personalised autowelcome.
    	if event.meta['nick'] == 'LordPotato_':
            return 'praise the mighty LordPotato_'
        return event.meta['nick'] + ': hi!'
