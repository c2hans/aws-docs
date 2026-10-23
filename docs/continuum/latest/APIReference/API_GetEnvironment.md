---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetEnvironment.html
---

# GetEnvironment
<a name="API_GetEnvironment"></a>

Retrieves the current state and configuration of an environment.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
GET /environments/{{environmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetEnvironment_RequestSyntax) **   <a name="continuum-GetEnvironment-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "codeConfiguration": {
         "collectorDetails": {
            "collectorDataAccessRoleArn": "string"
         },
         "environmentConfiguration": {
            "network": {
               "allowedDomains": [ "string" ]
            },
            "patchCreationPolicy": "string",
            "scanFrequency": "string"
         },
         "latestScan": {
            "completedAt": "string",
            "createdAt": "string",
            "failureMessage": "string",
            "failureStage": "string",
            "origin": "string",
            "scanRunId": "string",
            "status": "string"
         },
         "sourceConfiguration": {
            "repositorySources": [
               {
                  "defaultBranch": "string",
                  "integrationId": "string",
                  "repository": "string"
               }
            ],
            "s3Sources": [
               {
                  "codePrefix": "string",
                  "contextPrefix": "string",
                  "integrationId": "string"
               }
            ]
         }
      }
   },
   "createdAt": "string",
   "environmentArn": "string",
   "environmentId": "string",
   "name": "string",
   "status": "string",
   "statusMessage": "string",
   "statusUpdatedAt": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-configuration"></a>
The configuration.
Type: [EnvironmentConfigurationDetails](API_EnvironmentConfigurationDetails.md) object

 ** [createdAt](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [environmentArn](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-environmentArn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+`

 ** [environmentId](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [name](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.\-]{0,254}`

 ** [status](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE`

 ** [statusMessage](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-statusMessage"></a>
The status Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [statusUpdatedAt](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-statusUpdatedAt"></a>
The status Updated At.
Type: Timestamp

 ** [updatedAt](#API_GetEnvironment_ResponseSyntax) **   <a name="continuum-GetEnvironment-response-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp

## Errors
<a name="API_GetEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetEnvironment)
