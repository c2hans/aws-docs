---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RedshiftServerlessAuthConfiguration.html
---

# RedshiftServerlessAuthConfiguration
<a name="API_agent_RedshiftServerlessAuthConfiguration"></a>

Specifies configurations for authentication to a Redshift Serverless. Specify the type of authentication to use in the `type` field and include the corresponding field. If you specify IAM authentication, you don't need to include another field.

## Contents
<a name="API_agent_RedshiftServerlessAuthConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_RedshiftServerlessAuthConfiguration-type"></a>
The type of authentication to use.
Type: String
Valid Values: `IAM | USERNAME_PASSWORD`
Required: Yes

 ** usernamePasswordSecretArn **   <a name="bedrock-Type-agent_RedshiftServerlessAuthConfiguration-usernamePasswordSecretArn"></a>
The ARN of an Secrets Manager secret for authentication.
Type: String
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`
Required: No

## See Also
<a name="API_agent_RedshiftServerlessAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftServerlessAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftServerlessAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftServerlessAuthConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
