---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-2b.-achieve-prerequisites-manually-optional.html
---

# Step 2b. Fulfill prerequisites manually (optional)
<a name="step-2b.-achieve-prerequisites-manually-optional"></a>

**Note**
Use this procedure only for Organizations deployments.

Use the following procedure to manually fulfill prerequisites for the solution in your Organizations.

1. Activate **AWS Organizations Full Feature**.

1. Designate a member account as the [StackSets administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html). This account will be your hub account.

**Note**
The solution deploys service-managed StackSets. You must allow trusted access with AWS Organizations in the organization management account before you can use service-managed permissions on the AWS CloudFormation console (refer to [Enable trusted access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html?icmpid=docs_cfn_console) in the *AWS CloudFormation User Guide*) or AWS Organizations console (refer to [Enabling trusted access with AWS CloudFormation Stacksets](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html#integrate-enable-ta-cloudformation) in the *AWS Organizations User Guide*).
