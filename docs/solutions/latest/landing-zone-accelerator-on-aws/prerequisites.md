---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

You must meet the following prerequisites before launching the stack.

## Activate a multi-account management solution
<a name="activate-a-multi-account-management-solution"></a>

Landing Zone Accelerator on AWS solution can create, update, or reset an AWS Control Tower Landing Zone. When enabled, the solution will deploy AWS Control Tower in the home Region.

## For AWS Control Tower based installation
<a name="for-aws-control-tower-based-installation"></a>

### Auto-deploy AWS Control Tower by the solution (recommended)
<a name="auto-deploy-aws-control-tower-by-the-solution-recommended"></a>

Using the Landing Zone Accelerator on AWS solution, you can create, update, or reset an AWS Control Tower Landing Zone. It is possible to maintain the AWS Control Tower Landing Zone using the Landing Zone Accelerator solution. When the installer stack of the solution is deployed with the `ControlTowerEnabled` parameter set to `Yes`, then the Landing Zone Accelerator solution will deploy the AWS Control Tower Landing Zone with the most recent version available.

The Landing Zone Accelerator solution can deploy AWS Control Tower Landing Zone when the following prerequisites are met.
+ Configured AWS Organizations with all feature enabled in management account.

  Create AWS Organization and verify that your own the email address is provided for the management account in the organization. In order to learn more about setting up an AWS organization, you may refer to this [Creating an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) in the *AWS Organizations\_\_User Guide*.

