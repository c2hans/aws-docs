---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StackSetOperationResultSummary.html
---

# StackSetOperationResultSummary
<a name="API_StackSetOperationResultSummary"></a>

The structure that contains information about a specified operation's results for a given account in a given Region.

## Contents
<a name="API_StackSetOperationResultSummary_Contents"></a>

 ** Account **
[Self-managed permissions] The name of the AWS account for this operation result.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** AccountGateResult **
The results of the account gate function CloudFormation invokes, if present, before proceeding with StackSet operations in an account.
Type: [AccountGateResult](API_AccountGateResult.md) object
Required: No

 ** OrganizationalUnitId **
[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for [DeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html).
Type: String
Pattern: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`
Required: No

 ** Region **
The name of the AWS Region for this operation result.
Type: String
Pattern: `^[a-zA-Z0-9-]{1,128}$`
Required: No

 ** Status **
The result status of the StackSet operation for the given account in the given Region.
+  `CANCELLED`: The operation in the specified account and Region has been canceled. This is either because a user has stopped the StackSet operation, or because the failure tolerance of the StackSet operation has been exceeded.
+  `FAILED`: The operation in the specified account and Region failed.

  If the StackSet operation fails in enough accounts within a Region, the failure tolerance for the StackSet operation as a whole might be exceeded.
+  `RUNNING`: The operation in the specified account and Region is currently in progress.
+  `PENDING`: The operation in the specified account and Region has yet to start.
+  `SUCCEEDED`: The operation in the specified account and Region completed successfully.
Type: String
Valid Values: `PENDING | RUNNING | SUCCEEDED | FAILED | CANCELLED`
Required: No

 ** StatusReason **
The reason for the assigned result status.
Type: String
Required: No

## See Also
<a name="API_StackSetOperationResultSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperationResultSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperationResultSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperationResultSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
