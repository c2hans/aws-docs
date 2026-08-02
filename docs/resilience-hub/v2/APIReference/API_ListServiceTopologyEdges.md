---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServiceTopologyEdges.html
---

# ListServiceTopologyEdges
<a name="API_ListServiceTopologyEdges"></a>

Lists topology edges for a service.

## Request Syntax
<a name="API_ListServiceTopologyEdges_RequestSyntax"></a>

```
GET /v2/list-service-topology-edges?maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServiceTopologyEdges_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListServiceTopologyEdges_RequestSyntax) **   <a name="ngresiliencehub-ListServiceTopologyEdges-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListServiceTopologyEdges_RequestSyntax) **   <a name="ngresiliencehub-ListServiceTopologyEdges-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListServiceTopologyEdges_RequestSyntax) **   <a name="ngresiliencehub-ListServiceTopologyEdges-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Request Body
<a name="API_ListServiceTopologyEdges_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServiceTopologyEdges_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "serviceTopologyEdgeSummaries": [
      {
         "destinationAccount": "string",
         "destinationRegion": "string",
         "destinationResourceIdentifier": "string",
         "properties": [
            {
               "label": "string",
               "topologyType": "string"
            }
         ],
         "sourceAccount": "string",
         "sourceRegion": "string",
         "sourceResourceIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceTopologyEdges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServiceTopologyEdges_ResponseSyntax) **   <a name="ngresiliencehub-ListServiceTopologyEdges-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceTopologyEdgeSummaries](#API_ListServiceTopologyEdges_ResponseSyntax) **   <a name="ngresiliencehub-ListServiceTopologyEdges-response-serviceTopologyEdgeSummaries"></a>
The list of service topology edge summaries.
Type: Array of [ServiceTopologyEdgeSummary](API_ServiceTopologyEdgeSummary.md) objects

## Errors
<a name="API_ListServiceTopologyEdges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceTopologyEdges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListServiceTopologyEdges)
