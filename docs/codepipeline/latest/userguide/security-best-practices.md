---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html
---

# Security best practices
<a name="security-best-practices"></a>

**Topics**

CodePipeline provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

You use encryption and authentication for the source repositories that connect to your pipelines. These are the CodePipeline best practices for security:
+ If you create a pipeline or action configuration that needs to include secrets, such as tokens or passwords, do not enter secrets directly in the action configuration, or default values of variables defined at pipeline level or CloudFormation configuration, because the information will display in logs. Use Secrets Manager to set up and store secrets, and then use the referenced secret in the pipeline and action configuration, as described in [Use AWS Secrets Manager to track database passwords or third-party API keys](parameter-store-encryption.md).
+ If you create a pipeline that uses an S3 source bucket, configure server-side encryption for artifacts stored in Amazon S3 for CodePipeline by managing AWS KMS keys, as described in [Configure server-side encryption for artifacts stored in Amazon S3 for CodePipeline](S3-artifact-encryption.md).
+ If you are using the Jenkins action provider, when you use a Jenkins build provider for your pipeline’s build or test action, install Jenkins on an EC2 instance and configure a separate EC2 instance profile. Make sure that the instance profile grants Jenkins only the AWS permissions required to perform tasks for your project, such as retrieving files from Amazon S3. To learn how to create the role for your Jenkins instance profile, see the steps in [Create an IAM role to use for Jenkins integration](tutorials-four-stage-pipeline.md#tutorials-four-stage-pipeline-prerequisites-jenkins-iam-role).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
