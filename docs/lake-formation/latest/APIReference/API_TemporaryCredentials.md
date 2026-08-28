---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TemporaryCredentials.html
---

# TemporaryCredentials
<a name="API_TemporaryCredentials"></a>

A temporary set of credentials for an AWS Lake Formation user. These credentials are scoped down to only access the raw data sources that the user has access to.

The temporary security credentials consist of an access key and a session token. The access key consists of an access key ID and a secret key. When the credentials are created, they are associated with an IAM access control policy that limits what the user can do when using the credentials.

## Contents
<a name="API_TemporaryCredentials_Contents"></a>

 ** AccessKeyId **   <a name="lakeformation-Type-TemporaryCredentials-AccessKeyId"></a>
The access key ID for the temporary credentials.
Type: String
Required: No

 ** Expiration **   <a name="lakeformation-Type-TemporaryCredentials-Expiration"></a>
The date and time when the temporary credentials expire.
Type: Timestamp
Required: No

 ** SecretAccessKey **   <a name="lakeformation-Type-TemporaryCredentials-SecretAccessKey"></a>
The secret key for the temporary credentials.
Type: String
Required: No

 ** SessionToken **   <a name="lakeformation-Type-TemporaryCredentials-SessionToken"></a>
The session token for the temporary credentials.
Type: String
Required: No

## See Also
<a name="API_TemporaryCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TemporaryCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TemporaryCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TemporaryCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
