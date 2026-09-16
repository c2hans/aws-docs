---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetTestTemplate.html
---

# GetTestTemplate
<a name="API_GetTestTemplate"></a>

Retrieves a resilience test template by ARN, including the parameters it accepts and the fault actions it runs.

## Request Syntax
<a name="API_GetTestTemplate_RequestSyntax"></a>

```
GET /v2/get-test-template?testTemplateArn={{testTemplateArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTestTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testTemplateArn](#API_GetTestTemplate_RequestSyntax) **   <a name="ngresiliencehub-GetTestTemplate-request-uri-testTemplateArn"></a>
The ARN of the test template to retrieve.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Request Body
<a name="API_GetTestTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTestTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "testTemplate": {
      "actions": [
         {
            "actionId": "string",
            "description": "string",
            "resourceType": "string"
         }
      ],
      "description": "string",
      "name": "string",
      "parameters": [
         {
            "defaultValue": "string",
            "description": "string",
            "maxValues": number,
            "name": "string",
            "required": boolean,
            "type": "string"
         }
      ],
      "testTemplateArn": "string"
   }
}
```

## Response Elements
<a name="API_GetTestTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [testTemplate](#API_GetTestTemplate_ResponseSyntax) **   <a name="ngresiliencehub-GetTestTemplate-response-testTemplate"></a>
The requested test template.
Type: [TestTemplate](API_TestTemplate.md) object

## Errors
<a name="API_GetTestTemplate_Errors"></a>

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
<a name="API_GetTestTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/GetTestTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/GetTestTemplate)
