---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/tagging-capability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tagging capability
<a name="tagging-capability"></a>

Tagging is the act of assigning metadata to the different resources in your AWS environment for a variety of purposes, such as Attribute Based Access Control (ABAC), Cloud Financial Management, and automation (such as patching for select* tagged* instances). Tagging can also be used to create new resource constructs for visibility or control (such as grouping together resources that make up a micro-service, application, or workload). Tagging is fundamental to providing enterprise-level visibility and control.

 **Stakeholders:**
+  Central IT (Primary)
+  Finance
+  Security
+  Software Engineering

 **Personas: **
+  **Cloud Team** - the team(s) who make cloud available to customers.
+  **Security Team** - the members of the cloud team responsible for security in AWS.
+  **Finance Team** - the members of the finance team responsible for reporting, allocating, and forecasting cloud costs.
+  **Customer** - entity within the company that consumes the logs stored within the log storage.

 **Supporting capabilities:** [Identity Management and Access Control capability](identity-management-access-control-capability.md)

 **Scenarios:**
+ **CF23 - S1: Tag definition and assignment**
+ **CF23 - S2: Tag compliance**
+ **CF23 - S3: Tag usage**

Topics
+ [Overview](tagging-overview.md)
+ [Choosing tags for your environment](choosing-tags.md)
+ [Tagging standards](tagging-standards.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
