---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/audit-security-groups-access-public-ip.html
---

# Automatically audit AWS security groups that allow access from public IP addresses
<a name="audit-security-groups-access-public-ip"></a>

*Eugene Shifer and Stephen DiCato, Amazon Web Services*

## Summary
<a name="audit-security-groups-access-public-ip-summary"></a>

As a security best practice, it's crucial to minimize the exposure of AWS resources to only what is absolutely necessary. For example, web servers that serve the general public need to allow inbound access from the internet, but access to other workloads should be restricted to specific networks to reduce unnecessary exposure. [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in Amazon Virtual Private Cloud (Amazon VPC) are an effective control to help you limit resource access. However, evaluating security groups can be a cumbersome task, especially in multi-account architectures. [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) and [AWS Security Hub CSPM controls](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-view-manage.html) can help you identify security groups that permit access from the public internet (0.0.0.0/0) to specific network communication protocols, such as Secure Shell (SSH), HTTP, HTTPS, and Windows remote desktop protocol (RDP). However, these rules and controls are not applicable if services run on non-standard ports or if access is restricted to certain public IP addresses. For instance, this might occur when a web service is associated with TCP port 8443 instead of the standard TCP port 443. This might also occur when developers have access to the server from their home networks, such as for testing purposes.

To address this, you can use the infrastructure as code (IaC) solution provided in this pattern to identify security groups that allow access from any non-private ([RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) noncompliant) IP addresses to any workload in your AWS account or AWS organization. The [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template provisions a custom AWS Config rule, an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function, and the necessary permissions. You can deploy it as a [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in a single account or as a [stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) across the entire organization, managed through AWS Organizations.

## Prerequisites and limitations
<a name="audit-security-groups-access-public-ip-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Experience using [GitHub](https://github.com/skills/introduction-to-github?tab=readme-ov-file)
+ If you're deploying into a single AWS account:
  + [Permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) to create CloudFormation stacks
  + AWS Config [set up](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) in the target account
  + (Optional) Security Hub CSPM [set up](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html#securityhub-manual-setup-overview) in the target account
+ If you're deploying into an AWS organization:
  + [Permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) to create CloudFormation stack sets
  + Security Hub CSPM [set up](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html#securityhub-orgs-setup-overview) with AWS Organizations integration
  + AWS Config [set up](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) in the accounts where you are deploying this solution
  + Designate an AWS account to be the delegated administrator for AWS Config and Security Hub CSPM

**Limitations**
+ If you're deploying to an individual account that doesn't have Security Hub CSPM enabled, you can use AWS Config to evaluate the findings.
+ If you're deploying to an organization that doesn't have a delegated administrator for AWS Config and Security Hub CSPM, you must log into the individual member accounts to view the findings.
+ If you use AWS Control Tower to manage and govern the accounts in your organization, deploy the IaC in this pattern by using [Customizations for AWS Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html). Using the CloudFormation console would create configuration drift from AWS Control Tower guardrails and require that you re-enroll the organizational units (OUs) or managed accounts.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="audit-security-groups-access-public-ip-architecture"></a>

**Deploying into an individual AWS account**

The following architecture diagram shows the deployment of the AWS resources within a single AWS account. You provision the resources by using a CloudFormation template directly through the CloudFormation console. If Security Hub CSPM is enabled, you can view the results in either AWS Config or Security Hub CSPM. If Security Hub CSPM is not enabled, you can view the results only in AWS Config.

![Deployment of the IaC template as a CloudFormation stack in a single AWS account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/caa8013b-3578-434b-b2c0-5ca7faf45d2d/images/01318e4c-49b5-415f-ac7a-e45451c374cf.png)

The diagram shows the following workflow:

1. You create a CloudFormation stack. This deploys a Lambda function and an AWS Config rule. Both the rule and function are set up with the AWS Identity and Access Management (IAM) permissions that are required to publish resource evaluations in AWS Config and logs.

1. The AWS Config rule operates in [detective evaluation mode](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes) and invokes the Lambda function every 24 hours.

1. The Lambda function assesses the security groups and sends updates to AWS Config.

1. Security Hub CSPM receives all of the AWS Config findings.

1. You can view the findings in Security Hub CSPM or in AWS Config, depending on the services that you have set up in the account.

**Deploying into an AWS organization**

The following diagram shows deployment of the pattern across multiple accounts that are managed through AWS Organizations and AWS Control Tower. You deploy the CloudFormation template through CfCT. The assessment outcomes are centralized in Security Hub CSPM in the delegated administrator account. The AWS CodePipeline workflow section of the diagram shows the background steps that occur during CfCT deployment.

![Deployment of the IaC template as a CloudFormation stack set in an AWS organization.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/caa8013b-3578-434b-b2c0-5ca7faf45d2d/images/f4500347-a481-4cd3-ba14-25a034af7531.png)

The diagram shows the following workflow:

1. In the management account, you upload a compressed (ZIP) file of the IaC template to an Amazon Simple Storage Service (Amazon S3) bucket that is deployed by CfCT.

1. The CfCT pipeline unzips the file, runs [cfn-nag](https://github.com/stelligent/cfn_nag) (GitHub) checks, and deploys the template as a CloudFormation stack set.

1. Depending on the configuration you specify in the CfCT manifest file, CloudFormation StackSets deploys stacks into individual accounts or specified OUs. This deploys a Lambda function and an AWS Config rule in the target accounts. Both the rule and function are set up with the IAM permissions that are required to publish resource evaluations in AWS Config and logs.

1. The AWS Config rule operates in [detective evaluation mode](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes) and invokes the Lambda function every 24 hours.

1. The Lambda function assesses the security groups and sends updates to AWS Config.

1. AWS Config forwards all of the findings to Security Hub CSPM.

1. The Security Hub CSPM findings are aggregated in the delegated administrator account.

1. You can view the aggregated findings in Security Hub CSPM in the delegated administrator account.

## Tools
<a name="audit-security-groups-access-public-ip-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time. An AWS Config [rule](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) defines your ideal configuration settings for a resource, and AWS Config can evaluate whether your AWS resources comply with the conditions in the rule.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices. [Customizations for AWS Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html) helps you customize your AWS Control Tower landing zone and stay aligned with AWS best practices. Customizations for this solution are implemented through CloudFormation templates and AWS Organizations [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your AWS environment against security industry standards and best practices.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [Detect vulnerable security groups](https://github.com/aws-samples/detect-public-security-groups/tree/main) repository.

## Best practices
<a name="audit-security-groups-access-public-ip-best-practices"></a>

We recommend that you adhere to the best practices in the following resources:
+ [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/) (AWS Cloud Operations & Migrations Blog)
+ [Guidance for Establishing an Initial Foundation using AWS Control Tower on AWS](https://aws.amazon.com/solutions/guidance/establishing-an-initial-foundation-using-control-tower-on-aws/) (AWS Solutions Library)
+ [Guidance for creating and modifying AWS Control Tower resources](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-guidance.html) (AWS Control Tower documentation)
+ [CfCT deployment considerations ](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-considerations.html)(AWS Control Tower documentation)
+ [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) (IAM documentation)

## Epics
<a name="audit-security-groups-access-public-ip-epics"></a>

### Review the CloudFormation template
<a name="review-the-cfnshort-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine your deployment strategy. | Review the solution and code to determine the deployment strategy for your AWS environment. Determine whether you are deploying into a single account or an AWS organization. | App owner, General AWS |
| Clone the repository. | Enter the following command to clone the [Detect vulnerable security groups](https://github.com/aws-samples/detect-public-security-groups.git) repository:<pre>git clone https://github.com/aws-samples/detect-public-security-groups.git</pre> | App developer, App owner |
| Validate the Python version. | 1. Navigate into the top-level directory in the cloned repository:<pre>cd detect-public-security-groups</pre><br />2. Open **Security-Group-Public-Assessment.yaml**.<br />3. In the `SgPublicAccessCheckLambdaFunction` resource, confirm that the Python version is compatible with your target AWS Regions. By default, this function uses Python 3.12. For more information, see [AWS Lambda adds support for Python 3.12](https://aws.amazon.com/about-aws/whats-new/2023/12/aws-lambda-support-python-3-12/). If necessary, update the Python version.<br />4. Save and close **Security-Group-Public-Assessment.yaml**. | AWS administrator, App developer |

### Deploy the CloudFormation template
<a name="deploy-the-cfnshort-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | Deploy the CloudFormation template into your AWS environment. Do one of the following:+ If you're deploying to a single AWS account, follow the instructions in [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).<br />+ If you're deploying to an organization that isn't managed by AWS Control Tower, follow the instructions in [Create a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html).<br />+ If you're deploying to an organization that is managed by AWS Control Tower, see the instructions in the [Build your own customizations](https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-byo-customizations.html). | App developer, AWS administrator, General AWS |
| Verify the deployment. | In the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), verify that the stack or stack set has deployed successfully. | AWS administrator, App owner |

### Review the findings
<a name="review-the-findings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| View the AWS Config rule findings. | In Security Hub CSPM, do the following to view a list of individual findings:1. Open the [Security Hub CSPM console](https://console.aws.amazon.com/securityhub/).<br />2. In the navigation pane, choose **Findings**.<br />3. In the **Add filters** box, add the following filters:**Compliance Status** is `FAILED`**Title** is `SgPublicAccessCheck`<br />4. Choose **Apply**.<br />In Security Hub CSPM, do the following to view a list of total findings grouped by AWS account:1. Open the [Security Hub CSPM console](https://console.aws.amazon.com/securityhub/).<br />2. In the navigation pane, choose **Insights**.<br />3. Choose **Create insight**.<br />4. To select the grouping attribute for the insight:Choose the search box to display the filter options.Choose **Group by**.Select **AwsAccountId**.Choose **Apply**.<br />5. In the **Add filters** box, add the following filters:**Title** is `SgPublicAccessCheck`**Compliance Status** is `FAILED`<br />6. Choose **Create insight**.<br />7. Enter an **Insight name**, and then choose **Create insight**.<br />In AWS Config, to view a list of findings, follow the instructions in [Viewing Compliance Information and Evaluation Results](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_view-compliance.html) in the AWS Config documentation. | AWS administrator, AWS systems administrator, Cloud administrator |

## Troubleshooting
<a name="audit-security-groups-access-public-ip-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The CloudFormation stack set creation or deletion fails. | When AWS Control Tower is deployed, it enforces necessary guardrails and assumes control over AWS Config aggregators and rules. This includes preventing any direct alterations through CloudFormation. To properly deploy or remove this CloudFormation template, including all associated resources, you must use CfCT. |
| CfCT fails to delete the CloudFormation template. | If the CloudFormation template persists even after making necessary changes in the manifest file and removing the template files, confirm that the manifest file contains the `enable_stack_set_deletion` parameter and that the value is set to `false`. For more information, see [Delete a stack set](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-delete-stack.html) in the CfCT documentation. |

## Related resources
<a name="audit-security-groups-access-public-ip-resources"></a>
+ [AWS Config Custom Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) (AWS Config documentation)
