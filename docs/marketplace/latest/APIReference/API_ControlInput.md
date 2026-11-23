---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ControlInput.html
---

# ControlInput

A control to run as part of an assessment, and the input to run it with.

## Contents
<a name="API_ControlInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ControlId **   <a name="AWSMarketplaceService-Type-ControlInput-ControlId"></a>
The unique identifier of the control to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: Yes

 ** Input **   <a name="AWSMarketplaceService-Type-ControlInput-Input"></a>
Optional. The input for the control, as a JSON document. The fields that a control accepts depend on the control.
Type: JSON value
Required: No

## See Also
<a name="API_ControlInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ControlInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ControlInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ControlInput)
