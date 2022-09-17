
def execute_paramu_fn(args,hosei,fn):
    return fn(args,hosei)

if __name__ == "__main__":
    fn_max = execute_paramu_fn([1,2,3],4,lambda x,y:max(x)+y)
    fn_min = execute_paramu_fn([1,2,3],4,lambda a,b:min(a)-b)

print(fn_max)
print(fn_min)

