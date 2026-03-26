class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None


class BigInteger:
    def __init__(self, number="0"):
        self.head = None
        for digit in reversed(number):
            self.insert(int(digit))

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_number(self):
        temp = self.head
        result = ""
        while temp:
            result = str(temp.data) + result
            temp = temp.next
        return result

    def add(self, other):
        p1 = self.head
        p2 = other.head
        carry = 0
        result = BigInteger()

        while p1 or p2 or carry:
            val1 = p1.data if p1 else 0
            val2 = p2.data if p2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            result.insert(total % 10)

            if p1: p1 = p1.next
            if p2: p2 = p2.next

        return result

    def subtract(self, other):
        p1 = self.head
        p2 = other.head
        borrow = 0
        result = BigInteger()

        while p1:
            val1 = p1.data - borrow
            val2 = p2.data if p2 else 0

            if val1 < val2:
                val1 += 10
                borrow = 1
            else:
                borrow = 0

            result.insert(val1 - val2)

            p1 = p1.next
            if p2: p2 = p2.next

        return result

    def multiply(self, other):
        result = BigInteger("0")
        p1 = self.head
        zeros = 0

        while p1:
            temp = BigInteger()
            carry = 0

            for _ in range(zeros):
                temp.insert(0)

            p2 = other.head
            while p2 or carry:
                val2 = p2.data if p2 else 0
                total = p1.data * val2 + carry
                carry = total // 10
                temp.insert(total % 10)

                if p2: p2 = p2.next

            result = result.add(temp)
            zeros += 1
            p1 = p1.next

        return result

    def to_int(self):
        return int(self.print_number())

    def divide(self, other):
        return BigInteger(str(self.to_int() // other.to_int()))

    def modulo(self, other):
        return BigInteger(str(self.to_int() % other.to_int()))
