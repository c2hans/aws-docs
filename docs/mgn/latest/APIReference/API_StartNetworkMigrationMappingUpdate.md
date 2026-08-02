---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationMappingUpdate.html
---

# StartNetworkMigrationMappingUpdate
<a name="API_StartNetworkMigrationMappingUpdate"></a>

Starts a job to apply customer modifications to network migration mappings, such as changing properties.

## Request Syntax
<a name="API_StartNetworkMigrationMappingUpdate_RequestSyntax"></a>

```
POST /network-migration/StartNetworkMigrationMappingUpdate HTTP/1.1
Content-type: application/json

{
   "constructs": [
      {
         "constructID": "{{string}}",
         "constructType": "{{string}}",
         "operation": { ... },
         "segmentID": "{{string}}"
      }
   ],
   "networkMigrationDefinitionID": "{{string}}",
   "networkMigrationExecutionID": "{{string}}",
   "segments": [
      {
         "scopeTags": {
            "{{string}}" : "{{string}}"
         },
         "segmentID": "{{string}}",
         "targetAccount": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartNetworkMigrationMappingUpdate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartNetworkMigrationMappingUpdate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [constructs](#API_StartNetworkMigrationMappingUpdate_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMappingUpdate-request-constructs"></a>
A list of construct updates to apply.
Type: Array of [StartNetworkMigrationMappingUpdateConstruct](API_StartNetworkMigrationMappingUpdateConstruct.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [networkMigrationDefinitionID](#API_StartNetworkMigrationMappingUpdate_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMappingUpdate-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

 ** [networkMigrationExecutionID](#API_StartNetworkMigrationMappingUpdate_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMappingUpdate-request-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [segments](#API_StartNetworkMigrationMappingUpdate_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMappingUpdate-request-segments"></a>
A list of segment updates to apply.
Type: Array of [StartNetworkMigrationMappingUpdateSegment](API_StartNetworkMigrationMappingUpdateSegment.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_StartNetworkMigrationMappingUpdate_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "jobID": "string"
}
```

## Response Elements
<a name="API_StartNetworkMigrationMappingUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [jobID](#API_StartNetworkMigrationMappingUpdate_ResponseSyntax) **   <a name="mgn-StartNetworkMigrationMappingUpdate-response-jobID"></a>
The unique identifier of the mapping update job that was started.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_StartNetworkMigrationMappingUpdate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operating denied due to a file permission or access check error.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Exceeded the service quota code.
 ** quotaValue **
Exceeded the service quota value.
 ** resourceId **
Exceeded the service quota resource ID.
 ** resourceType **
Exceeded the service quota resource type.
 ** serviceCode **
Exceeded the service quota service code.
HTTP Status Code: 402

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
<a name="API_StartNetworkMigrationMappingUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartNetworkMigrationMappingUpdate)
