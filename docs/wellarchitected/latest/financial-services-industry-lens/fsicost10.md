---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost10.html
---

# FSICOST10: Do you use lower cost Regions to run less data-intensive or time-sensitive workloads?
<a name="fsicost10"></a>

 FSI companies usually have to plan their Disaster Recovery (DR) and also run a cadence of dry runs for regulatory purposes, and typically opt to setup their DR site in an alternate AWS Region. Depending on the SLA for latency, data sovereignty and compliance needs, you could run DR in a less costly Region.

## FSICOST10-BP01 Use less costly Regions for disaster recovery and test platforms
<a name="fsicost10-bp01-use-less-costly-regions-for-disaster-recovery-and-test-platforms"></a>

 FSI companies usually must plan their Disaster Recovery (DR) and also run a cadence of dry runs for regulatory purposes, typically opting to set up their DR site in an alternate AWS Region. Depending on the SLA for latency, data sovereignty, and compliance needs, you could run DR in a less costly Region. Consider cheaper Regions for non-production environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
