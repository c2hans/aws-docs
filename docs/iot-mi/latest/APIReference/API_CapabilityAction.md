---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CapabilityAction.html
---

# CapabilityAction
<a name="API_CapabilityAction"></a>

Action for an AWS capability, containing the action parameters for control.

## Contents
<a name="API_CapabilityAction_Contents"></a>

 ** name **   <a name="managedintegrations-Type-CapabilityAction-name"></a>
Describe a capability action with a name.
Type: String
Pattern: `[/a-zA-Z]+`
Required: Yes

 ** actionTraceId **   <a name="managedintegrations-Type-CapabilityAction-actionTraceId"></a>
Describe a capability action with an `actionTraceId` for a response command.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 20.
Pattern: `[a-zA-Z0-9]+=(?:_[0-9]+)?`
Required: No

 ** parameters **   <a name="managedintegrations-Type-CapabilityAction-parameters"></a>
Describe a capability action with a capability property.
Type: JSON value
Required: No

 ** ref **   <a name="managedintegrations-Type-CapabilityAction-ref"></a>
Describe a capability action with an reference.
Type: String
Pattern: `[a-zA-Z.]+`
Required: No

## See Also
<a name="API_CapabilityAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CapabilityAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CapabilityAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CapabilityAction)
