---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_FailedRemediationBatch.html
---

# FailedRemediationBatch
<a name="API_FailedRemediationBatch"></a>

List of each of the failed remediations with specific reasons.

## Contents
<a name="API_FailedRemediationBatch_Contents"></a>

 ** FailedItems **   <a name="config-Type-FailedRemediationBatch-FailedItems"></a>
Returns remediation configurations of the failed items.
Type: Array of [RemediationConfiguration](API_RemediationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** FailureMessage **   <a name="config-Type-FailedRemediationBatch-FailureMessage"></a>
Returns a failure message. For example, the resource is already compliant.
Type: String
Required: No

## See Also
<a name="API_FailedRemediationBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/FailedRemediationBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/FailedRemediationBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/FailedRemediationBatch)
