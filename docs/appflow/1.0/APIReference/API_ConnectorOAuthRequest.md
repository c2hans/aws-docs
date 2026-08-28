---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorOAuthRequest.html
---

# ConnectorOAuthRequest
<a name="API_ConnectorOAuthRequest"></a>

 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

## Contents
<a name="API_ConnectorOAuthRequest_Contents"></a>

 ** authCode **   <a name="appflow-Type-ConnectorOAuthRequest-authCode"></a>
 The code provided by the connector when it has been authenticated via the connected app.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`
Required: No

 ** redirectUri **   <a name="appflow-Type-ConnectorOAuthRequest-redirectUri"></a>
 The URL to which the authentication server redirects the browser after authorization has been granted.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

## See Also
<a name="API_ConnectorOAuthRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorOAuthRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorOAuthRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorOAuthRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
