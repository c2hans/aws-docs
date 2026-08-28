---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/agent-processing-location.html
---

# Investigative agent processing location
<a name="agent-processing-location"></a>

 The Security Incident Response investigative agent processes metadata in Amazon Bedrock's global region, regardless of which Region your case or findings data originates from. This processing is transient—the agent analyzes the metadata to generate insights and recommendations but does not store the metadata persistently in the Amazon Bedrock infrastructure.

 When the agent completes its analysis, the generated insights and recommendations are stored with your case investigation data in the Region where the case was created. The metadata used for processing is not retained in Amazon Bedrock global Region after the analysis completes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
