import sublime
import sublime_plugin

class AddListTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<list>\n'
			suffix = '</list>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)