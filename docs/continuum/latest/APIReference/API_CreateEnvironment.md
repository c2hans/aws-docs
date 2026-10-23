---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Creates an environment and starts its validation and any requested provisioning. Storage provisioning and dependency checks may continue after the initial 201 response; use GetEnvironment to observe completion.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
POST /environments HTTP/1.1
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
<a name="API_CreateEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_CreateEnvironment_RequestSyntax) **   <a name="continuum-CreateEnvironment-request-configuration"></a>
The configuration.
Type: [CreateEnvironmentConfiguration](API_CreateEnvironmentConfiguration.md) object
Required: No

 ** [name](#API_CreateEnvironment_RequestSyntax) **   <a name="continuum-CreateEnvironment-request-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.\-]{0,254}`
Required: Yes

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "environmentArn": "string",
   "environmentId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateEnvironment_ResponseSyntax) **   <a name="continuum-CreateEnvironment-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [environmentArn](#API_CreateEnvironment_ResponseSyntax) **   <a name="continuum-CreateEnvironment-response-environmentArn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+`

 ** [environmentId](#API_CreateEnvironment_ResponseSyntax) **   <a name="continuum-CreateEnvironment-response-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [status](#API_CreateEnvironment_ResponseSyntax) **   <a name="continuum-CreateEnvironment-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE`

## Errors
<a name="API_CreateEnvironment_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota. Review your quota and request an increase if needed.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CreateEnvironment)
