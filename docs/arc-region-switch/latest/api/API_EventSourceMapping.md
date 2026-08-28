---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EventSourceMapping.html
---

# EventSourceMapping
<a name="API_EventSourceMapping"></a>

The AWS Lambda event source mapping configuration, containing the resource ARN and optional cross-account configuration.

## Contents
<a name="API_EventSourceMapping_Contents"></a>

 ** arn **   <a name="regionswitch-Type-EventSourceMapping-arn"></a>
The Amazon Resource Name (ARN) of the Lambda event source mapping.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z0-9-]+:\d{12}:event-source-mapping:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-EventSourceMapping-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-EventSourceMapping-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

## See Also
<a name="API_EventSourceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/EventSourceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/EventSourceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/EventSourceMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
