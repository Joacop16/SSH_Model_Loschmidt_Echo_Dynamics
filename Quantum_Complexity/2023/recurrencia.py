from scipy.misc import derivative

def D_1(t):
    D_Kprima = derivative(D_0, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_0(t)*a_coefs[0] - b_coefs[0]*D_-1(t))/b_coefs[1]

def D_2(t):
    D_Kprima = derivative(D_1, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_1(t)*a_coefs[1] - b_coefs[1]*D_0(t))/b_coefs[2]

def D_3(t):
    D_Kprima = derivative(D_2, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_2(t)*a_coefs[2] - b_coefs[2]*D_1(t))/b_coefs[3]

def D_4(t):
    D_Kprima = derivative(D_3, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_3(t)*a_coefs[3] - b_coefs[3]*D_2(t))/b_coefs[4]

def D_5(t):
    D_Kprima = derivative(D_4, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_4(t)*a_coefs[4] - b_coefs[4]*D_3(t))/b_coefs[5]

def D_6(t):
    D_Kprima = derivative(D_5, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_5(t)*a_coefs[5] - b_coefs[5]*D_4(t))/b_coefs[6]

def D_7(t):
    D_Kprima = derivative(D_6, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_6(t)*a_coefs[6] - b_coefs[6]*D_5(t))/b_coefs[7]

def D_8(t):
    D_Kprima = derivative(D_7, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_7(t)*a_coefs[7] - b_coefs[7]*D_6(t))/b_coefs[8]

def D_9(t):
    D_Kprima = derivative(D_8, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_8(t)*a_coefs[8] - b_coefs[8]*D_7(t))/b_coefs[9]

def D_10(t):
    D_Kprima = derivative(D_9, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_9(t)*a_coefs[9] - b_coefs[9]*D_8(t))/b_coefs[10]

def D_11(t):
    D_Kprima = derivative(D_10, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_10(t)*a_coefs[10] - b_coefs[10]*D_9(t))/b_coefs[11]

def D_12(t):
    D_Kprima = derivative(D_11, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_11(t)*a_coefs[11] - b_coefs[11]*D_10(t))/b_coefs[12]

def D_13(t):
    D_Kprima = derivative(D_12, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_12(t)*a_coefs[12] - b_coefs[12]*D_11(t))/b_coefs[13]

def D_14(t):
    D_Kprima = derivative(D_13, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_13(t)*a_coefs[13] - b_coefs[13]*D_12(t))/b_coefs[14]

def D_15(t):
    D_Kprima = derivative(D_14, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_14(t)*a_coefs[14] - b_coefs[14]*D_13(t))/b_coefs[15]

def D_16(t):
    D_Kprima = derivative(D_15, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_15(t)*a_coefs[15] - b_coefs[15]*D_14(t))/b_coefs[16]

def D_17(t):
    D_Kprima = derivative(D_16, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_16(t)*a_coefs[16] - b_coefs[16]*D_15(t))/b_coefs[17]

def D_18(t):
    D_Kprima = derivative(D_17, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_17(t)*a_coefs[17] - b_coefs[17]*D_16(t))/b_coefs[18]

def D_19(t):
    D_Kprima = derivative(D_18, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_18(t)*a_coefs[18] - b_coefs[18]*D_17(t))/b_coefs[19]

def D_20(t):
    D_Kprima = derivative(D_19, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_19(t)*a_coefs[19] - b_coefs[19]*D_18(t))/b_coefs[20]

def D_21(t):
    D_Kprima = derivative(D_20, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_20(t)*a_coefs[20] - b_coefs[20]*D_19(t))/b_coefs[21]

def D_22(t):
    D_Kprima = derivative(D_21, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_21(t)*a_coefs[21] - b_coefs[21]*D_20(t))/b_coefs[22]

def D_23(t):
    D_Kprima = derivative(D_22, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_22(t)*a_coefs[22] - b_coefs[22]*D_21(t))/b_coefs[23]

def D_24(t):
    D_Kprima = derivative(D_23, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_23(t)*a_coefs[23] - b_coefs[23]*D_22(t))/b_coefs[24]

