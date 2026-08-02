---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyFilter.html
---

# PolicyFilter
<a name="API_PolicyFilter"></a>

Contains information about a filter to refine policies returned in a query.

This data type is used as a response parameter for the [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) operation.

## Contents
<a name="API_PolicyFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** policyTemplateId **   <a name="verifiedpermissions-Type-PolicyFilter-policyTemplateId"></a>
Filters the output to only template-linked policies that were instantiated from the specified policy template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: No

 ** policyType **   <a name="verifiedpermissions-Type-PolicyFilter-policyType"></a>
Filters the output to only policies of the specified type.
Type: String
Valid Values: `STATIC | TEMPLATE_LINKED`
Required: No

 ** principal **   <a name="verifiedpermissions-Type-PolicyFilter-principal"></a>
Filters the output to only policies that reference the specified principal.
Type: [EntityReference](API_EntityReference.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** resource **   <a name="verifiedpermissions-Type-PolicyFilter-resource"></a>
Filters the output to only policies that reference the specified resource.
Type: [EntityReference](API_EntityReference.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PolicyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyFilter)
