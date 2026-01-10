# Programmers: Jaden Alesi, Ryan Bodner, Cassandra Lanza
# Course: CS-255 Introduction to Artificial Intelligence
# Date Submitted: November 3, 2025
#
#
# Task: Use fuzzy logic to analyze customer satisfaction from four input categories
# and three output attributes.

import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


# Defining variable ranges
# All ratings range from 0 - 100

x_productQuality = np.arange(0, 101, 1)
x_timeliness = np.arange(0, 101, 1)
x_support = np.arange(0, 101, 1)
x_overallExperience = np.arange(0, 101, 1)

# x_productQuality = ctrl.Antecedent(np.arange(0, 100, 1), 'productQuality')
# x_timeliness = ctrl.Antecedent(np.arange(0, 100, 1), 'timeliness')
# x_support = ctrl.Antecedent(np.arange(0, 100, 1), 'support')
# x_overallExperience = ctrl.Antecedent(np.arange(0, 100, 1), 'overallExperience')


# Data Input

input_quality = int (input("Quality: "))
input_time = int (input("Delivery Timeliness: "))
input_support = int (input("Support Service: "))
input_experience = int (input("Overall Experience: "))

# Data Output
y_satisfaction = np.arange(0, 101, 1)
y_loyalty = np.arange(0, 101, 1)
y_retention_risk = np.arange(0, 101, 1)

# x_satisfaction = ctrl.Consequent(np.arange(0, 100, 1), 'satisfaction')
# x_loyalty = ctrl.Consequent(np.arange(0, 100, 1), 'loyalty')
# x_retention_risk = ctrl.Consequent(np.arange(0, 100, 1), 'retention_risk')


# Membership Functions

# Product Quality
productQuality_vd = fuzz.gauss2mf(x_productQuality, -30, 2, 10, 5)
productQuality_d = fuzz.gauss2mf(x_productQuality, 20, 7, 40, 5)
productQuality_n = fuzz.gauss2mf(x_productQuality, 45, 7, 55, 5)
productQuality_s = fuzz.gauss2mf(x_productQuality, 60, 7, 80, 5)
productQuality_vs = fuzz.gauss2mf(x_productQuality, 90, 7, 130, 5)

# x_productQuality['very_dissatisfied'] = productQuality_vd
# x_productQuality['dissatisfied'] = productQuality_d
# x_productQuality['neutral'] = productQuality_n
# x_productQuality['satisfied'] = productQuality_s
# x_productQuality['very_satisfied'] = productQuality_vs

# Timeliness
timeliness_vl = fuzz.trapmf(x_timeliness, [0, 0, 5, 20])
timeliness_l  = fuzz.trapmf(x_timeliness, [5, 15, 40, 50])
timeliness_o  = fuzz.trapmf(x_timeliness, [35, 45, 55, 65])
timeliness_e  = fuzz.trapmf(x_timeliness, [50, 60, 85, 95])
timeliness_ve = fuzz.trapmf(x_timeliness, [80, 95, 100, 100])

# x_timeliness['very_late'] = timeliness_vl
# x_timeliness['late'] = timeliness_l
# x_timeliness['on_time'] = timeliness_o
# x_timeliness['early'] = timeliness_e
# x_timeliness['very_early'] = timeliness_ve

# Support Service
support_p = fuzz.gauss2mf(x_support, -30, 2, 10, 5)              # Copied from Product Quality
support_f = fuzz.gauss2mf(x_support, 20, 7, 40, 5)
support_g = fuzz.gauss2mf(x_support, 45, 7, 55, 5)
support_v = fuzz.gauss2mf(x_support, 60, 7, 80, 5)
support_e = fuzz.gauss2mf(x_support, 90, 7, 130, 5)

# x_support['poor'] = support_p
# x_support['fair'] = support_f
# x_support['good'] = support_g
# x_support['very_good'] = support_v
# x_support['excellent'] = support_e

# Overall Experience
overallExperience_n = fuzz.trapmf(x_overallExperience, [0, 0, 15, 25])
overallExperience_sn = fuzz.trapmf(x_overallExperience, [15, 25, 35, 45])
overallExperience_neu = fuzz.trapmf(x_overallExperience, [35, 45, 55, 65])
overallExperience_p = fuzz.trapmf(x_overallExperience, [55, 65, 75, 85])
overallExperience_vp = fuzz.trapmf(x_overallExperience, [75, 85, 100, 100])

# x_overallExperience['negative'] = overallExperience_n
# x_overallExperience['slightly_negative'] = overallExperience_sn
# x_overallExperience['neutral'] = overallExperience_neu
# x_overallExperience['positive'] = overallExperience_p
# x_overallExperience['very_positive'] = overallExperience_vp

