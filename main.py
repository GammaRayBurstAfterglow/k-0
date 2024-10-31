import math
import numpy as np

###################################################
#
# Variable definitions and constant assignment
#
###################################################

# k = 0,2
# for now, only worried about k=0, but useful for future expansion
# For future iterations of the program, we will have a seperate match case system for k=2

b_values = [
1,2,3,7,9,10,11
]
# Spectral breaks needed to fulfil equations 5 and 9 from Granot and Sari
# Spectral breaks 1, 2, and 3 are needed for equation 5
# Spectral breaks 7, 9, 10, and 11 are needed for equation 9


nu = np.logspace(6, np.log10(2.418 * 10**26), 100)
# 100 values spaced evenly on a logarithmic scale from the range below
# range(10**(6), 2.418*(10**26))
# convert energies into frequencies
# KP - Converted TeV to Hz. Someone please check it just to make sure.


p = 2.23
# represents the spectral index of the electron distribution
# number of electrons with energy E is proportional to E^(-p)
# range between 2 - 4, 2.5 preferred value.

z = 1 
# cosmological red shift

epsilon_e = 0.1
#range(10**(-6), 0.4)
# fraction of the total energy density in electrons

epsilon_e_bar = (epsilon_e*(p-2)) / (p-1)

epsilon_B = 0.01
#range(10**(-9) 0.3)
# fraction total energy density in the magnetic field 

epsilon_p = 1 - (epsilon_e + epsilon_B)

n_0 = 1
#range(10**(-4), 10**(3))
# ambient density in units of particles/cm^3
# height of the density function for k = 0

E_52 = 1
#range(10**(-4), 10*(2))
# explosion energy of the GRB in units of 10^52 ergs

# A_star = 
# height of the density function for k = 2
# Only needed for k = 2, ignoring for now

t_days_values = [
1.157*(10**(-4)),
5.64*(10**(-2)),
5.585*(10**(-1)),
3.495,
13.831
]
# time since gamma ray burst in units of days(?)
# Set of 5 values taken from the output of GS2002.f90 to compare against
# [1.000E+01, 4.875E+03, 4.826E+04, 3.020E+05, 1.195E+06]
# iterations 0, 27, 37, 45, 51
# time since explosion in units of days in the observer frame(?)

d_L28 =  2.095 # (10**28)cm
# 6787.5 Mpc convert to 10^28
# luminosity distance in units of 10^28 cm
# ned wright cosmology calculator to convert z to d_L28
# Implement directly at some point if z != 1
# https://www.astro.ucla.edu/~wright/CosmoCalc.html



##############################################################
#
# BreakCase(): (Refer to line 328 of GS2002_test.f90)
# 
# This is the main file for the program. 
# BreakCase(): outputs equations 5 and 9 from Granot and Sari.
##############################################################


