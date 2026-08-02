---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/enable-fully-automated-remediations.html
---

# Enable fully-automated remediations
<a name="enable-fully-automated-remediations"></a>

The other mode of operation for the solution is to automatically remediate findings as they arrive in Security Hub.

**Important**
Before enabling fully automated remediations, ensure the solution is configured in the accounts and regions where you are conformable with the solution making automated changes. If you would like to narrow the scope of the solution’s automated remediations, see the section below on [filtering fully-automated remediations](#filter-remediations).

## Example: Enable fully-automated remediations for Lambda.1
<a name="enable-remediations-example"></a>

Enabling automatic remediations will initiate remediations on all resources matching the control you enable (Lambda.1).

**Important**
Confirm that you want all public Lambda Functions within the scope of the solution to have this permission revoked. Fully-automated remediations will not be limited in scope to the Function you created. The solution will remediate this control if it is detected in any of the accounts and Regions in which it is installed.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Confirm no desired public Functions | Confirm no desired public Functions |
|  `222222222222`  | Member | Confirm no desired public Functions | Confirm no desired public Functions |

## Locate the Remediation Configuration DynamoDB Table
<a name="locate-config-table"></a>

In the Admin account, view the `Outputs` for the Admin stack in the CloudFormation console. You will see an output titled `RemediationConfigurationDynamoDBTable`.

This is the name of the Remediation Configuration DynamoDB table, which controls automated remediation configurations for the solution. Copy the value of this output and locate the corresponding DynamoDB table in the DynamoDB console.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Locate the Remediation Configuration DynamoDB table. | None |
|  `222222222222`  | Member | None | None |

## Modify the Remediation Configuration Table
<a name="edit-table-item"></a>

In the DynamoDB console where you have located the Remediation Configuration table, select **Explore Table Items**.

Each item in the table corresponds to a Security Hub control supported by the solution. Each item has a `automatedRemediationEnabled` attribute that can be modified to enable fully-automated remediations for the associated control.

To enable Lambda.1, under **Scan or query items** select **Query**. Under **Partition key: controlId** enter `Lambda.1` and click **Run**. You will see a single item returned corresponding to the Lambda.1 control.

![remediation configuration table](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/remediation-configuration-table.png)

Now, select the `Lambda.1` item then click **Actions > Edit item**.

![remediation config edit item](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/remediation-config-edit-item.png)

Finally, change the `automatedRemediationEnabled` attribute value to **True**. Click **Save and Close**.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Modify the Remediation Configuration DynamoDB table. | None |
|  `222222222222`  | Member | None | None |

## Configure the resource
<a name="configure-the-resource"></a>

In the member account, re-configure the Lambda Function to allow public access.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | None | None |
|  `222222222222`  | Member | None | Configure the Lambda Function to allow public access |

## Confirm that the remediation resolved the finding
<a name="confirm-the-remediation-resolved-finding2"></a>

It may take some time for Config to detect the insecure configuration again. You should receive two SNS notifications. The first will indicate that a remediation has been initiated. The second will indicate that the remediation succeeded. After receiving the second notification, navigate to the Lambda console in the member account and confirm that the public access has been revoked.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | None | None |
|  `222222222222`  | Member | None | Confirm that the remediation succeeded |

## (Optional) Configure Filtering for Fully-Automated Remediations
<a name="filter-remediations"></a>

If you would like to limit the scope in which the solution runs remediations, you can apply filters. These filters will only apply to fully-automated remediations and will not impact manually invoked remediations.

The solution offers filtering on the following dimensions:

1. Account Ids

1. Organizational Units (OUs)

1. Resource Tags

Each dimension is configurable by modifying the Systems Manager Parameters deployed by the solution corresponding to the given dimension. All filtering parameters in Parameter Store can be located in the Admin account under the `/ASR/Filters/` path.

Each dimension has two parameters for configuration, one for filter value and another for the filter mode. For example, the Account Ids dimension has two parameters named `/ASR/Filters/AccountFilters` and `/ASR/Filters/AccountFilterMode`. Both must be modified to configure filtering on Account Ids.

For example, to limit fully-automated remediations to run in only accounts `111111111111` and `222222222222`, you would change the value of `/ASR/Filters/AccountFilters` to **"111111111111, 222222222222"**. Then, change the value of `/ASR/Filters/AccountFilterMode` to **"Include"**. The solution will then ignore any findings generated for accounts other than 111111111111 or 222222222222.

Each filter parameter takes a comma-delimited list of values to filter on, and each "mode" parameter can be set to either **Include**, **Exclude**, or **Disabled**.
