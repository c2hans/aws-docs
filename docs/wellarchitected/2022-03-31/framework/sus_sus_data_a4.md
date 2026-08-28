---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP03 Use lifecycle policies to delete unnecessary data
<a name="sus_sus_data_a4"></a>

 Manage the lifecycle of all your data and automatically enforce deletion timelines to minimize the total storage requirements of your workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define lifecycle policies for all your data classification types.
+  Set automated lifecycle policies to enforce lifecycle rules.
+  Delete unused volumes and snapshots.
+  Aggregate data where applicable based on lifecycle rules.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon ECR Lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)
+  [Amazon EFS lifecycle management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)
+  [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
+  [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)
+  [Managing your storage lifecycle on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)
+  [Object lifecycle policies in AWS Elemental MediaStore](https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle.html)

 **Related videos:**
+  [Amazon S3 Lifecycle](https://www.youtube.com/watch?v=53eHNSpaMJI&ab_channel=AmazonWebServices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