def D_25(t):
    D_Kprima = derivative(D_24, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_24(t)*a_coefs[24] - b_coefs[24]*D_23(t))/b_coefs[25]

def D_26(t):
    D_Kprima = derivative(D_25, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_25(t)*a_coefs[25] - b_coefs[25]*D_24(t))/b_coefs[26]

def D_27(t):
    D_Kprima = derivative(D_26, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_26(t)*a_coefs[26] - b_coefs[26]*D_25(t))/b_coefs[27]

def D_28(t):
    D_Kprima = derivative(D_27, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_27(t)*a_coefs[27] - b_coefs[27]*D_26(t))/b_coefs[28]

def D_29(t):
    D_Kprima = derivative(D_28, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_28(t)*a_coefs[28] - b_coefs[28]*D_27(t))/b_coefs[29]

def D_30(t):
    D_Kprima = derivative(D_29, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_29(t)*a_coefs[29] - b_coefs[29]*D_28(t))/b_coefs[30]

def D_31(t):
    D_Kprima = derivative(D_30, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_30(t)*a_coefs[30] - b_coefs[30]*D_29(t))/b_coefs[31]

def D_32(t):
    D_Kprima = derivative(D_31, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_31(t)*a_coefs[31] - b_coefs[31]*D_30(t))/b_coefs[32]

def D_33(t):
    D_Kprima = derivative(D_32, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_32(t)*a_coefs[32] - b_coefs[32]*D_31(t))/b_coefs[33]

def D_34(t):
    D_Kprima = derivative(D_33, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_33(t)*a_coefs[33] - b_coefs[33]*D_32(t))/b_coefs[34]

def D_35(t):
    D_Kprima = derivative(D_34, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_34(t)*a_coefs[34] - b_coefs[34]*D_33(t))/b_coefs[35]

def D_36(t):
    D_Kprima = derivative(D_35, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_35(t)*a_coefs[35] - b_coefs[35]*D_34(t))/b_coefs[36]

def D_37(t):
    D_Kprima = derivative(D_36, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_36(t)*a_coefs[36] - b_coefs[36]*D_35(t))/b_coefs[37]

def D_38(t):
    D_Kprima = derivative(D_37, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_37(t)*a_coefs[37] - b_coefs[37]*D_36(t))/b_coefs[38]

def D_39(t):
    D_Kprima = derivative(D_38, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_38(t)*a_coefs[38] - b_coefs[38]*D_37(t))/b_coefs[39]

def D_40(t):
    D_Kprima = derivative(D_39, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_39(t)*a_coefs[39] - b_coefs[39]*D_38(t))/b_coefs[40]

def D_41(t):
    D_Kprima = derivative(D_40, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_40(t)*a_coefs[40] - b_coefs[40]*D_39(t))/b_coefs[41]

def D_42(t):
    D_Kprima = derivative(D_41, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_41(t)*a_coefs[41] - b_coefs[41]*D_40(t))/b_coefs[42]

def D_43(t):
    D_Kprima = derivative(D_42, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_42(t)*a_coefs[42] - b_coefs[42]*D_41(t))/b_coefs[43]

def D_44(t):
    D_Kprima = derivative(D_43, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_43(t)*a_coefs[43] - b_coefs[43]*D_42(t))/b_coefs[44]

def D_45(t):
    D_Kprima = derivative(D_44, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_44(t)*a_coefs[44] - b_coefs[44]*D_43(t))/b_coefs[45]

def D_46(t):
    D_Kprima = derivative(D_45, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_45(t)*a_coefs[45] - b_coefs[45]*D_44(t))/b_coefs[46]

def D_47(t):
    D_Kprima = derivative(D_46, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_46(t)*a_coefs[46] - b_coefs[46]*D_45(t))/b_coefs[47]

def D_48(t):
    D_Kprima = derivative(D_47, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_47(t)*a_coefs[47] - b_coefs[47]*D_46(t))/b_coefs[48]

def D_49(t):
    D_Kprima = derivative(D_48, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_48(t)*a_coefs[48] - b_coefs[48]*D_47(t))/b_coefs[49]

