---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-control-tower/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>
+ In your AWS Organizations management account, check the quotas for the following services:
  + AWS CloudTrail
  + AWS Config
  + AWS CloudFormation StackSets
  + AWS Organizations management account
  + Service control policies
+ Perform an inventory and assessment of your existing AWS Landing Zone environment. At a minimum, look at the following resources:
  + AWS Landing Zone manifest.yaml file
    + Additional baselines
    + Additional AWS Service Catalog product
  + AWS Region where AWS IAM Identity Center (successor to AWS Single Sign-On) is configured, if used
  + CloudFormation stack sets
  + Customizations deployed
+ If you are using a new organization, create an email address for AWS Control Tower management account. (This isn't required if you are using an existing organization for AWS Control Tower deployment.)

  Make sure that this email address has never been used in AWS before.
+ (Optional) Create an email address for the log archive account. (This isn't required if you are using an existing organization for AWS Control Tower deployment.)

  Make sure that this email address has never been used in AWS before.
+ (Optional) Create an email address for the audit account. (This isn't required if you are using an existing account.)

  Make sure that this email address has never been used in AWS before.

  For more information about AWS Control Tower accounts, see [About AWS accounts in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/accounts.html).
+ Make sure you are not running the AWS CodePipeline pipeline for AWS Landing Zone during this transition. On the AWS Management Console, on the AWS-Control-Tower-Pipeline page, choose **Disable transition** between the **Source** stage and the **Build** stage in the AWS Landing Zone pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