# Satisfaction Level
y_satisfaction_l = fuzz.trapmf(y_satisfaction, [0, 0, 20, 40])
y_satisfaction_m = fuzz.trimf(y_satisfaction, [30, 50, 70])
y_satisfaction_h = fuzz.trimf(y_satisfaction, [60, 80, 100])

# Loyalty Likelihood
y_loyalty_l = fuzz.trapmf(y_loyalty, [0, 0, 20, 40])
y_loyalty_m = fuzz.trimf(y_loyalty, [30, 50, 70])
y_loyalty_h = fuzz.trimf(y_loyalty, [60, 80, 100])

# Customer Retention Risk
y_retention_risk_l = fuzz.trapmf(y_retention_risk, [0, 0, 20, 40])
y_retention_risk_m = fuzz.trimf(y_retention_risk, [30, 50, 70])
y_retention_risk_h = fuzz.trimf(y_retention_risk, [60, 80, 100])

# Membership Degrees - Fuzzification

# Product Quality
productQuality_fit_vd = fuzz.interp_membership(x_productQuality, productQuality_vd, input_quality)
productQuality_fit_d = fuzz.interp_membership(x_productQuality, productQuality_d, input_quality)
productQuality_fit_n = fuzz.interp_membership(x_productQuality, productQuality_n, input_quality)
productQuality_fit_s = fuzz.interp_membership(x_productQuality, productQuality_s, input_quality)
productQuality_fit_vs = fuzz.interp_membership(x_productQuality, productQuality_vs, input_quality)

# Timeliness
timeliness_fit_vl = fuzz.interp_membership(x_timeliness, timeliness_vl, input_time)
timeliness_fit_l = fuzz.interp_membership(x_timeliness, timeliness_l, input_time)
timeliness_fit_o = fuzz.interp_membership(x_timeliness, timeliness_o, input_time)
timeliness_fit_e = fuzz.interp_membership(x_timeliness, timeliness_e, input_time)
timeliness_fit_ve = fuzz.interp_membership(x_timeliness, timeliness_ve, input_time)

# Support Service
support_fit_p = fuzz.interp_membership(x_support, support_p, input_support)
support_fit_f = fuzz.interp_membership(x_support, support_f, input_support)
support_fit_g = fuzz.interp_membership(x_support, support_g, input_support)
support_fit_v = fuzz.interp_membership(x_support, support_v, input_support)
support_fit_e = fuzz.interp_membership(x_support, support_e, input_support)

# Overall Experience
overallExperience_fit_n = fuzz.interp_membership(x_overallExperience, overallExperience_n, input_experience)
overallExperience_fit_sn = fuzz.interp_membership(x_overallExperience, overallExperience_sn, input_experience)
overallExperience_fit_neu = fuzz.interp_membership(x_overallExperience, overallExperience_neu, input_experience)
overallExperience_fit_p = fuzz.interp_membership(x_overallExperience, overallExperience_p, input_experience)
overallExperience_fit_vp = fuzz.interp_membership(x_overallExperience, overallExperience_vp, input_experience)

# Rule Base
# Outputs : Satisfaction Level, Loyalty Likelihood, Customer Retention Risk

#Satisfaction Level (High -> Medium -> Low)
rule1s = np.fmin(np.fmin(np.fmin(np.fmax(np.fmax(productQuality_fit_vs, productQuality_fit_s), productQuality_fit_n), np.fmax(timeliness_fit_o, timeliness_fit_e)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g)), np.fmax(overallExperience_fit_vp, overallExperience_fit_p)) #high
rule2s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_vs, productQuality_fit_s), np.fmax(np.fmax(timeliness_fit_o, timeliness_fit_e), timeliness_fit_l)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g)), np.fmax(overallExperience_fit_vp, overallExperience_fit_p)) #high
rule3s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_vs, productQuality_fit_s), np.fmax(timeliness_fit_o, timeliness_fit_e)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g)), np.fmax(overallExperience_fit_vp, overallExperience_fit_p)) #high
rule4s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_vs, productQuality_fit_s), np.fmax(timeliness_fit_o, timeliness_fit_e)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g)), np.fmax(np.fmax(overallExperience_fit_vp, overallExperience_fit_p), overallExperience_fit_neu)) #high

