---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationMapperSegmentConstructs.html
---

# ListNetworkMigrationMapperSegmentConstructs
<a name="API_ListNetworkMigrationMapperSegmentConstructs"></a>

Lists constructs within a mapper segment, representing individual infrastructure components like VPCs, subnets, or security groups.

## Request Syntax
<a name="API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax"></a>

```
POST /network-migration/ListNetworkMigrationMapperSegmentConstructs HTTP/1.1
Content-type: application/json

{
   "filters": {
      "constructIDs": [ "{{string}}" ],
      "constructTypes": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "networkMigrationDefinitionID": "{{string}}",
   "networkMigrationExecutionID": "{{string}}",
   "nextToken": "{{string}}",
   "segmentID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListNetworkMigrationMapperSegmentConstructs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListNetworkMigrationMapperSegmentConstructs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-request-filters"></a>
Filters to apply when listing constructs, such as construct type or ID.
Type: [ListNetworkMigrationMapperSegmentConstructsFilters](API_ListNetworkMigrationMapperSegmentConstructsFilters.md) object
Required: No

 ** [maxResults](#API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [networkMigrationDefinitionID](#API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

 ** [networkMigrationExecutionID](#API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-request-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [segmentID](#API_ListNetworkMigrationMapperSegmentConstructs_RequestSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-request-segmentID"></a>
The unique identifier of the segment to list constructs for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_ListNetworkMigrationMapperSegmentConstructs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "constructID": "string",
         "constructType": "string",
         "createdAt": number,
         "description": "string",
         "excluded": boolean,
         "logicalID": "string",
         "name": "string",
         "properties": {
            "string" : "string"
         },
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNetworkMigrationMapperSegmentConstructs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListNetworkMigrationMapperSegmentConstructs_ResponseSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-response-items"></a>
A list of mapper segment constructs.
Type: Array of [NetworkMigrationMapperSegmentConstruct](API_NetworkMigrationMapperSegmentConstruct.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListNetworkMigrationMapperSegmentConstructs_ResponseSyntax) **   <a name="mgn-ListNetworkMigrationMapperSegmentConstructs-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListNetworkMigrationMapperSegmentConstructs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** ThrottlingException **
Reached throttling quota exception.
 ** quotaCode **
Reached throttling quota exception.
 ** retryAfterSeconds **
Reached throttling quota exception will retry after x seconds.
 ** serviceCode **
Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ListNetworkMigrationMapperSegmentConstructs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructs)
