---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_AuthenticationMode.html
---

# AuthenticationMode
<a name="API_AuthenticationMode"></a>

Specifies the authentication mode to use.

## Contents
<a name="API_AuthenticationMode_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Passwords.member.N **
Specifies the passwords to use for authentication if `Type` is set to `password`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** Type **
Specifies the authentication type. Possible options are IAM authentication, password and no password.
Type: String
Valid Values: `password | no-password-required | iam`
Required: No

## See Also
<a name="API_AuthenticationMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/AuthenticationMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/AuthenticationMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/AuthenticationMode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
