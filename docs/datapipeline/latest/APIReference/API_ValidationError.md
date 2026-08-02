---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ValidationError.html
---

# ValidationError
<a name="API_ValidationError"></a>

Defines a validation error. Validation errors prevent pipeline activation. The set of validation errors that can be returned are defined by AWS Data Pipeline.

## Contents
<a name="API_ValidationError_Contents"></a>

 ** errors **   <a name="DP-Type-ValidationError-errors"></a>
A description of the validation error.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** id **   <a name="DP-Type-ValidationError-id"></a>
The identifier of the object that contains the validation error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: No

## See Also
<a name="API_ValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ValidationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ValidationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ValidationError)
