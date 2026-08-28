---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/porting.html
---

# Porting existing phone numbers
<a name="porting"></a>

**Important**
Starting Friday, March, 01, 2024, Amazon Chime SDK phone number porting requests moved to the **Account and billing** section of the AWS Support Center console. To create a new support case for phone number porting, choose **Account and billing**, open the **Services** dropdown menu, and choose **Chime (Number Management)**.

In addition to provisioning phone numbers, you can also port numbers from your phone carrier into your Amazon Chime SDK inventory. This includes toll-free numbers. You can use ported numbers with Amazon Chime SDK Voice Connectors, and Amazon Chime SDK SIP media applications.

The following sections explain how to port phone numbers.

**Topics**
+ [Prerequisites for porting numbers](#porting-prereqs)
+ [Porting phone numbers into the Amazon Chime SDK](#port-in)
+ [Submitting required documents](#submit-required-docs)
+ [Viewing request status](#view-port-status)
+ [Assigning ported numbers](#assign-ported-numbers)
+ [Porting phone numbers out of the Amazon Chime SDK](#port-out)
+ [Phone number porting status definitions](#porting-status-definitions)

## Prerequisites for porting numbers
<a name="porting-prereqs"></a>

You must have the following in order to port numbers:
+ A Letter of Agency (LOA). You must have an LOA for US and international phone numbers. Download the [Letter of Agency (LOA) form](https://d1.awsstatic.com/whitepapers/AmazonChimeLOA.pdf) and fill it out. If you are porting phone numbers from different carriers, fill out a separate LOA for each carrier.
**Note**
A number of countries have documentation requirements for porting phone numbers. For more information, see [Country requirements for phone numbers](phone-country-reqs.md), in this guide.
+ Before you can port phone numbers for Amazon Chime SDK Voice Connectors, you must create a Voice Connector. For more information, see [Creating an Amazon Chime SDK Voice Connector](create-voicecon.md).

## Porting phone numbers into the Amazon Chime SDK
<a name="port-in"></a>

You create a support request to port existing phone numbers into the Amazon Chime SDK.

**To port existing phone numbers into the Amazon Chime SDK**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Contact Us**, choose **Support**.

   That takes you to the AWS Support console.
**Note**
You can also go directly to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page. If you do, choose **Create case**, then follow the steps below.

1. Under **How can we help**, do the following:

   1. Choose **Account and billing**.

   1. From the **Service** list, choose **Chime SDK (Number Management)**.

   1. From the **Category** list, choose **Phone Number Port In**.

   1. Choose **Next step: Additional information**.

1. Under **Additional information**, do the following

   1. Under **Subject**, enter **Porting phone numbers in**.

   1. Under **Description**, enter the following information:

      For porting US numbers:
      + Billing Telephone Number (BTN) of the account.
      + Authorizing person’s name. This is the person in charge of account billing with the current carrier.
      + Current carrier, if known.
      + Service account number, if this information is present with the current carrier.
      + Service PIN, if available.
      + Service address and customer name, as they appear in your current carrier contract.
      + Requested date and time for the port.
      + (Optional) If you want to port your BTN, indicate one of the following options:
        + **I am porting my BTN and I want to replace it with a new BTN that I am providing. I can confirm that this new BTN is on the same account with the current carrier.**
        + **I am porting my BTN and I want to close out my account with my current carrier.**
        + **I am porting my BTN because my account is currently set up so that each phone number is its own BTN.** (Select this option only when your account with the current carrier is set up this way.)
        + After you choose one of the options listed above, attach your Letter of Agency (LOA) to the request.

      **For porting international numbers:**
      + You must use the SIP Media Application Dial-In product type for non-US phone numbers.
      + Type of number (Local or Toll-Free)
      + Existing phone numbers to port in.
      + Estimate usage volume
      + Country

   1. From the **Phone number type** list, select **Business Calling**, **SIP Media Application Dial-In**, or **Voice Connector**.

   1. Under **Phone number**, enter at least one phone number, even if you're porting multiple numbers.

   1. Under **Porting Date**, enter the desired porting date.

   1. Under **Porting Time**, enter the desired time.

   1. Choose **Next step: Solve now or contact us**.

1. Under **Solve now or contact us**, choose **Contact us**.

1. From the **Preferred contact language list**, choose a language

1. Choose **Web** or **Phone**. If you choose **Phone**, enter your phone number. When finished, choose **Submit**.

AWS Support lets you know whether your phone numbers can be ported from your existing phone carrier. If you can, you need to submit any required documents. The steps in the next section explain how to submit those documents.

## Submitting required documents
<a name="submit-required-docs"></a>

After AWS Support says you can port phone numbers, you need to submit any required documents. The following steps explain how.

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

## Viewing request status
<a name="view-port-status"></a>

To use the Amazon Chime SDK console to view the status of your porting requests.

**To view the status**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **Phone number management**.

1. Choose the **Orders** tab.

The **Status** column shows the status of your request.

The **FOC Date** column shows the expected Firm Order Commit date of your request.

The number and current port order status will also show in the **Inventory** and **Pending** tabs.

Support also contacts you with updates and requests for further information, as needed. For more information, see [Phone number porting status definitions](#porting-status-definitions), later in this section.

## Assigning ported numbers
<a name="assign-ported-numbers"></a>

After your existing phone carrier confirms that the LOA is correct, they review and approve the requested port. Then they provide Support with a Firm Order Commit (FOC) date and time for the port to occur.

**To assign numbers**
+
  + Assign Amazon Chime SDK Voice Connector numbers to your Voice Connectors.
  + For Amazon Chime SDK SIP Media Application Dial-In numbers, use SIP rules to assign numbers. For more information about SIP rules, refer to [Creating SIP rules](https://docs.aws.amazon.com/chime/latest/ag/create-sip-rule.html).

  The phone numbers are not activated for use until after the Firm Order Commit (FOC) date is established, as shown in the following steps. For more information, see [Managing phone number inventory](phone-inventory.md) and [Creating an Amazon Chime SDK Voice Connector](create-voicecon.md).

Support contacts you with the FOC to confirm that the date and time works for you.

**Note**
The phone numbers cannot place or receive calls until you assign them.

On the FOC date, the ported phone numbers are activated for use with the Amazon Chime SDK.

## Porting phone numbers out of the Amazon Chime SDK
<a name="port-out"></a>

You can port US and non-US numbers out of the Amazon Chime SDK. You follow a different process for each type of number. Expand the following sections as needed to learn more.

### Porting out US numbers
<a name="port-out-us-numbers"></a>

You port numbers out of Amazon Chime by initiating a porting request with your winning carrier. When submitting information to your winning carrier, include your AWS account ID as the account ID associated with the phone number being ported.

When the porting process finishes and your winning carrier has the numbers, you must unassign and delete those numbers from your inventory. For more information, see [Unassigning Voice Connector phone numbers](unassign-numbers.md) and [Deleting phone numbers](delete-phone.md) in this guide.

**Important**
The ability to port numbers out depends on the winning carrier’s ability to accept those numbers.
Verifying the authenticity of the winning carrier's port-out request is critical for the security of your phone number. If the account details are not correct (for example, there's an account ID mismatch), your port-out request may be rejected, causing delays and requiring you to resubmit your request.

#### (Optional) Requesting a PIN to protect your number
<a name="port-out-pin"></a>

For additional security, you can contact us to apply a PIN to your number. The winning carrier then uses that PIN. Follow these steps:

**To request a PIN**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Contact Us**, choose **Support**.

   That takes you to the AWS Support console.
**Note**
You can also go directly to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page. If you do, choose **Create case**, then follow the steps below.

1. Under **How can we help**, do the following:

   1. Choose **Account and billing**.

   1. From the **Service** list, choose **Chime SDK (Number Management)**.

   1. From the **Category** list, choose **Phone Number Port Out**.

   1. Choose **Next step: Additional information**.

1. Under **Additional information**, do the following

   1. Under **Subject**, enter **Porting phone numbers out**.

   1. Under **Description**, enter the following.

      **I would like to assign a pin to my phone number: Pin: ABCD123 Phone Number: 1234567890**
**Note**
You must provide an alphanumeric PIN of 4 - 10 characters.

AWS Support associates a PIN with the phone number. When requesting the port with your winning carrier, provide your AWS account ID and PIN. We will use that information to validate any port requests received for your number.

### Porting out international numbers
<a name="port-out-international-numbers"></a>

The following steps explain now to port international numbers out of the Amazon Chime SDK.

**To port phone numbers out**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Contact Us**, choose **Support**.

   That takes you to the Support console.
**Note**
You can also go directly to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page. If you do, choose **Create case**, then follow the steps below.

1. Under **How can we help**, do the following:

   1. Choose **Account and billing**.

   1. From the **Service** list, choose **Chime SDK (Number Management)**.

   1. From the **Category** list, choose **Phone Number Port Out**.

   1. Choose **Next step: Additional information**.

1. Under **Additional information**, do the following:

   1. Under **Subject**, enter **Porting phone numbers out**.

   1. Under **Description**, enter any relevant data.

Support responds with the appropriate next steps. You receive responses based on your selected contact methods and any email addresses you entered for additional contacts.

When the porting process finishes and the phone numbers are ported to your new carrier, unassign and delete the phone numbers from your Amazon Chime SDK inventory. For more information, see [Unassigning Voice Connector phone numbers](unassign-numbers.md) and [Deleting phone numbers](delete-phone.md).

## Phone number porting status definitions
<a name="porting-status-definitions"></a>

After you submit a request to port existing phone numbers into the Amazon Chime SDK, you can view the status of your porting request in the Amazon Chime SDK console under **Calling**, **Phone number management**, **Pending**.

Porting statuses and definitions include the following:

**CANCELLED**
Support cancelled the porting order because of an issue with the port, such as a cancellation request from the carrier or from you. Support contacts you with details.

**CANCEL\_REQUESTED**
Support is processing a cancellation of the porting order because of an issue with the port, such as a cancellation request from the carrier or from you. Support contacts you with details.

**CHANGE\_REQUESTED**
Support is processing your change request, and the carrier response is pending. Allow for additional processing time.

**COMPLETED**
Your porting order is completed, and your phone numbers are activated.

**EXCEPTION**
Support contacts you for additional details needed to complete the port request. Allow for additional processing time.

**FOC**
The FOC date is confirmed with the carrier. Support contacts you to confirm the date.

**PENDING DOCUMENTS**
Support contacts you for additional documents needed to complete the port request. Allow for additional processing time.

**SUBMITTED**
Your porting order is submitted, and the carrier response is pending.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
