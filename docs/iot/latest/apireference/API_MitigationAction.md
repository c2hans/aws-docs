---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MitigationAction.html
---

# MitigationAction
<a name="API_MitigationAction"></a>

Describes which changes should be applied as part of a mitigation action.

## Contents
<a name="API_MitigationAction_Contents"></a>

 ** actionParams **   <a name="iot-Type-MitigationAction-actionParams"></a>
The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.
Type: [MitigationActionParams](API_MitigationActionParams.md) object
Required: No

 ** id **   <a name="iot-Type-MitigationAction-id"></a>
A unique identifier for the mitigation action.
Type: String
Required: No

 ** name **   <a name="iot-Type-MitigationAction-name"></a>
A user-friendly name for the mitigation action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** roleArn **   <a name="iot-Type-MitigationAction-roleArn"></a>
The IAM role ARN used to apply this mitigation action.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_MitigationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MitigationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MitigationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MitigationAction)
