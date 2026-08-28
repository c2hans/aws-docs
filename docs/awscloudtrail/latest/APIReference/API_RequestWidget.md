---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RequestWidget.html
---

# RequestWidget
<a name="API_RequestWidget"></a>

 Contains information about a widget on a CloudTrail Lake dashboard.

## Contents
<a name="API_RequestWidget_Contents"></a>

 ** QueryStatement **   <a name="awscloudtrail-Type-RequestWidget-QueryStatement"></a>
 The query statement for the widget. For custom dashboard widgets, you can query across multiple event data stores as long as all event data stores exist in your account.
When a query uses `?` with `eventTime`, `?` must be surrounded by single quotes as follows: `'?'`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `(?s).*`
Required: Yes

 ** ViewProperties **   <a name="awscloudtrail-Type-RequestWidget-ViewProperties"></a>
 The view properties for the widget. For more information about view properties, see [ View properties for widgets ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html) in the * AWS CloudTrail User Guide*.
Type: String to string map
Key Length Constraints: Minimum length of 3. Maximum length of 128.
Key Pattern: `^[a-zA-Z0-9._\-]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 128.
Value Pattern: `^[a-zA-Z0-9._\- ]+$`
Required: Yes

 ** QueryParameters **   <a name="awscloudtrail-Type-RequestWidget-QueryParameters"></a>
 The optional query parameters. The following query parameters are valid: `$StartTime$`, `$EndTime$`, and `$Period$`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_RequestWidget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/RequestWidget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/RequestWidget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/RequestWidget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
