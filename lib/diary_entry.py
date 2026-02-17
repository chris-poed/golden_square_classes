class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents


    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        calculated_reading_time = int(word_count / wpm)
        if calculated_reading_time < 1:
            return 'Estimated reading time is less than a minute'
        return f'Estimated reading time is {calculated_reading_time} minute'

    def reading_chunk(self, wpm, minutes):
        text_size = int(wpm * minutes)
        chunk_of_text = self.contents[:text_size]
        return chunk_of_text

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.