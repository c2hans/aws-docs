---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageSigningStatus.html
---

# ImageSigningStatus
<a name="API_ImageSigningStatus"></a>

The signing status for an image. Each status corresponds to a signing profile.

## Contents
<a name="API_ImageSigningStatus_Contents"></a>

 ** failureCode **   <a name="ECR-Type-ImageSigningStatus-failureCode"></a>
The failure code, which is only present if `status` is `FAILED`.
Type: String
Required: No

 ** failureReason **   <a name="ECR-Type-ImageSigningStatus-failureReason"></a>
A description of why signing the image failed. This field is only present if `status` is `FAILED`.
Type: String
Required: No

 ** signingProfileArn **   <a name="ECR-Type-ImageSigningStatus-signingProfileArn"></a>
The ARN of the AWS Signer signing profile used to sign the image.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^arn:aws(-[a-z]+)*:signer:[a-z0-9-]+:[0-9]{12}:\/signing-profiles\/[a-zA-Z0-9_]{2,}$`
Required: No

 ** status **   <a name="ECR-Type-ImageSigningStatus-status"></a>
The image's signing status. Possible values are:
+  `IN_PROGRESS` - Signing is currently in progress.
+  `COMPLETE` - The signature was successfully generated.
+  `FAILED` - Signing failed. See `failureCode` and `failureReason` for details.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## See Also
<a name="API_ImageSigningStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageSigningStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageSigningStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageSigningStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
