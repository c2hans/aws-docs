---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_UnprocessedAccount.html
---

# UnprocessedAccount
<a name="API_UnprocessedAccount"></a>

A member account that was included in a request but for which the request could not be processed.

## Contents
<a name="API_UnprocessedAccount_Contents"></a>

 ** AccountId **   <a name="detective-Type-UnprocessedAccount-AccountId"></a>
The AWS account identifier of the member account that was not processed.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** Reason **   <a name="detective-Type-UnprocessedAccount-Reason"></a>
The reason that the member account request could not be processed.
Type: String
Required: No

## See Also
<a name="API_UnprocessedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/UnprocessedAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/UnprocessedAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/UnprocessedAccount)
