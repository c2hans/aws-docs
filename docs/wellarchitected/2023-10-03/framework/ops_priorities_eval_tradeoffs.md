---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_priorities_eval_tradeoffs.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS01-BP06 Evaluate tradeoffs
<a name="ops_priorities_eval_tradeoffs"></a>

 Evaluate the impact of tradeoffs between competing interests or alternative approaches, to help make informed decisions when determining where to focus efforts or choosing a course of action. For example, accelerating speed to market for new features may be emphasized over cost optimization, or you may choose a relational database for non-relational data to simplify the effort to migrate a system, rather than migrating to a database optimized for your data type and updating your application.

 AWS can help you educate your teams about AWS and its services to increase their understanding of how their choices can have an impact on your workload. You should use the resources provided by [AWS Support](https://aws.amazon.com/premiumsupport/programs/) ([AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/), [AWS Discussion Forums](https://forums.aws.amazon.com/index.jspa), and [AWS Support Center](https://console.aws.amazon.com/support/home/)) and [AWS Documentation](https://docs.aws.amazon.com/) to educate your teams. Reach out to AWS Support through AWS Support Center for help with your AWS questions.

 AWS also shares best practices and patterns that we have learned through the operation of AWS in [The Amazon Builders' Library](https://aws.amazon.com/builders-library/). A wide variety of other useful information is available through the [AWS Blog](https://aws.amazon.com/blogs/) and [The Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast/).

 **Common anti-patterns:**
+  You are using a relational database to manage time series and non-relational data. There are database options that are optimized to support the data types you are using but you are unaware of the benefits because you have not evaluated the tradeoffs between solutions.
+  Your investors request that you demonstrate compliance with Payment Card Industry Data Security Standards (PCI DSS). You do not consider the tradeoffs between satisfying their request and continuing with your current development efforts. Instead you proceed with your development efforts without demonstrating compliance. Your investors stop their support of your company over concerns about the security of your platform and their investments.

 **Benefits of establishing this best practice:** Understanding the implications and consequences of your choices helps you to prioritize your options.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Evaluate tradeoffs: Evaluate the impact of tradeoffs between competing interests, to help make informed decisions when determining where to focus efforts. For example, accelerating speed to market for new features might be emphasized over cost optimization.
+  AWS can help you educate your teams about AWS and its services to increase their understanding of how their choices can have an impact on your workload. You should use the resources provided by AWS Support (AWS Knowledge Center, AWS Discussion Forums, and AWS Support Center) and AWS Documentation to educate your teams. Reach out to AWS Support through AWS Support Center for help with your AWS questions.
+  AWS also shares best practices and patterns that we have learned through the operation of AWS in The Amazon Builders' Library. A wide variety of other useful information is available through the AWS Blog and The Official AWS Podcast.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Blog](https://aws.amazon.com/blogs/)
+  [AWS Cloud Compliance](https://aws.amazon.com/compliance/)
+  [AWS Discussion Forums](https://forums.aws.amazon.com/index.jspa)
+  [AWS Documentation](https://docs.aws.amazon.com/)
+  [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
+  [AWS Support](https://aws.amazon.com/premiumsupport/)
+  [AWS Support Center](https://console.aws.amazon.com/support/home/)
+  [The Amazon Builders' Library](https://aws.amazon.com/builders-library/)
+  [The Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
