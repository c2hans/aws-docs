---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CredentialPair.html
---

# CredentialPair
<a name="API_CredentialPair"></a>

The combination of user name and password that are used as credentials.

## Contents
<a name="API_CredentialPair_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Password **   <a name="QS-Type-CredentialPair-Password"></a>
Password.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Username **   <a name="QS-Type-CredentialPair-Username"></a>
User name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** AlternateDataSourceParameters **   <a name="QS-Type-CredentialPair-AlternateDataSourceParameters"></a>
A set of alternate data source parameters that you want to share for these credentials. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the `DataSourceParameters` structure that's in the request with the structures in the `AlternateDataSourceParameters` allow list. If the structures are an exact match, the request is allowed to use the new data source with the existing credentials. If the `AlternateDataSourceParameters` list is null, the `DataSourceParameters` originally used with these `Credentials` is automatically allowed.
Type: Array of [DataSourceParameters](API_DataSourceParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_CredentialPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CredentialPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CredentialPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CredentialPair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
