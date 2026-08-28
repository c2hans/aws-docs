---
source_url: https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-rec-considerations.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Additional considerations for Amazon EC2 instance recommendations in AWS Migration Hub
<a name="ec2-rec-considerations"></a>

Keep the following considerations in mind when generating Amazon EC2 instance recommendations.
+ Burstable instances (T2 and T3) have an additional pricing mechanism that is computed based on CPU credits. For the burstable instances, we use the provided `average` and `peak` CPU data points to compute an estimated number of consumed CPU credits. This is translated into an adjusted overall recommendation.
+ Only current generation instances are recommended. The following types of instances are excluded from recommendations:
  + Previous generation instances (C3, for example)
  + Bare Metal instances
  + ARM instances (A1, for example)
  + 32-bit instances
+ If the operating system for a server is not supported by Amazon EC2, that server's returned recommendation will be `Linux`. Additional information can be found in the `Recommendation.EC2.Remarks` column for each affected server.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
