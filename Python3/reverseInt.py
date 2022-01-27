class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        x_str_list = list(str(x))
        i = 0
        j = len(x_str_list) - 1

        minus_flag = False
        if (x_str_list[0] == '-'):
            x_str_list.remove('-')
            j -= 1
            minus_flag = True

        while (j > i):
            
            x_str_list[i], x_str_list[j] = x_str_list[j], x_str_list[i]
            
            i += 1
            j -= 1

        ret_int = int(''.join(x_str_list))

        if (minus_flag):
            ret_int *= -1

        if (not(ret_int >= pow(-2, 31) and ret_int <= (pow(2, 31) - 1))):
            ret_int = 0


        return ret_int
