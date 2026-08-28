---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_JwtKey.html
---

# JwtKey
<a name="API_JwtKey"></a>

The JWT key stored in AWS Secrets Manager for Slurm REST API authentication.

## Contents
<a name="API_JwtKey_Contents"></a>

 ** secretArn **   <a name="PCS-Type-JwtKey-secretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the JWT key.
Type: String
Required: Yes

 ** secretVersion **   <a name="PCS-Type-JwtKey-secretVersion"></a>
The version of the AWS Secrets Manager secret containing the JWT key.
Type: String
Required: Yes

## See Also
<a name="API_JwtKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/JwtKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/JwtKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/JwtKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
