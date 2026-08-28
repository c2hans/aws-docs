---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RecordHandlerProgress.html
---

# RecordHandlerProgress
<a name="API_RecordHandlerProgress"></a>

Reports progress of a resource handler to CloudFormation.

Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html). Don't use this API in your code.

## Request Parameters
<a name="API_RecordHandlerProgress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** BearerToken **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ClientRequestToken **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`
Required: No

 ** CurrentOperationStatus **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED`
Required: No

 ** ErrorCode **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Valid Values: `NotUpdatable | InvalidRequest | AccessDenied | InvalidCredentials | AlreadyExists | NotFound | ResourceConflict | Throttling | ServiceLimitExceeded | NotStabilized | GeneralServiceException | ServiceInternalError | NetworkFailure | InternalFailure | InvalidTypeConfiguration | HandlerInternalFailure | NonCompliant | Unknown | UnsupportedTarget`
Required: No

 ** OperationStatus **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED`
Required: Yes

 ** ResourceModel **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** StatusMessage **
Reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## Errors
<a name="API_RecordHandlerProgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionalCheckFailed **
Error reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html). CloudFormation doesn't return this error to users.
HTTP Status Code: 400

 ** InvalidStateTransition **
Error reserved for use by the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html). CloudFormation doesn't return this error to users.
HTTP Status Code: 400

## See Also
<a name="API_RecordHandlerProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RecordHandlerProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RecordHandlerProgress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
