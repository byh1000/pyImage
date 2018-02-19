import pymssql
from io import BytesIO
from multiprocessing import Process
from urllib.request import urlopen

from flask import Flask

app = Flask(__name__)

ipdmList = []
impPathList = []


def trans_img(x):
    img_data = BytesIO(urlopen(x).read())
    return img_data

def ipdmSelect(skeys):
    conn = pymssql.connect(
        server='203.236.86.231',
        user='usr_wintelips2web',
        password='PoweR!Over^9Whelming',
        database='IPDM_UP_v2'
        )

    cursor = conn.cursor()
#    args=['WT','N', 'wips2017060', 'CC|DB|RDR|SKEY', '3518053000050,3518053000051,3518053000263,3518053000509,3518053000512,3518051000443,3518051000502,3518051000975,3518051000099,3518051000208', 'N', 0, '']
    args=['WT','N', 'wips2017060', 'CC|DB|RDR|SKEY', skeys, 'N', 0, '']
    cursor.callproc('download.up_list', args)

    cursor.nextset()
    result = cursor.fetchall()

    global ipdmList
    ipdmList = result
    for line in ipdmList:
        print(line)

    conn.commit()
    cursor.close()

    return result

def impPathSelect(skeys):
    conn = pymssql.connect(
        server='203.236.86.247',
        user='usr_wintelips2web',
        password='PoweR!Over^9Whelming',
        database='WT2MemberServicedb',
        charset='utf8'
    )
    cursor = conn.cursor()
    cursor.callproc('patent.up_srch_toc_exmp_img_path_select', [skeys])
    cursor.nextset()
    # result = list(cursor.fetchone())
    result = cursor.fetchall()
    global impPathList
    impPathList = result
    for line in result:
        print(line)

    conn.commit()
    cursor.close()

    return result

@app.route("/testPythonData", methods=['GET', 'POST'])
def receive_json():
#    print ("start")

    # print ("ipdmSelect start {}", "1")
    proIpdm1 = Process(target=ipdmSelect, args=("3518053000050,3518053000051",))
    proIpdm1.start()
    # print ("ipdmSelect end {}", "1")

    # print ("impPathSelect start {}", "2")
    proImpPath1 = Process(target=impPathSelect, args=("3518053000050,3518053000051",))
    proImpPath1.start()
    # print ("impPathSelect end {}", "2")

    proIpdm1.join()
    proImpPath1.join()

    print ("ipdm List start {}", "")
    for line in ipdmList:
        print(line)
#        for each in line:
#            print(each)
    print ("ipdm List end {}", "")
#
#     print ("impPath List start {}", "")
#     for line in impPathList:
#         print(line)
# #        for each in line:
# #            print(each)
#     print ("impPath List end {}", "")

    return "view4"



if __name__ == '__main__':
        app.debug = True
        #app.run(ssl_context='adhoc')
        app.run()
