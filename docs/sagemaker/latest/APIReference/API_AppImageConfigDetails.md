---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AppImageConfigDetails.html
---

# AppImageConfigDetails
<a name="API_AppImageConfigDetails"></a>

The configuration for running a SageMaker AI image as a KernelGateway app.

## Contents
<a name="API_AppImageConfigDetails_Contents"></a>

 ** AppImageConfigArn **   <a name="sagemaker-Type-AppImageConfigDetails-AppImageConfigArn"></a>
The ARN of the AppImageConfig.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:app-image-config/.*`
Required: No

 ** AppImageConfigName **   <a name="sagemaker-Type-AppImageConfigDetails-AppImageConfigName"></a>
The name of the AppImageConfig. Must be unique to your account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** CodeEditorAppImageConfig **   <a name="sagemaker-Type-AppImageConfigDetails-CodeEditorAppImageConfig"></a>
The configuration for the file system and the runtime, such as the environment variables and entry point.
Type: [CodeEditorAppImageConfig](API_CodeEditorAppImageConfig.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-AppImageConfigDetails-CreationTime"></a>
When the AppImageConfig was created.
Type: Timestamp
Required: No

 ** JupyterLabAppImageConfig **   <a name="sagemaker-Type-AppImageConfigDetails-JupyterLabAppImageConfig"></a>
The configuration for the file system and the runtime, such as the environment variables and entry point.
Type: [JupyterLabAppImageConfig](API_JupyterLabAppImageConfig.md) object
Required: No

 ** KernelGatewayImageConfig **   <a name="sagemaker-Type-AppImageConfigDetails-KernelGatewayImageConfig"></a>
The configuration for the file system and kernels in the SageMaker AI image.
Type: [KernelGatewayImageConfig](API_KernelGatewayImageConfig.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-AppImageConfigDetails-LastModifiedTime"></a>
When the AppImageConfig was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_AppImageConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AppImageConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AppImageConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AppImageConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
