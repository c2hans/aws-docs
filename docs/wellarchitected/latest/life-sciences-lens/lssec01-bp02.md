---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssec01-bp02.html
---

# LSSEC01-BP02 Maintain a history of IAM configurations and changes over time
<a name="lssec01-bp02"></a>

 By logging the IAM policy that was assigned to an IAM user, group, or role, you can determine the permissions that belonged to a user at a specific time. For example, you can view whether a user had permission to modify settings on a specific date in the past.

 **Desired outcome:** A complete history of IAM configurations is maintained and available for review.

 **Benefits of establishing this best practice:** Provide the ability to view the IAM policy that was assigned to an IAM user, group, or role over time.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Customize AWS Config to record configuration changes to IAM global resources in your home Region.

### Implementation steps
<a name="implementation-steps"></a>

1.  Determine a home AWS Region where you want AWS Config to record and store configuration changes to IAM resources, as the same IAM data is available in different AWS Regions.

1.  In your home region, enable recording by [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html) and enable recording of global resources or select specific IAM resources.

1.  Create a service control policy (SCP) to stop recording being turned off.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [How to Record and Govern Your IAM Resource Configurations Using AWS Config](https://aws.amazon.com/blogs/security/how-to-record-and-govern-your-iam-resource-configurations-using-aws-config/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
