---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/architecture-ingest-cti.html
---

# Ingesting CTI
<a name="architecture-ingest-cti"></a>

The first step in the ingestion process is to convert the cyber threat intelligence (CTI) data from the threat feeds into a format that your threat intelligence platform can ingest. This is called *CTI conversion*. Threat feed data can come in a range of formats, such as [Structured Threat Information Expression (STIX)](https://oasis-open.github.io/cti-documentation/stix/intro.html). You must restructure the incoming data into a predictable and easily consumable format that is suitable for the security products you are using in your AWS environment.

For maximum compatibility, we recommend that you convert the data into a JSON format. For example, [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) can consume data that is in JSON format, and automation workflows can more easily and consistently consume this format. More information about building automated workflows is provided in the next section, [Automating preventative and detective security controls](architecture-automate-controls.md).

To accelerate the ingestion of CTI data, you can automate the data transformations. The data is converted as it is ingested and then passed directly to the threat intelligence platform. You can use an AWS Lambda function to complete the transformation, and you can orchestrate the process through AWS services such as AWS Step Functions or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

When you ingest CTI, you can choose which attributes to extract and retain. The exact amount of detail required can vary depending on your business needs. However, to make updates to firewalls and other security services, we recommend the following minimum attributes:
+ IP address and domain
+ Threat
+ Add or remove from your internal threat lists

Extract the attributes you want to use, and then format them into a structured JSON template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
