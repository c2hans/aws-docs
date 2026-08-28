---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_MarketoConnectorProfileCredentials.html
---

# MarketoConnectorProfileCredentials
<a name="API_MarketoConnectorProfileCredentials"></a>

 The connector-specific profile credentials required by Marketo.

## Contents
<a name="API_MarketoConnectorProfileCredentials_Contents"></a>

 ** clientId **   <a name="appflow-Type-MarketoConnectorProfileCredentials-clientId"></a>
 The identifier for the desired client.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** clientSecret **   <a name="appflow-Type-MarketoConnectorProfileCredentials-clientSecret"></a>
 The client secret used by the OAuth client to authenticate to the authorization server.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** accessToken **   <a name="appflow-Type-MarketoConnectorProfileCredentials-accessToken"></a>
 The credentials used to access protected Marketo resources.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

 ** oAuthRequest **   <a name="appflow-Type-MarketoConnectorProfileCredentials-oAuthRequest"></a>
 The OAuth requirement needed to request security tokens from the connector endpoint.
Type: [ConnectorOAuthRequest](API_ConnectorOAuthRequest.md) object
Required: No

## See Also
<a name="API_MarketoConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/MarketoConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/MarketoConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/MarketoConnectorProfileCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
