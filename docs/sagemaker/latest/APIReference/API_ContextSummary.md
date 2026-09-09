---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContextSummary.html
---

# ContextSummary
<a name="API_ContextSummary"></a>

Lists a summary of the properties of a context. A context provides a logical grouping of other entities.

## Contents
<a name="API_ContextSummary_Contents"></a>

 ** ContextArn **   <a name="sagemaker-Type-ContextSummary-ContextArn"></a>
The Amazon Resource Name (ARN) of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:context/.*`
Required: No

 ** ContextName **   <a name="sagemaker-Type-ContextSummary-ContextName"></a>
The name of the context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,119}`
Required: No

 ** ContextType **   <a name="sagemaker-Type-ContextSummary-ContextType"></a>
The type of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Source **   <a name="sagemaker-Type-ContextSummary-Source"></a>
The source of the context.
Type: [ContextSource](API_ContextSource.md) object
Required: No

## See Also
<a name="API_ContextSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ContextSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ContextSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ContextSummary)