def D_50(t):
    D_Kprima = derivative(D_49, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_49(t)*a_coefs[49] - b_coefs[49]*D_48(t))/b_coefs[50]

def D_51(t):
    D_Kprima = derivative(D_50, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_50(t)*a_coefs[50] - b_coefs[50]*D_49(t))/b_coefs[51]

def D_52(t):
    D_Kprima = derivative(D_51, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_51(t)*a_coefs[51] - b_coefs[51]*D_50(t))/b_coefs[52]

def D_53(t):
    D_Kprima = derivative(D_52, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_52(t)*a_coefs[52] - b_coefs[52]*D_51(t))/b_coefs[53]

def D_54(t):
    D_Kprima = derivative(D_53, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_53(t)*a_coefs[53] - b_coefs[53]*D_52(t))/b_coefs[54]

def D_55(t):
    D_Kprima = derivative(D_54, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_54(t)*a_coefs[54] - b_coefs[54]*D_53(t))/b_coefs[55]

def D_56(t):
    D_Kprima = derivative(D_55, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_55(t)*a_coefs[55] - b_coefs[55]*D_54(t))/b_coefs[56]

def D_57(t):
    D_Kprima = derivative(D_56, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_56(t)*a_coefs[56] - b_coefs[56]*D_55(t))/b_coefs[57]

def D_58(t):
    D_Kprima = derivative(D_57, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_57(t)*a_coefs[57] - b_coefs[57]*D_56(t))/b_coefs[58]

def D_59(t):
    D_Kprima = derivative(D_58, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_58(t)*a_coefs[58] - b_coefs[58]*D_57(t))/b_coefs[59]

def D_60(t):
    D_Kprima = derivative(D_59, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_59(t)*a_coefs[59] - b_coefs[59]*D_58(t))/b_coefs[60]

def D_61(t):
    D_Kprima = derivative(D_60, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_60(t)*a_coefs[60] - b_coefs[60]*D_59(t))/b_coefs[61]

def D_62(t):
    D_Kprima = derivative(D_61, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_61(t)*a_coefs[61] - b_coefs[61]*D_60(t))/b_coefs[62]

def D_63(t):
    D_Kprima = derivative(D_62, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_62(t)*a_coefs[62] - b_coefs[62]*D_61(t))/b_coefs[63]

def D_64(t):
    D_Kprima = derivative(D_63, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_63(t)*a_coefs[63] - b_coefs[63]*D_62(t))/b_coefs[64]

def D_65(t):
    D_Kprima = derivative(D_64, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_64(t)*a_coefs[64] - b_coefs[64]*D_63(t))/b_coefs[65]

def D_66(t):
    D_Kprima = derivative(D_65, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_65(t)*a_coefs[65] - b_coefs[65]*D_64(t))/b_coefs[66]

def D_67(t):
    D_Kprima = derivative(D_66, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_66(t)*a_coefs[66] - b_coefs[66]*D_65(t))/b_coefs[67]

def D_68(t):
    D_Kprima = derivative(D_67, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_67(t)*a_coefs[67] - b_coefs[67]*D_66(t))/b_coefs[68]

def D_69(t):
    D_Kprima = derivative(D_68, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_68(t)*a_coefs[68] - b_coefs[68]*D_67(t))/b_coefs[69]

def D_70(t):
    D_Kprima = derivative(D_69, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_69(t)*a_coefs[69] - b_coefs[69]*D_68(t))/b_coefs[70]

def D_71(t):
    D_Kprima = derivative(D_70, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_70(t)*a_coefs[70] - b_coefs[70]*D_69(t))/b_coefs[71]

def D_72(t):
    D_Kprima = derivative(D_71, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_71(t)*a_coefs[71] - b_coefs[71]*D_70(t))/b_coefs[72]

def D_73(t):
    D_Kprima = derivative(D_72, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_72(t)*a_coefs[72] - b_coefs[72]*D_71(t))/b_coefs[73]

def D_74(t):
    D_Kprima = derivative(D_73, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_73(t)*a_coefs[73] - b_coefs[73]*D_72(t))/b_coefs[74]

