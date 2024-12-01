def read_lists_file(file_name):
	a, b = [], []

	with open(f"../{file_name}") as f:
		lines = f.readlines()

	for line in lines:
		id_a, id_b = line.split("   ")
		a.append(int(id_a))
		b.append(int(id_b))

	return a, b


def test_lists():
	return ([3, 4, 2, 1, 3, 3],
	        [4, 3, 5, 3, 9, 3])


def total_distance_sort_lists(a, b):
	if len(a) != len(b):
		print("Lists have different lengths")

	a_sorted = sorted(a)
	b_sorted = sorted(b)

	return sum(abs(elem_a - elem_b) for elem_a, elem_b in zip(a_sorted, b_sorted))


def similarity_score(a, b):
	score = 0
	b_elem_counts = {}

	for elem in b:
		elem_count = b_elem_counts.get(elem)
		if elem_count is None:
			b_elem_counts[elem] = 1
		else:
			b_elem_counts[elem] = elem_count + 1

	for elem_a in a:
		b_count = b_elem_counts.get(elem_a)
		if b_count is not None:
			score += elem_a * b_count

	return score


if __name__ == '__main__':
	# first, second = test_lists()
	first, second = read_lists_file("input.txt")

	print(total_distance_sort_lists(first, second))  # 1506483
	print(similarity_score(first, second))  # 23126924
