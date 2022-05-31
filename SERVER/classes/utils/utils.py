class Utils:
    def format_date(self):
        d = datetime.datetime.now()
        day = str(d.strftime("%a"))
        month = str(d.strftime("%b"))
        hr = str(d.strftime("%H"))
        mint = str(d.strftime("%M"))
        now = day + "-"+ hr + "-"+mint
        return now