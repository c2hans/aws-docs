---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_S3Action.html
---

# S3Action
<a name="API_S3Action"></a>

Writes the MIME content of the email to an S3 bucket.

## Contents
<a name="API_S3Action_Contents"></a>

 ** RoleArn **   <a name="sesmailmanager-Type-S3Action-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM Role to use while writing to S3. This role must have access to the s3:PutObject, kms:Encrypt, and kms:GenerateDataKey APIs for the given bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** S3Bucket **   <a name="sesmailmanager-Type-S3Action-S3Bucket"></a>
The bucket name of the S3 bucket to write to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 62.
Pattern: `[a-zA-Z0-9.-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-S3Action-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified the bucket has been deleted.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

 ** S3Prefix **   <a name="sesmailmanager-Type-S3Action-S3Prefix"></a>
The S3 prefix to use for the write to the s3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 62.
Pattern: `[a-zA-Z0-9!_.*'()/-]+`
Required: No

 ** S3SseKmsKeyId **   <a name="sesmailmanager-Type-S3Action-S3SseKmsKeyId"></a>
The KMS Key ID to use to encrypt the message in S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9-:/]+`
Required: No

## See Also
<a name="API_S3Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/S3Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/S3Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/S3Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