**Note**
In the event that AWS Organizations has been configured, but not all features have been enabled, the solution will enable all features for your organization.
+ There are no AWS services enabled for AWS Organizations.
+ There are no organization units created in the AWS Organizations.
+ The only AWS account in the AWS Organization is the management account.
+ The management account does not have AWS IAM Identity Center configured.
+ The following AWS Control Tower service roles are not preset in the management account.
  +  [AWSControlTowerAdmin](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerAdmin)
  +  [AWSControlTowerCloudTrailRole](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerCloudTrailRole)
  +  [AWSControlTowerStackSetRole](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerStackSetRole)
  +  [AWSControlTowerConfigAggregatorRoleForOrganizations](https://docs.aws.amazon.com/controltower/latest/userguide/roles-how.html#config-role-for-organizations)

Landing Zone Accelerator performs the following prerequisites before deploying AWS Control Tower Landing Zone. This [document](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-prereques.html) provides more information about AWS Control Tower prerequisites. The solution will not perform any of the prerequisites if there is an existing AWS Control Tower Landing Zone.
+ Deploy following AWS Control Tower service roles in the management account:
  +  [AWSControlTowerAdmin](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerAdmin)
  +  [AWSControlTowerCloudTrailRole](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerCloudTrailRole)
  +  [AWSControlTowerStackSetRole](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerStackSetRole)
  +  [AWSControlTowerConfigAggregatorRoleForOrganizations](https://docs.aws.amazon.com/controltower/latest/userguide/roles-how.html#config-role-for-organizations)
+ Deploy AWS KMS CMK with alias `alias/aws-controltower/key` in the management account home Region.
+ Create shared accounts (`LogArchive` and `Audit`) and invite to AWS Organizations.
+ Deploy AWS Control Tower Landing Zone in the management account home Region.

**Note**
Landing Zone Accelerator on AWS uses the [AWS Control Tower API](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-apis.html) to create and manage the AWS Control Tower Landing Zone.

**Important**
The AWS Console should be used to enable or disable the Region deny property for your AWS Control Tower Landing Zone. Currently, the Landing Zone Accelerator solution does not support the modification of the Region deny feature. Due to the fact that the Landing Zone Accelerator may deploy certain global AWS services, such as AWS IAM and AWS Organizations, the solution will add the global Region to the list of governed Regions in the AWS Control Tower if the home Region of the Landing Zone Accelerator is not the same as the global Region.

### Manually deploy AWS Control Tower
<a name="manually-deploy-aws-control-tower"></a>

To set up AWS Control Tower, refer to [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) in the *AWS Control Tower User Guide*.

**Note**
If you’re using AWS Control Tower, we strongly recommended creating an AWS KMS customer managed key before deploying your landing zone. This AWS KMS key is used by services that AWS Control Tower manages to apply encryption at rest to sensitive log ﬁles. For more information on activating encryption for AWS Control Tower, see [Conﬁgure your shared accounts and encryption](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html#configure-shared-accounts).
If you’re deploying a new AWS Control Tower landing zone, you can add the prerequisite **Infrastructure** OU during the initial setup wizard. By default, the landing zone deploys with an additional **Sandbox** OU. You can rename this OU to **Infrastructure** if desired. Alternatively, you can create the **InfrastructureOU** after the landing zone is provisioned.
For more information about customizing the additional OU created during Control Tower setup, see [Step 2b. Conﬁgure your organizational units (OUs)](https://docs.aws.amazon.com/controltower/latest/userguide/configure-ous.html) in the *Control Tower User Guide*.

## For AWS Organizations based installation (without AWS Control Tower)
<a name="for-aws-organizations-based-installation-without-aws-control-tower"></a>

To set up AWS Organizations, refer to [Getting started with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html) in the *AWS Organization User Guide*.

Ensure the [Mandatory accounts](mandatory-accounts.md) are created. The Landing Zone Accelerator on AWS requires these three accounts at minimum to successfully deploy to your environment.

For more information on managing accounts in an AWS Organization, refer to [Managing the AWS accounts in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html) in the *AWS Organization User Guide*.

## Update AWS CodeBuild concurrency quota
<a name="update-codebuild-conncurrency-quota"></a>

Follow this procedure to check your current CodeBuild concurrency quota.

1. Navigate to the [Service Quotas console](https://console.aws.amazon.com/servicequotas/) in the account and Region for which you will deploy the Landing Zone Accelerator on AWS solution.

1. In the navigation pane, choose **AWS services**.

1. Search for then select AWS CodeBuild.

1. Select **Concurrently running builds for Linux/Large environment**.

1. If the value under **Applied quota value** is less than 3, select the quota link. Otherwise, skip the remaining steps.

1. Choose **Request increase at account-level**. In the **Increase quota value** box, enter `3` or more as the new quota value.

1. Choose **Request**. Ensure this quota increase request has been approved prior to deploying the solution. You can view your request status by choosing **Quota request history** in the navigation sidebar.

## Ensure your global Region is accessible
<a name="ensure-your-global-region-is-accessible"></a>

Some AWS services and features apply configurations to your accounts at a global level rather than a regional level. In addition to the Regions that you enable in the solution configuration files; this solution requires access to the Region where global service API endpoints are hosted. The global Region depends on the AWS partition you will be deploying the solution to.

 **AWS partitions and their corresponding global Region**

| AWS Partition | Global Region |
| --- | --- |
|  **Standard (aws)**  |  `us-east-1`  |
|  **GovCloud US (aws-us-gov)**  |  `us-gov-west-1`  |
|  **China (aws-cn)**  |  `cn-northwest-1`  |

**Important**
Ensure that you don’t have any existing AWS Organizations service control policies and/or Control Tower Region deny settings configured in your environment that would block access to the global Region listed above. You might experience Core pipeline failures if you do not allow access to this Region.

## Create a GitHub personal access token and store in Secrets Manager
<a name="create-a-github-personal-access-token-and-store-in-secrets-manager"></a>

You require a GitHub access token to access the Landing Zone Accelerator on AWS code repository. Instructions on how to create a personal access token are located on [GitHub Docs](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

**Note**
The GitHub access token must have `public_repo` permissions.

Store the personal access token in Secrets Manager as plain text in the home Region. Name the secret `accelerator/github-token` (case sensitive).

With the AWS Management Console in the home Region:

1. Store a new secret, and select **Other type of secrets**, **Plaintext**.

1. Paste your secret with no formatting, leading, or trailing spaces (completely remove the example text).

1. Select an encryption key.

1. Set the secret name to `accelerator/github-token` (case sensitive).

1. Select **Disable rotation**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
