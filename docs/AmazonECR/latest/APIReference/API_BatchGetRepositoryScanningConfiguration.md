---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetRepositoryScanningConfiguration.html
---

# BatchGetRepositoryScanningConfiguration
<a name="API_BatchGetRepositoryScanningConfiguration"></a>

Gets the scanning configuration for one or more repositories.

## Request Syntax
<a name="API_BatchGetRepositoryScanningConfiguration_RequestSyntax"></a>

```
{
   "repositoryNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetRepositoryScanningConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [repositoryNames](#API_BatchGetRepositoryScanningConfiguration_RequestSyntax) **   <a name="ECR-BatchGetRepositoryScanningConfiguration-request-repositoryNames"></a>
One or more repository names to get the scanning configuration for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_BatchGetRepositoryScanningConfiguration_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "failureCode": "string",
         "failureReason": "string",
         "repositoryName": "string"
      }
   ],
   "scanningConfigurations": [
      {
         "appliedScanFilters": [
            {
               "filter": "string",
               "filterType": "string"
            }
         ],
         "repositoryArn": "string",
         "repositoryName": "string",
         "scanFrequency": "string",
         "scanOnPush": boolean
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetRepositoryScanningConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_BatchGetRepositoryScanningConfiguration_ResponseSyntax) **   <a name="ECR-BatchGetRepositoryScanningConfiguration-response-failures"></a>
Any failures associated with the call.
Type: Array of [RepositoryScanningConfigurationFailure](API_RepositoryScanningConfigurationFailure.md) objects

 ** [scanningConfigurations](#API_BatchGetRepositoryScanningConfiguration_ResponseSyntax) **   <a name="ECR-BatchGetRepositoryScanningConfiguration-response-scanningConfigurations"></a>
The scanning configuration for the requested repositories.
Type: Array of [RepositoryScanningConfiguration](API_RepositoryScanningConfiguration.md) objects

## Errors
<a name="API_BatchGetRepositoryScanningConfiguration_Errors"></a>

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
<a name="API_BatchGetRepositoryScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/BatchGetRepositoryScanningConfiguration)
