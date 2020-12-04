# Single Defaul User
# import boto3

# iam_console = boto3.resource(service_name="iam", region_name="us-east-1")

# for each_user in iam_console.users.all():
#     print(each_user.name)

#############################################################
# Use Different Sessions
# iam_con_re = boto3.resource("iam")
# aws_mag_con = boto3.session.Session(profile_name="darmedes")
# ec2_con_resource = aws_mag_con.resource(
#     service_name="ec2", region_name="us-east-2")

#############################################################
# Implement Boto3 Scripts
import boto3

aws_management_console_darm = boto3.session.Session(profile_name="darmedes")

ec2 = aws_management_console_darm.resource('ec2')
