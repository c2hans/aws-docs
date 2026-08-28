---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Authentication.html
---

# Authentication
<a name="API_Authentication"></a>

Indicates whether the user requires a password to authenticate.

## Contents
<a name="API_Authentication_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PasswordCount **
The number of passwords belonging to the user. The maximum is two.
Type: Integer
Required: No

 ** Type **
Indicates whether the user requires a password to authenticate.
Type: String
Valid Values: `password | no-password | iam`
Required: No

## See Also
<a name="API_Authentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Authentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Authentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Authentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
