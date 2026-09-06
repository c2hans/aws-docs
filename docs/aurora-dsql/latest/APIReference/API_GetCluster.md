---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetCluster.html
---

# GetCluster
<a name="API_GetCluster"></a>

Retrieves information about a cluster.

## Request Syntax
<a name="API_GetCluster_RequestSyntax"></a>

```
GET /cluster/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_GetCluster_RequestSyntax) **   <a name="auroradsql-GetCluster-request-uri-identifier"></a>
The ID of the cluster to retrieve.
Pattern: `[a-z0-9]{26}`
Required: Yes

## Request Body
<a name="API_GetCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCluster_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": number,
   "deletionProtectionEnabled": boolean,
   "encryptionDetails": {
      "encryptionStatus": "string",
      "encryptionType": "string",
      "kmsKeyArn": "string"
   },
   "endpoint": "string",
   "identifier": "string",
   "multiRegionProperties": {
      "clusters": [ "string" ],
      "witnessRegion": "string"
   },
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-arn"></a>
The ARN of the retrieved cluster.
Type: String
Pattern: `arn:aws(-[^:]+)?:dsql:[a-z0-9-]{1,20}:[0-9]{12}:cluster/[a-z0-9]{26}`

 ** [creationTime](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-creationTime"></a>
The time of when the cluster was created.
Type: Timestamp

 ** [deletionProtectionEnabled](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-deletionProtectionEnabled"></a>
Whether deletion protection is enabled in this cluster.
Type: Boolean

 ** [encryptionDetails](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-encryptionDetails"></a>
The current encryption configuration details for the cluster.
Type: [EncryptionDetails](API_EncryptionDetails.md) object

 ** [endpoint](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-endpoint"></a>
The connection endpoint for the cluster.
Type: String
Pattern: `[a-zA-Z0-9.-]+`

 ** [identifier](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-identifier"></a>
The ID of the retrieved cluster.
Type: String
Pattern: `[a-z0-9]{26}`

 ** [multiRegionProperties](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-multiRegionProperties"></a>
Returns the current multi-Region cluster configuration, including witness region and linked cluster information.
Type: [MultiRegionProperties](API_MultiRegionProperties.md) object

 ** [status](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-status"></a>
The status of the retrieved cluster.
Type: String
Valid Values: `CREATING | ACTIVE | IDLE | INACTIVE | UPDATING | DELETING | DELETED | FAILED | PENDING_SETUP | PENDING_DELETE`

 ** [tags](#API_GetCluster_ResponseSyntax) **   <a name="auroradsql-GetCluster-response-tags"></a>
Map of tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.:/=+\-@ ]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9_.:/=+\-@ ]*`

## Errors
<a name="API_GetCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
Retry after seconds.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceId **
The resource ID could not be found.
 ** resourceType **
The resource type could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
The message that the request was denied due to request throttling.
 ** quotaCode **
The request exceeds a request rate quota.
 ** retryAfterSeconds **
The request exceeds a request rate quota. Retry after seconds.
 ** serviceCode **
The request exceeds a service quota.
HTTP Status Code: 429

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dsql-2018-05-10/GetCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dsql-2018-05-10/GetCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/GetCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dsql-2018-05-10/GetCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/GetCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dsql-2018-05-10/GetCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dsql-2018-05-10/GetCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dsql-2018-05-10/GetCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dsql-2018-05-10/GetCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/GetCluster)
