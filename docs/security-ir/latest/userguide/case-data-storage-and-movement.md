---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/case-data-storage-and-movement.html
---

# Case investigation data storage and movement
<a name="case-data-storage-and-movement"></a>

 Case investigation data remains in the AWS Region where you open the security incident case. When you create a case in a specific Region, all logs, metadata, and case information collected for that investigation are stored in that Region. This data doesn't move to other Regions.

 For standard AWS Regions (Regions available by default), case investigation data stays in the Region where the case was created throughout the investigation lifecycle and the 90-day retention period.

 For AWS opt-in Regions (such as Middle East (Bahrain), Africa (Cape Town), or Asia Pacific (Hong Kong)), case investigation data also remains in the Region where the case was created. However, if you enable Security Incident Response in an opt-in Region, all case data from that Region automatically replicates to the US East (N. Virginia) Region (us-east-1) for centralized case management and analysis.

**Important**
 If you operate in opt-in Regions, your case investigation data automatically flows to us-east-1. Organizations with strict data residency requirements must evaluate whether this cross-Region replication is compatible with their compliance obligations. Data never flows between different opt-in Regions, and data from non-opt-in Regions never replicates to opt-in Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
