---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Credentials.html
---

# Credentials
<a name="API_Credentials"></a>

The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.

## Contents
<a name="API_Credentials_Contents"></a>

 ** AccessKeyId **   <a name="systemsmanager-Type-Credentials-AccessKeyId"></a>
The access key ID that identifies the temporary security credentials.
Type: String
Pattern: `\w{16,128}`
Required: Yes

 ** ExpirationTime **   <a name="systemsmanager-Type-Credentials-ExpirationTime"></a>
The datetime on which the current credentials expire.
Type: Timestamp
Required: Yes

 ** SecretAccessKey **   <a name="systemsmanager-Type-Credentials-SecretAccessKey"></a>
The secret access key that can be used to sign requests.
Type: String
Required: Yes

 ** SessionToken **   <a name="systemsmanager-Type-Credentials-SessionToken"></a>
The token that users must pass to the service API to use the temporary credentials.
Type: String
Required: Yes

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Credentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