def D_75(t):
    D_Kprima = derivative(D_74, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_74(t)*a_coefs[74] - b_coefs[74]*D_73(t))/b_coefs[75]

def D_76(t):
    D_Kprima = derivative(D_75, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_75(t)*a_coefs[75] - b_coefs[75]*D_74(t))/b_coefs[76]

def D_77(t):
    D_Kprima = derivative(D_76, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_76(t)*a_coefs[76] - b_coefs[76]*D_75(t))/b_coefs[77]

def D_78(t):
    D_Kprima = derivative(D_77, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_77(t)*a_coefs[77] - b_coefs[77]*D_76(t))/b_coefs[78]

def D_79(t):
    D_Kprima = derivative(D_78, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_78(t)*a_coefs[78] - b_coefs[78]*D_77(t))/b_coefs[79]

def D_80(t):
    D_Kprima = derivative(D_79, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_79(t)*a_coefs[79] - b_coefs[79]*D_78(t))/b_coefs[80]

def D_81(t):
    D_Kprima = derivative(D_80, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_80(t)*a_coefs[80] - b_coefs[80]*D_79(t))/b_coefs[81]

def D_82(t):
    D_Kprima = derivative(D_81, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_81(t)*a_coefs[81] - b_coefs[81]*D_80(t))/b_coefs[82]

def D_83(t):
    D_Kprima = derivative(D_82, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_82(t)*a_coefs[82] - b_coefs[82]*D_81(t))/b_coefs[83]

def D_84(t):
    D_Kprima = derivative(D_83, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_83(t)*a_coefs[83] - b_coefs[83]*D_82(t))/b_coefs[84]

def D_85(t):
    D_Kprima = derivative(D_84, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_84(t)*a_coefs[84] - b_coefs[84]*D_83(t))/b_coefs[85]

def D_86(t):
    D_Kprima = derivative(D_85, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_85(t)*a_coefs[85] - b_coefs[85]*D_84(t))/b_coefs[86]

def D_87(t):
    D_Kprima = derivative(D_86, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_86(t)*a_coefs[86] - b_coefs[86]*D_85(t))/b_coefs[87]

def D_88(t):
    D_Kprima = derivative(D_87, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_87(t)*a_coefs[87] - b_coefs[87]*D_86(t))/b_coefs[88]

def D_89(t):
    D_Kprima = derivative(D_88, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_88(t)*a_coefs[88] - b_coefs[88]*D_87(t))/b_coefs[89]

def D_90(t):
    D_Kprima = derivative(D_89, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_89(t)*a_coefs[89] - b_coefs[89]*D_88(t))/b_coefs[90]

def D_91(t):
    D_Kprima = derivative(D_90, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_90(t)*a_coefs[90] - b_coefs[90]*D_89(t))/b_coefs[91]

def D_92(t):
    D_Kprima = derivative(D_91, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_91(t)*a_coefs[91] - b_coefs[91]*D_90(t))/b_coefs[92]

def D_93(t):
    D_Kprima = derivative(D_92, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_92(t)*a_coefs[92] - b_coefs[92]*D_91(t))/b_coefs[93]

def D_94(t):
    D_Kprima = derivative(D_93, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_93(t)*a_coefs[93] - b_coefs[93]*D_92(t))/b_coefs[94]

def D_95(t):
    D_Kprima = derivative(D_94, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_94(t)*a_coefs[94] - b_coefs[94]*D_93(t))/b_coefs[95]

def D_96(t):
    D_Kprima = derivative(D_95, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_95(t)*a_coefs[95] - b_coefs[95]*D_94(t))/b_coefs[96]

def D_97(t):
    D_Kprima = derivative(D_96, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_96(t)*a_coefs[96] - b_coefs[96]*D_95(t))/b_coefs[97]

def D_98(t):
    D_Kprima = derivative(D_97, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_97(t)*a_coefs[97] - b_coefs[97]*D_96(t))/b_coefs[98]

def D_99(t):
    D_Kprima = derivative(D_98, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_98(t)*a_coefs[98] - b_coefs[98]*D_97(t))/b_coefs[99]

