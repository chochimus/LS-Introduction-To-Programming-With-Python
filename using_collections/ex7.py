info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)