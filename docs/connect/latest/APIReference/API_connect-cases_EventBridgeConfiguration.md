---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_EventBridgeConfiguration.html
---

# EventBridgeConfiguration
<a name="API_connect-cases_EventBridgeConfiguration"></a>

Configuration to enable EventBridge case event delivery and determine what data is delivered.

## Contents
<a name="API_connect-cases_EventBridgeConfiguration_Contents"></a>

 ** enabled **   <a name="connect-Type-connect-cases_EventBridgeConfiguration-enabled"></a>
Indicates whether the to broadcast case event data to the customer.
Type: Boolean
Required: Yes

 ** includedData **   <a name="connect-Type-connect-cases_EventBridgeConfiguration-includedData"></a>
Details of what case and related item data is published through the case event stream.
Type: [EventIncludedData](API_connect-cases_EventIncludedData.md) object
Required: No

## See Also
<a name="API_connect-cases_EventBridgeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/EventBridgeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/EventBridgeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/EventBridgeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
