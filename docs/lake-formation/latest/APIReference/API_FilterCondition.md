---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_FilterCondition.html
---

# FilterCondition
<a name="API_FilterCondition"></a>

This structure describes the filtering of columns in a table based on a filter condition.

## Contents
<a name="API_FilterCondition_Contents"></a>

 ** ComparisonOperator **   <a name="lakeformation-Type-FilterCondition-ComparisonOperator"></a>
The comparison operator used in the filter condition.
Type: String
Valid Values: `EQ | NE | LE | LT | GE | GT | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN`
Required: No

 ** Field **   <a name="lakeformation-Type-FilterCondition-Field"></a>
The field to filter in the filter condition.
Type: String
Valid Values: `RESOURCE_ARN | ROLE_ARN | LAST_MODIFIED`
Required: No

 ** StringValueList **   <a name="lakeformation-Type-FilterCondition-StringValueList"></a>
A string with values used in evaluating the filter condition.
Type: Array of strings
Required: No

## See Also
<a name="API_FilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/FilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/FilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/FilterCondition)
