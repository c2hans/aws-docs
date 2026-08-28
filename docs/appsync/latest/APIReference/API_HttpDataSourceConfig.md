---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_HttpDataSourceConfig.html
---

# HttpDataSourceConfig
<a name="API_HttpDataSourceConfig"></a>

Describes an HTTP data source configuration.

## Contents
<a name="API_HttpDataSourceConfig_Contents"></a>

 ** authorizationConfig **   <a name="appsync-Type-HttpDataSourceConfig-authorizationConfig"></a>
The authorization configuration in case the HTTP endpoint requires authorization.
Type: [AuthorizationConfig](API_AuthorizationConfig.md) object
Required: No

 ** endpoint **   <a name="appsync-Type-HttpDataSourceConfig-endpoint"></a>
The HTTP URL endpoint. You can specify either the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If you don't specify the port, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
Type: String
Required: No

## See Also
<a name="API_HttpDataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/HttpDataSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/HttpDataSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/HttpDataSourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
