---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationMapping.html
---

# StartNetworkMigrationMapping
<a name="API_StartNetworkMigrationMapping"></a>

Starts the network migration mapping process for a given network migration execution.

## Request Syntax
<a name="API_StartNetworkMigrationMapping_RequestSyntax"></a>

```
POST /network-migration/StartNetworkMigrationMapping HTTP/1.1
Content-type: application/json

{
   "networkMigrationDefinitionID": "{{string}}",
   "networkMigrationExecutionID": "{{string}}",
   "securityGroupMappingStrategy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartNetworkMigrationMapping_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartNetworkMigrationMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [networkMigrationDefinitionID](#API_StartNetworkMigrationMapping_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMapping-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

 ** [networkMigrationExecutionID](#API_StartNetworkMigrationMapping_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMapping-request-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [securityGroupMappingStrategy](#API_StartNetworkMigrationMapping_RequestSyntax) **   <a name="mgn-StartNetworkMigrationMapping-request-securityGroupMappingStrategy"></a>
The security group mapping strategy to use.
Type: String
Valid Values: `MAP | SKIP | MAP_DHCP`
Required: No

## Response Syntax
<a name="API_StartNetworkMigrationMapping_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "jobID": "string"
}
```

## Response Elements
<a name="API_StartNetworkMigrationMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [jobID](#API_StartNetworkMigrationMapping_ResponseSyntax) **   <a name="mgn-StartNetworkMigrationMapping-response-jobID"></a>
The unique identifier of the mapping job that was started.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_StartNetworkMigrationMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
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
The request could not be completed because it exceeded the service quota.
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
<a name="API_StartNetworkMigrationMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartNetworkMigrationMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartNetworkMigrationMapping)
