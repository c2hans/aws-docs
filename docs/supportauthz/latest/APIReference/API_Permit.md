---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_Permit.html
---

# Permit
<a name="API_Permit"></a>

The permit definition specifying the authorized actions, resources, and time-window conditions for a support operator.

## Contents
<a name="API_Permit_Contents"></a>

 ** actions **   <a name="supportauthorization-Type-Permit-actions"></a>
The set of actions that the support operator is authorized to perform.
Type: [ActionSet](API_ActionSet.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** resources **   <a name="supportauthorization-Type-Permit-resources"></a>
The set of resources that the support operator is authorized to act upon.
Type: [ResourceSet](API_ResourceSet.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** conditions **   <a name="supportauthorization-Type-Permit-conditions"></a>
The time-window conditions that constrain when the permit is valid. Maximum of 2 conditions.
Type: Array of [Condition](API_Condition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## See Also
<a name="API_Permit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/Permit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/Permit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/Permit)
