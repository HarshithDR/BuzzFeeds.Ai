# import mysql.connector

# def setup_db():
#   # Using mysql-connector-python
#   mydb = mysql.connector.connect(
#   host="localhost",       # or your host, e.g., "127.0.0.1"
#   user="root",    # your database username
#   password="root",# your database password
#   database="summaraize"   # the name of the database you want to connect to
#   )
#   return mydb


# # def get_userinterests(userid):
# #     try:
# #         db = setup_db()
# #         cursor = db.cursor()
# #         print(12)
# #         sql = "SELECT interests FROM summaraize.interests where useremailid = %s"
# #         cursor.execute(sql, (userid))
# #         return cursor.fetchall()
# #     except Exception as e:
# #         return {"success" : False, "error_message" : str(e)}
  
# # def accessuserfeed(userId):
# #     user_interests = get_userinterests(userId)
# #     print("here I am",user_interests)
# #     lst_user_interests = user_interests
# #     get_feeddetails(lst_user_interests,userId)
# #     return {'userId': userId, 'message': 'Im still under build'}

# # accessuserfeed('testuser123@gmail.com')

# # print(get_userinterests('testuser123@gmail.com'))

# db = setup_db()
# cursor = db.cursor()
# print(123)
# # val = 'testuser123@gmail.com'
# # sql = f'Select interests from summaraize.interests where useremailid = {val}'
# # cursor.execute(sql)
# # print(cursor.fetchall())


# # use this

# val = 'testuser123@gmail.com'
# sql = 'SELECT interests FROM summaraize.interests WHERE useremailid = %s'
# cursor.execute(sql, (val,))
# print(cursor.fetchall())


# Output from the database
# data = [('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, activex, actionx',), ('testx, activex, actionx',)]

# # Create a list by unpacking the tuples
# data_list = [item for item, in data]

# # Print the resulting list
# print(data_list)


# Output from the database
# data = [('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, activex, actionx',), ('testx, activex, actionx',)]

# # Flatten the list of tuples and split each string on ','
# fields = [field.strip() for row in data for field in row[0].split(',')]

# # Convert the list to a set to remove duplicates, then back to a list
# unique_fields = list(set(fields))

# print(unique_fields)

# from dataclasses import dataclass

# @dataclass
# class Position():
#     def __init__(self) -> None:
#         name = ""
#         lat = 0
    
# data = Position()
# data.name = "sdhgsdfg"
# data.lat = 324
# print(data)


# data = [('ssss.json',)]
# print(type(data[0][0]))


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import patches
# from scipy.signal import TransferFunction, tf2zpk

# # Define the transfer function G(s)
# numerator = [1, 2]
# denominator = [1, 3, 4, 2]
# tf = TransferFunction(numerator, denominator)

# # Compute poles and zeros
# zeros, poles, gain = tf2zpk(numerator, denominator)

# # Create a new figure
# fig, ax = plt.subplots()

# # Plot zeros
# ax.scatter(np.real(zeros), np.imag(zeros), color='blue', s=50, label='Zeros', zorder=5)
# ax.scatter(np.real(poles), np.imag(poles), color='red', s=50, label='Poles', zorder=5)

# # Set up the plot
# ax.axhline(y=0, color='k', lw=1)
# ax.axvline(x=0, color='k', lw=1)

# # Plotting Asymptotes for large values of k (if needed)
# total_poles = len(poles)
# total_zeros = len(zeros)
# asymptotes_angle = [180 + (360 / (total_poles - total_zeros)) * i for i in range(total_poles - total_zeros)]

# # Center of asymptotes
# center_of_asymptotes = (np.sum(poles) - np.sum(zeros)) / (total_poles - total_zeros)
# for angle in asymptotes_angle:
#     # Convert angle to radians
#     angle_rad = np.deg2rad(angle)
#     # Draw the asymptotes
#     ax.plot([center_of_asymptotes, center_of_asymptotes + 10*np.cos(angle_rad)],
#             [0, 10*np.sin(angle_rad)], 'g--')

# # Setting axis limits
# ax.set_xlim([-3, 1])
# ax.set_ylim([-3, 3])

# # Add grid and legend
# ax.grid(True)
# ax.legend()

# # Set labels and title
# ax.set_xlabel('Real Part')
# ax.set_ylabel('Imaginary Part')
# ax.set_title('Root Locus Plot')

# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# import control as ctl

# # Define the numerator and denominator of the transfer function G(s)
# numerator = [1, 2]   # s + 2
# denominator = [1, 4, 5, 2]  # s^3 + 4s^2 + 5s + 2

# # Create the transfer function
# G = ctl.TransferFunction(numerator, denominator)

# # Plot the root locus
# fig, ax = plt.subplots()
# rl_data = ctl.root_locus(G, grid=True, ax=ax)

# # Enhance plot
# ax.set_title('Root Locus of G(s) = (s+2)/((s+1)(s^2+2s+2))')
# ax.set_xlabel('Real Axis')
# ax.set_ylabel('Imaginary Axis')

# # Show the plot
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # Define the transfer function numerator and denominator coefficients
# numerator = [100, 10000]
# denominator = [1, 700, 100000]

# # Create the transfer function
# sys = signal.TransferFunction(numerator, denominator)

# # Frequency range for Bode plot
# w = np.logspace(-1, 4, 1000)

# # Calculate frequency response
# w, mag, phase = signal.bode(sys, w)

# # Plot Bode magnitude plot
# plt.figure()
# plt.semilogx(w, mag)
# plt.title('Bode Magnitude Plot')
# plt.xlabel('Frequency [rad/s]')
# plt.ylabel('Magnitude [dB]')
# plt.grid(True)
# plt.show()

# # Plot Bode phase plot
# plt.figure()
# plt.semilogx(w, phase)
# plt.title('Bode Phase Plot')
# plt.xlabel('Frequency [rad/s]')
# plt.ylabel('Phase [degrees]')
# plt.grid(True)
# plt.show()