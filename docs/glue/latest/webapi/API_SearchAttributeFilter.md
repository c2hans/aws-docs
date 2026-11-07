---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchAttributeFilter.html
---

# SearchAttributeFilter
<a name="API_SearchAttributeFilter"></a>

A filter that compares an attribute value using an operator.

## Contents
<a name="API_SearchAttributeFilter_Contents"></a>

 ** Attribute **   <a name="Glue-Type-SearchAttributeFilter-Attribute"></a>
The attribute name to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Operator **   <a name="Glue-Type-SearchAttributeFilter-Operator"></a>
The comparison operator. Valid values are `equals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, and `notExists`.
Type: String
Valid Values: `equals | greaterThan | greaterThanOrEquals | lessThan | lessThanOrEquals | notExists`
Required: Yes

 ** Value **   <a name="Glue-Type-SearchAttributeFilter-Value"></a>
The value to compare against.
Type: [SearchFilterValue](API_SearchFilterValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_SearchAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchAttributeFilter)
