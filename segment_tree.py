def addRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.ranges, left)
        r = bisect.bisect_right(self.ranges, right)

        sub_range = []
        if l % 2 == 0: # does not overlap
            sub_range.append(left)
        if r % 2 == 0: # does not overlap
            sub_range.append(right)
        print(l,r)
        self.ranges[l:r] = sub_range
        print(self.ranges)
        
    def queryRange(self, left: int, right: int) -> bool:
        l = bisect.bisect_right(self.ranges, left)
        r = bisect.bisect_left(self.ranges, right)
        return l == r and l % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.ranges, left)
        r = bisect.bisect_right(self.ranges, right)
        sub_range = []
        if l % 2 == 1: # overlaps
            sub_range.append(left)
        if r % 2 == 1: # overlaps
            sub_range.append(right)
            
        self.ranges[l:r] = sub_range
