import csv

class MinBase():
    """A module to fetch the smallest base for which the first 1000 positive 
    integers are Palindromic
    """  
    def find_min_base(self,decimal_number):
        """For any given Integer number of base 10 finds the smallest base
        so that the number is a palindrome in smallest base

        Args(int): A Positive Integer
        """
        if decimal_number < 0:
            raise ValueError("Please give only Positive Integers")
        elif decimal_number <= 2:
            return decimal_number+1
        else:
            smallest_base = 2
            largest_base = 1
            while smallest_base**2 < decimal_number:
                temp = decimal_number
                palindrome_array = []

                while temp:
                    palindrome_array.append(temp % smallest_base)
                    temp //=smallest_base
                if all(palindrome_array[i] == palindrome_array[-1-i] for i in range(len(palindrome_array)//2)):
                    return smallest_base
                if palindrome_array[0] == 0:
                    largest_base = smallest_base

                smallest_base+=1
        return decimal_number//largest_base-1

    def get_min_base(self):
        """Get the smallest base for the first 1000 decimal integers
        """
        try:
            base_dict = {each_number+1:self.find_min_base(each_number+1) for each_number in range(1000)}
            with open('output.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Decimal Number', 'Smallest Base'])
                for key, value in base_dict.items():
                    writer.writerow([key, value])
            return 0
        except Exception as e:
            print(e)
            return -1

            
