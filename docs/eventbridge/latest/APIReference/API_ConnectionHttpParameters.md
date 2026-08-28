---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionHttpParameters.html
---

# ConnectionHttpParameters
<a name="API_ConnectionHttpParameters"></a>

Any additional parameters for the connection.

## Contents
<a name="API_ConnectionHttpParameters_Contents"></a>

 ** BodyParameters **   <a name="eventbridge-Type-ConnectionHttpParameters-BodyParameters"></a>
Any additional body string parameters for the connection.
Type: Array of [ConnectionBodyParameter](API_ConnectionBodyParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** HeaderParameters **   <a name="eventbridge-Type-ConnectionHttpParameters-HeaderParameters"></a>
Any additional header parameters for the connection.
Type: Array of [ConnectionHeaderParameter](API_ConnectionHeaderParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** QueryStringParameters **   <a name="eventbridge-Type-ConnectionHttpParameters-QueryStringParameters"></a>
Any additional query string parameters for the connection.
Type: Array of [ConnectionQueryStringParameter](API_ConnectionQueryStringParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_ConnectionHttpParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionHttpParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionHttpParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionHttpParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
