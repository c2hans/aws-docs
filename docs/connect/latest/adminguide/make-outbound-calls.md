---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/make-outbound-calls.html
---

# Make outbound calls using the Contact Control Panel (CCP)
<a name="make-outbound-calls"></a>

Before you can make an outbound call, your contact center must be set up to allow agents to make calls. For more information, see [Step 3: Set telephony](amazon-connect-instances.md#get-started-telephony) in [Create a Connect Customer instance](amazon-connect-instances.md).

For information about the caller ID that's displayed when you make an outbound call, see [Set up outbound caller ID in Connect Customer](queues-callerid.md).

**Note**
**IT administrators**: For a list of countries available for outbound calls based on the Region of your instance, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/). If a country is not available in your dropdown menu, open a ticket to add it to your allow list. For more information, see [Countries that call centers using Connect Customer can call by default](country-code-allow-list.md).

**To make an outbound call**

1. In your Contact Control Panel, choose **Number pad**.

1. Use the dropdown menu to choose the country, then enter the number.
![The CCP, the number pad, the Call button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ccp-make-outbound-call.png)

1. Choose **Call**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
