---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AppDetails.html
---

# AppDetails
<a name="API_AppDetails"></a>

Details about an Amazon SageMaker AI app.

## Contents
<a name="API_AppDetails_Contents"></a>

 ** AppName **   <a name="sagemaker-Type-AppDetails-AppName"></a>
The name of the app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** AppType **   <a name="sagemaker-Type-AppDetails-AppType"></a>
The type of app.
Type: String
Valid Values: `JupyterServer | KernelGateway | DetailedProfiler | TensorBoard | CodeEditor | JupyterLab | RStudioServerPro | RSessionGateway | Canvas`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-AppDetails-CreationTime"></a>
The creation time.
Type: Timestamp
Required: No

 ** DomainId **   <a name="sagemaker-Type-AppDetails-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** ResourceSpec **   <a name="sagemaker-Type-AppDetails-ResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** SpaceName **   <a name="sagemaker-Type-AppDetails-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** Status **   <a name="sagemaker-Type-AppDetails-Status"></a>
The status.
Type: String
Valid Values: `Deleted | Deleting | Failed | InService | Pending`
Required: No

 ** UserProfileName **   <a name="sagemaker-Type-AppDetails-UserProfileName"></a>
The user profile name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_AppDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AppDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AppDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AppDetails)
