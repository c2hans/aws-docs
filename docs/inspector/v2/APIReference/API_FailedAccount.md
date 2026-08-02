---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FailedAccount.html
---

# FailedAccount
<a name="API_FailedAccount"></a>

An object with details on why an account failed to enable Amazon Inspector.

## Contents
<a name="API_FailedAccount_Contents"></a>

 ** accountId **   <a name="inspector2-Type-FailedAccount-accountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** errorCode **   <a name="inspector2-Type-FailedAccount-errorCode"></a>
The error code explaining why the account failed to enable Amazon Inspector.
Type: String
Valid Values: `ALREADY_ENABLED | ENABLE_IN_PROGRESS | DISABLE_IN_PROGRESS | SUSPEND_IN_PROGRESS | RESOURCE_NOT_FOUND | ACCESS_DENIED | INTERNAL_ERROR | SSM_UNAVAILABLE | SSM_THROTTLED | EVENTBRIDGE_UNAVAILABLE | EVENTBRIDGE_THROTTLED | RESOURCE_SCAN_NOT_DISABLED | DISASSOCIATE_ALL_MEMBERS | ACCOUNT_IS_ISOLATED | EC2_SSM_RESOURCE_DATA_SYNC_LIMIT_EXCEEDED | EC2_SSM_ASSOCIATION_VERSION_LIMIT_EXCEEDED | BLOCKED_BY_ORGANIZATION_POLICY`
Required: Yes

 ** errorMessage **   <a name="inspector2-Type-FailedAccount-errorMessage"></a>
The error message received when the account failed to enable Amazon Inspector.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** resourceStatus **   <a name="inspector2-Type-FailedAccount-resourceStatus"></a>
An object detailing which resources Amazon Inspector is enabled to scan for the account.
Type: [ResourceStatus](API_ResourceStatus.md) object
Required: No

 ** status **   <a name="inspector2-Type-FailedAccount-status"></a>
The status of Amazon Inspector for the account.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: No

## See Also
<a name="API_FailedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FailedAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FailedAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FailedAccount)
