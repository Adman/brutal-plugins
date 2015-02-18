from brutal.core.plugin import BotPlugin, cmd, match, event


class StickyNotes(BotPlugin):
    def setup(self, *args, **kwargs):
        self.notes = self.open_storage('sticky_notes')

    @cmd
    def stickynote(self, event):
        """Create a sticky note for a given user."""
        args = event.args

        if len(args) < 1:
            return "Sticky note needs to be adressed to someone."
        elif len(args) < 2:
            return "Sticky note needs to contain some actual note."
        else:
            user = event.args[0]
            content = ' '.join(event.args[1:])

        if user not in self.notes:
            self.notes[user] = []

        notes = self.notes[user]
        notes.append("Note from {0}: {1}".format(event.meta['nick'], content))
        self.notes[user] = notes

        return "Sticky note for {0} prepared.".format(user)

    @event
    def send_notes(self, event):
        format_note = lambda x, y: "{0}: {1}".format(x, y)

        if event.event_type == 'join':
            nick = event.meta['nick']
            if nick in self.notes and len(self.notes[nick]) > 0:
                last_note = self.notes[nick].pop()
                while len(self.notes[nick]) > 1:
                    note = self.notes[nick].pop()
                    self.msg(format_note(nick, note), event=event)
                return format_note(nick, last_note)