def D_100(t):
    D_Kprima = derivative(D_99, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_99(t)*a_coefs[99] - b_coefs[99]*D_98(t))/b_coefs[100]

def D_101(t):
    D_Kprima = derivative(D_100, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_100(t)*a_coefs[100] - b_coefs[100]*D_99(t))/b_coefs[101]

def D_102(t):
    D_Kprima = derivative(D_101, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_101(t)*a_coefs[101] - b_coefs[101]*D_100(t))/b_coefs[102]

def D_103(t):
    D_Kprima = derivative(D_102, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_102(t)*a_coefs[102] - b_coefs[102]*D_101(t))/b_coefs[103]

def D_104(t):
    D_Kprima = derivative(D_103, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_103(t)*a_coefs[103] - b_coefs[103]*D_102(t))/b_coefs[104]

def D_105(t):
    D_Kprima = derivative(D_104, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_104(t)*a_coefs[104] - b_coefs[104]*D_103(t))/b_coefs[105]

def D_106(t):
    D_Kprima = derivative(D_105, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_105(t)*a_coefs[105] - b_coefs[105]*D_104(t))/b_coefs[106]

def D_107(t):
    D_Kprima = derivative(D_106, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_106(t)*a_coefs[106] - b_coefs[106]*D_105(t))/b_coefs[107]

def D_108(t):
    D_Kprima = derivative(D_107, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_107(t)*a_coefs[107] - b_coefs[107]*D_106(t))/b_coefs[108]

def D_109(t):
    D_Kprima = derivative(D_108, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_108(t)*a_coefs[108] - b_coefs[108]*D_107(t))/b_coefs[109]

def D_110(t):
    D_Kprima = derivative(D_109, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_109(t)*a_coefs[109] - b_coefs[109]*D_108(t))/b_coefs[110]

def D_111(t):
    D_Kprima = derivative(D_110, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_110(t)*a_coefs[110] - b_coefs[110]*D_109(t))/b_coefs[111]

def D_112(t):
    D_Kprima = derivative(D_111, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_111(t)*a_coefs[111] - b_coefs[111]*D_110(t))/b_coefs[112]

def D_113(t):
    D_Kprima = derivative(D_112, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_112(t)*a_coefs[112] - b_coefs[112]*D_111(t))/b_coefs[113]

def D_114(t):
    D_Kprima = derivative(D_113, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_113(t)*a_coefs[113] - b_coefs[113]*D_112(t))/b_coefs[114]

def D_115(t):
    D_Kprima = derivative(D_114, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_114(t)*a_coefs[114] - b_coefs[114]*D_113(t))/b_coefs[115]

def D_116(t):
    D_Kprima = derivative(D_115, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_115(t)*a_coefs[115] - b_coefs[115]*D_114(t))/b_coefs[116]

def D_117(t):
    D_Kprima = derivative(D_116, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_116(t)*a_coefs[116] - b_coefs[116]*D_115(t))/b_coefs[117]

def D_118(t):
    D_Kprima = derivative(D_117, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_117(t)*a_coefs[117] - b_coefs[117]*D_116(t))/b_coefs[118]

def D_119(t):
    D_Kprima = derivative(D_118, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_118(t)*a_coefs[118] - b_coefs[118]*D_117(t))/b_coefs[119]

def D_120(t):
    D_Kprima = derivative(D_119, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_119(t)*a_coefs[119] - b_coefs[119]*D_118(t))/b_coefs[120]

def D_121(t):
    D_Kprima = derivative(D_120, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_120(t)*a_coefs[120] - b_coefs[120]*D_119(t))/b_coefs[121]

def D_122(t):
    D_Kprima = derivative(D_121, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_121(t)*a_coefs[121] - b_coefs[121]*D_120(t))/b_coefs[122]

def D_123(t):
    D_Kprima = derivative(D_122, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_122(t)*a_coefs[122] - b_coefs[122]*D_121(t))/b_coefs[123]

def D_124(t):
    D_Kprima = derivative(D_123, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_123(t)*a_coefs[123] - b_coefs[123]*D_122(t))/b_coefs[124]

def D_125(t):
    D_Kprima = derivative(D_124, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_124(t)*a_coefs[124] - b_coefs[124]*D_123(t))/b_coefs[125]

