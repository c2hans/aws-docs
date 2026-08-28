---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobDataSourceCredentials.html
---

# AssetBundleImportJobDataSourceCredentials
<a name="API_AssetBundleImportJobDataSourceCredentials"></a>

The login credentials to use to import a data source resource.

## Contents
<a name="API_AssetBundleImportJobDataSourceCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CredentialPair **   <a name="QS-Type-AssetBundleImportJobDataSourceCredentials-CredentialPair"></a>
A username and password credential pair to be used to create the imported data source. Keep this field blank if you are using a Secrets Manager secret to provide credentials.
Type: [AssetBundleImportJobDataSourceCredentialPair](API_AssetBundleImportJobDataSourceCredentialPair.md) object
Required: No

 ** SecretArn **   <a name="QS-Type-AssetBundleImportJobDataSourceCredentials-SecretArn"></a>
The ARN of the Secrets Manager secret that's used to create the imported data source. Keep this field blank, unless you are using a secret in place of a credential pair.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:[-a-z0-9]*:secretsmanager:[-a-z0-9]*:[0-9]{12}:secret:.+`
Required: No

## See Also
<a name="API_AssetBundleImportJobDataSourceCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobDataSourceCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobDataSourceCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobDataSourceCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