def BreakCase(b, t_days, nu):
	# b, t_days, and nu are passed arguments from __main__:


	# In future iterations, add If k = 0: (or another match case system) for spectral breaks where k = 2
	match(b):
	# Values for b, k, beta_1, beta_2, s, and nu_b are given by Granot and Sari

		# Break 1 for k = 0
		case(1):

			# Given values for b = 1 in Granot and Sari
			b = 1
			k = 0
			beta_1 = 2
			beta_2 = 1/3
			s = 1.64
			# nu_b = nu_sa
			# nu_sa is the self absortion frequency


			# Dummy variables for calculating nu_b
			# Dummy variation notation will follow as such for all break cases:
			# var_i = var_x_i for b = x and i being the iteration, x is understood by the case of BreakCase():
			var1 = (pow((p - 1), 3/5)) / (pow((3*p + 2), 3/5))
			var2 = pow((1 + z), -1)
			var3 = pow(epsilon_e_bar, -1)
			var4 = pow(epsilon_B, 1/5)
			var5 = pow(n_0, 3/5)
			var6 = pow(E_52, 1/5)

			# The frequency for the spectral break, b = 1, is the product of the dummy variables
			nu_1 = 1.24 * var1 * (10**9) * var2 * var3 * var4 * var5 * var6
			

			# Dummy variables for calculating nu_b_ext 
			# Dummy variation notation is slightly modified, but should be easily understood
			# var_x_ext_i for b = x and i being the iteration, x is understood by the case of BreakCase():
			var_1_ext_1 = (pow((p - 1), 6/5)) / ((3*p - 1)*(pow((3*p + 2), 1/5)))
			var_1_ext_2 = pow((1 + z), 1/2)
			var_1_ext_3 = pow(epsilon_e_bar, -1)
			var_1_ext_4 = pow(epsilon_B, 2/5)
			var_1_ext_5 = pow(n_0, 7/10)
			var_1_ext_6 = pow(E_52, 9/10)
			var_1_ext_7 = pow(t_days, 1/2)
			var_1_ext_8 = pow(d_L28, -2)


			# The external frequency for the spectral break, b = 1, is the product of the previous dummy variables
			nu_1_ext = 0.647 * var_1_ext_1 * var_1_ext_2 * var_1_ext_3 * var_1_ext_4 * var_1_ext_5 * var_1_ext_6 * var_1_ext_7 * var_1_ext_8


			# This flux density equation is taken from Granot and Sari and will be used to solve equation 5. 
			F_nu_1 = nu_1_ext * (pow((nu/nu_1), -s*beta_1) + pow((nu/nu_1), -s*beta_2))**(-1/s)


			# This is just for debugging, replace with file output
			#print(f'F_nu_1: {F_nu_1}')


			return F_nu_1



		# Break 2 for k = 0
		case(2):

			# Given values for b = 2 in Granot and Sari
			b = 2
			k = 0
			beta_1 = 1/3
			beta_2 = ((1-p)/2)
			s = (1.84-(0.40*p))
			# nu_b = nu_m
			# nu_b being the peak frequency, thus nu_2 should be larger than nu_1 and nu_3
			
			# Dummy variables for calculating nu_2
			var1 = (p - 0.67) * (10**15)
			var2 = pow((1 + z), 1/2)
			var3 = pow(E_52, 1/2)
			var4 = pow(epsilon_e_bar, 2)
			var5 = pow(epsilon_B, 1/2)
			var6 = pow(t_days, -3/2)

			nu_2 = 3.73 * var1 * var2 * var3 * var4 * var5 * var6

			F_tilde_2 = (1 + pow((nu/nu_2), s*(beta_1 - beta_2)))**(-1/s)

			#print(f'F_tilde_2: {F_tilde_2}')
			return F_tilde_2



		# Break 3 for k = 0
		case(3):

			# Given values for b = 3 in Granot and Sari
			b = 3
			k = 0
			beta_1 = ((1-p)/2)
			beta_2 = (-p/2)
			s = (1.15-(0.06*p))
			# nu_b = nu_c

			# Dummy variables for calculating nu_3
			var1 = (p - 0.46) * (10**13)
			var2 = math.exp(-1.16*p)
			var3 = pow((1 + z), -1/2)
			var4 = pow(epsilon_B, -3/2)
			var5 = pow(n_0, -1)
			var6 = pow(E_52, -1/2)
			var7 = pow(t_days, -1/2)
					  
			nu_3 = 6.37 * var1 * var2 * var3 * var4 * var5 * var6 * var7

			F_tilde_3 = (1 + pow((nu/nu_3), s*(beta_1 - beta_2)))**(-1/s)

			#print(f'F_tilde_3: {F_tilde_3}')
			return F_tilde_3



		# Break 7 for k = 0
		case(7):

			# Given values for b = 7 in Granot and Sari
			b = 7
			k = 0
			beta_1 = 2
			beta_2 = 11/8
			s = (1.99 - 0.04*p)
			#nu_b = nu_ac

			# dummy variables for calculating nu_7
			var1 = ( ((3*p-1)**(8/5)) / ((3*p+2)**(8/5)) )
			var2 = (1+z)**(-13/10)
			var3 = (epsilon_e_bar**(-8/5))
			var4 = (epsilon_B**(-2/5))
			var5 = (n_0**(3/10))
			var6 = (E_52**(-1/10))
			var7 = (t_days**(3/10))


			# Function given by nu_b of Granot and Sari
			nu_7 = 1.12 * var1 * (10**8) * var2 * var3 * var4 * var5 * var6 * var7


			#nu_7_ext: 

			#dummy variables to shorten nu_7_ext
			var_7_ext_1 = ((pow(3*p-1, 11/5)) / (pow(3*p+2, 11/5)))
			var_7_ext_2 = pow(1+z, -1/10)
			var_7_ext_3 = pow(epsilon_e_bar, -4/5)
			var_7_ext_4 = pow(epsilon_B, -4/5)
			var_7_ext_5 = pow(n_0, 1/10)
			var_7_ext_6 = pow(E_52, 3/10)
			var_7_ext_7 = pow(t_days, 11/10)
			var_7_ext_8 = pow(d_L28, -2)

			nu_7_ext = 5.27 * pow(10, -3) * var_7_ext_1 * var_7_ext_2 * var_7_ext_3 * var_7_ext_4 * var_7_ext_5 * var_7_ext_6 * var_7_ext_7 * var_7_ext_8

			F_nu_7 = nu_7_ext*( (nu/nu_7)**(-s * beta_1) + (nu/nu_7)**(-s * beta_2) )**(-1/s)

			#print(f'F_nu_7: {F_nu_7}')
			return F_nu_7



		# Break 9 for k = 0
		case(9):

			# Given values for b = 9 in Granot and Sari
			b = 9
			k = 0
			beta_1 = -1/2
			beta_2 = -p/2
			s = (3.34 - 0.82 * p)
			#nu_b = nu_m

			# dummy variables calculating nu_9
			var1 = (p - 0.74)
			var2 = (1 + z)**(1/2)
			var3 = epsilon_e_bar**2
			var4 = epsilon_B**(1/2)
			var5 = E_52**(1/2)
			var6 = t_days**(-3/2)

			# Function given by nu_b of Granot and Sari
			nu_9 = 3.94 * var1 * 10**15 * var2 * var3 * var4 * var5 * var6

			F_tilde_9 = ( 1 + (nu/nu_9)**(s * (beta_1 - beta_2) ) )**(-1/s)

			#print(f'F_tilde_9: {F_tilde_9}')
			return F_tilde_9


		# Break 10 for k = 0
		case(10):


			# Given values for b = 10 in Granot and Sari
			b = 10
			k = 0
			beta_1 = 11/8
			beta_2 = 1/3
			s = (1.213)
			#nu_b = nu_sa

			# Dummy variables to calculate nu_10
			var1 = (1+z)**(-1/2)
			var2 = epsilon_B**(6/5)
			var3 = n_0**(-1)
			var4 = E_52**(7/10)
			var5 = t_days**(-1/2)

			# Function given by nu_b of Granot and Sari
			nu_10 = 1.32 * 10**10 * var1 * var2 * var3 * var4 * var5 


			F_tilde_10= ( 1 + (nu/nu_10)**(s * (beta_1 - beta_2) ) )**(-1/s)

			#print(f'F_tilde_10: {F_tilde_10}')
			return F_tilde_10


		# Break 11 for k = 0
		case(11):


			# Given values for b = 11 in Granot and Sari
			b = 11
			k = 0
			beta_1 = 1/3
			beta_2 = -1/2
			s = 0.597
			#nu_b = nu_c

			#dummy variables to shorten nu_11
			var1 = pow((1+z), -1/2)
			var2 = pow(epsilon_B, -3/2)
			var3 = pow(n_0, -1)
			var4 = pow(E_52, -1/2)
			var5 = pow(t_days, -1/2)

			# Function given by nu_b of Granot and Sari
			nu_11 = 5.86 * 10**12 * var1 * var2 * var3 * var4

			F_tilde_11 = ( 1 + (nu/nu_11)**(s * (beta_1 - beta_2) ) )**(-1/s)

			#print(f'F_tilde_11: {F_tilde_11}')
			return(F_tilde_11)


		# Else case, I.E. invalid option for b, k, breaks code and outputs error message
		case _:
			print("Error: Invalid option for b, k")
			pass




