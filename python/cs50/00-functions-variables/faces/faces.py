# Take input string from user
text = input()

# Convert emoticons to emojis
emojis = text.replace(":)", "🙂").replace(":(", "🙁")

# Print output
print(emojis)
