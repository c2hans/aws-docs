---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetTest.html
---

# GetTest
<a name="API_GetTest"></a>

Retrieves a test by ID.

## Request Syntax
<a name="API_GetTest_RequestSyntax"></a>

```
GET /v2/get-test?serviceArn={{serviceArn}}&testId={{testId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceArn](#API_GetTest_RequestSyntax) **   <a name="ngresiliencehub-GetTest-request-uri-serviceArn"></a>
The ARN of the service the test belongs to.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [testId](#API_GetTest_RequestSyntax) **   <a name="ngresiliencehub-GetTest-request-uri-testId"></a>
The identifier of the test to retrieve.
Length Constraints: Minimum length of 1.
Required: Yes

## Request Body
<a name="API_GetTest_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTest_ResponseSyntax"></a>

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
<a name="API_GetTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [test](#API_GetTest_ResponseSyntax) **   <a name="ngresiliencehub-GetTest-response-test"></a>
The requested test.
Type: [Test](API_Test.md) object

## Errors
<a name="API_GetTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

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
<a name="API_GetTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/GetTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/GetTest)
