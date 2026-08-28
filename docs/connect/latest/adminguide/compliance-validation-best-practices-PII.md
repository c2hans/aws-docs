---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/compliance-validation-best-practices-PII.html
---

# Best practices for PII compliance in Connect Customer
<a name="compliance-validation-best-practices-PII"></a>

Following this list of best practices can help you ensure your Connect Customer contact center is PII (Personally Identifiable Information) compliant.
+ Conduct compliance eligibility audits for all services used in your contact center, as well as any third party integration points.
+ AWS Key Management Service (KMS) encrypts Amazon S3 contents at the object level, which covers recordings, logs, and saved reports by default for Amazon S3. Make sure encryption in transit and at rest rules apply downstream or to third party apps.
+ Use encryption in the **Store customer input** block for sensitive DTMF information.
+ Use your own KMS key when ingesting data in Connect Customer Customer Profile domains.
+ Do not upload content containing customer PII to Connect Customer agent assist.
+ When using Connect Customer Voice ID, do not use PII in the `CustomerSpeakerId`.
+ As with any AWS service, we strongly recommend that you not use sensitive information to name resources.
+ When using pre-defined attributes in a Connect Customer instance, do not use sensitive information in it's name and values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
