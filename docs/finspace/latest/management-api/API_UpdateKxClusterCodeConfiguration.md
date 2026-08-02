---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterCodeConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# UpdateKxClusterCodeConfiguration
<a name="API_UpdateKxClusterCodeConfiguration"></a>

 Allows you to update code configuration on a running cluster. By using this API you can update the code, the initialization script path, and the command line arguments for a specific cluster. The configuration that you want to update will override any existing configurations on the cluster.

## Request Syntax
<a name="API_UpdateKxClusterCodeConfiguration_RequestSyntax"></a>

```
PUT /kx/environments/{{environmentId}}/clusters/{{clusterName}}/configuration/code HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "code": {
      "s3Bucket": "{{string}}",
      "s3Key": "{{string}}",
      "s3ObjectVersion": "{{string}}"
   },
   "commandLineArguments": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "deploymentConfiguration": {
      "deploymentStrategy": "{{string}}"
   },
   "initializationScript": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateKxClusterCodeConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterName](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-uri-clusterName"></a>
The name of the cluster.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-uri-environmentId"></a>
 A unique identifier of the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_UpdateKxClusterCodeConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [code](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-code"></a>
The structure of the customer code available within the running cluster.
Type: [CodeConfiguration](API_CodeConfiguration.md) object
Required: Yes

 ** [clientToken](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [commandLineArguments](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-commandLineArguments"></a>
Specifies the key-value pairs to make them available inside the cluster.
You cannot update this parameter for a `NO_RESTART` deployment.
Type: Array of [KxCommandLineArgument](API_KxCommandLineArgument.md) objects
Required: No

 ** [deploymentConfiguration](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-deploymentConfiguration"></a>
 The configuration that allows you to choose how you want to update the code on a cluster.
Type: [KxClusterCodeDeploymentConfiguration](API_KxClusterCodeDeploymentConfiguration.md) object
Required: No

 ** [initializationScript](#API_UpdateKxClusterCodeConfiguration_RequestSyntax) **   <a name="finspace-UpdateKxClusterCodeConfiguration-request-initializationScript"></a>
Specifies a Q program that will be run at launch of a cluster. It is a relative path within *.zip* file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, `somedir/init.q`.
You cannot update this parameter for a `NO_RESTART` deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\_\-\.\/\\]+$`
Required: No

## Response Syntax
<a name="API_UpdateKxClusterCodeConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateKxClusterCodeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateKxClusterCodeConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateKxClusterCodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/UpdateKxClusterCodeConfiguration)
