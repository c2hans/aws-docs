---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_evolve_ops_drivers_for_imp.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS11-BP05 Define drivers for improvement
<a name="ops_evolve_ops_drivers_for_imp"></a>

 Identify drivers for improvement to help you evaluate and prioritize opportunities.

 On AWS, you can aggregate the logs of all your operations activities, workloads, and infrastructure to create a detailed activity history. You can then use AWS tools to analyze your operations and workload health over time (for example, identify trends, correlate events and activities to outcomes, and compare and contrast between environments and across systems) to reveal opportunities for improvement based on your drivers.

 You should use CloudTrail to track API activity (through the AWS Management Console, CLI, SDKs, and APIs) to know what is happening across your accounts. Track your AWS developer Tools deployment activities with CloudTrail and CloudWatch. This will add a detailed activity history of your deployments and their outcomes to your CloudWatch Logs log data.

 [Export your log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) for long-term storage. Using [AWS Glue](https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc), you discover and prepare your log data in Amazon S3 for analytics. Use [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc), through its native integration with AWS Glue, to analyze your log data. Use a business intelligence tool like [Quick](https://aws.amazon.com/quicksight/) to visualize, explore, and analyze your data

 **Common anti-patterns:**
+  You have a script that works but is not elegant. You invest time in rewriting it. It is now a work of art.
+  Your start-up is trying to get another set of funding from a venture capitalist. They want you to demonstrate compliance with PCI DSS. You want to make them happy so you document your compliance and miss a delivery date for a customer, losing that customer. It wasn't a wrong thing to do but now you wonder if it was the right thing to do.

 **Benefits of establishing this best practice:** By determining the criteria you want to use for improvement, you can minimize the impact of event based motivations or emotional investment.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Understand drivers for improvement: You should only make changes to a system when a desired outcome is supported.
  +  Desired capabilities: Evaluate desired features and capabilities when evaluating opportunities for improvement.
    +  [What's New with AWS](https://aws.amazon.com/new/)
  +  Unacceptable issues: Evaluate unacceptable issues, bugs, and vulnerabilities when evaluating opportunities for improvement.
    +  [AWS Latest Security Bulletins](https://aws.amazon.com/security/security-bulletins/)
    +  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
  +  Compliance requirements: Evaluate updates and changes required to maintain compliance with regulation, policy, or to remain under support from a third party, when reviewing opportunities for improvement.
    +  [AWS Compliance](https://aws.amazon.com/compliance/)
    +  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
    +  [AWS Compliance Latest News](https://aws.amazon.com/compliance/compliance-latest-news/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
+  [Quick](https://aws.amazon.com/quicksight/)
+  [AWS Compliance](https://aws.amazon.com/compliance/)
+  [AWS Compliance Latest News](https://aws.amazon.com/compliance/compliance-latest-news/)
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
+  [AWS Glue](https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
+  [AWS Latest Security Bulletins](https://aws.amazon.com/security/security-bulletins/)
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
+  [Export your log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html)
+  [What's New with AWS](https://aws.amazon.com/new/)
