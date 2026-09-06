---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/design-considerations.html
---

# Design considerations
<a name="design-considerations"></a>

 This guidance fully leverages infrastructure as code principles and best practices that allow you to rapidly evolve the guidance. Storing your Extract Transform and Load (ETL) job, crawler, and data lake definitions as code makes them easier to share, inspect for compliance, and reproduce. Additionally, each change you make is tracked by the CI/CD pipeline, facilitating change control management, rollbacks, and auditing.

## Regional deployment
<a name="regional-deployment"></a>

 This guidance uses the AWS CodePipeline service, which is currently available in specific AWS Regions only. Therefore, you must launch this guidance in an AWS Region where this service is available. For the most current service availability by AWS Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). The guidance has been tested in all Regions.
