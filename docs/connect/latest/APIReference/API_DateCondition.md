---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DateCondition.html
---

# DateCondition
<a name="API_DateCondition"></a>

An object to specify the hours of operation override date condition.

## Contents
<a name="API_DateCondition_Contents"></a>

 ** ComparisonType **   <a name="connect-Type-DateCondition-ComparisonType"></a>
An object to specify the hours of operation override date condition `comparisonType`.
Type: String
Valid Values: `GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL_TO | LESS_THAN_OR_EQUAL_TO | EQUAL_TO`
Required: No

 ** FieldName **   <a name="connect-Type-DateCondition-FieldName"></a>
An object to specify the hours of operation override date field.
Type: String
Required: No

 ** Value **   <a name="connect-Type-DateCondition-Value"></a>
An object to specify the hours of operation override date value.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

## See Also
<a name="API_DateCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DateCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DateCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DateCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
