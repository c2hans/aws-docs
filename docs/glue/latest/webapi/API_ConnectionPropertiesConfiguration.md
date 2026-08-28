---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectionPropertiesConfiguration.html
---

# ConnectionPropertiesConfiguration
<a name="API_ConnectionPropertiesConfiguration"></a>

Configuration that defines the base URL and additional request parameters needed during connection creation.

## Contents
<a name="API_ConnectionPropertiesConfiguration_Contents"></a>

 ** AdditionalRequestParameters **   <a name="Glue-Type-ConnectionPropertiesConfiguration-AdditionalRequestParameters"></a>
Key-value pairs of additional request parameters that may be needed during connection creation, such as API versions or service-specific configuration options.
Type: Array of [ConnectorProperty](API_ConnectorProperty.md) objects
Required: No

 ** Url **   <a name="Glue-Type-ConnectionPropertiesConfiguration-Url"></a>
The base instance URL for the endpoint that this connection type will connect to.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

## See Also
<a name="API_ConnectionPropertiesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectionPropertiesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectionPropertiesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectionPropertiesConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
