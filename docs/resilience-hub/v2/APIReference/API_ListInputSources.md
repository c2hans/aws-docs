---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListInputSources.html
---

# ListInputSources
<a name="API_ListInputSources"></a>

Lists input sources for a service.

## Request Syntax
<a name="API_ListInputSources_RequestSyntax"></a>

```
GET /v2/list-input-sources?maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInputSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListInputSources_RequestSyntax) **   <a name="ngresiliencehub-ListInputSources-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListInputSources_RequestSyntax) **   <a name="ngresiliencehub-ListInputSources-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListInputSources_RequestSyntax) **   <a name="ngresiliencehub-ListInputSources-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [type](#API_ListInputSources_RequestSyntax) **   <a name="ngresiliencehub-ListInputSources-request-uri-type"></a>
Filter input sources by type.
Valid Values: `CFN_STACK | TAGS | EKS | TERRAFORM | DESIGN_FILE | MONITORING`

## Request Body
<a name="API_ListInputSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInputSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "inputSourceSummaries": [
      {
         "cfnStackArn": "string",
         "createdAt": number,
         "designFileS3Url": "string",
         "eks": {
            "clusterArn": "string",
            "namespaces": [ "string" ]
         },
         "inputSourceId": "string",
         "resourceTags": [
            {
               "key": "string",
               "values": [ "string" ]
            }
         ],
         "tfStateFileUrl": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInputSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [inputSourceSummaries](#API_ListInputSources_ResponseSyntax) **   <a name="ngresiliencehub-ListInputSources-response-inputSourceSummaries"></a>
The list of input source summaries.
Type: Array of [InputSourceSummary](API_InputSourceSummary.md) objects

 ** [nextToken](#API_ListInputSources_ResponseSyntax) **   <a name="ngresiliencehub-ListInputSources-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListInputSources_Errors"></a>

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
<a name="API_ListInputSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListInputSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListInputSources)
