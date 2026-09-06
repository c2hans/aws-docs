---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetNetworkMigrationMapperSegmentConstruct.html
---

# GetNetworkMigrationMapperSegmentConstruct
<a name="API_GetNetworkMigrationMapperSegmentConstruct"></a>

Retrieves detailed information about a specific construct within a mapper segment, including its properties and configuration data.

## Request Syntax
<a name="API_GetNetworkMigrationMapperSegmentConstruct_RequestSyntax"></a>

```
POST /network-migration/GetNetworkMigrationMapperSegmentConstruct HTTP/1.1
Content-type: application/json

{
   "constructID": "{{string}}",
   "networkMigrationDefinitionID": "{{string}}",
   "networkMigrationExecutionID": "{{string}}",
   "segmentID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetNetworkMigrationMapperSegmentConstruct_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetNetworkMigrationMapperSegmentConstruct_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [constructID](#API_GetNetworkMigrationMapperSegmentConstruct_RequestSyntax) **   <a name="mgn-GetNetworkMigrationMapperSegmentConstruct-request-constructID"></a>
The unique identifier of the construct within the segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [networkMigrationDefinitionID](#API_GetNetworkMigrationMapperSegmentConstruct_RequestSyntax) **   <a name="mgn-GetNetworkMigrationMapperSegmentConstruct-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

 ** [networkMigrationExecutionID](#API_GetNetworkMigrationMapperSegmentConstruct_RequestSyntax) **   <a name="mgn-GetNetworkMigrationMapperSegmentConstruct-request-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [segmentID](#API_GetNetworkMigrationMapperSegmentConstruct_RequestSyntax) **   <a name="mgn-GetNetworkMigrationMapperSegmentConstruct-request-segmentID"></a>
The unique identifier of the mapper segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_GetNetworkMigrationMapperSegmentConstruct_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "construct": {
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
}
```

## Response Elements
<a name="API_GetNetworkMigrationMapperSegmentConstruct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [construct](#API_GetNetworkMigrationMapperSegmentConstruct_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationMapperSegmentConstruct-response-construct"></a>
The construct metadata including type, name, and configuration.
Type: [NetworkMigrationMapperSegmentConstruct](API_NetworkMigrationMapperSegmentConstruct.md) object

## Errors
<a name="API_GetNetworkMigrationMapperSegmentConstruct_Errors"></a>

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

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_GetNetworkMigrationMapperSegmentConstruct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/GetNetworkMigrationMapperSegmentConstruct)
