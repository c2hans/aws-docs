---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StarburstParameters.html
---

# StarburstParameters
<a name="API_StarburstParameters"></a>

The parameters that are required to connect to a Starburst data source.

## Contents
<a name="API_StarburstParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Catalog **   <a name="QS-Type-StarburstParameters-Catalog"></a>
The catalog name for the Starburst data source.
Type: String
Length Constraints: Maximum length of 128.
Required: Yes

 ** Host **   <a name="QS-Type-StarburstParameters-Host"></a>
The host name of the Starburst data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Port **   <a name="QS-Type-StarburstParameters-Port"></a>
The port for the Starburst data source.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** AuthenticationType **   <a name="QS-Type-StarburstParameters-AuthenticationType"></a>
The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.
Type: String
Valid Values: `PASSWORD | KEYPAIR | TOKEN | X509`
Required: No

 ** DatabaseAccessControlRole **   <a name="QS-Type-StarburstParameters-DatabaseAccessControlRole"></a>
The database access control role.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** OAuthParameters **   <a name="QS-Type-StarburstParameters-OAuthParameters"></a>
An object that contains information needed to create a data source connection between an Quick Sight account and Starburst.
Type: [OAuthParameters](API_OAuthParameters.md) object
Required: No

 ** ProductType **   <a name="QS-Type-StarburstParameters-ProductType"></a>
The product type for the Starburst data source.
Type: String
Valid Values: `GALAXY | ENTERPRISE`
Required: No

## See Also
<a name="API_StarburstParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StarburstParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StarburstParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StarburstParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
