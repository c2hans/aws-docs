---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ImportTaskError.html
---

# ImportTaskError
<a name="API_ImportTaskError"></a>

Import task error.

## Contents
<a name="API_ImportTaskError_Contents"></a>

 ** errorData **   <a name="mgn-Type-ImportTaskError-errorData"></a>
Import task error data.
Type: [ImportErrorData](API_ImportErrorData.md) object
Required: No

 ** errorDateTime **   <a name="mgn-Type-ImportTaskError-errorDateTime"></a>
Import task error datetime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** errorType **   <a name="mgn-Type-ImportTaskError-errorType"></a>
Import task error type.
Type: String
Valid Values: `VALIDATION_ERROR | PROCESSING_ERROR`
Required: No

## See Also
<a name="API_ImportTaskError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ImportTaskError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ImportTaskError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ImportTaskError)