rule5s = np.fmin(np.fmin(np.fmin(np.fmax(np.fmax(productQuality_fit_n, productQuality_fit_d), productQuality_fit_vd), np.fmax(np.fmax(timeliness_fit_o, timeliness_fit_e), timeliness_fit_ve)), np.fmax(np.fmax(support_fit_v, support_fit_g), support_fit_f)), np.fmax(overallExperience_fit_p, overallExperience_fit_neu)) #medium
rule6s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_n, productQuality_fit_s), np.fmax(np.fmax(timeliness_fit_e, timeliness_fit_ve), timeliness_fit_l)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g)), np.fmax(overallExperience_fit_p, overallExperience_fit_vp)) #medium
rule7s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_n, productQuality_fit_s), np.fmax(np.fmax(timeliness_fit_o, timeliness_fit_e), timeliness_fit_ve)), np.fmax(np.fmax(support_fit_g, support_fit_f), support_fit_p)), np.fmax(overallExperience_fit_p, overallExperience_fit_neu)) #medium
rule8s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_n, productQuality_fit_s), np.fmax(np.fmax(timeliness_fit_o, timeliness_fit_e), timeliness_fit_ve)), np.fmax(support_fit_g, support_fit_f)), np.fmax(np.fmax(overallExperience_fit_p, overallExperience_fit_neu), overallExperience_fit_sn)) #medium

rule9s = np.fmin(np.fmin(np.fmin(np.fmax(productQuality_fit_d, productQuality_fit_vd), np.fmax(timeliness_fit_l, timeliness_fit_vl)), np.fmax(support_fit_f, support_fit_p)), np.fmax(overallExperience_fit_n, overallExperience_fit_sn))#low

#Loyalty Liklihood (High -> Medium -> Low)
rule1l = np.fmin(np.fmax(np.fmax(productQuality_fit_vs, productQuality_fit_s), productQuality_fit_n), np.fmax(overallExperience_fit_vp, overallExperience_fit_p))
rule2l = np.fmin(np.fmax(productQuality_fit_vs, productQuality_fit_s), np.fmax(np.fmax(overallExperience_fit_vp, overallExperience_fit_p), overallExperience_fit_neu))

rule3l = np.fmin(productQuality_fit_s, np.fmax(np.fmax(overallExperience_fit_p, overallExperience_fit_sn), overallExperience_fit_neu))
rule4l = np.fmin(np.fmax(productQuality_fit_s, productQuality_fit_n), overallExperience_fit_p)

rule5l = np.fmin(np.fmax(productQuality_fit_d, productQuality_fit_vd), np.fmax(np.fmax(overallExperience_fit_p, overallExperience_fit_sn), overallExperience_fit_neu))
rule6l = np.fmin(np.fmax(productQuality_fit_d, productQuality_fit_vd), np.fmax(np.fmax(overallExperience_fit_sn, overallExperience_fit_neu), overallExperience_fit_n))

#Retention Risk (Low -> Medium -> High)
rule1r = np.fmin(np.fmin(np.fmax(np.fmax(productQuality_fit_vs, productQuality_fit_s), productQuality_fit_n), np.fmax(overallExperience_fit_vp, overallExperience_fit_p)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g))
rule2r = np.fmin(np.fmin(np.fmax(productQuality_fit_vs, productQuality_fit_s), np.fmax(np.fmax(overallExperience_fit_vp, overallExperience_fit_p), overallExperience_fit_neu)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g))
rule3r = np.fmin(np.fmin(np.fmax(productQuality_fit_vs, productQuality_fit_s), np.fmax(overallExperience_fit_vp, overallExperience_fit_p)), np.fmax(np.fmax(support_fit_e, support_fit_v), support_fit_g))

rule4r = np.fmin(np.fmin(np.fmax(productQuality_fit_n, productQuality_fit_d), np.fmax(overallExperience_fit_neu, overallExperience_fit_p)), np.fmax(np.fmax(support_fit_f, support_fit_v), support_fit_g))
rule5r = np.fmin(np.fmin(np.fmax(productQuality_fit_n, productQuality_fit_s), np.fmax(np.fmax(overallExperience_fit_neu, overallExperience_fit_p), overallExperience_fit_sn)), np.fmax(np.fmax(support_fit_f, support_fit_v), support_fit_g))

rule6r = np.fmin(np.fmin(np.fmax(productQuality_fit_d, productQuality_fit_vd), np.fmax(overallExperience_fit_n, overallExperience_fit_sn)), support_fit_p)

# Inference Engine

# out_satis_high = np.fmax(np.fmax(np.fmax(rule1s, rule2s), rule3s), rule4s) 
# out_satis_medium = np.fmax(np.fmax(np.fmax(rule5s, rule6s), rule7s), rule8s)
# out_satis_low = rule9s

# out_loyal_high = np.fmax(rule1l, rule2l)
# out_loyal_medium = np.fmax(rule3l, rule4l)
# out_loyal_low = np.fmax(rule5l, rule6l)

# out_risk_low = np.fmax(np.fmax(rule1r, rule2r), rule3r)
# out_risk_medium = np.fmax(rule4r, rule5r)
# out_risk_high = rule6r

