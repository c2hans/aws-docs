---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/ai-opt-out.html
---

# AI-based services and AWS Control Tower
<a name="ai-opt-out"></a>

You can create service control policies (SCPs) that allow you to opt out of having your data stored by AI-based services on AWS. These SCP policies specify that AI-based services, such as Amazon Rekognition or Amazon CodeWhisperer, cannot store and use your data to improve other AI-based AWS services.

These AI opt-out SCP policies can apply to your entire organization, to an OU, or to a specific account. The policies are global in effect. You can find more information about these policies at [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html), in the AWS Organizations documentation.

For a list of AWS services that use AI, along with examples of policies, see [AI services opt-out policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.html), in the *AWS Organizations User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
