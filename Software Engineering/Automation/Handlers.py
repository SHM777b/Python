class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def sub_callback(self, prefix, name, match):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(match)

    def start(self, name, file2):
        return self.callback('start_', name, file2)

    def end(self, name, file2):
        return self.callback('end_', name, file2)

    def sub(self, name):
        def substitution(match):
            result = self.sub_callback('sub_', name, match)
            if result is None:
                return match.group(0)
            return result
        return substitution


class HTMLRenderer(Handler):
    """
    A specific handler used to render HTML.

    The methods in HTMLRenderer are accessed from the superclass Handler's start(), end() and sub() methods. They
    implement basic markup as used in HTML documents.
    """
    def start_html(self, file2):
        print('<html><head><title>HTML Text Renderer</title></head><body>', file=file2)

    def end_html(self, file2):
        print('</body></html>', file=file2)

    def start_paragraph(self, file2):
        print('<p>', file=file2)

    def end_paragraph(self, file2):
        print('</p>', file=file2)

    def start_heading(self, file2):
        print('<h2>', file=file2)

    def end_heading(self, file2):
        print('</h2>', file=file2)

    def start_list(self, file2):
        print('<ul>', file=file2)

    def end_list(self, file2):
        print('</ul>', file=file2)

    def start_listitem(self, file2):
        print('<li>', file=file2)

    def end_listitem(self, file2):
        print('</li>', file=file2)

    def start_title(self, file2):
        print('<h1>', file=file2)

    def end_title(self, file2):
        print('</h1>', file=file2)

    def sub_emphasize(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_weblink(self, match):
        return '<a href={}>{}</a>'.format(match.group(1), match.group(1))

    def sub_allCapital(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_email(self, match):
        return '<a href = "{}">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, block, file2):
        print(block, file=file2)
