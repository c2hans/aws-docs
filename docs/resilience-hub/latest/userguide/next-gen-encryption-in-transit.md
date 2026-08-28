---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-encryption-in-transit.html
---

# Encryption in transit
<a name="next-gen-encryption-in-transit"></a>

All data in transit is encrypted using TLS 1.2 or later, including:
+ API calls to Next generation Resilience Hub endpoints
+ Cross-service communication (Next generation Resilience Hub to topology service, Next generation Resilience Hub to Amazon Bedrock)
+ Cross-account credential passing (encrypted with AWS KMS before transmission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
