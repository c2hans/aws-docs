---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListResources.html
---

# ListResources
<a name="API_ListResources"></a>

List resources.

## Request Syntax
<a name="API_ListResources_RequestSyntax"></a>

```
GET /v2/list-resources?awsRegion={{awsRegion}}&billable={{billable}}&maxResults={{maxResults}}&nextToken={{nextToken}}&resourceTypes={{resourceTypes}}&serviceArn={{serviceArn}}&serviceFunctionId={{serviceFunctionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [awsRegion](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-awsRegion"></a>
Filter resources by AWS Region.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`

 ** [billable](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-billable"></a>
Specifies whether to filter non-billable resources. When true (the default), the operation returns only billable resources.

 ** [maxResults](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [resourceTypes](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-resourceTypes"></a>
The CloudFormation resource types to include in the response.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [serviceArn](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [serviceFunctionId](#API_ListResources_RequestSyntax) **   <a name="ngresiliencehub-ListResources-request-uri-serviceFunctionId"></a>
Filter resources by service function identifier.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`

## Request Body
<a name="API_ListResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "serviceFunctionId": "string",
   "serviceResources": [
      {
         "inputSource": {
            "identifier": "string",
            "type": "string"
         },
         "resource": {
            "awsAccountId": "string",
            "awsRegion": "string",
            "identifier": "string",
            "resourceType": "string"
         },
         "resourceIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListResources_ResponseSyntax) **   <a name="ngresiliencehub-ListResources-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceFunctionId](#API_ListResources_ResponseSyntax) **   <a name="ngresiliencehub-ListResources-response-serviceFunctionId"></a>
The service function identifier for the returned resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`

 ** [serviceResources](#API_ListResources_ResponseSyntax) **   <a name="ngresiliencehub-ListResources-response-serviceResources"></a>
The list of service resources.
Type: Array of [ServiceResource](API_ServiceResource.md) objects

## Errors
<a name="API_ListResources_Errors"></a>

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
<a name="API_ListResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
