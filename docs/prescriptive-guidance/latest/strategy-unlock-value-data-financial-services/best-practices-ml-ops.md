---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-unlock-value-data-financial-services/best-practices-ml-ops.html
---

# Best practices
<a name="best-practices-ml-ops"></a>

This section provides an overview of AWS best practices for MLOps.

## Account management and separation
<a name="account-management-and-separation.74799255-f056-580a-a697-c3eacc27acc5"></a>

[AWS best practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/aws-account-management-and-separation.html) for account management recommend that you divide your accounts into four accounts for each use case: experimentation, dev, test, and prod. It's also a best practice to have a governance account for providing shared MLOps resources across the organization and a data lake account for providing centralized data access. The rationale for this is to completely separate the development, test, and production environments, avoid delays caused by service limits being hit through multiple use cases and data science teams sharing the same set of accounts, and provide a complete overview of the costs for each use case. Finally, it's a best practice to separate account-level data, as each use case has its own set of accounts.

## Security standards
<a name="security-standards.62bd435e-f705-5b84-b017-f92017d0ba23"></a>

To meet security requirements, it's a best practice to turn off public internet access and encrypt all data with custom keys. Then, you can deploy a secure instance of Amazon SageMaker Studio to the development account in a matter of minutes by using Service Catalog. You can also get auditing and model monitoring capabilities for each use case by using SageMaker through templates deployed with SageMaker Projects.

## Use case capabilities
<a name="use-case-capabilities.3308fdbd-08c8-5659-993a-2f03b9b3a5cc"></a>

After the account setup is complete, your organization's data scientists can request a new use case template by using SageMaker Projects in SageMaker Studio. This process deploys the necessary infrastructure to have MLOps capabilities in the development account (with minimal support required from central teams), such as CI/CD pipelines, unit testing, model testing, and model monitoring.

Each use case is then developed (or refactored in the case of an existing application code base) to run in a SageMaker architecture by using SageMaker capabilities such as experiment tracking, model explainability, bias detection, and data/model quality monitoring. You can add these capabilities to each use case pipeline by using [pipelines steps](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html) in SageMaker Pipelines.

## MLOps maturity journey
<a name="mlops-maturity-journey.cf84ce84-fdb5-53bc-9eb5-ec5a53414909"></a>

The MLOps maturity journey defines the necessary MLOps capabilities made available in a company-wide setup to ensure that an end-to-end model workflow is in place. The maturity journey consists of four stages:

1. **Initial** – In this stage, you establish the experimentation account. You also secure a new AWS account within your organization where you can experiment with SageMaker Studio and other new AWS services.

1. **Repeatable** – In this stage, you standardize code repositories and the ML solution development. You also adopt a multi-account implementation approach, and standardize your code repositories to support model governance and model audits as you scale out the offering. It's a best practice to adopt a production-ready model development approach with standard solutions that are provided by a governance account. The data is stored in a data lake account and use cases are developed in two accounts. The first account is for experimentation during the data science exploration period. In this account, data scientists discover models for solving the business problem and experiment with multiple possibilities. The other account is for development, which takes place after the best model has been identified and the data science team is ready to work in the inference pipeline.

1. **Reliable** – In this stage, you introduce testing, deployment, and multi-account deployment. You must understand MLOps requirements and introduce automated testing. Implement MLOps best practices to ensure models are both robust and secure. During this phase, introduce two new use case accounts: a test account for testing models developed in an environment that emulates the production environment and a production account for running model inference during business operations. Finally, use automated model testing, deployment, and monitoring in a multi-account setup to ensure that your models meet the high quality and performance bar that you set.

1. **Scalable** – In this stage, you templatize and productionize multiple ML solutions. Multiple teams and ML use cases start to adopt MLOps during the end-to-end model building process. To achieve scalability in this stage, you also increase the number of templates in your template library through contributions from a wider base of data scientists, reduce time to value from idea to production model for more teams across the organization, and iterate as you scale.

For more information on the MLOps maturity models, see [MLOps foundation roadmap for enterprises with Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/mlops-foundation-roadmap-for-enterprises-with-amazon-sagemaker/) on the AWS Machine Learning Blog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
