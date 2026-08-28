---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RestConfiguration.html
---

# RestConfiguration
<a name="API_RestConfiguration"></a>

Configuration that defines HTTP request and response handling, validation endpoints, and entity configurations for REST API interactions.

## Contents
<a name="API_RestConfiguration_Contents"></a>

 ** EntityConfigurations **   <a name="Glue-Type-RestConfiguration-EntityConfigurations"></a>
A map of entity configurations that define how to interact with different data entities available through the REST API, including their schemas and access patterns.
Type: String to [EntityConfiguration](API_EntityConfiguration.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_ -]+`
Required: No

 ** GlobalSourceConfiguration **   <a name="Glue-Type-RestConfiguration-GlobalSourceConfiguration"></a>
Global configuration settings that apply to all REST API requests for this connection type, including common request methods, paths, and parameters.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: No

 ** ValidationEndpointConfiguration **   <a name="Glue-Type-RestConfiguration-ValidationEndpointConfiguration"></a>
Configuration for the endpoint used to validate connection credentials and test connectivity during connection creation.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: No

## See Also
<a name="API_RestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
