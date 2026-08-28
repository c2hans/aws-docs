---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/step-2.-await-initial-environment-deployment.html
---

# Step 2. Await initial environment deployment
<a name="step-2.-await-initial-environment-deployment"></a>

Use the following procedure to ensure the Landing Zone Accelerator on AWS deploys a minimum configuration to your environment.

1. Sign in to the AWS Management Console and navigate to the **AWS CodePipeline** console. The `AWSAccelerator-Installer` pipeline should show a status of either `In Progress` or `Complete`. If `In Progress`, wait for the pipeline to complete.

1. When the `AWSAccelerator-Installer` pipeline has completed, a new `AWSAccelerator-Pipeline` pipeline is created that’s now `In Progress`. Refresh the AWS CodePipeline console if the new pipeline isn’t visible.

1. The `AWSAccelerator-Pipeline` pipeline takes approximately 45 minutes to complete. This initial deployment prepares your environment for Landing Zone Accelerator on AWS and deploy a minimal configuration. Resources deployed include AWS CloudFormation custom resources, CloudWatch Logs log groups for the custom resources, AWS KMS keys for encryption at rest, and Amazon S3 buckets for AWS service logging.

1. After completion of the preceding steps, your environment is ready to customize.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
