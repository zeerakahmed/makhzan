import sublime
import sublime_plugin

class AddAnnotationTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<annotation lang=\"\">'
			suffix = '</annotation>'
			self.view.insert(edit, region.begin() + charsInserted, prefix)
			charsInserted += len(prefix)
			self.view.insert(edit, region.end() + charsInserted, suffix)
			charsInserted += len(suffix)