---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnectionApiKeyAuthRequestParameters.html
---

# CreateConnectionApiKeyAuthRequestParameters
<a name="API_CreateConnectionApiKeyAuthRequestParameters"></a>

The API key authorization parameters for the connection.

## Contents
<a name="API_CreateConnectionApiKeyAuthRequestParameters_Contents"></a>

 ** ApiKeyName **   <a name="eventbridge-Type-CreateConnectionApiKeyAuthRequestParameters-ApiKeyName"></a>
The name of the API key to use for authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[ \t]*[^\x00-\x1F:\x7F]+([ \t]+[^\x00-\x1F:\x7F]+)*[ \t]*$`
Required: Yes

 ** ApiKeyValue **   <a name="eventbridge-Type-CreateConnectionApiKeyAuthRequestParameters-ApiKeyValue"></a>
The value for the API key to use for authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[ \t]*[^\x00-\x1F:\x7F]+([ \t]+[^\x00-\x1F:\x7F]+)*[ \t]*$`
Required: Yes

## See Also
<a name="API_CreateConnectionApiKeyAuthRequestParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateConnectionApiKeyAuthRequestParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateConnectionApiKeyAuthRequestParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateConnectionApiKeyAuthRequestParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
