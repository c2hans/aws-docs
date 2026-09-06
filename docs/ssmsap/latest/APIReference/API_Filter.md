---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A specific result obtained by specifying the name, value, and operator.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="ssmsap-Type-Filter-Name"></a>
The name of the filter. Filter names are case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** Operator **   <a name="ssmsap-Type-Filter-Operator"></a>
The operator for the filter.
Type: String
Valid Values: `Equals | GreaterThanOrEquals | LessThanOrEquals`
Required: Yes

 ** Value **   <a name="ssmsap-Type-Filter-Value"></a>
The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an OR, and the request returns all results that match any of the specified values
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Filter)
