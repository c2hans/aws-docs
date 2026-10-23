---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateEnvironment.html
---

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

Updates the customer-controlled mutable properties of an environment. Only the name, the environment's S3 integration source and repository selections, its scan frequency, its network policy, and its patch creation policy can be changed.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
PATCH /environments/{{environmentId}} HTTP/1.1
Content-type: application/json

{
   "configuration": {
      "codeConfiguration": {
         "environmentConfiguration": {
            "network": {
               "allowedDomains": [ "{{string}}" ]
            },
            "patchCreationPolicy": "{{string}}",
            "scanFrequency": "{{string}}"
         },
         "sourceConfiguration": {
            "repositorySources": [
               {
                  "defaultBranch": "{{string}}",
                  "integrationId": "{{string}}",
                  "repository": "{{string}}"
               }
            ],
            "s3Sources": [
               {
                  "codePrefix": "{{string}}",
                  "contextPrefix": "{{string}}",
                  "integrationId": "{{string}}"
               }
            ]
         }
      }
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_UpdateEnvironment_RequestSyntax) **   <a name="continuum-UpdateEnvironment-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateEnvironment_RequestSyntax) **   <a name="continuum-UpdateEnvironment-request-configuration"></a>
The configuration.
Type: [UpdateEnvironmentConfiguration](API_UpdateEnvironmentConfiguration.md) object
Required: No

 ** [name](#API_UpdateEnvironment_RequestSyntax) **   <a name="continuum-UpdateEnvironment-request-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.\-]{0,254}`
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

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
   "statusUpdatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-configuration"></a>
The configuration.
Type: [EnvironmentConfigurationDetails](API_EnvironmentConfigurationDetails.md) object

 ** [createdAt](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [environmentArn](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-environmentArn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+`

 ** [environmentId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [name](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.\-]{0,254}`

 ** [status](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE`

 ** [statusMessage](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-statusMessage"></a>
The status Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [statusUpdatedAt](#API_UpdateEnvironment_ResponseSyntax) **   <a name="continuum-UpdateEnvironment-response-statusUpdatedAt"></a>
The status Updated At.
Type: Timestamp

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

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
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/UpdateEnvironment)
