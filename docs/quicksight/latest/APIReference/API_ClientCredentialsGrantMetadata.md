---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ClientCredentialsGrantMetadata.html
---

# ClientCredentialsGrantMetadata
<a name="API_ClientCredentialsGrantMetadata"></a>

Configuration for OAuth 2.0 client credentials grant authentication, including client ID, client secret, token endpoint, and optional scopes.

## Contents
<a name="API_ClientCredentialsGrantMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-ClientCredentialsGrantMetadata-BaseEndpoint"></a>
The base endpoint URL for the external service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** ClientCredentialsDetails **   <a name="QS-Type-ClientCredentialsGrantMetadata-ClientCredentialsDetails"></a>
The detailed client credentials configuration including client ID, client secret, and token endpoint.
Type: [ClientCredentialsDetails](API_ClientCredentialsDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ClientCredentialsSource **   <a name="QS-Type-ClientCredentialsGrantMetadata-ClientCredentialsSource"></a>
The source of the client credentials configuration.
Type: String
Valid Values: `PLAIN_CREDENTIALS`
Required: No

## See Also
<a name="API_ClientCredentialsGrantMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ClientCredentialsGrantMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ClientCredentialsGrantMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ClientCredentialsGrantMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
