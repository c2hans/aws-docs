---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateTest.html
---

# UpdateTest
<a name="API_UpdateTest"></a>

Updates the configuration of an existing test.

## Request Syntax
<a name="API_UpdateTest_RequestSyntax"></a>

```
POST /v2/update-test HTTP/1.1
Content-type: application/json

{
   "loggingConfiguration": {
      "cloudWatchLogGroupArn": "{{string}}",
      "logSchemaVersion": "{{string}}",
      "s3BucketName": "{{string}}"
   },
   "parameters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "roleName": "{{string}}",
   "serviceArn": "{{string}}",
   "stopConditions": [
      {
         "source": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "testId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTest_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [loggingConfiguration](#API_UpdateTest_RequestSyntax) **   <a name="ngresiliencehub-UpdateTest-request-loggingConfiguration"></a>
The updated logging configuration for the test.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** [parameters](#API_UpdateTest_RequestSyntax) **   <a name="ngresiliencehub-UpdateTest-request-parameters"></a>
The updated parameter values for the test.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[\w.-]+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [roleName](#API_UpdateTest_RequestSyntax) **   <a name="ngresiliencehub-UpdateTest-request-roleName"></a>
The updated IAM execution role name.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** [serviceArn](#API_UpdateTest_RequestSyntax) **   <a name="ngresiliencehub-UpdateTest-request-serviceArn"></a>
The ARN of the service the test belongs to.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [stopConditions](#API_UpdateTest_RequestSyntax) **   <a name="ngresiliencehub-UpdateTest-request-stopConditions"></a>
The updated stop conditions for the test.
Type: Array of [StopCondition](API_StopCondition.md) objects
Required: No

 ** [testId](#API_UpdateTest_RequestSyntax) **   <a name="ngresiliencehub-UpdateTest-request-testId"></a>
The identifier of the test to update.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateTest_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "test": {
      "actions": [
         {
            "actionId": "string",
            "description": "string",
            "resourceType": "string"
         }
      ],
      "creationTime": number,
      "loggingConfiguration": {
         "cloudWatchLogGroupArn": "string",
         "logSchemaVersion": "string",
         "s3BucketName": "string"
      },
      "name": "string",
      "parameters": {
         "string" : [ "string" ]
      },
      "roleName": "string",
      "serviceArn": "string",
      "stopConditions": [
         {
            "source": "string",
            "value": "string"
         }
      ],
      "successfulTestRuns": number,
      "testId": "string",
      "testTemplateArn": "string",
      "totalTestRuns": number
   }
}
```

## Response Elements
<a name="API_UpdateTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [test](#API_UpdateTest_ResponseSyntax) **   <a name="ngresiliencehub-UpdateTest-response-test"></a>
The updated test.
Type: [Test](API_Test.md) object

## Errors
<a name="API_UpdateTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** ConflictException **
Conflict — resource already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/UpdateTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/UpdateTest)
