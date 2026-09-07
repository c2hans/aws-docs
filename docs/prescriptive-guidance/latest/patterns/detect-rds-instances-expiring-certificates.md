---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/detect-rds-instances-expiring-certificates.html
---

# Detect Amazon RDS and Aurora database instances that have expiring CA certificates
<a name="detect-rds-instances-expiring-certificates"></a>

*Stephen DiCato and Eugene Shifer, Amazon Web Services*

## Summary
<a name="detect-rds-instances-expiring-certificates-summary"></a>

As a security best practice, it is recommended that you encrypt data in transit between application servers and relational databases. You can use SSL or TLS to encrypt a connection to a database (DB) instance or cluster. These protocols help provide confidentiality, integrity, and authenticity between an application and database. The database uses a server certificate, which is issued by a [certificate authority (CA)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificateAuthorities) and is used to perform server identity verification. SSL or TLS verifies the authenticity of the certificate by validating its digital signature and ensuring it is not expired.

In the AWS Management Console, [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) and [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) provide notifications about DB instances that require certificate updates. However, to check for these notifications, you must log into each AWS account and navigate to the service console in each AWS Region. This task becomes more complex if you need to assess certificate validity across many AWS accounts that are managed as an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

By provisioning the infrastructure as code (IaC) provided in this pattern, you can detect expiring CA certificates for all Amazon RDS and Aurora DB instances in your AWS account or AWS organization. The [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template provisions an AWS Config rule, an AWS Lambda function, and the necessary permissions. You can deploy it into a single account as a [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html), or you can deploy it across the entire AWS organization as a [stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

## Prerequisites and limitations
<a name="detect-rds-instances-expiring-certificates-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ If you're deploying into a single AWS account:
  + Ensure that you have [permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) to create CloudFormation stacks.
  + [Enable](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) AWS Config in the target account.
  + (Optional) [Enable](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html#securityhub-manual-setup-overview) AWS Security Hub CSPM in the target account.
+ If you're deploying into an AWS organization:
  + Ensure that you have [permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) to create CloudFormation stack sets.
  + [Enable](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html#securityhub-orgs-setup-overview) Security Hub CSPM with AWS Organizations integration.
  + [Enable](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) AWS Config in the accounts where you are deploying this solution.
  + Designate an AWS account to be the delegated administrator for AWS Config and Security Hub CSPM.

**Limitations**
+ If you're deploying to an individual account that doesn't have Security Hub CSPM enabled, you can use AWS Config to evaluate the findings.
+ If you're deploying to an organization that doesn't have a delegated administrator for AWS Config and Security Hub CSPM, you must log into the individual member accounts to view the findings.
+ If you use AWS Control Tower to manage and govern the accounts in your organization, deploy the IaC in this pattern by using [Customizations for AWS Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html). Using the CloudFormation console will create configuration drift from AWS Control Tower guardrails and require that you re-enroll the organizational units (OUs) or managed accounts.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="detect-rds-instances-expiring-certificates-architecture"></a>

**Deploying into an individual AWS account**

The following architecture diagram shows the deployment of the AWS resources within a single AWS account. It's implemented by using a CloudFormation template directly through the CloudFormation console. If Security Hub CSPM is enabled, you can view the results in either AWS Config or Security Hub CSPM. If Security Hub CSPM is not enabled, you can view the results only in the AWS Config console.

![Deployment of the provided CloudFormation template in a single account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d34fe1f1-6764-4485-b7a7-04e5861f1e9b/images/0b07133a-d4f8-4d87-8d00-2b5e2c453ece.png)

The diagram shows the following steps:

1. You create a CloudFormation stack. This deploys a Lambda function and an AWS Config rule. Both the rule and function are set up with the AWS Identity and Access Management (IAM) permissions required to publish resource evaluations in AWS Config and logs.

1. The AWS Config rule operates in [detective evaluation mode](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes) and runs every 24 hours.

1. Security Hub CSPM receives all AWS Config findings.

1. You can view the findings in Security Hub CSPM or in AWS Config, depending on the account's configuration.

**Deploying into an AWS organization**

The following diagram shows the assessment of certificate expiration across multiple accounts that are managed through AWS Organizations and AWS Control Tower. You deploy the CloudFormation template through CfCT. The assessment outcomes are centralized in Security Hub CSPM in the delegated administrator account. The AWS CodePipeline workflow depicted in the diagram shows the background steps that occur during CfCT deployment.

![Deployment of the provided CloudFormation template to multiple accounts in an AWS Organization.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d34fe1f1-6764-4485-b7a7-04e5861f1e9b/images/8d870cbb-54cf-43ec-96f2-00730e0134af.png)

The diagram shows the following steps:

1. Depending on the configuration for CfCT, in the management account, you push the IaC to an AWS CodeCommit repository or you upload a compressed (ZIP) file of the IaC to an Amazon Simple Storage Service (Amazon S3) bucket.

1. The CfCT pipeline unzips the file, runs [cfn-nag](https://github.com/stelligent/cfn_nag) (GitHub) checks, and deploys it as a CloudFormation stack set.

1. Depending on the configuration specified in the CfCT manifest file, CloudFormation StackSets deploys stacks into individual accounts or specified OUs. This deploys a Lambda function and an AWS Config rule in the target accounts. Both the rule and function are set up with the IAM permissions required to publish resource evaluations in AWS Config and logs.

1. The AWS Config rule operates in [detective evaluation mode](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes) and runs every 24 hours.

1. AWS Config forwards all findings to Security Hub CSPM.

1. Security Hub CSPM findings are aggregated in the delegated administrator account.

1. You can view the findings in Security Hub CSPM in the delegated administrator account.

## Tools
<a name="detect-rds-instances-expiring-certificates-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time. An AWS Config [rule](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) defines your ideal configuration settings for a resource, and AWS Config can evaluate whether your AWS resources comply with the conditions in your rules.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices. [Customizations for AWS Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html) helps you customize your AWS Control Tower landing zone and stay aligned with AWS best practices. Customizations are implemented with CloudFormation templates and service control policies (SCPs).
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your AWS environment against security industry standards and best practices.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [Detect Amazon RDS instances with expiring CA certificates](https://github.com/aws-samples/config-rds-ca-expiry) repository.

## Best practices
<a name="detect-rds-instances-expiring-certificates-best-practices"></a>

We recommend that you adhere to the best practices in the following resources:
+ [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/) (AWS Cloud Operations & Migrations Blog)
+ [Guidance for Establishing an Initial Foundation using AWS Control Tower on AWS](https://aws.amazon.com/solutions/guidance/establishing-an-initial-foundation-using-control-tower-on-aws/) (AWS Solutions Library)
+ [Guidance for creating and modifying AWS Control Tower resources](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-guidance.html) (AWS Control Tower documentation)
+ [CfCT deployment considerations ](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-considerations.html)(AWS Control Tower documentation)

## Epics
<a name="detect-rds-instances-expiring-certificates-epics"></a>

### Review the solution and code
<a name="review-the-solution-and-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine your deployment strategy. | Review the solution and code to determine how you will deploy it into your AWS environment. Determine if you will be deploying into a single account or an AWS organization. | App owner, General AWS |
| Clone the repository. | Enter the following command to clone the [Detect Amazon RDS instances with expiring CA certificates](https://github.com/aws-samples/config-rds-ca-expiry) repository.<pre>git clone https://github.com/aws-samples/config-rds-ca-expiry.git</pre> | App developer, App owner |
| Validate the Python version. | 1. Navigate into the top-level directory in the cloned repository.<pre>cd config-rds-ca-expiry</pre><br />2. Open **config-rds-ca-expiry.yaml**.<br />3. In the `CertExpirationCheckLambdaFunction` resource, confirm that the Python version is compatible with your target AWS Regions. By default, this function uses Python 3.12. For more information, see [AWS Lambda adds support for Python 3.12](https://aws.amazon.com/about-aws/whats-new/2023/12/aws-lambda-support-python-3-12/). If necessary, update the Python version.<br />4. Save and close **config-rds-ca-expiry.yaml**. | App developer, App owner |

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | Deploy the CloudFormation template to your AWS environment. Do one of the following:+ If you're deploying to a single AWS account, follow the instructions in [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).<br />+ If you're deploying to an organization that isn't managed by AWS Control Tower, follow the instructions in [Create a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html).<br />+ If you're deploying to an organization that is managed by AWS Control Tower, see the instructions in the [Build your own customizations](https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-byo-customizations.html). | App developer, AWS administrator, General AWS |
| Verify the deployment. | In the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), verify that the stack or stack set has deployed successfully. | AWS administrator, App owner |

### Review the findings
<a name="review-the-findings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| View the AWS Config rule findings. | In Security Hub CSPM, do the following to view a list of individual findings:1. Open the [Security Hub CSPM console](https://console.aws.amazon.com/securityhub/).<br />2. In the navigation pane, choose **Findings**.<br />3. In the **Add filters** box, add the following filters:**Compliance Status** is `FAILED`**Title** is `rds-has-expiring-ca`<br />4. Choose **Apply**.<br />In Security Hub CSPM, do the following to view a list of total findings grouped by AWS account:1. Open the [Security Hub CSPM console](https://console.aws.amazon.com/securityhub/).<br />2. In the navigation pane, choose **Insights**.<br />3. Choose **Create insight**.<br />4. To select the grouping attribute for the insight:Choose the search box to display the filter options.Choose **Group by**.Select **AwsAccountId**.Choose **Apply**.<br />5. In the **Add filters** box, add the following filters:**Title** is `rds-has-expiring-ca`**Compliance Status** is `FAILED`<br />6. Choose **Create insight**.<br />7. Enter an **Insight name**, and then choose **Create insight**.<br />In AWS Config, to view a list of findings, follow the instructions in [Viewing Compliance Information and Evaluation Results](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_view-compliance.html#evaluate-config_view-compliance-console) in the AWS Config documentation. | AWS administrator, AWS systems administrator, Cloud administrator |

## Troubleshooting
<a name="detect-rds-instances-expiring-certificates-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| CloudFormation stack set creation or deletion fails | When AWS Control Tower is deployed, it enforces necessary guardrails and assumes control over AWS Config aggregators and rules. This includes preventing any direct alterations through CloudFormation. To properly deploy or remove this CloudFormation template, including all associated resources, you must use CfCT. |
| CfCT fails to delete the CloudFormation template | If the CloudFormation template persists even after making necessary changes in the manifest file and removing the template files, confirm that the manifest file contains the `enable_stack_set_deletion` parameter and that the value is set to `false`. For more information, see [Delete a stack set](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-delete-stack.html) in the CfCT documentation. |

## Related resources
<a name="detect-rds-instances-expiring-certificates-resources"></a>
+ [Using SSL/TLS to encrypt a connection to a DB instance or cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) (Amazon RDS documentation)
+ [AWS Config Custom Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) (AWS Config documentation)
