import sublime
import sublime_plugin
import re

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
		removeLeadingSpacePattern = r'\s[۔،:\(\[“‘]'
		region = self.view.find(removeLeadingSpacePattern, 0)
		while region.begin() > 0:
			text = self.view.substr(region)
			text = text[1:]
			self.view.replace(edit, region, text)
			region = self.view.find(removeLeadingSpacePattern, 0)


		# add trailing space
		addTrailingSpacePattern = r'[۔،:\(\[“‘][^\s]'
		region = self.view.find(addTrailingSpacePattern, 0)
		while region.begin() > 0:
			self.view.insert(edit, region.end() - 1, ' ')
			region = self.view.find(addTrailingSpacePattern, 0)

		# add leading space
		addLeadingSpacePattern = r'[^\s][\)\]”’]'
		region = self.view.find(addLeadingSpacePattern, 0)
		while region.begin() > 0:
			self.view.insert(edit, region.begin() + 1, ' ')
			region = self.view.find(addLeadingSpacePattern, 0)

		# remove trailing space
		removeTrailingSpacePattern = r'[\)\]”’]\s'
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