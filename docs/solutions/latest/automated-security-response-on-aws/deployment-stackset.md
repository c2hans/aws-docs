---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/deployment-stackset.html
---

# Automated deployment - StackSets
<a name="deployment-stackset"></a>

**Note**
We recommend deploying with StackSets. However, for single account deployments or for testing or evaluation purposes, consider the [stacks deployment](deployment.md) option.

Before you launch the solution, review the architecture, solution components, security, and design considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your AWS Organizations.

 **Time to deploy:** Approximately 30 minutes per account, depending upon StackSet parameters.

## Prerequisites
<a name="prerequisites-stackset"></a>

 [AWS Organizations](https://aws.amazon.com/organizations/) helps you centrally manage and govern your multi-account AWS environment and resources. StackSets work best with AWS Organizations.

If you have previously deployed v1.3.x or earlier of this solution, you must uninstall the existing solution. For more information, refer to [Update the solution](update-the-solution.md).

Before you deploy this solution, review your AWS Security Hub deployment:
+ There must be a delegated Security Hub admin account in your AWS Organization.
+ Security Hub should be configured to aggregate findings across Regions. For more information, refer to [Aggregating findings across Regions](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) in the AWS Security Hub User Guide.
+ You should [activate Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-prereq-config.html) for your organization in each Region where you have AWS usage.

This procedure assumes that you have multiple accounts using AWS Organizations, and have delegated an AWS Organizations admin account and an AWS Security Hub admin account.

 **This solution works with both [AWS Security Hub and AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html).**

## Deployment overview
<a name="deployment-overview-stackset"></a>

**Note**
StackSets deployment for this solution uses a combination of service-managed and self-managed StackSets. Self-managed StackSets must be used currently because they use nested stacks, which are not yet supported with service-managed StackSets.

Deploy the StackSets from a [delegated administrator account](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html) in your AWS Organizations.

**Planning**
Use the following form to help with StackSets deployment. Prepare your data, then copy and paste the values during deployment.

```
AWS Organizations admin account ID: _______________
Security Hub admin account ID: _______________
CloudTrail Logs Group: ______________________________
Member account IDs (comma-separated list):
___________________,
___________________,
___________________,
___________________,
___________________
AWS Organizations OUs (comma-separated list):
___________________,
___________________,
___________________,
___________________,
___________________
```

 [(Optional) Step 0: Deploy the ticketing integration stack](#step-0-stackset)
+ If you intend to use the ticketing feature, deploy the ticketing integration stack into your Security Hub admin account first.
+ Copy the Lambda function name from this stack and provide it as input to the admin stack (see Step 1).

 [Step 1: Launch the admin stack in the delegated Security Hub admin account](#step-1-stackset)
+ Using a self-managed StackSet, launch the `automated-security-response-admin.template` AWS CloudFormation template into your AWS Security Hub admin account in the same Region as your Security Hub admin. This template uses nested stacks.
+ Choose which Security Standards to install. By default, only SC is selected (Recommended).
+ Choose an existing Orchestrator log group to use. Choose `Yes` if `SO0111-ASR-Orchestrator` already exists from a previous installation.
+ Choose whether to enable the solution’s Web UI. If you choose to enable this feature, you must also enter an email address to be assigned an administrator role.
+ Choose your preferences for collecting CloudWatch metrics related to the solution’s operational health.

For more information on self-managed StackSets, refer to [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the *AWS CloudFormation User Guide*.

 [Step 2: Install the remediation roles into each AWS Security Hub member account](#step-2-stackset)

Wait for Step 1 to complete deployment, because the template in Step 2 references IAM roles created by Step 1.
+ Using a service-managed StackSet, launch the `automated-security-response-member-roles.template` AWS CloudFormation template into a single Region in each account in your AWS Organizations.
+ Choose to install this template automatically when a new account joins the organization.
+ Enter the account ID of your AWS Security Hub admin account.
+ Enter a value for the `namespace` which will be used to prevent resource name conflicts with a previous or concurrent deployment in the same account. Enter a string of up to 9 lowercase alphanumeric characters.

 [Step 3: Launch the member stack into each AWS Security Hub member account and Region](#step-3-stackset)
+ Using self-managed StackSets, launch the `automated-security-response-member.template` AWS CloudFormation template into all Regions where you have AWS resources in every account in your AWS Organization managed by the same Security Hub admin.
**Note**
Until service-managed StackSets support nested stacks, you must do this step for any new accounts that join the organization.
+ Choose which Security Standard playbooks to install.
+ Provide the name of a CloudTrail log group (used by some remediations).
+ Enter the account ID of your AWS Security Hub admin account.
+ Enter a value for the `namespace` which will be used to prevent resource name conflicts with a previous or concurrent deployment in the same account. Enter a string of up to 9 lowercase alphanumeric characters. This should match the `namespace` value you selected for the Member Roles stack, additionally, the namespace value does not need to be unique per member account.

## (Optional) Step 0: Launch a ticket system integration stack
<a name="step-0-stackset"></a>

1. If you intend to use the ticketing feature, launch the respective integration stack first.

1. Choose the provided integration stacks for Jira or ServiceNow, or use them as a blueprint to implement your own custom integration.

    **To deploy the Jira stack**:

   1. Enter a name for your stack.

   1. Provide the URI to your Jira instance.

   1. Provide the project key for the Jira project that you want to send tickets to.

   1. Create a new key-value secret in AWS Secrets Manager that holds your Jira `Username` and `Password`.
**Note**
You can choose to use a Jira API key in place of your password by providing your username as `Username` and your API key as the `Password`.

   1. Add the ARN of this secret as input to the stack.

       **Provide a stack name, Jira project information, and Jira API credentials.**
![Jira ticket system integration stack configuration](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/ticket-system-integration-stack-jira.png)

       **Jira Field Configuration**:

      After deploying the Jira stack, you can customize Jira ticket fields by setting the `JIRA_FIELDS_MAPPING` environment variable on the Lambda function. This JSON string overrides default Jira ticket fields and must follow the Jira API fields structure.

      Default values when `JIRA_FIELDS_MAPPING` is empty or fields are not specified:
      +  **priority**: `{"id": "3"}` (Medium priority)
      +  **issuetype**: `{"id": "10006"}` (Task)
      +  **accountId**: Automatically retrieved using the `GET /rest/api/2/myself` API endpoint

        Example configuration with custom fields:

        ```
        {
          "reporter": {"accountId": "123456:494dcbff-1b80-482c-a89d-56ae81c145a4"},
          "priority": {"id": "1"},
          "issuetype": {"id": "10006"},
          "assignee": {"accountId": "123456:another-user-id"},
          "customfield_10001": "custom value"
        }
        ```

        Common Jira field IDs:
      +  **Priority IDs**: 1 (Highest), 2 (High), 3 (Medium), 4 (Low), 5 (Lowest)
      +  **Issue Type ID**: Varies by Jira project (for example, 10006 for Task)
      +  **Account ID**: Format `123456:494dcbff-1b80-482c-a89d-56ae81c145a4`

        You can find your Jira field IDs and account IDs using the Jira REST API:
      +  `GET /rest/api/2/myself` for account ID
      +  `GET /rest/api/2/priority` for priority IDs
      +  `GET /rest/api/2/project/{projectKey}` for issue type IDs

        For more information, refer to the [Jira REST API v2 Issue POST format](https://developer.atlassian.com/server/jira/platform/rest/v10000/api-group-issue/#api-api-2-issue-post).

         **To deploy the ServiceNow stack**:

   1. Enter a name for your stack.

   1. Provide the URI of your ServiceNow instance.

   1. Provide your ServiceNow table name.

   1. Create an API key in ServiceNow with permission to modify the table you intend to write to.

   1. Create a secret in Secrets Manager with the key `API_Key` and provide the secret ARN as input to the stack.

       **Provide a stack name, ServiceNow project information, and ServiceNow API credentials.**
![ServiceNow ticket system integration stack configuration](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/ticket-system-integration-stack-servicenow.png)

       **To create a custom integration stack**: Include a Lambda function that the solution orchestrator Step Functions can call for each remediation. The Lambda function should take the input provided by Step Functions, construct a payload according to the requirements of your ticketing system, and make a request to your system to create the ticket.

## Step 1: Launch the admin stack in the delegated Security Hub admin account
<a name="step-1-stackset"></a>

1. Launch the [admin stack](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template), `automated-security-response-admin.template`, with your Security Hub admin account. Typically, one per organization in a single Region. Because this stack uses nested stacks, you must deploy this template as a self-managed StackSet.

### Parameters
<a name="parameters"></a>

| Parameter | Default | Description |
| --- | --- | --- |
|  **Load SC Admin Stack**  |  `yes`  | Specify whether to install the admin components for automated remediation of SC controls. |
|  **Load AFSBP Admin Stack**  |  `no`  | Specify whether to install the admin components for automated remediation of FSBP controls. |
|  **Load CIS120 Admin Stack**  |  `no`  | Specify whether to install the admin components for automated remediation of CIS120 controls. |
|  **Load CIS140 Admin Stack**  |  `no`  | Specify whether to install the admin components for automated remediation of CIS140 controls. |
|  **Load CIS300 Admin Stack**  |  `no`  | Specify whether to install the admin components for automated remediation of CIS300 controls. |
|  **Load PCI321 Admin Stack**  |  `no`  | Specify whether to install the admin components for automated remediation of PCI321 controls. |
|  **Load NIST Admin Stack**  |  `no`  | Specify whether to install the admin components for automated remediation of NIST controls. |
|  **Reuse Orchestrator Log Group**  |  `no`  | Select whether or not to reuse an existing `SO0111-ASR-Orchestrator` CloudWatch Logs group. This simplifies reinstallation and upgrades without losing log data from a previous version. Reuse existing `Orchestrator Log Group` choose `yes` if the `Orchestrator Log Group` still exists from an earlier deployment in this account, otherwise `no`. If you are performing a stack update from an earlier version than v2.3.0 choose `no`  |
|  **ShouldDeployWebUI**  |  `yes`  | Deploy the Web UI components including API Gateway, Lambda functions, and CloudFront distribution. Choose "yes" to enable the web-based user interface for viewing findings and remediation status. If you choose to disable this feature, you can still configure automated remediations and run remediations on-demand using the Security Hub CSPM custom action. |
|  **AdminUserEmail**  |  *(Optional input)*  | Email address for the initial admin user. This user will have full administrative access to the ASR Web UI. Required **only** when Web UI is enabled. |
|  **Use CloudWatch Metrics**  |  `yes`  | Specify whether to enable CloudWatch Metrics for monitoring the solution. This will create a CloudWatch Dashboard for viewing metrics. |
|  **Use CloudWatch Metrics Alarms**  |  `yes`  | Specify whether to enable CloudWatch Metrics Alarms for the solution. This will create Alarms for certain metrics collected by the solution. |
|  **RemediationFailureAlarmThreshold**  |  `5`  | Specify the threshold for percentage of remediation failures per control ID. For example, if you enter `5`, you receive an alarm if a control ID fails more than 5% of remediations at a given day.<br />This parameter functions only if alarms are created (see the **Use CloudWatch Metrics Alarms** parameter). |
|  **EnableEnhancedCloudWatchMetrics**  |  `no`  | If `yes`, creates additional CloudWatch metrics to track all control IDs individually on the CloudWatch dashboard and as CloudWatch alarms.<br />See the [Cost](cost.md#additional-cost-enhanced-metrics) section to understand the additional cost that this incurs. |
|  **TicketGenFunctionName**  |  *(Optional input)*  | Optional. Leave blank if you don’t want to integrate a ticketing system. Otherwise, provide the Lambda function name from the stack output of [Step 0](#step-0-stackset), for example: `SO0111-ASR-ServiceNow-TicketGenerator`. |

 **Configure StackSet options**

![Configure StackSet options page](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/configure-stackset-options.png)

1. For the **Account numbers** parameter, enter the account ID of the AWS Security Hub admin account.

1. For the **Specify regions** parameter, select only the Region where Security Hub admin is turned on. Wait for this step to complete before going on to Step 2.

   You can view the status of the StackSet operation in the AWS CloudFormation console on the StackSet details page. You should receive a **SUCCEEDED** operation status in approximately 15 minutes.

## Step 2: Install the remediation roles into each AWS Security Hub member account
<a name="step-2-stackset"></a>

Use a service-managed StackSets to deploy the [member roles template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member-roles.template), `automated-security-response-member-roles.template`. This StackSet must be deployed in one Region per member account. It defines the global roles that allow cross-account API calls from the ASR Orchestrator step function.

### Parameters
<a name="parameters-2"></a>

| Parameter | Default | Description |
| --- | --- | --- |
|  **Namespace**  |  {{<Requires input>}}  | Enter a string of up to 9 lowercase alphanumeric characters. Unique namespace to be added as a suffix to remediation IAM role names. The same namespace should be used in the Member Roles and Member stacks. This string should be unique for each solution deployment, but does not need to be changed during stack updates. The namespace value does **not** need to be unique per member account. |
|  **Sec Hub Admin Account**  |  {{<Requires input>}}  | Enter the 12-digit account ID for the AWS Security Hub admin account. This value grants permissions to the admin account’s solution role. |

1. Deploy to the entire organization (typical) or to organizational units, as per your organizations policies.

1. Turn on automatic deployment so new accounts in the AWS Organizations receive these permissions.

1. For the **Specify regions** parameter, select a single Region. IAM roles are global. You can continue to Step 3 while this StackSet deploys.

   You can view the status of the StackSet operation in the AWS CloudFormation console on the StackSet details page. You should receive a **SUCCEEDED** operation status in approximately 5 minutes.

    **Specify StackSet details**
![Specify StackSet details page](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/specify-stackset-details.png)

## Step 3: Launch the member stack into each AWS Security Hub member account and Region
<a name="step-3-stackset"></a>

Because the [member stack](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member.template) uses nested stacks, you must deploy as a self-managed StackSet. This does not support automatic deployment to new accounts in the AWS Organization.

### Parameters
<a name="parameters"></a>

| Parameter | Default | Description |
| --- | --- | --- |
|  **Provide the name of the LogGroup to be used to create Metric Filters and Alarms**  |  {{<Requires input>}}  | Specify the name of a CloudWatch Logs group where CloudTrail logs API calls. This is used for CIS 3.1-3.14 remediations. |
|  **Load SC Member Stack**  |  `yes`  | Specify whether to install the member components for automated remediation of SC controls. |
|  **Load AFSBP Member Stack**  |  `no`  | Specify whether to install the member components for automated remediation of FSBP controls. |
|  **Load CIS120 Member Stack**  |  `no`  | Specify whether to install the member components for automated remediation of CIS120 controls. |
|  **Load CIS140 Member Stack**  |  `no`  | Specify whether to install the member components for automated remediation of CIS140 controls. |
|  **Load CIS300 Member Stack**  |  `no`  | Specify whether to install the member components for automated remediation of CIS300 controls. |
|  **Load PCI321 Member Stack**  |  `no`  | Specify whether to install the member components for automated remediation of PCI321 controls. |
|  **Load NIST Member Stack**  |  `no`  | Specify whether to install the member components for automated remediation of NIST controls. |
|  **Create S3 Bucket For Redshift Audit Logging**  |  `no`  | Choose `yes` to create the S3 bucket for the FSBP RedShift.4 remediation. For details of the S3 bucket and the remediation, review the [Redshift.4 remediation](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html#fsbp-redshift-4) in the *AWS Security Hub User Guide*. |
|  **Sec Hub Admin Account**  |  {{<Requires input>}}  | Enter the 12-digit account ID for the AWS Security Hub admin account. |
|  **Namespace**  |  {{<Requires input>}}  | Enter a string of up to 9 lowercase alphanumeric characters. This string becomes part of the IAM role names and Action Log S3 bucket. Use the same value for member stack deployment and member roles stack deployment. String should be unique for each solution deployment, but does not need to be changed during stack updates. |
|  **EnableCloudTrailForASRActionLog**  |  `no`  | Select `yes` if you want to monitor management events conducted by the solution on the CloudWatch dashboard. The solution creates a CloudTrail trail in each member account where you select `yes`. You must deploy the solution into an AWS Organization to enable this feature. **Additionally, you can only enable this feature in a single region within the same account.** See the [Cost](cost.md#additional-cost-action-log) section to understand the additional cost that this incurs. |

 **Accounts**

![Accounts deployment configuration page](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/accounts.png)

 **Deployment locations**: You can specify a list of account numbers or organizational units.

 **Specify regions**: Select all of the Regions where you want to remediate findings. You can adjust Deployment options as appropriate for the number of accounts and Regions. Region Concurrency can be parallel.

You can view the status of the StackSet operation in the AWS CloudFormation console on the StackSet details page. You should receive a **SUCCEEDED** operation status for each account and Region combination. Deployment time varies based on the number of accounts and Regions selected.
