import sys, os
import zlib, base64

sss = "eJx1XFmW4zgOvIqPwJ3g_S82jAW0s_rNR3Zm2RLFJQAEAlDXWtr89PaJz4z6qbV8Wp3-3T41yqeO-jn3V78f7_73o_2p7XzW_bS1T2txPzr39_js-MT9so_7zf22jE-7P3Uf3oBh7lft_onhYn1O_ez6WfeJdzpzfRom0-on7pAzPve-c2_Dk9tn3LvunxxwheZ5J9cwwfvoGveSO_idQh0Lw86G8TEJ_PDPxpnWuj_zPnZ-Bta8tDhMsq9PHA57f2Gp94vBf9whMfdxV3efcO46O6-7j8Q_Gv97H4EfjtR17eFImuronOnc_Kzqsfnoeid0p17jszThPXAfdgJf57jv8sNtK3cDNxeGD_PCe7B4uK89d1ETqwluZ2hP9vLEsd8z3ozvTRzRR_4zFP8Zn9GIAPz6nVhZmPGfj757UPOhdx6DEMExcar9Oz5WAPCFfl8EzX7RwjPBSQFWdyUTACAs7n_r4IYCubXfnwrYTQJzFs6KcLsXn409uDPAYs_k-ENYxwxwwHfwVu-2d-xThUHgN06vHB4N9ruewfm1i6IRPKCQUUw99344j-A6iPmDcw8h8T50awPbveIiApsGg8KodxEYI1E4cFbnJAppisDg0rHq9O7FwFUpvJiHDHzDOHFK_cHAmKMtCoSBD-4tBvoXW8HbsY2L4P-DvLQCfwTobW7Mu3181vpzsgYhjTDyb4wPjAuRv89_-BlcNr-qD3sGOu5r_x96d2_r9yMY1z3-CZ_zZu6FYNhK9MHcCj3O0Xms-d9J_WuIF3Tz33mfr3X4qy_eGqBUiJLaNhDOi_JxF-2AwIaDq5gRwJ0D-6K2aX7D2wb7FU6uU6h3wF6HDUG-jNjp__ou4kYe5sjj-txz3lEeZoLu9QFmPGBdL0JYX-TSex15r2u291BoAvH3PH9M_4ucP77re3LCOk6NSJEnp6eDE1mcT9OWDc4GqxHkgI7yrIWrGdqE_j38meAjiPYXRHm0nadEi-lwG5hKhyOJ8f9ghMntt8H0JYyIlUPJItNyWw4Py1i_pvl7Bv9x-S199_esPOLvlZUOjKfxNc37e21i4-7gnV2_g7U7t373EIH1Rs06m7z_negcctsT8fWCCf4Ws-tdpwhs3GUy5M7vZH8-qjyoCgtphdO4rhGnfqPunfGUmeBqOLeMiXCrh5yAT413emQfFZPfel6DU4axNVsKnjARG-B7N5007qiTYefuHw4ZbjK4RUN-HC6EMQezKMF9vquACWKzGp90vI5rmrDarpi7aER3VfcJ9-ODjZw0wzYX_TJMAUvDBSImi-cCn3BXAnOHsd6DQagC4u8916g5DvZp60Q3iRiAgmC3TIOA73vQg8PCgjKM2iwZ2IBFTKzTFxRiFOeO6Mm9vXO5m45ABVp1f7fuXV_bvKmSw4Hl4UF39fRXF_qHPA5nhw_wRR082bsyuBVsz-QSQhtBNA4iDBvN4YIgoA8B9sofMgVswz5_DEJPxIQvvJe4GNCx-Atnepe4FNuwSG5b59SbpoaNGY7GogBtcfk2ggbfdiHIfwZjSCMiC8HPlWGrMdLhz6yEVr3AWrQlbNZhBNVZFjqOwQ-9Ae3uAOHVF8cDXxjArTzI3X3aY-ji8i-qSBju7BZ9AyzgiEtMhwBA5AdVvq_qZICqxbM4mh735a67dbki7FqYhHZNyrEfw9yPQHxBsRoRTwJ1TYo4qjz5NnBghrfdF0wJJ91EMPD8RVcO6GJCdD_tD4a6METbbziS7dwixJvbMHoGocJDxrbeneqYwi6e9tZMAdcz_Xfh2QNtcMgniMkG1KdPAfqw_1UpQ38gJEaXY7SYDzMSpCJwkyCgyDAYdyr2mfSxKHvaNO6hRAqexQ6GexmaNdzTNZz1yKX8WdMWVO0f_Qtj1L0Fk5-VC3jOJeg_LjIHrRVI4P3k1MbAEmMAwLZ9U-PzudbNmeOgBjkHPNBWKLybjOcfPI47vMfXtcDtboYnupZ7_DjiuuTjhnxRo_9kYBmi2bCLJhzj-qHYDxO788Mo-OY0Bc5NB08E39UOBdtr_UgEN7MFHB0PU3deS2vwDpp8C-ZapFgFcZEwuo-FG4BXKAz8U2maJwobnj4mkgLGqskFw1PiBu5LMFq34ySjyDhmOLNQcGIGTbDeqIz0YSK3vJu0yWkWqVwTybLPxMrpPxu9BnfK3nHKrykeJYudiu9M6O1UM6RqK2H5cDoA2H2mPEUjl8VKph5ddOyLVn4Xie3qJh9wG9vhtEYyYSgEGA_fIhMV7wOKC7ExHv1JrnDniPljyxaJitNx2AWAUeXD7rKXOKhJlMaS14ct4JtKHjqYc2y5c3j1zaR4c0bE6z2INsMcEnZ17wbaC_0ktucwATkSQiYDH_wT7YZsdHn5VXjTXJIDie6CVCu9hD06jw4i8Q66dZTElPgorAnnP815sVLCeTBl2SFhg1YEKiIm38VzcGqc2ORkYLUAA3wGxBExdW5qpyKCzaK_VzwbylRA5A43Fwvz1bhSHO7uzOh_iT75tGj9BYlybwsorXIDtlJinlPjmZpYN5KoxKTo3pC6g4A65AKu4yTnLnSeJEhbHqFqlnR6W9pR6RJguiip4ZJmY1GBQyprJaildFVHiNkF_5MpRqNvwEaEtC2RUdHl-xFYrp9zz2a3l9Rv7SBlgQEIck5NfqqY9lgAgWeaSpcbCRmI47KDUfgZ1LjuiNBFCIKHSPIOInJx5nBWmzmS4lcYjqk-kQMOHuSiBrSrjLBwCMwYNEShSJpS1UrhFk77Rqz_oLESjdeSg4fFADLIgROK3VAc3CjukDSVofgPNIbRuITcRgDiFODJhuyq_-pSDfOdyl8xTcTYrRjghAnYXYpmCM4KU8xCB5w3PKCYh8hA_OaWP8LA95NpGco5WU03bAUrquAb9A8cUAktVoxAc33UYNyAz2NCEVrg4eYxWkAqlSyDRRXmtGM-qeQuljCf3Bv5TgYeeL1g5CN_olW2Reggcm55qwusKSV0OvkZ9KeYylLgmXIGhfrUVqImsSAxJtMJORiY-6SnKJwWQmzIZxwx_yZqL_I_pESk6jOpAMAVkWhOmcaROLyxywDNZoKDCWJv_ds5MMl8lbUiZ8AFQc-KXRlK6wDvdQTNrmOMj8GM_RXLmEMkeEtP0h5dS7tj9qZbT9e-yr-Gjm2HckXGokyRabckNkuTo6daUkM2sSxydNcAJ3_hi_0t3YIhtYtgHKOTsYYr8alK-mFym2gdAjeiJ-LHaeJR8vCry1IHZQvjaf5o45PiKenDz0eMhvxmDRIYOOSTDxMluZsUpFy4manUfALP4aLmV2OEU-vKILaSlCZ3CTp2uCs9z58UZmixTIfEdGHzISoTdhpF7qYpMtw1gh0ocDKUdpYLKCsHN9SHQH1ra2H0k-bI9zdc4FeeptOKnrC2sKqagCTCO_41tnaY1GEymzF3TDuutnb6jVNk7E6VGjxuCLzSlqIoNRv0yeQaG7uD6EoLHk5bqmsosDnBmuJEUD574ehGu1B6ASMjfMonc49kIVO6k7Rmnt6F0kX0pnkDdnSf11hB7Me0zAtTl-RfRNXC9DpEKYtcwZJRRy7-WLWY3JrKpEbCG4KKXPc0y0yxTJIwLEa2PfSU4QX0YnYrZjXlq_jk0Xy0EhmqkkISVuB9OS-lOuT6Vqi6QCLj0NiK2cVw_k_PW50GKarcJ636DUVH0hVvrwJ0kcawzYGKCgLIRGnolUNC9zpNWJjSpmyYBiR5kfVIErrBCBQzdcd77IAj9m74cOIdLU2iKEOP4sAIYC55lHZcatiyL6uRRdrgUCpMoYOJDljMkPSvuGtcEhdzybt2-9lYQvL8ppH6jukdcCHGyaJNMwN2VCUm28kCF5gS3E7RyhwhEV3F4oqISZiI4EirqDiD1VDeqdrJUF3t2J9CMqpeccjx0xm6zvGlCPwhj8GJCDiTZrFF4blKokl7f6js58W0jiGmmBZt1hC_8nWI6O7954k6oB9afrZCCY3yp_TiYS09eMAkJa4tMaAP5aFEAdxsJxwXA2hTVBvrVau0JBHdvy5RGKxEFE8yXA-eTN6tuTSXR1S7S_yHZGhXNL9lsGGGWmTMOOSRNa_DUAlauujKBpM_qmPcx2kZAfxkalnD0jD9HmWJ5rStkiPBPQwnRUUUuhG7W_EjdRJlggzuG8bftjbNOsOinDE0JdrRqTr7-RKI9QpUrMoELVJO3Go9npwl9eOjo3YIPWhn4a2mxxB16dUqXPuWGxRhgjKHDYYlTiI67Vx5dXRFc6sYKl3DcGd5qNKIoAiD1bfDSYZCu5gs8UTn_K0YonQxX-S8P6JObcpqV3WawWUtqggk-s5CLAannw5JCkfkmdmRL27UZkhziwTuIRqwlBJSXlTmB6a4m2TU8cYku7iOf1enVQNuVcQf2IbKAUrS5WMahQ658yU54SudTCkmIRnzKOckigqF8pBOWq3zUJ5zawJlZ9H2XLjKpa0pV2-UXIlDBS0gT34fQhgLg1PRqjlaKSQo6I7z8post95nGFtpc1Ji4RKhnjA1PCqUxc7a17ck27GxyKtCBlaVXYQcluyVi-hZkv25FSmRqw2TYs5RdqVcGbdRkwaDmln4peU6v8t6ZTcgUxjr-1vQV25I4ZLs1tS8yMBhA2HBr1rmo1VrB3Fee36ydDqH9zVLi8zOyI8lpDDekStY_2lTK5n66Ghyu1n6tdLU3JFj-3VB-V_4i3qczE2PKhdFSl-zYnVR0IaCuJ30heayem_4DjU0sP60KS5kfsF0QKpdioEqDy96aes6Crs4ekOvSp2ztxz1UQ7LZUeVbnX_NJ9_0T50aeldmhXOcSc4Bx3PVFkX1C1WYolOZ_xikO0SctDG4VLd9t1zBDawmPGoUjqW2tLq4cAmdcMfNPYfNFYG5l1tVAlIl7xdD69SJp2wdPqdsAutD5ajWPtx4X76CgU8aHjWcrfqKD_NE0xIN1Fm0TukkbSsbXQaPMFe3rfZ1oC5HOWa-LlmFKofxZ-EJ3mJtQ3rFi1HbQqrLvNmmZ17KkFGegPJv0oZqOYiqQ_Jv21Kmh8GOh2k1iLldzh8_qLtNSSx7gGoIfHLxgFF2OVcgEijrzyktPeu3vbbciUVmPAqKqXzkVbQWIhdEtv26-hypJWQwCNxeHfqPn48XTagubcJQbQbkJJ04MBVxWxKwCF3jaPMSZ1VTHNqqkjuCirKfId9DL0ja_30AvfjpszlSMKsLoEMBkJdO_rzz-drn96WJZbGqHJvztrYcGWp29SJZsynylaQvAO20qeRmrSn7pf9OvmW-l6a_PRuaXRhUSBkwPNrzlO5E2VH8fKQ3fW04mWpOVwnZLGESeJgo0RbZjcw4Lu1i2VTWOFS0xglo1c3qdmYE4q71C_pkOy1tkI6jpRK4HwZp5QM0dBhnQe-fTh1DhfdDzcCigiDKs9zazuWeARmVFkwVidQdfltarmoBTXdtPajW6BoGQglAJ3MqXQfFW5O7GkMyERxVGYBfCi9_qGyqGI3oLmY3Q2lCeJEkoJDrQSzve6gHR-nzINtoUp16ESYkjsdb07qJ8UyrA1teb37GyWjSD-prXEkJQgUnLAmsHGWvYvFYtUEqgqIUxsVVd0BPWtf1lwl2CpABvViPGDRIpaEePtE0g2fch1P93TeEuw3yR7bpiDqhJAHgFyweEGSw9GbAjZAcLmOAIukugkMDxfYuiqjLcm0ZHjkNnDlrJKqwwAVGN0NFzgY-EfLHqO72xhUog9Fo3jXVuLGrTBU35T4sUFFypMDj7VCxfStjWuqlB7ysblSeYJeCw01VL9Yrh7vlr0ewXOhDOKczu1VqnmvKmgxXqD1oMpWmCWRf1sq7KomBLOZGA7S1ZCD_16WEHe2jsj9sBEPjoUduO54cMtpTmQIIz3LknPz2Nij1j9uIgJLObmgbCnuVDpUbLcIanpvisayAPdtM4ybYA7FlWpPWtTDhMOkPE11bRzXNZeQSXtv7udjeXa4zaW1L2siR97qKjnVXQLHqZPYAZ5BovMYxrHJo36lTaWiodyqreNidvxKEeZniKWbv5AbbsITg0-V_MsWxT5MsaRN8hRHki_WZDuwAVweHdxqEh175iNZ1V40olAGR-buMm2TFR3144jOgKwP9ftV19icdBR1PyEod4kGkxLFkbJfn3jEgrRag3Z5ek48J6ckmdHddRi1N5csp6g9y-nkHbQXBp8xHQpkFZufLFGgrpIwc-2iugnc8ZTIEarOs9LqtkmpgCE-Cxw53E3poOw7oZS-XhMOBcW-LcSqNU_SVBCqsJpOtsWvOhmOHeHZz172kDpJsot-Fvb3THJeGgW9j8hXqK03tdNVklHz-zD1mFapmyiyFPUtn84r6jF91baq_j3dmcU0QiZbtyMkp7JI2OB8hnsJEsePz5o-V14M7TZl7yoRtolUBPe88i0GqsiZh-7MhL8fOQqIelsOHO9zmGRrr5jWdxbGmLAuy7vSYuqv4MdgQIq0upxG5UzXdJlePb0WA1Uje32GOcbYH9d2XjN5Y-60dpLSUIHqCIAc2d0OU3WmlxRtEVOYeVPNo7llZzV3FYgoHwpMIGvlJBfDqSyl024UhJ0eQtFBk2-naEJHmnRKuDBlpMRIqWUvh9c5TAz7zN9GXWXfRzQYxaNtTXFp5sfvkrhVWXyUd1lSmK-VbatFYlm9LcTmVhRSBhLTndFeCcMUQT3kYUMhKbrKmEM8KdzyrRbuUDU8FLlYYWe6s_UegV7nUeOJCX8w6RyqEimx_31BIHgMUvGb2zcoCHR6dZi-WhfoDNhv07MtVFpz1b4elaq2vOUhKdhanmpRK9JPTiUcS69UMPTzmEaW-8vTxYZbL6oej9ygCxlwzUt8na7NEXBxXLccbWeGr_N720LcwqPXGkbx6zZwNIPJU2tqZKKGy67zplc9Xiv7FDfbXfhQ22h1LQwVytUTNgSDoNiMAlKSTDpUS6GUP1LcdCUTKTRPYOQpPTDC8YQV7JoibzZpbnWOLeGDhQJGrxVeweG8I5uUkLXDrRQnEjt75tEocnRgTXhkRTfCNecvHtmzpVLxIkOUfM1CrJUka4ZwHT9yTMSXczzlTXLpc8tN_SCHgm6IxMzzpO2u14BUESRd3NpUn3Bd-Z7EKUpMSTNUzGNSQT-z1QehMuBSGXAsP4LBY_vFlZEjQzisehRXjMyeLe69uY3L7EISYaU8PF5vmHwtCqB80eT1N1b1pjlXWIb2VhckyxJHpw-xYNLt2ReVMBLl9jCH-GRzLZup01aJMPkJ2pPU_sXU49T0fr2c7JmoThMVjxZXtxQlqh6-rLa2rBQwuVluXHCBgdqOYGM_h2zU1dKqRqZpZkAhTdBRWVpxHo1jS-SvSB1Y4kEqvX393-JhgMW3lWXCphhzGHpVIl1-u-9b32NL-rLke9TaJXm4PdKmni2YyOSHLjSIJ7rhDLVe1O5Uz2S7DklJHHlh5bhbMtcZn2zY7NnH_BqXwj0NXRyzqK0V-lqX9r22CwYrnoc_lv3dNkPMj3QGVHakarBjQoy-Ou87KvW0NIWvzEJqHkwoZqbupGiHNcLlcvSRWEfDPMo5U4mg9tf2c8rHHx_Lbp7idtTe0lF35hdL-eJMSZzMTGkjy3t2FsM9ACt5C9nSVLwe7KaT00d9L3aatAvwkdJ0U40p0vNbNFG_V77EFCrjU4Ylp5Sg_317y_XRJxqcR8zcfcWXI92l951ClNdALoFHzjeJZZPbCjUkCJtQA4_I8lFFb79p7vc2Z5biDkWcyZqhQvDyCzwUhHS5pelslVFKtmtmCe4COsvNTV-pEcE6Q1bN3MkfUPFwwaTLAI_zM6ERjEdCO2sJ3HWwnmU1ClUgOm-i_EgKrO9dIJdZtAiCQt2ibOEMD6NklsbwW-yx_i8dgC6NWTj8SWcIZXRVcRlT2UpjtrSMI958RJMlqz1Cs78wnH_Z8LerYFS3TUX_BwwWs9WK8z2WmfZECxwG5HQjF6ettvAfQIq7pXRluUeA5DPVe6KCA5_ZzSL9wvWg8lD17eTwtg6E0L3NARKq7hQY74WRL9AtgVGG7czo1G54LHY2aVMyR4NS7qH393Kt6Pl4bbkqOTo76N5mbItbIKNkVFnflC9-GGjRKYcEgpWlOTrz-6_sgJNQqkqGzVBVgIjPD4WxmVuPJKdpn-xPpQXDI-mVBYvT2c_gNjbOYKk8YnrUZ75Tymp2Vbuj4jPdS5BYDClweIeFTRcUh4dqjOnx5FYKk25XwaI85zSSw30_hL9Tj0zSwP7r8pxM-jWclpz5297Er5RQixO8SGfM9Aygqqu78Y0zbqrIURep783iclxXHioVfYFs9n3y9dz2Xo2VQ30V4-zKkUKR_Rx-Ry8lBVZG_TrjliIX0wTAWu9kQ4y7__84de2NDQXe8GSdGuLF-78C_Fi8HKbKL_bo1e-TivRUTTX5pHMivfULLjNVXjXMuzSZle-wIkSHonl9IC_O4JWSN78Le_R6UcsJXQz9D1kFFe4="

def decompress_string(compressed_string):
  compressed_string = compressed_string.encode('utf8')
  if compressed_string == "":
    return None
  try:
    actual_string = zlib.decompress(base64.urlsafe_b64decode(compressed_string))
  except (zlib.error, TypeError):
    print "Could not decode base64 zlib string %s" % (compressed_string)
    return None
  return actual_string
  
print(decompress_string(sss))