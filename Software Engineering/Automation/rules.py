class Rule:
    def action(self, block, file2, handler):
        handler.start(self.type, file2)
        handler.feed(block, file2)
        handler.end(self.type, file2)
        return True


class HeadingRule(Rule):
    """
    Heading is a block that is shorter than 70 characters and does not end with a column
    """
    type = 'heading'

    def condition(self, block):  # This func returns true if all statements below are True, meaning that it is heading
        return not '\n' in block and block[-1] != ':' and len(block) <= 70


class TitleRule(HeadingRule):
    """
    Title is the first block in the document, provided that it is a heading
    """
    type = 'title'
    first_block = True

    def condition(self, block):
        if self.first_block:
            self.first_block = False
            return HeadingRule.condition(self, block)
        else:
            return None

class ListItemRule(Rule):
    """
    List item is a line that starts with a hyphen. The hyphen is removed as part of mark up process
    """
    type = 'listitem'

    def condition(self, block):
        return block.startswith('-')

    def action(self, block, file2, handler):
        handler.start(self.type, file2)
        handler.feed(block[1:], file2)
        handler.end(self.type, file2)
        return True


class ListRule(ListItemRule):
    """
    List begins with a block that is not a list item and ends between a list item and a non-list item paragraph
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, file2, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type, file2)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type, file2)
        return False


class ParagraphRule(Rule):
    """
    It is a paragraph if it is not a heading or a list
    """
    type = 'paragraph'

    def condition(self, block):
        return True
