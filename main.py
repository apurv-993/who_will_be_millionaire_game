questions = [
["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],

["Which data type is used to store whole numbers in Python?", "float", "str", "int", "bool", 3],

["What is the binary equivalent of decimal 10?", "1010", "1100", "1001", "1110", 1],

["Which logic gate gives output 1 only when all inputs are 1?", "OR", "XOR", "AND", "NOT", 3],

["Who is known as the father of computers?", "Charles Babbage", "Alan Turing", "John von Neumann", "Bill Gates", 1],

["What is the value of 2^5?", "10", "25", "32", "64", 3],

["Which microprocessor has a 16-bit data bus?", "8085", "8086", "8051", "Pentium", 2],

["What does CPU stand for?", "Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Control Processing Unit", 1],

["Which protocol is primarily used for web browsing?", "FTP", "SMTP", "HTTP", "TCP", 3],

["What is the output of a Half Adder when A=1 and B=1 (Sum, Carry)?", "0,0", "1,0", "1,1", "0,1", 4]
]
prize = 0
for question in questions:
    print(f"QUESTION : {question[0]} \n 1. {question[1]} \n 2. {question[2]} \n 3. {question[3]} \n 4. {question[4]}")
    answer = int(input("Enter your answer (1-4): "))
    
    if(answer == question[5]):
        print("Correct!\n")
        prize = prize + 2000
        print(f"Congratulations! You have won {prize}\n")
    else:
        print("Wrong!\n")
