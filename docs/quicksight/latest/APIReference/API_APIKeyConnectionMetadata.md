---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_APIKeyConnectionMetadata.html
---

# APIKeyConnectionMetadata
<a name="API_APIKeyConnectionMetadata"></a>

Configuration for API key-based authentication to external services.

## Contents
<a name="API_APIKeyConnectionMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApiKey **   <a name="QS-Type-APIKeyConnectionMetadata-ApiKey"></a>
The API key used for authentication.
Type: String
Required: Yes

 ** BaseEndpoint **   <a name="QS-Type-APIKeyConnectionMetadata-BaseEndpoint"></a>
The base URL endpoint for the external service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** Email **   <a name="QS-Type-APIKeyConnectionMetadata-Email"></a>
The email address associated with the API key, if required.
Type: String
Pattern: `[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`
Required: No

## See Also
<a name="API_APIKeyConnectionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/APIKeyConnectionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/APIKeyConnectionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/APIKeyConnectionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
