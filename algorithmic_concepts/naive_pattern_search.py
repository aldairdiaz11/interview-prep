def pattern_search(text, pattern):
    print("Input Text:", text, "Input Pattern:", pattern)
    for index in range(len(text)):
        print("Text Index:", index)
        match_count = 0

        for char in range(len(pattern)):
            print("Pattern Index:", char)
            if pattern[char] == text[char + index]:
                print("Matching index found")
                print(f"Match Count: {match_count}")
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print(f"{pattern} found at index {index}")


text_test = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern_test = "NEEDLE"
pattern_search(text_test, pattern_test)
