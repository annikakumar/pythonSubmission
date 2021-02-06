def validateInput(hectoc_input: int) -> str:
    if not isinstance(int, hectoc_input):
        return "Unfortunately your input does not fit the specifications for the hectoc-Problem. Please insert the input in the" \
               " following format: '123456'. You can put six random digits from 1-9"
