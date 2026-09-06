---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TargetIdentifier.html
---

# TargetIdentifier
<a name="API_TargetIdentifier"></a>

A target identifier is a pair of identifying information for a scope that is included in a target. A target identifier is made up of a target ID and a target type. Currently the target ID is always an account ID and the target type is always ACCOUNT.

## Contents
<a name="API_TargetIdentifier_Contents"></a>

 ** targetId **   <a name="networkflowmonitor-Type-TargetIdentifier-targetId"></a>
The identifier for a target, which is currently always an account ID .
Type: [TargetId](API_TargetId.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** targetType **   <a name="networkflowmonitor-Type-TargetIdentifier-targetType"></a>
The type of a target. A target type is currently always `ACCOUNT`.
Type: String
Valid Values: `ACCOUNT`
Required: Yes

## See Also
<a name="API_TargetIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/TargetIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/TargetIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/TargetIdentifier)
