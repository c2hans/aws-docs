---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_NoBidModuleParameters.html
---

# NoBidModuleParameters
<a name="API_NoBidModuleParameters"></a>

Describes the parameters of a no bid module.

## Contents
<a name="API_NoBidModuleParameters_Contents"></a>

 ** passThroughPercentage **   <a name="rtbfabric-Type-NoBidModuleParameters-passThroughPercentage"></a>
The pass through percentage.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** reason **   <a name="rtbfabric-Type-NoBidModuleParameters-reason"></a>
The reason description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** reasonCode **   <a name="rtbfabric-Type-NoBidModuleParameters-reasonCode"></a>
The reason code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

## See Also
<a name="API_NoBidModuleParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/NoBidModuleParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/NoBidModuleParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/NoBidModuleParameters)
