---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetSystem.html
---

# GetSystem
<a name="API_GetSystem"></a>

Retrieves a system by ARN.

## Request Syntax
<a name="API_GetSystem_RequestSyntax"></a>

```
GET /v2/get-system?systemArn={{systemArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSystem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [systemArn](#API_GetSystem_RequestSyntax) **   <a name="ngresiliencehub-GetSystem-request-uri-systemArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Request Body
<a name="API_GetSystem_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSystem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "system": {
      "createdAt": number,
      "description": "string",
      "kmsKeyId": "string",
      "name": "string",
      "organizationId": "string",
      "ouId": "string",
      "sharingEnabled": boolean,
      "systemArn": "string",
      "systemId": "string",
      "tags": {
         "string" : "string"
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [system](#API_GetSystem_ResponseSyntax) **   <a name="ngresiliencehub-GetSystem-response-system"></a>
The requested system.
Type: [System](API_System.md) object

## Errors
<a name="API_GetSystem_Errors"></a>

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
<a name="API_GetSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/GetSystem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/GetSystem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
