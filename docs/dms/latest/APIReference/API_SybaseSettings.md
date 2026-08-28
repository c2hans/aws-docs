---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_SybaseSettings.html
---

# SybaseSettings
<a name="API_SybaseSettings"></a>

Provides information that defines a SAP ASE endpoint.

## Contents
<a name="API_SybaseSettings_Contents"></a>

 ** DatabaseName **   <a name="DMS-Type-SybaseSettings-DatabaseName"></a>
Database name for the endpoint.
Type: String
Required: No

 ** Password **   <a name="DMS-Type-SybaseSettings-Password"></a>
Endpoint connection password.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-SybaseSettings-Port"></a>
Endpoint TCP port. The default is 5000.
Type: Integer
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-SybaseSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the SAP ASE endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-SybaseSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the SAP SAE endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-SybaseSettings-ServerName"></a>
Fully qualified domain name of the endpoint.
Type: String
Required: No

 ** Username **   <a name="DMS-Type-SybaseSettings-Username"></a>
Endpoint connection user name.
Type: String
Required: No

## See Also
<a name="API_SybaseSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/SybaseSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/SybaseSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/SybaseSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
