---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_FailedAccount.html
---

# FailedAccount
<a name="API_FailedAccount"></a>

An account that was in scope for an Organizational Report but could not be processed, along with the reason for the failure.

## Contents
<a name="API_FailedAccount_Contents"></a>

 ** accountId **   <a name="wellarchitected-Type-FailedAccount-accountId"></a>
The AWS account ID that failed.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** reason **   <a name="wellarchitected-Type-FailedAccount-reason"></a>
A human-readable explanation of why the account could not be processed.
Type: String
Required: Yes

## See Also
<a name="API_FailedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/FailedAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/FailedAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/FailedAccount)