out_satis_high = np.fmax(np.fmin(rule1s, y_satisfaction_h), np.fmax(np.fmin(rule2s, y_satisfaction_h), np.fmax(np.fmin(rule3s, y_satisfaction_h), np.fmin(rule4s, y_satisfaction_h))))
out_satis_medium = np.fmax(np.fmin(rule5s, y_satisfaction_m), np.fmax(np.fmin(rule6s, y_satisfaction_m), np.fmax(np.fmin(rule7s, y_satisfaction_m), np.fmin(rule8s, y_satisfaction_m))))
out_satis_low = np.fmin(rule9s, y_satisfaction_l)

out_loyal_high = np.fmax(np.fmin(rule1l, y_loyalty_h), np.fmin(rule2l, y_loyalty_h))
out_loyal_medium = np.fmax(np.fmin(rule3l, y_loyalty_m), np.fmin(rule4l, y_loyalty_m))
out_loyal_low = np.fmax(np.fmin(rule5l, y_loyalty_l), np.fmin(rule6l, y_loyalty_l))

out_risk_low = np.fmax(np.fmin(rule1r, y_retention_risk_l), np.fmax(np.fmin(rule2r, y_retention_risk_l), np.fmin(rule3r, y_retention_risk_l)))
out_risk_medium = np.fmax(np.fmin(rule4r, y_retention_risk_m), np.fmin(rule5r, y_retention_risk_m))
out_risk_high = np.fmin(rule6r, y_retention_risk_h)

# Function Plots

plt.plot(x_productQuality, productQuality_vd, label="Very Dissatisfied")
plt.plot(x_productQuality, productQuality_d, label="Dissastisfied")
plt.plot(x_productQuality, productQuality_n, label="Neutral")
plt.plot(x_productQuality, productQuality_s, label="Satisfied")
plt.plot(x_productQuality, productQuality_vs, label="Very Satisfied")
plt.legend()
plt.xlabel("Quality Rating")
plt.ylabel("Degree of Membership")
plt.show()
plt.savefig("quality_membership_functions.png")

plt.figure()
plt.plot(x_timeliness, timeliness_ve, label="Very Early")
plt.plot(x_timeliness, timeliness_e, label="Early")
plt.plot(x_timeliness, timeliness_o, label="On Time")
plt.plot(x_timeliness, timeliness_l, label="Late")
plt.plot(x_timeliness, timeliness_vl, label="Very Late")
plt.legend()
plt.xlabel("Timeliness Rating")
plt.ylabel("Degree of Membership")
plt.savefig("timeliness_membership_functions.png")
plt.show()

plt.figure()
plt.plot(x_support, support_p, label="Poor")
plt.plot(x_support, support_f, label="Fair")
plt.plot(x_support, support_g, label="Good")
plt.plot(x_support, support_v, label="Very Good")
plt.plot(x_support, support_e, label="Excellent")
plt.legend()
plt.xlabel("Support Service Rating")
plt.ylabel("Degree of Membership")
plt.savefig("support_membership_functions.png")
plt.show()

plt.figure()
plt.plot(x_overallExperience, overallExperience_n, label="Negative")
plt.plot(x_overallExperience, overallExperience_sn, label="Slightly Negative")
plt.plot(x_overallExperience, overallExperience_neu, label="Neutral")
plt.plot(x_overallExperience, overallExperience_p, label="Positive")
plt.plot(x_overallExperience, overallExperience_vp, label="Very Positive")
plt.legend()
plt.xlabel("Overall Experience Rating")
plt.ylabel("Degree of Membership")
plt.savefig("experience_membership_functions.png")
plt.show()


# defuzzifier
# combine all levels into one fuzzy set

out_satisfaction = np.fmax(np.fmax(out_satis_low, out_satis_medium), out_satis_high)
out_loyalty = np.fmax(np.fmax(out_loyal_low, out_loyal_medium), out_loyal_high)
out_retention = np.fmax(np.fmax(out_risk_low, out_risk_medium), out_risk_high)

# defuzzification - get the value

sat_defuzzied = fuzz.defuzz(y_satisfaction, out_satisfaction, 'centroid')
loy_defuzzied = fuzz.defuzz(y_loyalty, out_loyalty, 'centroid')
ret_defuzzied = fuzz.defuzz(y_retention_risk, out_retention, 'centroid')

# Find membership of crisp value

sat_result = fuzz.interp_membership(y_satisfaction, out_satisfaction, sat_defuzzied)
loy_result = fuzz.interp_membership(y_loyalty, out_loyalty, loy_defuzzied)
ret_result = fuzz.interp_membership(y_retention_risk, out_retention, ret_defuzzied)


print("Satisfaction Level: ", sat_defuzzied)
print(sat_result)
print("Loyalty Likelihood: ", loy_defuzzied)
print(loy_result)
print("Customer Retention Risk: ", ret_defuzzied)
print(ret_result)