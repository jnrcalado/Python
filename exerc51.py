primeiro_termo = int(input('\033[1mPrimeiro termo:\033[m '))
razão = int(input('\033[1mRazão:\033[m '))
decimo = primeiro_termo + (10 - 1) * razão
for PA in range(primeiro_termo, decimo + razão, razão):
    print(f"{PA}", end=' → ')
print('\033[1mFim dos termos\033[m')
