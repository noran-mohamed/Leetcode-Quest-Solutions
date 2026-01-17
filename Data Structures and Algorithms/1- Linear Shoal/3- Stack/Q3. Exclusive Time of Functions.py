class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0 for i in range(n)]
        prev_time = 0
        stack = []

        for log in logs :
            parts = log.split(":")
            fid = int(parts[0])
            event = parts[1]
            time = int(parts[2])
            if event == "start" :
                if stack :
                    result[stack[-1]] += (time - prev_time)
                stack.append(fid)
                prev_time = time
            else :
                ended = stack.pop()
                result[ended] += (time - prev_time + 1)
                prev_time = time +1
        return result

        
