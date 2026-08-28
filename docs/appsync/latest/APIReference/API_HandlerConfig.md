---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_HandlerConfig.html
---

# HandlerConfig
<a name="API_HandlerConfig"></a>

The configuration for a handler.

## Contents
<a name="API_HandlerConfig_Contents"></a>

 ** behavior **   <a name="appsync-Type-HandlerConfig-behavior"></a>
The behavior for the handler.
Type: String
Valid Values: `CODE | DIRECT`
Required: Yes

 ** integration **   <a name="appsync-Type-HandlerConfig-integration"></a>
The integration data source configuration for the handler.
Type: [Integration](API_Integration.md) object
Required: Yes

## See Also
<a name="API_HandlerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/HandlerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/HandlerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/HandlerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
