---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_UserAuthConfig.html
---

# UserAuthConfig
<a name="API_UserAuthConfig"></a>

Specifies the details of authentication used by a proxy to log in as a specific database user.

## Contents
<a name="API_UserAuthConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthScheme **
The type of authentication that the proxy uses for connections from the proxy to the underlying database.
Type: String
Valid Values: `SECRETS`
Required: No

 ** ClientPasswordAuthType **
The type of authentication the proxy uses for connections from clients. The following values are defaults for the corresponding engines:
+ RDS for MySQL: `MYSQL_CACHING_SHA2_PASSWORD`
+ RDS for SQL Server: `SQL_SERVER_AUTHENTICATION`
+ RDS for PostgreSQL: `POSTGRES_SCRAM_SHA2_256`
Type: String
Valid Values: `MYSQL_NATIVE_PASSWORD | MYSQL_CACHING_SHA2_PASSWORD | POSTGRES_SCRAM_SHA_256 | POSTGRES_MD5 | SQL_SERVER_AUTHENTICATION`
Required: No

 ** Description **
A user-specified description about the authentication used by a proxy to log in as a specific database user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** IAMAuth **
A value that indicates whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. The `ENABLED` value is valid only for proxies with RDS for Microsoft SQL Server.
Type: String
Valid Values: `DISABLED | REQUIRED | ENABLED`
Required: No

 ** SecretArn **
The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** UserName **
The name of the database user to which the proxy connects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_UserAuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/UserAuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/UserAuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/UserAuthConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
