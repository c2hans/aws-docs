---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedInputItem.html
---

# BatchIsAuthorizedInputItem
<a name="API_BatchIsAuthorizedInputItem"></a>

An authorization request that you include in a `BatchIsAuthorized` API request.

## Contents
<a name="API_BatchIsAuthorizedInputItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** action **   <a name="verifiedpermissions-Type-BatchIsAuthorizedInputItem-action"></a>
Specifies the requested action to be authorized. For example, `PhotoFlash::ReadPhoto`.
Type: [ActionIdentifier](API_ActionIdentifier.md) object
Required: No

 ** context **   <a name="verifiedpermissions-Type-BatchIsAuthorizedInputItem-context"></a>
Specifies additional context that can be used to make more granular authorization decisions.
Type: [ContextDefinition](API_ContextDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** principal **   <a name="verifiedpermissions-Type-BatchIsAuthorizedInputItem-principal"></a>
Specifies the principal for which the authorization decision is to be made.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** resource **   <a name="verifiedpermissions-Type-BatchIsAuthorizedInputItem-resource"></a>
Specifies the resource that you want an authorization decision for. For example, `PhotoFlash::Photo`.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

## See Also
<a name="API_BatchIsAuthorizedInputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchIsAuthorizedInputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchIsAuthorizedInputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchIsAuthorizedInputItem)
