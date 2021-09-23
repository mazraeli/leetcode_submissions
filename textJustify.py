import copy as cp

class Solution(object):

    def fillSpaces(self, line, spaces, pads):
        """
        :type line: List
        :type spaces: int
        :type pads: int
        """
        tline = ""
        one_pad_length = int(spaces / pads)
        pad = ""
        if (spaces % pads == 0):
            for i in range(0, one_pad_length):
                pad += " "

            for i in range(0, len(line) - 1):
                tline += line[i] + pad
            tline += line[-1]
        else:
            for i in range(0, one_pad_length):
                pad += " "
            left_pads_count = spaces % pads
            right_pads_count = pads - left_pads_count
            for i in range(0, len(line) - 1):
                if (i < left_pads_count):
                    tline += line[i] + pad + " "
                else:
                    tline += line[i] + pad
            tline += line[-1]
            
        return tline


    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        line_char_count = 0 # count the number of chars in the line
        lines_wo_jstf = [] # lines of words without justification
        list_t = [] # temporary list
        for w in words:
            # if adding a word would exceed the maxWidth
            if (len(w) + line_char_count > maxWidth):
                # append a sub list of words
                lines_wo_jstf.append(cp.deepcopy(list_t))
                # clear the temp vars
                list_t.clear()
                line_char_count = 0
                # add it to a new temp list
                list_t.append(w)
                line_char_count += len(w) + 1
            # adding a word wouldn't exceed the maxWidth
            else:
                list_t.append(w)
                line_char_count += len(w) + 1

        # check if words left in the temp list
        if (len(list_t) > 0):
            lines_wo_jstf.append(cp.deepcopy(list_t))
        list_t.clear() # clear the temp list clearly

        line_char_count_list = [] # a list which keep the number of all characters added 
                                # to a line without considering the space between them
        for l in lines_wo_jstf:
            count = 0
            for w in l:
                count += len(w)
            line_char_count_list.append(count)

        # iterate over the lines except the last lines
        lines_justified = [] # the final justified line list
        for i in range(0, len(lines_wo_jstf) - 1):
            numofSpaces = maxWidth - line_char_count_list[i]
            numofWords = len(lines_wo_jstf[i])
            numofPads = numofWords - 1
            if (numofPads == 0):
                right_space_count = maxWidth - len(lines_wo_jstf[i][0])
                tline = lines_wo_jstf[i][0]
                for i in range(0, right_space_count):
                    tline += " "
                lines_justified.append(tline)
            else:
                lines_justified.append(self.fillSpaces(lines_wo_jstf[i], numofSpaces, numofPads))
        
        last_line = ''
        for i in range(0, len(lines_wo_jstf[-1]) - 1):
            last_line += lines_wo_jstf[-1][i] + " "
        last_line += lines_wo_jstf[-1][-1]

        right_space_count = maxWidth - len(last_line)
        for i in range(0, right_space_count):
            last_line += " "
        lines_justified.append(last_line)

        return lines_justified
            

