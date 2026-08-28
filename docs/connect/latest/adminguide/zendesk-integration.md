---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/zendesk-integration.html
---

# Embed the Connect Customer Contact Control Panel (CCP) into Zendesk
<a name="zendesk-integration"></a>

To integrate Connect Customer and Zendesk, you need:
+ An Connect Customer instance.
+ A [Zendesk Support](https://www.zendesk.com/support/) account and the [Contact Center add-on](https://www.zendesk.com/pricing/), or a Zendesk trial account.
+ A Zendesk for Contact Center instance configured by Zendesk.

Before installing the [Zendesk for Contact Center app](https://www.zendesk.com/marketplace/apps/support/1000872/amazon-connect-for-zendesk/) you need to connect your Zendesk for Contact Center instance to your Connect Customer instance using a CloudFormation stack installation. The template for this will be provided to you by Zendesk when your Zendesk for Contact Center instance is set up.

After your Zendesk for Contact Center instance is created and linked to your Connect Customer instance, install and configure the [Zendesk for Contact Center app](https://www.zendesk.com/marketplace/apps/support/1000872/amazon-connect-for-zendesk/) in your Zendesk Support account, and then connect the app with your Zendesk for Contact Center instance.

For more information, see the [Zendesk for Contact Center documentation](https://support.zendesk.com/hc/en-us/sections/9248688983706-Using-Zendesk-for-Contact-Center).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
