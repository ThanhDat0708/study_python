def sv_diem_max(list_sv):
    list_sv_max = list_sv[0]
    for sv in list_sv:
        if sv["diem"] > list_sv_max["diem"]:
            list_sv_max = sv
    return list_sv_max
def sv_diem_min(list_sv):
    list_sv_min = list_sv[0]
    for sv in list_sv:
        if sv["diem"] < list_sv_min["diem"]:
            list_sv_min = sv
    return list_sv_min