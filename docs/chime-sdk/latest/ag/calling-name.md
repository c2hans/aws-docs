---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/calling-name.html
---

# Setting outbound calling names
<a name="calling-name"></a>

You can assign calling names to the phone numbers in your inventory. This applies to toll-based numbers only, and excludes toll-free numbers. The names appear to recipients of outbound calls. You can update the names every seven days.

**Note**
When you use an Amazon Chime SDK Voice Connector to place a call, that call is routed through a public switched telephone network to the telephone carrier of the called party. Some carriers don't support caller ID names, and some carriers don't use the Voice Connectors' CNAM database. As a result, a called party may not see calling names, or they might see a calling name different from the one you set.
US carriers are increasingly blocking or labeling phone numbers that exhibit spam or fraud characteristics, such as high call volumes and short or unanswered calls. To reduce the risk of your calls being similarly categorized, consider registering your outbound calls with the [Free Caller Registry](https://www.freecallerregistry.com/fcr/#) service.

The following sets of steps explain how to add outbound calling names.

**To set an outbound calling name**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, choose the number that you want to add the name to.

1. On the **Details** page, choose **Edit**.

1. In the **Calling name** box, enter a name. You can use up to 15 characters.

1. Choose **Save**.

Allow 72 hours for the system to add the name.

**To update a default calling name**
+ Repeat the procedure above. Allow 72 hours for the system to update the name.
