import hashlib

student_email = "simenmyr@stud.ntnu.no"

md5_hash = hashlib.md5(student_email.encode()).hexdigest()
leftmost_8_hex = md5_hash[:8]
hex_as_int = int(leftmost_8_hex, 16)
print(hex_as_int)
# fcrackzip -c 1 -p   -b -u simenmyr_trace.zip