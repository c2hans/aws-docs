---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_Credentials.html
---

# Credentials
<a name="API_Credentials"></a>

 AWS credentials for API authentication.

## Contents
<a name="API_Credentials_Contents"></a>

 ** AccessKeyId **
The access key ID that identifies the temporary security credentials.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]*`
Required: Yes

 ** Expiration **
The date on which the current credentials expire.
Type: Timestamp
Required: Yes

 ** SecretAccessKey **
The secret access key that can be used to sign requests.
Type: String
Required: Yes

 ** SessionToken **
The token that users must pass to the service API to use the temporary credentials.
Type: String
Required: Yes

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/Credentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Token Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query STS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
