import sublime
import sublime_plugin

class AddParagraphTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			for line in self.view.lines(region):
				prefix = '<p>'
				suffix = '</p>'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
				self.view.insert(edit, line.end() + charsInserted, suffix)
				charsInserted += len(suffix)