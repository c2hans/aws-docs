---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressAnalysis.html
---

# IngressAnalysis
<a name="API_IngressAnalysis"></a>

The Add On ARN and its returned value that is evaluated in a policy statement's conditional expression to either deny or block the incoming email.

## Contents
<a name="API_IngressAnalysis_Contents"></a>

 ** Analyzer **   <a name="sesmailmanager-Type-IngressAnalysis-Analyzer"></a>
The Amazon Resource Name (ARN) of an Add On.
Type: String
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ResultField **   <a name="sesmailmanager-Type-IngressAnalysis-ResultField"></a>
The returned value from an Add On.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(addon\.)?[\sa-zA-Z0-9_]+`
Required: Yes

## See Also
<a name="API_IngressAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressAnalysis)
