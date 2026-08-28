---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/provision-deployable-architectures.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Provision pre-approved deployable architectures
<a name="provision-deployable-architectures"></a>

As you adopt the cloud you will see common workload patterns emerge, which may include standard 3-tier web applications, serverless frameworks, or many other architecture patterns. At the same time, certain skill sets may vary as teams learn to leverage the cloud. Common patterns may be implemented with any number of variations, along with potential for limited people knowledge has a risk to deploy non-compliant workloads. Pre-approving and building a pattern library will provide a common and repeatable mechanism to maintain controls and boundaries around workloads. Instead of application teams relying on run-book, process documentation, or lengthy review processes, cloud platform teams can publish ready to deploy patterns which include common resources along with included control guardrails. For example, a 3-tier web app will include a typical set of compute instances placed within the appropriate public and private network segments to prevent accidental exposure to internal systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
