---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-control-tower/deploy.html
---

# Deploying AWS Control Tower in an AWS Landing Zone organization
<a name="deploy"></a>

This scenario details the steps involved in deploying AWS Control Tower in an AWS Organizations organization that is currently running the AWS Landing Zone solution.

1. Make sure that you can create two new accounts without exceeding the current service quotas. If necessary, [request service quota increases](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). The new accounts will be deployed as a part of AWS Control Tower deployment unless you are using [existing accounts](https://aws.amazon.com/about-aws/whats-new/2022/05/aws-control-tower-now-use-customer-provided-core-accounts/) from the landing zone that you used for AWS Landing Zone.

1. If you are currently using AWS IAM Identity Center (successor to AWS Single Sign-On), deploy AWS Control Tower in the same AWS Region where IAM Identity Center is configured.

1. On the AWS Organizations console, choose **Disable trusted access** for AWS Config and AWS CloudTrail services if they are activated. For more information, see the [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).

1. Deploy AWS Control Tower. For more information, see the [AWS documentation](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html#getting-started-configure).

Here's what to expect when you set up your AWS Control Tower landing zone in an existing organization.

1. You can have one landing zone in each AWS Organizations organization.

1. AWS Control Tower uses the management account from your existing AWS Organizations organization as its management account. No new management account is needed.

1. AWS Control Tower sets up two new accounts in a registered Security OU: an audit account and a log archive account, unless you are using existing accounts during setup. If you are using existing accounts, AWS Control Tower will move the audit and log archive accounts under the OU that you created during AWS Control Tower deployment.

1. After launch, AWS Control Tower guardrails apply automatically to accounts in that OU.

1. You can enroll additional existing AWS accounts into an OU that's governed by AWS Control Tower, so that guardrails apply to those accounts.

If you want to enroll any existing AWS accounts or OUs into AWS Control Tower after it is set up, see the [Enrolling existing AWS accounts with AWS Control Tower in an existing organization](#enroll-to-existing) section of the guide.

## Enrolling existing AWS accounts with AWS Control Tower in an existing organization
<a name="enroll-to-existing"></a>

You can extend AWS Control Tower governance to an individual, existing AWS account when you *enroll* it into an organizational unit (OU) that's already governed by AWS Control Tower. Eligible accounts exist in *unregistered OUs that are part of the same AWS Organizations organization *as the AWS Control Tower OU.

You can register an OU to AWS Control Tower from the AWS Control Tower console. When you register an OU, AWS Control Tower will enroll all the accounts under the OU to AWS Control Tower.

We recommend registering an OU, instead of enrolling individual accounts. The benefit of this approach is that the OU ID does not change. If you have any policies or rules that use the OU ID, you won't need to make any changes.

Before you enroll AWS accounts with AWS Control Tower, delete the AWS CloudFormation stack instances from the stack set named AWS-Landing-Zone-Baseline-EnableConfig. In each account that you want to enroll, in every AWS Region where AWS Control Tower is deployed, you must delete AWS-Landing-Zone-Baseline-EnableConfig stack instance. Because deleting the complete stack set takes time, we recommend deleting the stack instances only for the accounts that you are enrolling. Ideally, deleting the stack instances for a specific account should result in deleting the AWS Config recorder and delivery channel. You can verify the deletion by running the following commands for that account.

```
      aws configservice describe-configuration-recorders --region <region_name>
      aws configservice describe-delivery-channels --region <region_name>
```

### Use the AWS Control Tower Register OU feature from the AWS Control Tower console
<a name="use-the-aws-control-tower-register-ou-feature-from-the-aws-control-tower-console.2d793f50-a567-5c36-9bb2-42563c621ed8"></a>

Before you register an entire OU that has existing AWS accounts, make sure to do the following:
+ Delete the AWS Config recorder and delivery channel from all the Regions of all the accounts under that OU, as mentioned previously.

For more information, see [Register an existing organizational unit with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/importing-existing.html).

After an account is enrolled in AWS Control Tower, you will see another provisioned product in AWS Service Catalog for the account that you enrolled. The name of the provisioned product will be prefixed with **Enroll-**. This means that you now have two provisioned products in AWS Service Catalog for a single account:
+ One provisioned product from the AWS Landing Zone Account Vending Machine
+ One provisioned product from the enrollment into AWS Control Tower

You have an option to terminate the provisioned product for an account from AWS Landing Zone, but we recommend that you wait until after completing the transition.

When you terminate the provisioned product for accounts vended in AWS Landing Zone environment, the Terminate operation will start deleting the associated baseline CloudFormation stack sets, which you might want to retain. Be sure to assess the baseline stack sets in manifest.yaml, and understand the implications of deleting the stack sets. If you have any resources in the stack sets that you want to retain, avoid deleting the provisioned product. A partial deletion will render the provisioned product in the **Tainted** state in the AWS Service Catalog console.

Alternatively, you can retain the provisioned product created by Account Vending Machine from AWS Landing Zone.

## Enrolling AWS accounts from an existing organization into AWS Control Tower in a new organization
<a name="enroll-to-new"></a>

You might want to deploy AWS Control Tower in a new AWS Organizations organization. To set up AWS Control Tower in a new organization, complete the following steps:

1. Create a new [AWS account](https://repost.aws/knowledge-center/create-and-activate-aws-account).

1. [Deploy AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) in the newly created account.

1. To migrate an AWS account from an existing organization to the new organization where you deployed AWS Control Tower, see the [instructions](https://aws.amazon.com/premiumsupport/knowledge-center/organizations-move-accounts/). It's important to review and understand all the account access, billing, licensing, and tax considerations that are covered.

1. To understand the process of migrating AWS accounts between organizations, see the [Migrating accounts between AWS Organizations with consolidated billing to all features](https://aws.amazon.com/blogs/mt/migrating-accounts-between-aws-organizations-with-consolidated-billing-to-all-features/) blog post.

1. Start enrolling the AWS account in AWS Control Tower. To perform the enrollment, see the section Enrolling existing AWS accounts into AWS Control Tower.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
