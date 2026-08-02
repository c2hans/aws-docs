---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfileSearchCriteria.html
---

# RoutingProfileSearchCriteria
<a name="API_RoutingProfileSearchCriteria"></a>

The search criteria to be used to return routing profiles.

**Note**
The `name` and `description` fields support "contains" queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.

## Contents
<a name="API_RoutingProfileSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-RoutingProfileSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an AND condition.
Type: Array of [RoutingProfileSearchCriteria](#API_RoutingProfileSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-RoutingProfileSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an OR condition.
Type: Array of [RoutingProfileSearchCriteria](#API_RoutingProfileSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-RoutingProfileSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
The currently supported values for `FieldName` are `associatedQueueIds`, `name`, `description`, and `resourceID`.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_RoutingProfileSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfileSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfileSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfileSearchCriteria)
