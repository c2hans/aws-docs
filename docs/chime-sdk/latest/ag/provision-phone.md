---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/provision-phone.html
---

# Provisioning phone numbers
<a name="provision-phone"></a>

You use the Amazon Chime SDK console to provision phone numbers for your Amazon Chime SDK account. Choose from the following approaches:
+ Amazon Chime SDK Voice Connectors – Integrate with an existing phone system. For more information, see [Managing Amazon Chime SDK Voice Connectors](voice-connectors.md).
+ Amazon Chime SDK SIP media applications – Integrate with Amazon Chime SDK meetings and interactive voice response services such as Amazon Lex. For more information, see [Managing SIP media applications](manage-sip-applications.md).

You provision phone numbers from a pool of numbers provided by the Amazon Chime SDK. When provisioning finishes, the phone numbers appear in your inventory, and you can assign them to individual users.

**Important**
You only follow these steps for countries that do not have identification requirements. For information about provisioning phone numbers in countries with identification requirements, see [Requesting international phone numbers](request-intl-numbers.md).

**To provision phone numbers**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone numbers**, choose **Phone number management**.

1. Choose the **Orders** tab, then choose **Provision phone numbers**.

1. In the **Provision phone numbers** dialog box, choose **Voice Connector**, or **SIP Media Application Dial-In**, then choose **Next**.
**Note**
The product type assigned to a phone number affects your billing. If you set a default calling name, the system assigns it to newly provisioned phone numbers in the United States. Also, for Voice Connector and SIP media application outbound calls, the caller ID must match a number in your inventory. Alternately, for SIP media applications, it may match the original caller ID from an inbound call that was sent back by the associated Lambda function. For example, the function could use the `CallAndBridge` action. For more information, see [Setting outbound calling names](calling-name.md) in this guide, and [CallAndBridge](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-and-bridge.html) in the *Amazon Chime SDK Developer Guide*.

1. On the **Provision phone numbers** page, do the following:
   + Open the **Select Application Type** list and choose one of the options, **Voice Connector** or **SIP Media Application Dial-in**.

     Your choice affects the countries that you see in step 6.
   + (Optional) Under **Phone number(s) details**, in the **Name** box, enter a descriptive name for the phone number, such as a cost center or office location.

     This field differs from outbound calling names. For more information about outbound calling names, refer to [Setting outbound calling names](calling-name.md) in this guide.

1. Under **Number Search**, open the **Country** list and select a country, then do one of the following:
   + For numbers outside the U.S.:

     1. Open the **Type** list and select an option.

        Depending on the country you select, one of the types may not be available. For example, you can only select local numbers for Canada and toll-free numbers for Italy.

     1. Choose the **Search** button.
   + For U.S. numbers:

     1. Open the **Type** list and select an option.

     1. Open the **Area** list and choose **Location** or **Area code**.
        + If you choose **Location**, open the **State** list and choose a state, then enter a city and choose the **Search** button.
**Note**
If the search doesn't return numbers, clear the **City** field and search again.
        + If you choose **Area code**, enter an area code in the **Area Code** box and choose the **Search** button.

1. From the resulting list, select one or more phone numbers.

1. (Optional) Under **Phone number(s) details**, enter a name for the number or numbers. If you selected multiple numbers in the previous steps, the name applies to all of them.

1. Choose **Create Phone Number Order**.

The phone numbers appear in the **Orders** and **Pending** tabs while the provisioning occurs. When provisioning finishes, the numbers appear on the **Inventory** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
