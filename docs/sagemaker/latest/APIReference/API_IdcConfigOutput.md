---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IdcConfigOutput.html
---

# IdcConfigOutput
<a name="API_IdcConfigOutput"></a>

Contains the AWS IAM Identity Center configuration of a SageMaker Partner AI App that uses `IDC` authorization.

## Contents
<a name="API_IdcConfigOutput_Contents"></a>

 ** InstanceArn **   <a name="sagemaker-Type-IdcConfigOutput-InstanceArn"></a>
The ARN of the AWS IAM Identity Center instance that the SageMaker Partner AI App uses to authenticate users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sso:::instance/(sso)?ins-[a-zA-Z0-9.-]{16}`
Required: Yes

 ** ApplicationArn **   <a name="sagemaker-Type-IdcConfigOutput-ApplicationArn"></a>
The ARN of the AWS IAM Identity Center application that SageMaker creates for the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sso::[0-9]{12}:application/(sso)?ins-[a-zA-Z0-9.-]{16}/apl-[a-zA-Z0-9.-]{16}`
Required: No

## See Also
<a name="API_IdcConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IdcConfigOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IdcConfigOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IdcConfigOutput)
