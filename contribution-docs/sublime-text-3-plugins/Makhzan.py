import sublime
import sublime_plugin

class FixInpageIssuesCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# use correct right double quotation marks
		rightQuotesPattern = r'’’'
		region = self.view.find(rightQuotesPattern, 0)
		while region.begin() > 0:
			self.view.replace(edit, region, '”')
			region = self.view.find(rightQuotesPattern, 0)

		# use correct left double quotation marks
		leftQuotesPattern = r'‘‘'
		region = self.view.find(leftQuotesPattern, 0)
		while region.begin() > 0:
			self.view.replace(edit, region, '“')
			region = self.view.find(leftQuotesPattern, 0)

		# remove leading space
		removeLeadingSpacePattern = r'\s[۔،:?!\)\]“‘]'
		region = self.view.find(removeLeadingSpacePattern, 0)
		while region.begin() > 0:
			text = self.view.substr(region)
			text = text[1:]
			self.view.replace(edit, region, text)
			region = self.view.find(removeLeadingSpacePattern, 0)

		# add trailing space
		addTrailingSpacePattern = r'[۔،:?!\)\]“‘][^\s]'
		region = self.view.find(addTrailingSpacePattern, 0)
		while region.begin() > 0:
			self.view.insert(edit, region.end() - 1, ' ')
			region = self.view.find(addTrailingSpacePattern, 0)

		# add leading space
		addLeadingSpacePattern = r'[^\s][\(\[”’]'
		region = self.view.find(addLeadingSpacePattern, 0)
		while region.begin() > 0:
			self.view.insert(edit, region.begin() + 1, ' ')
			region = self.view.find(addLeadingSpacePattern, 0)

		# remove trailing space
		removeTrailingSpacePattern = r'[\(\[”’]\s'
		region = self.view.find(removeTrailingSpacePattern, 0)
		while region.begin() > 0:
			text = self.view.substr(region)
			text = text[:-1]
			self.view.replace(edit, region, text)
			region = self.view.find(removeTrailingSpacePattern, 0)

		# remove multiple spaces
		doubleSpacePattern = r'  '
		region = self.view.find(doubleSpacePattern, 0)
		while region.begin() > 0:
			self.view.replace(edit, region, ' ')
			region = self.view.find(doubleSpacePattern, 0)

class AddBodyTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<body>\n'
			suffix = '</body>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)

class AddSectionTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<section>\n'
			suffix = '</section>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)

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

class AddHeadingTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			for line in self.view.lines(region):
				prefix = '<heading>'
				suffix = '</heading>'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
				self.view.insert(edit, line.end() + charsInserted, suffix)
				charsInserted += len(suffix)

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

class AddListItemTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			for line in self.view.lines(region):
				prefix = '<li>'
				suffix = '</li>'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
				self.view.insert(edit, line.end() + charsInserted, suffix)
				charsInserted += len(suffix)

class AddBlockquoteTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<blockquote>\n'
			suffix = '</blockquote>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)

class AddVerseTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<verse>\n'
			suffix = '</verse>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)

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