##############################################################
#
# Corresponding flux density functions
#
# F and F_tilde are implemented directly into BreakCase():
#
##############################################################


# Needs to be implemented somewhere in __main__
#F5(F_nu_1, F_tilde_2, F_tilde_3)
#F9(F_nu_7, F_tilde_9, F_tilde_10, F_tilde_11)

def F5(F_nu_1, F_tilde_2, F_tilde_3):
	# Equation 5 from Granot and Sari
	# Concerned only with breaks, 1, 2, and 3

	F5 = F_nu_1 * F_tilde_2 * F_tilde_3
	#print(F5)
	return F5
	# Needs to output somewhere, preferably to a file

def F9(F_nu_7, F_tilde_9, F_tilde_10, F_tilde_11):
	# Equation 9 from Granot and Sari
	# Concerned only with breaks, 7, 9, 10, and 11
	
	F9 = F_nu_7 * F_tilde_9 * F_tilde_10 * F_tilde_11
	#print(F9)
	return F9	
	# Needs to output somewhere, preferably to a file


##############################################################
#
# MAIN
#
##############################################################




# runs code on startup
if __name__ == '__main__':

	# Loop through the specified days
	for t_days in t_days_values:
		print(f'\n\nResults for t_days={t_days}:\n')


		# These are each an array for the value t_days
		F_nu_1 = BreakCase(1, t_days, nu)
		F_tilde_2 = BreakCase(2, t_days, nu)
		F_tilde_3 = BreakCase(3, t_days, nu)

		# Multiplying each array f_nu_1, f_tilde_2, f_tilde_3 for F5

		# Do we need the F5 function ?

		F5_results = F5(F_nu_1, F_tilde_2, F_tilde_3)

		F_nu_7 = BreakCase(7, t_days, nu)
		F_tilde_9 = BreakCase(9, t_days, nu)
		F_tilde_10 = BreakCase(10, t_days, nu)
		F_tilde_11 = BreakCase(11, t_days, nu)
		
		F9_results = F9(F_nu_7, F_tilde_9, F_tilde_10, F_tilde_11)


		print(f"F5 values:\n{F5_results}")

		print(f"\nF9 values:\n{F9_results}")

		print(f"\n nu:\n{nu}")
  
