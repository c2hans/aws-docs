---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DateTimeCondition.html
---

# DateTimeCondition
<a name="API_DateTimeCondition"></a>

A datetime search condition for Search APIs.

## Contents
<a name="API_DateTimeCondition_Contents"></a>

 ** ComparisonType **   <a name="connect-Type-DateTimeCondition-ComparisonType"></a>
Datetime property comparison type.
Type: String
Valid Values: `GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL_TO | LESS_THAN_OR_EQUAL_TO | EQUAL_TO | RANGE`
Required: No

 ** FieldName **   <a name="connect-Type-DateTimeCondition-FieldName"></a>
A name of the datetime property to be searched
Type: String
Required: No

 ** MaxValue **   <a name="connect-Type-DateTimeCondition-MaxValue"></a>
A maximum value of the property.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z?$`
Required: No

 ** MinValue **   <a name="connect-Type-DateTimeCondition-MinValue"></a>
A minimum value of the property.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z?$`
Required: No

## See Also
<a name="API_DateTimeCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DateTimeCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DateTimeCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DateTimeCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
