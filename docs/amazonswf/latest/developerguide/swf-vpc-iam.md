---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-iam.html
---

# Amazon Virtual Private Cloud Endpoint Policies for Amazon SWF
<a name="swf-vpc-iam"></a>

You can create an Amazon VPC endpoint policy for Amazon SWF in which you specify the following:
+ The **principal** that can perform actions.
+ The actions that can be performed.
+ The resources on which the actions can be performed.

The following example adds a specific IAM role to a policy:

```
"Principal": {
   "AWS": "arn:aws:iam::123456789012:role/MyRole"
}
```
+ For more information about creating endpoint policies, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html).
+ For information about how you can use IAM to control access to your AWS and Amazon SWF resources, see [Identity and Access Management in Amazon Simple Workflow Service](swf-dev-iam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
