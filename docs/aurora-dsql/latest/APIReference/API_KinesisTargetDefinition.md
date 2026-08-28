---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_KinesisTargetDefinition.html
---

# KinesisTargetDefinition
<a name="API_KinesisTargetDefinition"></a>

Kinesis stream target configuration.

## Contents
<a name="API_KinesisTargetDefinition_Contents"></a>

 ** roleArn **   <a name="auroradsql-Type-KinesisTargetDefinition-roleArn"></a>
The ARN of the IAM role that grants permission to write to the Kinesis stream. This can be a standard role (`arn:aws:iam::account-id:role/role-name`) or a role with a path prefix (`arn:aws:iam::account-id:role/service-role/role-name`), such as roles auto-created by the console.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role(/[a-zA-Z0-9+=,.@_-]+)+`
Required: Yes

 ** streamArn **   <a name="auroradsql-Type-KinesisTargetDefinition-streamArn"></a>
The ARN of the Kinesis stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:kinesis:[a-z0-9-]*:[0-9]{12}:stream/[a-zA-Z0-9+=,.@_/\-]+`
Required: Yes

## See Also
<a name="API_KinesisTargetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/KinesisTargetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/KinesisTargetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/KinesisTargetDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
