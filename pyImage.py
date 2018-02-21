import pymssql
import sys

if __name__ == '__main__':
    conn = pymssql.connect(
        server='203.236.86.231',
        user='usr_wintelips2web',
        password='PoweR!Over^9Whelming',
        database='IPDM_UP_v2'
        )

    cursor = conn.cursor()

    args=['WT','N', 'wips2017060', 'CC|DB|RDR|SKEY', '3518053000050,3518053000051,3518053000263,3518053000509,3518053000512,3518051000443,3518051000502,3518051000975,3518051000099,3518051000208', 'N', 0, '']
    cursor.callproc('download.up_list', args)

    cursor.nextset()

    result = cursor.fetchall()
    cursor.close()
    conn.commit()


#    for i in range(0, 1000000):
#        print(i)




    print(result)
    print(sys.argv)

    ssss112233445566667777 = sys.argv

#for i in s.split(','):
#    print (i+ " "+sys.argv[i])