def D_126(t):
    D_Kprima = derivative(D_125, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_125(t)*a_coefs[125] - b_coefs[125]*D_124(t))/b_coefs[126]

def D_127(t):
    D_Kprima = derivative(D_126, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_126(t)*a_coefs[126] - b_coefs[126]*D_125(t))/b_coefs[127]

def D_128(t):
    D_Kprima = derivative(D_127, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_127(t)*a_coefs[127] - b_coefs[127]*D_126(t))/b_coefs[128]

def D_129(t):
    D_Kprima = derivative(D_128, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_128(t)*a_coefs[128] - b_coefs[128]*D_127(t))/b_coefs[129]

def D_130(t):
    D_Kprima = derivative(D_129, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_129(t)*a_coefs[129] - b_coefs[129]*D_128(t))/b_coefs[130]

def D_131(t):
    D_Kprima = derivative(D_130, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_130(t)*a_coefs[130] - b_coefs[130]*D_129(t))/b_coefs[131]

def D_132(t):
    D_Kprima = derivative(D_131, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_131(t)*a_coefs[131] - b_coefs[131]*D_130(t))/b_coefs[132]

def D_133(t):
    D_Kprima = derivative(D_132, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_132(t)*a_coefs[132] - b_coefs[132]*D_131(t))/b_coefs[133]

def D_134(t):
    D_Kprima = derivative(D_133, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_133(t)*a_coefs[133] - b_coefs[133]*D_132(t))/b_coefs[134]

def D_135(t):
    D_Kprima = derivative(D_134, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_134(t)*a_coefs[134] - b_coefs[134]*D_133(t))/b_coefs[135]

def D_136(t):
    D_Kprima = derivative(D_135, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_135(t)*a_coefs[135] - b_coefs[135]*D_134(t))/b_coefs[136]

def D_137(t):
    D_Kprima = derivative(D_136, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_136(t)*a_coefs[136] - b_coefs[136]*D_135(t))/b_coefs[137]

def D_138(t):
    D_Kprima = derivative(D_137, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_137(t)*a_coefs[137] - b_coefs[137]*D_136(t))/b_coefs[138]

def D_139(t):
    D_Kprima = derivative(D_138, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_138(t)*a_coefs[138] - b_coefs[138]*D_137(t))/b_coefs[139]

def D_140(t):
    D_Kprima = derivative(D_139, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_139(t)*a_coefs[139] - b_coefs[139]*D_138(t))/b_coefs[140]

def D_141(t):
    D_Kprima = derivative(D_140, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_140(t)*a_coefs[140] - b_coefs[140]*D_139(t))/b_coefs[141]

def D_142(t):
    D_Kprima = derivative(D_141, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_141(t)*a_coefs[141] - b_coefs[141]*D_140(t))/b_coefs[142]

def D_143(t):
    D_Kprima = derivative(D_142, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_142(t)*a_coefs[142] - b_coefs[142]*D_141(t))/b_coefs[143]

def D_144(t):
    D_Kprima = derivative(D_143, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_143(t)*a_coefs[143] - b_coefs[143]*D_142(t))/b_coefs[144]

def D_145(t):
    D_Kprima = derivative(D_144, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_144(t)*a_coefs[144] - b_coefs[144]*D_143(t))/b_coefs[145]

def D_146(t):
    D_Kprima = derivative(D_145, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_145(t)*a_coefs[145] - b_coefs[145]*D_144(t))/b_coefs[146]

def D_147(t):
    D_Kprima = derivative(D_146, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_146(t)*a_coefs[146] - b_coefs[146]*D_145(t))/b_coefs[147]

def D_148(t):
    D_Kprima = derivative(D_147, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_147(t)*a_coefs[147] - b_coefs[147]*D_146(t))/b_coefs[148]

def D_149(t):
    D_Kprima = derivative(D_148, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_148(t)*a_coefs[148] - b_coefs[148]*D_147(t))/b_coefs[149]

def D_150(t):
    D_Kprima = derivative(D_149, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_149(t)*a_coefs[149] - b_coefs[149]*D_148(t))/b_coefs[150]

