---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-resiliency.html
---

# How Flink supports high availability and job resiliency
<a name="jobruns-flink-resiliency"></a>

The following sections outline how Flink makes jobs more reliable and highly available. It does this through built-in capabilities like Flink high availability and various recovery capabilities if failures occur.

**Topics**
+ [Using high availability (HA) for Flink Operators and Flink Applications](jobruns-flink-using-ha.md)
+ [Optimizing Flink job restart times for task recovery and scaling operations with Amazon EMR on EKS](jobruns-flink-restart.md)
+ [Graceful decommission of Spot Instances with Flink on Amazon EMR on EKS](jobruns-flink-decommission.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
