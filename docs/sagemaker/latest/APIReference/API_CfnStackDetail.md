---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CfnStackDetail.html
---

# CfnStackDetail
<a name="API_CfnStackDetail"></a>

 Details about the CloudFormation stack.

## Contents
<a name="API_CfnStackDetail_Contents"></a>

 ** StatusMessage **   <a name="sagemaker-Type-CfnStackDetail-StatusMessage"></a>
 A human-readable message about the stack's current status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.{1,4096}`
Required: Yes

 ** Id **   <a name="sagemaker-Type-CfnStackDetail-Id"></a>
 The unique identifier of the CloudFormation stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(?=.{1,256}$)arn:aws[a-z\-]*:cloudformation:[a-z0-9\-]*:[0-9]{12}:stack/[a-zA-Z][a-zA-Z0-9-]{0,127}/.*`
Required: No

 ** Name **   <a name="sagemaker-Type-CfnStackDetail-Name"></a>
 The name of the CloudFormation stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z][A-Za-z0-9-]{0,127}`
Required: No

## See Also
<a name="API_CfnStackDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CfnStackDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CfnStackDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CfnStackDetail)
