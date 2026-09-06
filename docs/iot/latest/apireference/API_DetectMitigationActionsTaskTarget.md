---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionsTaskTarget.html
---

# DetectMitigationActionsTaskTarget
<a name="API_DetectMitigationActionsTaskTarget"></a>

 The target of a mitigation action task.

## Contents
<a name="API_DetectMitigationActionsTaskTarget_Contents"></a>

 ** behaviorName **   <a name="iot-Type-DetectMitigationActionsTaskTarget-behaviorName"></a>
 The name of the behavior.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** securityProfileName **   <a name="iot-Type-DetectMitigationActionsTaskTarget-securityProfileName"></a>
 The name of the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** violationIds **   <a name="iot-Type-DetectMitigationActionsTaskTarget-violationIds"></a>
 The unique identifiers of the violations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

## See Also
<a name="API_DetectMitigationActionsTaskTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetectMitigationActionsTaskTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetectMitigationActionsTaskTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetectMitigationActionsTaskTarget)
