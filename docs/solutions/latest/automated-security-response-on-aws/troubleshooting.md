---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

 [Known issue resolution](known-issue-resolution.md) provides instructions to mitigate known errors. If these instructions don’t address your issue, [Contact AWS Support](contact-aws-support.md) provides instructions for opening an AWS Support case for this solution.

## PutS3BucketPolicyDeny fails
<a name="puts3bucketpolicydeny-fails"></a>

Associated controls: AWS FSBP v1.0.0 S3.6, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

Issue: The PutS3BucketPolicyDeny with the following error:

 `Unable to create an explicit deny statement for {bucket_name}.`

If the principals for all policies on the target bucket are "\*", the solution cannot add the deny policy to the target bucket as it would block out all bucket actions for all principals.

 **Resolution:** Modify the bucket policy to allow actions to specific accounts instead of using "\*" principals and restrict denied actions.

## How to disable the solution
<a name="how-to-disable-the-solution"></a>

In the event of an incident, you may find that you need to disable the solution without removing any of the infrastructure. These scenarios detail how to disable different components in the solution.

 **Scenario 1**: Disable automatic remediation for a single control

1. In the Admin account, navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Locate the Admin stack and view its **Outputs** tab.

1. Copy the value of the `RemediationConfigurationDynamoDBTable` output.

1. Navigate to the [DynamoDB console](https://console.aws.amazon.com/dynamodbv2/home?) and open the Remediation Configuration table.

1. Select **Explore Table Items**.

1. Under **Scan or query items**, select **Query**.

1. Enter the control ID (for example, `Lambda.1`) in the **Partition key: controlId** field and click **Run**.

1. Select the returned item, then click **Actions > Edit item**.

1. Change the `automatedRemediationEnabled` attribute value to **False**.

1. Click **Save and Close**.

 **Scenario 2**: Disable automatic remediation for all controls

1. Follow steps 1-5 from Scenario 1 to access the Remediation Configuration table items.

1. Under **Scan or query items**, select **Scan** to view all controls.

1. For each control with `automatedRemediationEnabled` set to **True**, select the item and click **Actions > Edit item**.

1. Change the `automatedRemediationEnabled` attribute value to **False** and click **Save and Close**.

1. Repeat for all controls you wish to disable.

 **Scenario 3**: Disable manual remediation for an account

1. Navigate to the [EventBridge console](https://console.aws.amazon.com/events/home?).

1. Select **Rules** in the sidebar.

1. Select the **default** event bus and search for `Remediate_with_ASR_CustomAction`.

1. Select the rule and click the **Disable** button.
