---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/aws-cloudformation-template.html
---

# AWS CloudFormation template
<a name="aws-cloudformation-template"></a>

 This guidance uses AWS CloudFormation to automate the deployment of the Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS in the AWS Cloud. It includes the following AWS CloudFormation template, which you can download before deployment.

[![Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS view template button](http://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/genomics-tertiary-analysis-and-data-lakes-using-aws-glue-and-amazon-athena/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template) **guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template:** Use this template to launch this guidance and all associated components. The default configuration deploys an AWS CodePipeline deployment pipeline, an AWS CodeCommit repository for the pipeline code, an AWS CodeCommit repository for the guidance code, Amazon S3 buckets, Amazon Omics Reference, Variant and Annotation stores, AWS Glue jobs, crawlers, workflow, and a data catalog, AWS Identity and Access Management (IAM) roles and policies, an AWS Key Management Service (KMS) key, and an Amazon SageMaker AI notebook instance. You can also customize the template based on your specific needs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
