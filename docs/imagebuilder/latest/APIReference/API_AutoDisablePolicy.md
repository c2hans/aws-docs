---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_AutoDisablePolicy.html
---

# AutoDisablePolicy
<a name="API_AutoDisablePolicy"></a>

Defines the rules by which an image pipeline is automatically disabled when it fails.

## Contents
<a name="API_AutoDisablePolicy_Contents"></a>

 ** failureCount **   <a name="imagebuilder-Type-AutoDisablePolicy-failureCount"></a>
The number of consecutive scheduled image pipeline executions that must fail before Image Builder automatically disables the pipeline.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

## See Also
<a name="API_AutoDisablePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/AutoDisablePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/AutoDisablePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/AutoDisablePolicy)
