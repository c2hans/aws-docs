---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionBodyParameter.html
---

# ConnectionBodyParameter
<a name="API_ConnectionBodyParameter"></a>

Additional parameter included in the body. You can include up to 100 additional body parameters per request. An event payload cannot exceed 64 KB.

## Contents
<a name="API_ConnectionBodyParameter_Contents"></a>

 ** IsValueSecret **   <a name="eventbridge-Type-ConnectionBodyParameter-IsValueSecret"></a>
Specifies whether the value is secret.
Type: Boolean
Required: No

 ** Key **   <a name="eventbridge-Type-ConnectionBodyParameter-Key"></a>
The key for the parameter.
Type: String
Required: No

 ** Value **   <a name="eventbridge-Type-ConnectionBodyParameter-Value"></a>
The value associated with the key.
Type: String
Required: No

## See Also
<a name="API_ConnectionBodyParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionBodyParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionBodyParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionBodyParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
