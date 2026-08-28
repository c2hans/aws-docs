---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFormationStackDetails.html
---

# AwsCloudFormationStackDetails
<a name="API_AwsCloudFormationStackDetails"></a>

Nests a stack as a resource in a top-level template. Nested stacks are stacks created as resources for another stack.

## Contents
<a name="API_AwsCloudFormationStackDetails_Contents"></a>

 ** Capabilities **   <a name="securityhub-Type-AwsCloudFormationStackDetails-Capabilities"></a>
The capabilities allowed in the stack.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** CreationTime **   <a name="securityhub-Type-AwsCloudFormationStackDetails-CreationTime"></a>
The time at which the stack was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsCloudFormationStackDetails-Description"></a>
A user-defined description associated with the stack.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DisableRollback **   <a name="securityhub-Type-AwsCloudFormationStackDetails-DisableRollback"></a>
Boolean to enable or disable rollback on stack creation failures.
Type: Boolean
Required: No

 ** DriftInformation **   <a name="securityhub-Type-AwsCloudFormationStackDetails-DriftInformation"></a>
Information about whether a stack's actual configuration differs, or has drifted, from its expected configuration, as defined in the stack template and any values specified as template parameters.
Type: [AwsCloudFormationStackDriftInformationDetails](API_AwsCloudFormationStackDriftInformationDetails.md) object
Required: No

 ** EnableTerminationProtection **   <a name="securityhub-Type-AwsCloudFormationStackDetails-EnableTerminationProtection"></a>
Whether termination protection is enabled for the stack.
Type: Boolean
Required: No

 ** LastUpdatedTime **   <a name="securityhub-Type-AwsCloudFormationStackDetails-LastUpdatedTime"></a>
The time the nested stack was last updated. This field will only be returned if the stack has been updated at least once.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NotificationArns **   <a name="securityhub-Type-AwsCloudFormationStackDetails-NotificationArns"></a>
The Amazon Resource Names (ARNs) of the Amazon SNS topic to which stack-related events are published.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Outputs **   <a name="securityhub-Type-AwsCloudFormationStackDetails-Outputs"></a>
A list of output structures.
Type: Array of [AwsCloudFormationStackOutputsDetails](API_AwsCloudFormationStackOutputsDetails.md) objects
Required: No

 ** RoleArn **   <a name="securityhub-Type-AwsCloudFormationStackDetails-RoleArn"></a>
The ARN of an IAM role that's associated with the stack.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StackId **   <a name="securityhub-Type-AwsCloudFormationStackDetails-StackId"></a>
Unique identifier of the stack.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StackName **   <a name="securityhub-Type-AwsCloudFormationStackDetails-StackName"></a>
The name associated with the stack.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StackStatus **   <a name="securityhub-Type-AwsCloudFormationStackDetails-StackStatus"></a>
Current status of the stack.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StackStatusReason **   <a name="securityhub-Type-AwsCloudFormationStackDetails-StackStatusReason"></a>
Success or failure message associated with the stack status.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TimeoutInMinutes **   <a name="securityhub-Type-AwsCloudFormationStackDetails-TimeoutInMinutes"></a>
The length of time, in minutes, that CloudFormation waits for the nested stack to reach the `CREATE_COMPLETE` state.
Type: Integer
Required: No

## See Also
<a name="API_AwsCloudFormationStackDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFormationStackDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFormationStackDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFormationStackDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
