def smallestWindow(self, s, p):
        #code here
        n = len(s)
        if n < len(p):
            return -1
        mp = [0]*256
     
        # Starting index of ans
        start = 0
     
        # Answer
        # Length of ans
        ans = n + 1
        cnt = 0
     
        # creating map
        for i in p:
            mp[ord(i)] += 1
            if mp[ord(i)] == 1:
                cnt += 1
             
        # References of Window       
        j = 0
        i = 0
     
        # Traversing the window
        while(j < n):
            # Calculating
            mp[ord(s[j])] -= 1
            if mp[ord(s[j])] == 0:
                cnt -= 1
             
                # Condition matching
                while cnt == 0:
                    if ans > j - i + 1:
                        # calculating answer.
                        ans = j - i + 1
                        start = i
                     
                    # Sliding I
                    # Calculation for removing I
                    mp[ord(s[i])] += 1
                    if mp[ord(s[i])] > 0:
                        cnt += 1
                    i += 1
            j += 1
        if ans > n:
            return "-1"
        return s[start:start+ans]
