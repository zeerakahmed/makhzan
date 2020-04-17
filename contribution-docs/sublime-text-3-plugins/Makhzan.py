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
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
			prefix = '<body>\n'
			suffix = '</body>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)

class AddSectionTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
			prefix = '<section>\n'
			suffix = '</section>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)

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
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
			prefix = '<list>\n'
			suffix = '</list>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)

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
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
			prefix = '<blockquote>\n'
			suffix = '</blockquote>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)

class AddVerseTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			for line in self.view.lines(region):
				prefix = '\t'
				self.view.insert(edit, line.begin() + charsInserted, prefix)
				charsInserted += len(prefix)
			prefix = '<verse>\n'
			suffix = '</verse>\n'
			self.view.insert(edit, self.view.full_line(region).begin(), prefix)
			self.view.insert(edit, self.view.full_line(region).end(), suffix)

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

class AddAnnotationTagsEnCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<annotation lang=\"en\">'
			suffix = '</annotation>'
			self.view.insert(edit, region.begin() + charsInserted, prefix)
			charsInserted += len(prefix)
			self.view.insert(edit, region.end() + charsInserted, suffix)
			charsInserted += len(suffix)

class AddAnnotationTagsArCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		charsInserted = 0
		for region in self.view.sel():
			prefix = '<annotation lang=\"ar\">'
			suffix = '</annotation>'
			self.view.insert(edit, region.begin() + charsInserted, prefix)
			charsInserted += len(prefix)
			self.view.insert(edit, region.end() + charsInserted, suffix)
			charsInserted += len(suffix)

def display_message(message):
	active_window = sublime.active_window()
	panel = active_window.create_output_panel('makhzan_plugin')
	active_window.run_command('show_panel', {'panel': 'output.makhzan_plugin'})
	panel.run_command('insert', {'characters': message})

def get_xml_from_dom(dom, level):
	output = ""
	for key in dom.keys():
		if isinstance(dom[key], list):
			output += "{}<{}>\n".format("\t"*level, key)
			for element in dom[key]:
				if isinstance(element,dict):
					output += get_xml_from_dom(element, level+1)
				else:
					output += "{}{}\n".format("\t"*(level+1), element)
			output += "{}</{}>\n".format("\t"*level, key)
		else:
			output += "{}<{}>{}</{}>\n".format("\t"*level, key, dom[key], key)
	return output

class AddBunyadStylesCommand(sublime_plugin.TextCommand):
	def run(self, edit, **kwargs):
		if not "styles" in kwargs:
			active_window = sublime.active_window()
			active_window.show_input_panel("Please enter bunyad styles (one for each line of currently open text):",
										   "Typing\nShair Name\nTyping\ntext", self.validate_styles, None, None)
		else:
			styles = kwargs["styles"].split("\n")
			self.process_text(edit, styles)

	def validate_styles(self, user_input):
		styles_line_count = user_input.count("\n") + 1
		content_line_count = self.view.rowcol(self.view.size())[0] + 1
		if styles_line_count != content_line_count:
			display_message("Error: The number of style lines ({}) and content lines ({}) are not equal".format(
				styles_line_count, content_line_count))
		else:
			self.view.run_command("add_bunyad_styles", {"styles": user_input})

	def process_text(self, edit, styles):
		dom = {
			"document": [
				{
					"meta": [
						{
							"title": ""
						},
						{
							"author": [
								{
									"name": ""
								}
							]
						}
					]
				},
				{
					"body": [
						{
							"section": []
						}
					]
				}
			]
		}
		i = 0
		while i < len(styles):
			current_line_style = styles[i]
			current_line_region = self.view.line(self.view.text_point(i, 0))
			current_line_content = self.view.substr(current_line_region)
			if current_line_style == "Shair Name":
				dom["document"][0]["meta"][1]["author"][0]["name"] = current_line_content
			elif current_line_style == "text":
				dom["document"][0]["meta"][0]["title"] = current_line_content
			elif current_line_style in ["Typing", "Normal"]:
				dom["document"][1]["body"][0]["section"].append(
					{"p": current_line_content})
			elif current_line_style == "Qotions":
				blockquote = {"blockquote": [
					{"p": current_line_content}]}
				while styles[i+1] == current_line_style:
					next_line_content = self.view.substr(
						self.view.line(self.view.text_point(i+1, 0)))
					blockquote["blockquote"].append(
						{"p": next_line_content})
					i += 1
				dom["document"][1]["body"][0]["section"].append(blockquote)
			elif current_line_style == "First Share":
				lines = [current_line_content]
				while styles[i+1] == current_line_style:
					next_line_content = self.view.substr(
						self.view.line(self.view.text_point(i+1, 0)))
					lines.append(next_line_content)
					i += 1
				dom["document"][1]["body"][0]["section"].append({"blockquote": [{"verse": lines}]})
			else:
				dom["document"][1]["body"][0]["section"].append(
					{"UNPROCESSED_{}".format(current_line_style.replace(" ", "_")): current_line_content})
			i += 1
		all_lines_region = sublime.Region(0, self.view.size())
		self.view.replace(edit, all_lines_region, get_xml_from_dom(dom, 0))
