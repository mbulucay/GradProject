from obspy import read


st = read('./BAKL.BHZ.sac', debug_headers=True)
print(st)

print(st[0].stats)

# for key, val in st.traces[0].stats.items():
#     print(key)

# for key, val in st[0].stats.sac.items():
#     print(key + ': ' + str(val))

print()
print("Data")
print(st[0].data)

print("Length of data " + str(len(st[0].data)))