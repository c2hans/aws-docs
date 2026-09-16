---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateNetworkMigrationMapperSegment.html
---

# UpdateNetworkMigrationMapperSegment
<a name="API_UpdateNetworkMigrationMapperSegment"></a>

Updates a mapper segment's configuration, such as changing its scope tags.

## Request Syntax
<a name="API_UpdateNetworkMigrationMapperSegment_RequestSyntax"></a>

```
POST /network-migration/UpdateNetworkMigrationMapperSegment HTTP/1.1
Content-type: application/json

{
   "networkMigrationDefinitionID": "{{string}}",
   "networkMigrationExecutionID": "{{string}}",
   "scopeTags": {
      "{{string}}" : "{{string}}"
   },
   "segmentID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateNetworkMigrationMapperSegment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateNetworkMigrationMapperSegment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [networkMigrationDefinitionID](#API_UpdateNetworkMigrationMapperSegment_RequestSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

 ** [networkMigrationExecutionID](#API_UpdateNetworkMigrationMapperSegment_RequestSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-request-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [scopeTags](#API_UpdateNetworkMigrationMapperSegment_RequestSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-request-scopeTags"></a>
The updated scope tags for the segment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z0-9\s+\-=._:/@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s+\-=._:/@]*`
Required: No

 ** [segmentID](#API_UpdateNetworkMigrationMapperSegment_RequestSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-request-segmentID"></a>
The unique identifier of the segment to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_UpdateNetworkMigrationMapperSegment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "checksum": {
      "encryptionAlgorithm": "string",
      "hash": "string"
   },
   "createdAt": number,
   "description": "string",
   "jobID": "string",
   "logicalID": "string",
   "name": "string",
   "networkMigrationDefinitionID": "string",
   "networkMigrationExecutionID": "string",
   "outputS3Configuration": {
      "s3Bucket": "string",
      "s3BucketOwner": "string",
      "s3Key": "string"
   },
   "referencedSegments": [ "string" ],
   "scopeTags": {
      "string" : "string"
   },
   "segmentID": "string",
   "segmentType": "string",
   "targetAccount": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateNetworkMigrationMapperSegment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [checksum](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-checksum"></a>
The checksum of the segment data for integrity verification.
Type: [Checksum](API_Checksum.md) object

 ** [createdAt](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-createdAt"></a>
The timestamp when the segment was created.
Type: Timestamp

 ** [description](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-description"></a>
A description of the segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`

 ** [jobID](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-jobID"></a>
The unique identifier of the job that created this segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [logicalID](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-logicalID"></a>
The logical identifier for the segment in the infrastructure code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`

 ** [name](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-name"></a>
The name of the segment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [networkMigrationDefinitionID](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`

 ** [networkMigrationExecutionID](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [outputS3Configuration](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-outputS3Configuration"></a>
The S3 location where segment artifacts are stored.
Type: [S3Configuration](API_S3Configuration.md) object

 ** [referencedSegments](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-referencedSegments"></a>
A list of other segments that this segment depends on or references.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [scopeTags](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-scopeTags"></a>
Scope tags for the segment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z0-9\s+\-=._:/@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s+\-=._:/@]*`

 ** [segmentID](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-segmentID"></a>
The unique identifier of the segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [segmentType](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-segmentType"></a>
The category of the network migration segment. A segment groups the network constructs (such as VPCs, subnets, and security groups) that are migrated together. Valid values: `WORKLOAD`, `APPLIANCE`.
Type: String
Valid Values: `WORKLOAD | APPLIANCE`

 ** [targetAccount](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-targetAccount"></a>
The target AWS account where this segment will be deployed.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`

 ** [updatedAt](#API_UpdateNetworkMigrationMapperSegment_ResponseSyntax) **   <a name="mgn-UpdateNetworkMigrationMapperSegment-response-updatedAt"></a>
The timestamp when the segment was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateNetworkMigrationMapperSegment_Errors"></a>

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
<a name="API_UpdateNetworkMigrationMapperSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UpdateNetworkMigrationMapperSegment)
