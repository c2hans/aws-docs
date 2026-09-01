---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DateTimeFilterExpression.html
---

# DateTimeFilterExpression
<a name="API_DateTimeFilterExpression"></a>

The timestamp in date-time format.

## Contents
<a name="API_DateTimeFilterExpression_Contents"></a>

 ** dateTime **   <a name="deadlinecloud-Type-DateTimeFilterExpression-dateTime"></a>
The date and time.
Type: Timestamp
Required: Yes

 ** name **   <a name="deadlinecloud-Type-DateTimeFilterExpression-name"></a>
The name of the date-time field to filter on.
Type: String
Required: Yes

 ** operator **   <a name="deadlinecloud-Type-DateTimeFilterExpression-operator"></a>
The type of comparison to use to filter the results.
Type: String
Valid Values: `EQUAL | NOT_EQUAL | GREATER_THAN_EQUAL_TO | GREATER_THAN | LESS_THAN_EQUAL_TO | LESS_THAN | ANY_EQUALS | ALL_NOT_EQUALS`
Required: Yes

## See Also
<a name="API_DateTimeFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/DateTimeFilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/DateTimeFilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/DateTimeFilterExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
