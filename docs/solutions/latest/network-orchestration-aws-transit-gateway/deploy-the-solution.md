---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

**Note**
If you have previously deployed this solution, see [Update the solution](update-the-solution.md) for update instructions.

## Prerequisites
<a name="prerequisites"></a>

You must meet the following prerequisites before launching the stacks.

If your accounts are part of Organizations, you must first manually activate AWS RAM in the Organizations console and obtain the Organizations management account ID and organization ID before deploying the solution templates.

### Activate AWS RAM for Organizations accounts
<a name="activate-aws-ram-for-organizations-accounts"></a>

Use the following procedure to activate AWS RAM using the AWS Organizations console.

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/home/).

1. In the navigation pane, select **Settings**.

1. Navigate to **AWS RAM**, and select **Enable access**.

Use the following procedure to activate the sharing option in the AWS RAM console.

1. Sign in to the [AWS RAM console](https://console.aws.amazon.com/ram/home).

1. In the navigation pane, select **Settings**.

1. Choose \*Enable sharing**\*with AWS Organizations**.

1. Choose **Save settings**.

### Identify the Organizations ARN
<a name="identify-the-organizations-arn"></a>

To use this solution with accounts connected to AWS Organizations, you must specify the AWS Organizations ARN when you launch the hub template. The ARN value consists of the AWS Organizations management account ID and the organization ID. You can build the ARN string manually if you have access to the AWS Organizations management account ID and the organization ID, or you can use the AWS Command Line Interface (AWS CLI) to query the Organization ARN.

**Note**
If you don’t have access to the management account ID and the Organization ID, contact your organization’s management account administrator.

Use the following procedure to build the Organizations ARN manually after you have the Organizations management account ID and the organization ID.

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/home/) from your organization’s management account.

1. Select **AWS accounts** from the navigation menu.

1. Identify the management account and record the **Account ID**.

1. Select **Settings** from the navigation menu.

1. Record the entry for **Organization ID**.

1. Use the following sample to manually build the Organization ARN. Replace the placeholders with your management account and organization IDs.

   ```
   arn:<AWS_PARTITION>:organizations::<ORG_MANAGEMENT_ACCOUNT_ID>:organization/<ORG-ID>
   ```

To use the AWS CLI to query the ARN, use the [describe-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-organization.html) API call. To set up AWS CLI, refer to [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface\_User Guide*.

## Deployment process overview
<a name="deployment-process-overview"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

**Important**
This solution includes data collection. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

Before you launch the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security.md), and other considerations discussed earlier in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 25 minutes

 [Step 1. (Optional) Launch the organization role stack](step-1-launch-the-organization-role-stack-optional.md)
+ Launch the CloudFormation template in your Organizations management account.
+ Enter values for the required **HubAccount** parameter.

 [Step 2. (Optional) Launch the service- linked role for AWS RAM hub stack](step-2-launch-the-service-linked-role-hub-stack-optional.md)

**Note**
If the `AWSServiceRoleForResourceAccessManager` role already exists, skip this step.
+ Launch the CloudFormation template in your hub account.

 [Step 3. Launch the hub stack](step-3-launch-the-hub-stack.md)
+ Launch the CloudFormation template in your hub account.
+ Enter values for the required **Account List or AWS Organizations ARN** parameter.
+ If deploying the web UI, enter values for the following parameters: **Allowed Listed Ranges**, **Console Login Information Email**, and **Cognito Domain Prefix**.
+ Review the other template parameters and adjust, if necessary.

 [Step 4. Launch the spoke stack(s)](step-4-launch-the-spoke-stacks.md)
+ Launch the CloudFormation template into your spoke account(s).
+ Enter a value for the required **Network (Hub) Account** parameter.

 [Step 5. Add tags](step-5-add-tags.md)
+ Add the required tags to the spoke VPCs and subnets.
+ Validate and view transit gateway attachments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
