import math

class Pagination(object):
	def __init__(self, page, per_page, total_count):
		self.page = int(page)
		self.per_page = per_page
		self.total_count = total_count

	@property
	def pages(self):
		pages = int(math.ceil(self.total_count / float(self.per_page)))
		pages = pages if pages <= 98 else 98
		return pages

	@property
	def has_prev(self):
		return self.page > 1

	@property
	def has_next(self):
		return self.page < self.pages

	def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
		last = 0
		for num in range(1, self.pages + 1):
			if num <= left_edge or \
			(num > self.page - left_current - 1 and \
			num < self.page + right_current) or \
			num > self.pages - right_edge:
				if last + 1 != num:
					yield None
				yield num
				last = num
