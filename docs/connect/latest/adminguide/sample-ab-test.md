---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/sample-ab-test.html
---

# Sample flow in Connect Customer for A/B contact distribution testing
<a name="sample-ab-test"></a>

**Note**
This topic explains a sample flow that is included with Connect Customer. For information about locating the sample flows in your instance, see [Sample flows in Connect Customer](contact-flow-samples.md).

Type: Flow (inbound)

This flow shows how to perform an A/B call distribution based on a percentage. Here's how it works:

1. The **Play prompt** block uses Amazon Polly, the text-to-speech service, to say "Connect Customer will now simulate rolling dice by using the Distribute randomly block. Now rolling."

1. The contact reaches the **Distribute by percentage** block, which routes the customer randomly based on a percentage.

   **Distribute by percentage** simulates a dice roll, resulting in a values between 2 to 12 with different percentages. For example, there is 3 percent chance for the "2" option, 6 percent chance for the "3" option, and so on.

1. After the contact gets routed, the **Play prompt** tells the customer which number the dice rolled.

1. At the end of the sample, the **Transfer to flow** block transfers the customer back to the [Sample inbound flow](sample-inbound-flow.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
