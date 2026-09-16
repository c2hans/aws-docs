---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentFailureContext.html
---

# ComponentFailureContext
<a name="API_ComponentFailureContext"></a>

Contains details about the component that caused the image creation process to fail. The details identify the first step that failed when the component ran.

## Contents
<a name="API_ComponentFailureContext_Contents"></a>

 ** action **   <a name="imagebuilder-Type-ComponentFailureContext-action"></a>
The action that the failed step runs, for example `ExecuteBash`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** componentArn **   <a name="imagebuilder-Type-ComponentFailureContext-componentArn"></a>
The Amazon Resource Name (ARN) of the component build version that failed.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** errorMessage **   <a name="imagebuilder-Type-ComponentFailureContext-errorMessage"></a>
The error message from the step that failed. Image Builder truncates messages that are longer than 1024 characters. The component log in Amazon CloudWatch Logs contains the full output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 384000.
Required: No

 ** phaseName **   <a name="imagebuilder-Type-ComponentFailureContext-phaseName"></a>
The name of the phase in the component document where the failure occurred, such as `build`, `validate`, or `test`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** stepName **   <a name="imagebuilder-Type-ComponentFailureContext-stepName"></a>
The name of the step in the component document that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ComponentFailureContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentFailureContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentFailureContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentFailureContext)
