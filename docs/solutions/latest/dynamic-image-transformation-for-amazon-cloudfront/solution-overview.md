---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/solution-overview.html
---

# Solution Overview
<a name="solution-overview"></a>

Dynamic Image Transformation for Amazon CloudFront (formerly known as Serverless Image Handler) enables real-time image processing and optimization, eliminating the need for pre-processing images or maintaining multiple versions of the same image. Dynamic Image Transformation (DIT) empowers developers with the flexibility to transform images on-demand for specific use cases, enabling responsive design. DIT can automatically optimize images for each user’s device, delivering the highest quality images at the smallest possible file size. This not only reduces operational costs through efficient storage and bandwidth usage but also enhances the end-user experience through faster load times and improved visual quality.

Users can specify image transformations either through URL query parameters or predefined transformation policies. DIT also includes advanced features such as request signing for enhanced security, smart cropping, and content moderation powered by Amazon Rekognition.

This implementation guide walks you through the Dynamic Image Transformation for Amazon CloudFront solution, including its architecture, components, deployment considerations, and configuration steps for AWS Cloud implementation.

The guide is designed for solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals who want to implement DIT in their environment.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know how to troubleshoot common issues with this solution. |  [Troubleshooting](troubleshooting.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](supported-aws-regions.md)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/serverless-image-handler/tree/main)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
