---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/aif-setup-inverting.html
---

# Changing the roles of the failover pair
<a name="aif-setup-inverting"></a>

When you set up for input failover in a MediaLive channel, you can reverse the roles of the two failover inputs, so that the primary input becomes the secondary input.

**To reverse the roles of the inputs**

1. From the list of input attachments, choose the first input that you attached.

1. In the **Automatic input failover settings** section, choose **Disable automatic input failover settings**.

1. Choose the second input and choose **Enable automatic input failover settings** for that input. The second input is now the primary input.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
