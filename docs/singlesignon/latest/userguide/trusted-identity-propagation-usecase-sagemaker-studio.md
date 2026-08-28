---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/trusted-identity-propagation-usecase-sagemaker-studio.html
---

# Trusted identity propagation with Amazon SageMaker Studio
<a name="trusted-identity-propagation-usecase-sagemaker-studio"></a>

[Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) integrates with IAM Identity Center, and it supports [user background sessions](user-background-sessions.md) and trusted identity propagation. User background sessions allow a user to initiate a long-running job on SageMaker Studio, without that user having to remain signed in while the job runs. The job runs immediately and in the background, using the permissions of the user who initiated the job. The job can continue to run even if the user turns off their computer, their IAM Identity Center sign-in session expires, or the user signs out of the AWS access portal. The default session duration for user background sessions is 7 days, but you can specify a maximum duration of 90 days. Trusted identity propagation allows fine-grained access to be provided to AWS resources such as Amazon S3 buckets based on the user's identity or group membership.

The following diagram shows a trusted identity propagation configuration for SageMaker Studio, with access to data stored in an Amazon S3 bucket. User background sessions are enabled for IAM Identity Center, which allows the SageMaker Studio training job to run in the background. Access control for the training data is provided by Amazon S3 Access Grants.

![Diagram of trusted identity propagation for SageMaker Studio, with a SageMaker Studio training job running in a user background session, and access to the training data in Amazon S3 provided by Amazon S3 Access Grants.](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/sagemaker-studio-s3-user-background-session-training-job-s3-access-grants-diagram.png)

**AWS managed application**

The following AWS managed client-facing application supports trusted identity propagation:
+ [Amazon SageMaker Studio](setting-up-trusted-identity-propagation-sagemaker-studio.md)

**To enable trusted identity propagation and user background sessions, follow these steps:**
+ [Set up SageMaker Studio as the client-facing application.](setting-up-trusted-identity-propagation-sagemaker-studio.md)
+ [Set up Amazon S3 Access Grants](tip-tutorial-s3.md) to enable temporary access to the underlying data locations in Amazon S3.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
