---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociatedRole.html
---

# AssociatedRole
<a name="API_AssociatedRole"></a>

Information about the associated IAM roles.

## Contents
<a name="API_AssociatedRole_Contents"></a>

 ** associatedRoleArn **
The ARN of the associated IAM role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** certificateS3BucketName **
The name of the Amazon S3 bucket in which the Amazon S3 object is stored.
Type: String
Required: No

 ** certificateS3ObjectKey **
The key of the Amazon S3 object where the certificate, certificate chain, and encrypted private key bundle are stored. The object key is formatted as follows: `role_arn`/`certificate_arn`.
Type: String
Required: No

 ** encryptionKmsKeyId **
The ID of the KMS key used to encrypt the private key.
Type: String
Required: No

## See Also
<a name="API_AssociatedRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociatedRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociatedRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociatedRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
