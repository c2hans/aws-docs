---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-serverless-application-model.html
---

# AWS Serverless Application Model
<a name="aws-serverless-application-model"></a>

The [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) (AWS SAM) is an open-source framework that you can use to build [serverless applications](https://aws.amazon.com/serverless/) on AWS.

AWS SAM integrates with other AWS services, so creating serverless applications with AWS SAM provides the following benefits:
+ **Single-deployment configuration** — AWS SAM makes it easy to organize related components and resources, and operate on a single stack. You can use AWS SAM to share configuration (such as memory and timeouts) between resources, and deploy all related resources together as a single, versioned entity.
+ **Extension of CloudFormation** — Because AWS SAM is an extension of CloudFormation, you get the reliable deployment capabilities of CloudFormation. You can define resources by using CloudFormation in your AWS SAM template.
+ **Built-in best practices** — You can use AWS SAM to define and deploy your IaC. This makes it possible for you to use and enforce best practices such as code reviews.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
