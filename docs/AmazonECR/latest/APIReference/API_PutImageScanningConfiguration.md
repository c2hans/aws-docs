---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImageScanningConfiguration.html
---

# PutImageScanningConfiguration
<a name="API_PutImageScanningConfiguration"></a>

**Important**
The `PutImageScanningConfiguration` API is being deprecated, in favor of specifying the image scanning configuration at the registry level. For more information, see [PutRegistryScanningConfiguration](API_PutRegistryScanningConfiguration.md).

Updates the image scanning configuration for the specified repository.

## Request Syntax
<a name="API_PutImageScanningConfiguration_RequestSyntax"></a>

```
{
   "imageScanningConfiguration": {
      "scanOnPush": {{boolean}}
   },
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutImageScanningConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageScanningConfiguration](#API_PutImageScanningConfiguration_RequestSyntax) **   <a name="ECR-PutImageScanningConfiguration-request-imageScanningConfiguration"></a>
The image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: Yes

 ** [registryId](#API_PutImageScanningConfiguration_RequestSyntax) **   <a name="ECR-PutImageScanningConfiguration-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to update the image scanning configuration setting. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_PutImageScanningConfiguration_RequestSyntax) **   <a name="ECR-PutImageScanningConfiguration-request-repositoryName"></a>
The name of the repository in which to update the image scanning configuration setting.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_PutImageScanningConfiguration_ResponseSyntax"></a>

```
{
   "imageScanningConfiguration": {
      "scanOnPush": boolean
   },
   "registryId": "string",
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_PutImageScanningConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageScanningConfiguration](#API_PutImageScanningConfiguration_ResponseSyntax) **   <a name="ECR-PutImageScanningConfiguration-response-imageScanningConfiguration"></a>
The image scanning configuration setting for the repository.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object

 ** [registryId](#API_PutImageScanningConfiguration_ResponseSyntax) **   <a name="ECR-PutImageScanningConfiguration-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_PutImageScanningConfiguration_ResponseSyntax) **   <a name="ECR-PutImageScanningConfiguration-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

## Errors
<a name="API_PutImageScanningConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_PutImageScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/PutImageScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/PutImageScanningConfiguration)
