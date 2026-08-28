---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/request-intl-numbers.html
---

# Requesting international phone numbers
<a name="request-intl-numbers"></a>

The steps in this section explain how to request international phone numbers for use with the Amazon Chime SDK. You can only use international numbers with the **SIP Media Application Dial-In** product type.

To purchase international numbers, regulations in many countries require you to have the following items:
+ A local address
+ Proof of your identity, from the Amazon Chime SDK or our carriers

Allow 2-6 weeks for the Amazon Chime SDK to fulfill your request. For more information about the documentation requirements for various countries, see [Country requirements for phone numbers](phone-country-reqs.md).

**To request international phone numbers in countries with identification requirements**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Contact Us**, choose **Support**.

   That takes you to the AWS Support console.
**Note**
You can also go directly to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page. If you do, choose **Create case**, then follow the steps below.

1. If it isn't already selected, choose **Account and billing**.

1. For **Service**, choose **Chime SDK (Number Management)**.

1. For **Category**, choose **Phone Number Requests**, then choose **Next step: Additional information**.

1. For **Subject**, enter **Provisioning international numbers**.

1. For **Issue or Description**, enter the following:
   + Individual or Business
   + Name (Individual Name or Business Name)
   + Type of number (Local or Toll-Free)
   + Country
   + Quantity of phone numbers

1. Under **Email**, enter the email address associated with your Amazon Chime administrator account, then choose **Submit request**.

   AWS Support responds to your support request via email to let you know whether the phone numbers can be provisioned. Once the numbers are provisioned, you can view them in the Amazon Chime SDK console. Under **Phone numbers**, choose **Phone number management**. Your numbers appear on the **Inventory** page.

1. Use SIP rules to assign the phone numbers to the appropriate SIP media application.

## Submitting required documents
<a name="submit-required-docs"></a>

After you receive the requested phone numbers, you submit any required documents. The following steps explain how.

**Note**
AWS Support provides a secure Amazon S3 link for uploading all requested documents. Do not proceed until you receive the link.

**To submit documents**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. Sign in to your AWS account, then open the Amazon S3 upload link generated specifically for your account.
**Note**
The link expires after ten days. It is generated specifically for the account that created the case. The link requires an authorized user from the account to perform the upload.

1. Choose **Add Files**, then select the identity documents related to your request.

1. Expand the **Permissions** section, and choose **Specify individual ACL permissions**.

1. At the end of the **Access control list (ACL)** section, choose **Add grantee**, then paste the key provided by AWS Support into the **Grantee** box.

1. Under **Objects**, choose the **Read** checkbox, then choose **Upload**.

After you provide the Letter of Agency (LOA), Support confirms with your existing phone carrier that the information on the LOA is correct. If the information provided on the LOA does not match the information that your phone carrier has on file, Support contacts you to update the information provided on the LOA.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
