---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/partner_response_sustainability.html
---

# Responding to requests as a Partner
<a name="partner_response_sustainability"></a>

As a Partner, you can accept or decline Partner requests, review and respond to data requests.

## Reviewing or responding to data requests
<a name="accepting_data_requests"></a>

 You will receive a daily digest letting you know if you have received any data requests within the last 24 hour period. Select the link in the email to view any new data requests.

![Reviewing data requests](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/reviewing_data_requests_example.png)

1. On the **Sustainability** page, under **Data Requests**, you will see all the data requests from your partners.

1. Under **Title**, choose the data request that you want to view or take action on.

1. On the **Sustainability** page, under **Please complete the following sections**, review and provide the requested information.

1. Choose **Submit response**.

1. You can choose to **Download** the data request. The download option downloads the template requested by the partner.

1. You can also choose to **Decline** to answer the data request. You will be prompted to provide a reason for choosing to decline to answer.

You can export data in bulk and the data responses are exported every 24 hours to your Amazon S3 bucket. The folder structure would be `s3://aws-supply-chain-data-{{Instance ID}}/export/DisclosureDataResponse/{{YYYY/MM/DD}}/{{Execution ID}}`. Under your Amazon S3 folder, you will find an audit history and a data response file for each data type.

## Reviewing and accepting partner invites
<a name="accepting_partner_invites"></a>

As a **Partner**, you should have received an email to join the AWS Supply Chain network. Select the link on the email to review and accept the invite.

**Note**
When you are accepting invites for the first time, you can view the onboarding pages that highlight the key features. This helps you to get familiar with the AWS Supply Chain capabilities.

1. On the AWS Supply Chain login page, enter the *username* which is the partner's email address.

   You will be sent a verification code to the same email you received the invite to join.

1. On the **Additional verification required** page, under **Verification code**, enter the verification code from the email.
**Note**
If you plan to use the same computer to log into AWS Supply Chain, after you use the verification code to access AWS Supply Chain for the first time, choose **Trusted device** on your computer to access AWS Supply Chain without the verification code the next time.

1. On the **Choose your password** page, create a password to sign into AWS Supply Chain.

1. On the **Complete your user profile** page, the *firstname* and *lastname* are auto-populated. Enter your *title* and *timezone*.

1. Choose **Next**.

1. On the **Let's add your organization's information** page, choose **Upload logo** to upload your organization's logo, and then enter the **Organization name**.

1. Choose **Complete setup**.

   The **Sustainability** page displays.

1. On the **Sustainability** page, under **Partner Network**, you can view all the invites that you have received.

1. Review and select a partner to accept or decline the invite.

   The **Sustainability** page displays with the partner details.

1. Choose **Accept connection**. You will see the **Invite accepted** message.
**Note**
If you choose to decline the invite, you must provide a reason on the **Decline connection invite** page.

## Reviewing or responding to emission data forms
<a name="emission_response"></a>

After you receive an emission data form request, you will view the request details and check the collaboration history.

![Partner response to emission data forms](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/emission_data_form4.png)

1. Under **Add country**, enter the countries where you have facilities and products within those facilities.
![Partner response to emission data forms - Add countries](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/emission_data_form5.png)

1. Choose **Add emission information** to add emission information for each country.
![Partner response to emission data forms - Add emission information](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/emission_data_form6.png)

1. Enter the emission information. All fields are mandatory.

## Reviewing or responding to transportation (GLEC) emission data forms
<a name="glec_emission_response"></a>

After you receive a transportation emission data form request, you will view the request details and check the collaboration history.

![Partner response to transportation (GLEC) emission data forms](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/GLEC_partner_response.png)

Under **Transport Emissions by Parcel**, download the .csv files, populate the .csv with the transport emissions, and upload the file. Choose **Submit**.

Make sure the information you populate in the .csv file is in the correct format. If not, you will receive a rework request explaining the issue in the .csv file.
