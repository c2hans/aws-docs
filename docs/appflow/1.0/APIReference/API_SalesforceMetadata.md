---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SalesforceMetadata.html
---

# SalesforceMetadata
<a name="API_SalesforceMetadata"></a>

 The connector metadata specific to Salesforce.

## Contents
<a name="API_SalesforceMetadata_Contents"></a>

 ** dataTransferApis **   <a name="appflow-Type-SalesforceMetadata-dataTransferApis"></a>
The Salesforce APIs that you can have Amazon AppFlow use when your flows transfers data to or from Salesforce.
Type: Array of strings
Valid Values: `AUTOMATIC | BULKV2 | REST_SYNC`
Required: No

 ** oauth2GrantTypesSupported **   <a name="appflow-Type-SalesforceMetadata-oauth2GrantTypesSupported"></a>
The OAuth 2.0 grant types that Amazon AppFlow can use when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.
AUTHORIZATION\_CODE
Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.
JWT\_BEARER
Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.
The CLIENT\_CREDENTIALS value is not supported for Salesforce.
Type: Array of strings
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | JWT_BEARER`
Required: No

 ** oAuthScopes **   <a name="appflow-Type-SalesforceMetadata-oAuthScopes"></a>
 The desired authorization scope for the Salesforce account.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

## See Also
<a name="API_SalesforceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SalesforceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SalesforceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SalesforceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
