---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_HoneycodeConnectorProfileCredentials.html
---

# HoneycodeConnectorProfileCredentials
<a name="API_HoneycodeConnectorProfileCredentials"></a>

 The connector-specific credentials required when using Amazon Honeycode.

## Contents
<a name="API_HoneycodeConnectorProfileCredentials_Contents"></a>

 ** accessToken **   <a name="appflow-Type-HoneycodeConnectorProfileCredentials-accessToken"></a>
 The credentials used to access protected Amazon Honeycode resources.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

 ** oAuthRequest **   <a name="appflow-Type-HoneycodeConnectorProfileCredentials-oAuthRequest"></a>
 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
Type: [ConnectorOAuthRequest](API_ConnectorOAuthRequest.md) object
Required: No

 ** refreshToken **   <a name="appflow-Type-HoneycodeConnectorProfileCredentials-refreshToken"></a>
 The credentials used to acquire new access tokens.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

## See Also
<a name="API_HoneycodeConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/HoneycodeConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/HoneycodeConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/HoneycodeConnectorProfileCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
