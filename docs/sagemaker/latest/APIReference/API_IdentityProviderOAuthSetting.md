---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IdentityProviderOAuthSetting.html
---

# IdentityProviderOAuthSetting
<a name="API_IdentityProviderOAuthSetting"></a>

The Amazon SageMaker Canvas application setting where you configure OAuth for connecting to an external data source, such as Snowflake.

## Contents
<a name="API_IdentityProviderOAuthSetting_Contents"></a>

 ** DataSourceName **   <a name="sagemaker-Type-IdentityProviderOAuthSetting-DataSourceName"></a>
The name of the data source that you're connecting to. Canvas currently supports OAuth for Snowflake and Salesforce Data Cloud.
Type: String
Valid Values: `SalesforceGenie | Snowflake`
Required: No

 ** SecretArn **   <a name="sagemaker-Type-IdentityProviderOAuthSetting-SecretArn"></a>
The ARN of an AWS Secrets Manager secret that stores the credentials from your identity provider, such as the client ID and secret, authorization URL, and token URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:secretsmanager:[a-z0-9\-]*:[0-9]{12}:secret:.*`
Required: No

 ** Status **   <a name="sagemaker-Type-IdentityProviderOAuthSetting-Status"></a>
Describes whether OAuth for a data source is enabled or disabled in the Canvas application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_IdentityProviderOAuthSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IdentityProviderOAuthSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IdentityProviderOAuthSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IdentityProviderOAuthSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