def D_151(t):
    D_Kprima = derivative(D_150, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_150(t)*a_coefs[150] - b_coefs[150]*D_149(t))/b_coefs[151]

def D_152(t):
    D_Kprima = derivative(D_151, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_151(t)*a_coefs[151] - b_coefs[151]*D_150(t))/b_coefs[152]

def D_153(t):
    D_Kprima = derivative(D_152, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_152(t)*a_coefs[152] - b_coefs[152]*D_151(t))/b_coefs[153]

def D_154(t):
    D_Kprima = derivative(D_153, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_153(t)*a_coefs[153] - b_coefs[153]*D_152(t))/b_coefs[154]

def D_155(t):
    D_Kprima = derivative(D_154, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_154(t)*a_coefs[154] - b_coefs[154]*D_153(t))/b_coefs[155]

def D_156(t):
    D_Kprima = derivative(D_155, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_155(t)*a_coefs[155] - b_coefs[155]*D_154(t))/b_coefs[156]

def D_157(t):
    D_Kprima = derivative(D_156, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_156(t)*a_coefs[156] - b_coefs[156]*D_155(t))/b_coefs[157]

def D_158(t):
    D_Kprima = derivative(D_157, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_157(t)*a_coefs[157] - b_coefs[157]*D_156(t))/b_coefs[158]

def D_159(t):
    D_Kprima = derivative(D_158, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_158(t)*a_coefs[158] - b_coefs[158]*D_157(t))/b_coefs[159]

def D_160(t):
    D_Kprima = derivative(D_159, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_159(t)*a_coefs[159] - b_coefs[159]*D_158(t))/b_coefs[160]

def D_161(t):
    D_Kprima = derivative(D_160, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_160(t)*a_coefs[160] - b_coefs[160]*D_159(t))/b_coefs[161]

def D_162(t):
    D_Kprima = derivative(D_161, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_161(t)*a_coefs[161] - b_coefs[161]*D_160(t))/b_coefs[162]

def D_163(t):
    D_Kprima = derivative(D_162, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_162(t)*a_coefs[162] - b_coefs[162]*D_161(t))/b_coefs[163]

def D_164(t):
    D_Kprima = derivative(D_163, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_163(t)*a_coefs[163] - b_coefs[163]*D_162(t))/b_coefs[164]

def D_165(t):
    D_Kprima = derivative(D_164, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_164(t)*a_coefs[164] - b_coefs[164]*D_163(t))/b_coefs[165]

def D_166(t):
    D_Kprima = derivative(D_165, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_165(t)*a_coefs[165] - b_coefs[165]*D_164(t))/b_coefs[166]

def D_167(t):
    D_Kprima = derivative(D_166, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_166(t)*a_coefs[166] - b_coefs[166]*D_165(t))/b_coefs[167]

def D_168(t):
    D_Kprima = derivative(D_167, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_167(t)*a_coefs[167] - b_coefs[167]*D_166(t))/b_coefs[168]

def D_169(t):
    D_Kprima = derivative(D_168, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_168(t)*a_coefs[168] - b_coefs[168]*D_167(t))/b_coefs[169]

def D_170(t):
    D_Kprima = derivative(D_169, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_169(t)*a_coefs[169] - b_coefs[169]*D_168(t))/b_coefs[170]

def D_171(t):
    D_Kprima = derivative(D_170, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_170(t)*a_coefs[170] - b_coefs[170]*D_169(t))/b_coefs[171]

def D_172(t):
    D_Kprima = derivative(D_171, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_171(t)*a_coefs[171] - b_coefs[171]*D_170(t))/b_coefs[172]

def D_173(t):
    D_Kprima = derivative(D_172, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_172(t)*a_coefs[172] - b_coefs[172]*D_171(t))/b_coefs[173]

def D_174(t):
    D_Kprima = derivative(D_173, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_173(t)*a_coefs[173] - b_coefs[173]*D_172(t))/b_coefs[174]

def D_175(t):
    D_Kprima = derivative(D_174, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_174(t)*a_coefs[174] - b_coefs[174]*D_173(t))/b_coefs[175]

