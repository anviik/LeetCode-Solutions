class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tr = collections.defaultdict(list)
        res = []
        for t in transactions:
            name, time, amt, city = t.split(",")
            tr[name].append((int(time), city))

        for i in range(len(transactions)):
            curname, curtime, curamt, curcity = transactions[i].split(",")
            curtime, curamt = int(curtime), int(curamt)

            if  curamt > 1000:
                res.append(transactions[i])
                continue
            for othertime, othercity in tr[curname]:
                if (abs(curtime-othertime)) <= 60 and curcity != othercity:
                    res.append(transactions[i])
                    break
        return res


            

