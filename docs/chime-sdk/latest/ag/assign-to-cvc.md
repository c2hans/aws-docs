---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/assign-to-cvc.html
---

# Assigning numbers to a Voice Connector or Voice Connector group
<a name="assign-to-cvc"></a>

The following steps explain how to assign phone numbers to Amazon Chime SDK Voice Connectors and Voice Connector groups. Assigning numbers enables you to place calls.

You can assign individual numbers or groups of numbers to Voice Connectors and Voice Connector groups. The following sets of steps explain how.

**To assign individual phone numbers**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, choose the phone number that you want to assign, then choose **Edit**.

1. (Optional) In the **Calling name** box, enter a name for the phone number.

1. Under **Product type**, ensure that **Voice Connector** is selected

1. Under **Assignment type**, choose **Voice Connector** or **Voice Connector group**, then do one of the following.

   1. If you chose **Voice Connector**, open the **Voice Connector options** list and select a Voice Connector.

   1. If you chose **Voice Connector group**, open the **Voice Connector group options** list and select a Voice Connector group.

1. Choose **Save**.

**To assign groups of phone numbers**

1. On the **Inventory** tab, select the check boxes next to the phone numbers that you want to assign.
**Note**
The phone numbers must have the **Voice Connector** product type. Also, check the **Status** column and make sure you only select unassigned numbers.

1. Choose **Assign**, and in the **Assignment Type** dialog box, choose **Voice connector** or **Voice connector group**.

1. Choose **Assign**, and in the **Assign phone numbers** dialog box, choose **Voice Connector** or **Voice Connector group**, then choose **Next**.

1. Select the Voice Connector or Voice Connector group, then choose **Assign**.
