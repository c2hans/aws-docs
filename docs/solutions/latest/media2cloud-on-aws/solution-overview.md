---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/solution-overview.html
---

# Extract key details from your media files in your AWS accounts
<a name="solution-overview"></a>

Publication date: *January 2019 ([last update](revisions.md): November 2023*)

 Migrating your digital asset management to the cloud allows you to take advantage of the latest innovations in asset management and supply chain applications. However, transferring your existing video archives to the cloud can be a challenging and slow process.

 The Media2Cloud on AWS solution helps streamline and automate the content ingestion process. It sets up serverless end-to-end ingestion and analysis workflows to move your video assets and associated metadata to the Amazon Web Services (AWS) Cloud. During the migration, this solution analyzes and extracts machine learning metadata from your video and images using [Amazon Rekognition](https://aws.amazon.com/rekognition/), [Amazon Transcribe](https://aws.amazon.com/transcribe/), and [Amazon Comprehend](https://aws.amazon.com/comprehend/). It extracts tabular information from scanned documents using [Amazon Textract](https://aws.amazon.com/textract/). This solution also includes a web interface to help you to immediately start ingesting and analyzing your content.

 Media2Cloud on AWS is designed to provide a serverless framework for accelerating the setup and configuration of a content ingestion and analysis process. We recommend that you use this solution as a baseline and customize it to meet your specific needs.

 This implementation guide provides an overview of the Media2Cloud solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the AWS Cloud.

 The guide is intended for IT infrastructure architects and developers who have practical experience working with video workflows and architecting in the AWS Cloud.

 Use this navigation table to quickly find answers to these questions:

|  If you want to . . .  |  Read . . .  |
| --- | --- |
|  Know the cost for running this solution. <br /> The estimated cost for running this solution on 100 hours of videos totaling one terabyte with the default settings in the US East (N. Virginia) Region is **$2,149.95** (one time processing) with **$104.60**/month (recurring) for Amazon S3 data storage and Amazon OpenSearch Service search engine.  |  [Cost](cost.md)  |
|  Understand the security considerations for this solution.  |  [Security](security-1.md)  |
|  Know how to plan for quotas for this solution.  |  [Quotas](quotas.md)  |
|  Know which AWS Regions support this solution.  |  [Supported AWS Regions](supported-aws-regions.md) |
|  View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution.  |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. | [GitHub repository](https://github.com/aws-solutions-library-samples/guidance-for-media2cloud-on-aws/) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