def D_176(t):
    D_Kprima = derivative(D_175, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_175(t)*a_coefs[175] - b_coefs[175]*D_174(t))/b_coefs[176]

def D_177(t):
    D_Kprima = derivative(D_176, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_176(t)*a_coefs[176] - b_coefs[176]*D_175(t))/b_coefs[177]

def D_178(t):
    D_Kprima = derivative(D_177, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_177(t)*a_coefs[177] - b_coefs[177]*D_176(t))/b_coefs[178]

def D_179(t):
    D_Kprima = derivative(D_178, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_178(t)*a_coefs[178] - b_coefs[178]*D_177(t))/b_coefs[179]

def D_180(t):
    D_Kprima = derivative(D_179, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_179(t)*a_coefs[179] - b_coefs[179]*D_178(t))/b_coefs[180]

def D_181(t):
    D_Kprima = derivative(D_180, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_180(t)*a_coefs[180] - b_coefs[180]*D_179(t))/b_coefs[181]

def D_182(t):
    D_Kprima = derivative(D_181, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_181(t)*a_coefs[181] - b_coefs[181]*D_180(t))/b_coefs[182]

def D_183(t):
    D_Kprima = derivative(D_182, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_182(t)*a_coefs[182] - b_coefs[182]*D_181(t))/b_coefs[183]

def D_184(t):
    D_Kprima = derivative(D_183, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_183(t)*a_coefs[183] - b_coefs[183]*D_182(t))/b_coefs[184]

def D_185(t):
    D_Kprima = derivative(D_184, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_184(t)*a_coefs[184] - b_coefs[184]*D_183(t))/b_coefs[185]

def D_186(t):
    D_Kprima = derivative(D_185, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_185(t)*a_coefs[185] - b_coefs[185]*D_184(t))/b_coefs[186]

def D_187(t):
    D_Kprima = derivative(D_186, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_186(t)*a_coefs[186] - b_coefs[186]*D_185(t))/b_coefs[187]

def D_188(t):
    D_Kprima = derivative(D_187, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_187(t)*a_coefs[187] - b_coefs[187]*D_186(t))/b_coefs[188]

def D_189(t):
    D_Kprima = derivative(D_188, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_188(t)*a_coefs[188] - b_coefs[188]*D_187(t))/b_coefs[189]

def D_190(t):
    D_Kprima = derivative(D_189, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_189(t)*a_coefs[189] - b_coefs[189]*D_188(t))/b_coefs[190]

def D_191(t):
    D_Kprima = derivative(D_190, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_190(t)*a_coefs[190] - b_coefs[190]*D_189(t))/b_coefs[191]

def D_192(t):
    D_Kprima = derivative(D_191, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_191(t)*a_coefs[191] - b_coefs[191]*D_190(t))/b_coefs[192]

def D_193(t):
    D_Kprima = derivative(D_192, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_192(t)*a_coefs[192] - b_coefs[192]*D_191(t))/b_coefs[193]

def D_194(t):
    D_Kprima = derivative(D_193, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_193(t)*a_coefs[193] - b_coefs[193]*D_192(t))/b_coefs[194]

def D_195(t):
    D_Kprima = derivative(D_194, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_194(t)*a_coefs[194] - b_coefs[194]*D_193(t))/b_coefs[195]

def D_196(t):
    D_Kprima = derivative(D_195, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_195(t)*a_coefs[195] - b_coefs[195]*D_194(t))/b_coefs[196]

def D_197(t):
    D_Kprima = derivative(D_196, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_196(t)*a_coefs[196] - b_coefs[196]*D_195(t))/b_coefs[197]

def D_198(t):
    D_Kprima = derivative(D_197, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_197(t)*a_coefs[197] - b_coefs[197]*D_196(t))/b_coefs[198]

def D_199(t):
    D_Kprima = derivative(D_198, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_198(t)*a_coefs[198] - b_coefs[198]*D_197(t))/b_coefs[199]

def D_200(t):
    D_Kprima = derivative(D_199, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_199(t)*a_coefs[199] - b_coefs[199]*D_198(t))/b_coefs[200]

