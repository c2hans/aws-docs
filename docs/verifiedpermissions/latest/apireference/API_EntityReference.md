---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityReference.html
---

# EntityReference
<a name="API_EntityReference"></a>

Contains information about a principal or resource that can be referenced in a Cedar policy.

This data type is used as part of the [PolicyFilter](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyFilter.html) structure that is used as a request parameter for the [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) operation..

## Contents
<a name="API_EntityReference_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** identifier **   <a name="verifiedpermissions-Type-EntityReference-identifier"></a>
The identifier of the entity. It can consist of either an EntityType and EntityId, a principal, or a resource.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** unspecified **   <a name="verifiedpermissions-Type-EntityReference-unspecified"></a>
Used to indicate that a principal or resource is not specified. This can be used to search for policies that are not associated with a specific principal or resource.
Type: Boolean
Required: No

## See Also
<a name="API_EntityReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/EntityReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/EntityReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/EntityReference)
