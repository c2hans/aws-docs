---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the solution.

If these instructions don’t address your issue, [Contact Support](contact-aws-support.md) provides instructions for opening an Support case for this solution.

## Problem: Deploying a VPC-enabled configuration, with Create a VPC for me, fails
<a name="problem-deploying-a-vpc-enabled-configuration-with-create-a-vpc-for-me-fails"></a>

The Deployment dashboard stack or the use case stack fails deployment because the CloudFormation was not able to provision VPC networking resources.

### Resolution
<a name="resolution-problem-deploying-a-vpc-enabled-configuration-with-create-a-vpc-for-me-fails"></a>

Check the quota limits for VPCs, and Elastic IPs in your account. Default limits are 5 each for Elastic IPs and VPCs per AWS account, per AWS Region.

**Note**
When the solution creates a VPC, a single VPC-enabled deployment (Deployment Dashboard or Use Case) is a 2-AZ deployment with 1 public and 1 private subnet in each AZ, each public subnet deploys 1 NAT Gateway. With 2 NAT Gateways, the deployment consumes 2 public IP addresses from the quota limit.

Some limits to be aware of (per account, per Region):
+ Number of VPCs - 5
+ Number of public IP addresses - 5
+ Number of Gateway VPC Endpoints - 20
+ Number of Inteface VPC Endpoints - 20

## Problem: Use case stack can’t be deleted in CloudFormation after the Deployment dashboard stack gets deleted
<a name="problem-use-case-stack-cant-be-deleted-in-cloudformation-after-the-deployment-management-stack-gets-deleted"></a>

If the Deployment dashboard stack is deleted in CloudFormation before all of the use case stacks are deleted, the use cases can end up in a locked (unusable) state. This is due to an IAM role created by the Deployment dashboard stack no longer exists preventing modifications to the use case stack.

### Resolution
<a name="resolution-problem-use-case-stack-cant-be-deleted-in-cloudformation-after-the-deployment-management-stack-gets-deleted"></a>

**Warning**
Ensure you clean up any manually created roles immediately after usage. These are elevated permissions that users could exploit for role elevation.

Recreate the deleted IAM role to enable the deletion of the CloudFormation stacks:

1. Open the CloudFormation console and determine the role that is associated with your locked stack.

   1. The role ARN can be found in the stack info section labeled **IAM role.**

   1. The role name is what follows after **:role/** in the IAM role ARN (for example, **arn:aws:iam::<account-id>:role/<role-name>**)

1. Create a new role in IAM with the same name as the deleted role.

   1. Select **AWS service** as the trusted entity and select **CloudFormation** from the drop down.

   1. Add the necessary permissions. If you’re unsure about the required permissions, you can use the AWS managed **AdministratorAccess** policy.

   1. Enter the role name exactly as obtained in Step 1.

1. Return to the CloudFormation console and delete the locked stacks.

1. Once all locked stacks have been successfully deleted, return to IAM and delete any roles created in Step 2.

## Problem: Use case UI does not reflect changes in settings
<a name="problem-use-case-ui-does-not-reflect-changes-in-settings"></a>

When use cases are updated, the UI is deployed to CloudFront. However, because CloudFront caches deployments as well as the configuration file that dictates how some settings are shown to the user, these changes might not be reflected immediately.

### Resolution
<a name="resolution-problem-use-case-ui-does-not-reflect-changes-in-settings"></a>

The CloudFront distribution can be invalidated to force the new configuration to be propagated to frontend users.

1. Open the CloudFormation console and determine the CloudFront distribution that is associated with your use case stack.

   1. The use case stack should start with the same name you used when deploying the use case.

   1. Locate the nested stack corresponding to the UI. The nested stack name should begin with **WebAppS3UINestedStackS3UINestedStackResource**.

   1. Under the **Resources** tab, locate the resource of type **AWS::CloudFront::Distribution**, then select the physical ID. This will open the distribution in the CloudFront console.

1. Navigate to the **Invalidations** tab, then choose **Create Invalidation**, and input a path of /\*. This will invalidate all paths.

1. In your own browser, delete any cookies and cached files related to the use case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
