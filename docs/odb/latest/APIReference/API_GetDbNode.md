---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_GetDbNode.html
---

# GetDbNode
<a name="API_GetDbNode"></a>

Returns information about the specified DB node.

## Request Syntax
<a name="API_GetDbNode_RequestSyntax"></a>

```
{
   "cloudVmClusterId": "{{string}}",
   "dbNodeId": "{{string}}",
   "exadbVmClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDbNode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudVmClusterId](#API_GetDbNode_RequestSyntax) **   <a name="odb-GetDbNode-request-cloudVmClusterId"></a>
The unique identifier of the VM cluster that contains the DB node. You must specify either this parameter or `exadbVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** [dbNodeId](#API_GetDbNode_RequestSyntax) **   <a name="odb-GetDbNode-request-dbNodeId"></a>
The unique identifier of the DB node to retrieve information about.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [exadbVmClusterId](#API_GetDbNode_RequestSyntax) **   <a name="odb-GetDbNode-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster that contains the DB node. You must specify either this parameter or `cloudVmClusterId`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

## Response Syntax
<a name="API_GetDbNode_ResponseSyntax"></a>

```
{
   "dbNode": {
      "additionalDetails": "string",
      "backupIpId": "string",
      "backupVnic2Id": "string",
      "backupVnicId": "string",
      "cpuCoreCount": number,
      "createdAt": "string",
      "dbNodeArn": "string",
      "dbNodeId": "string",
      "dbNodeStorageSizeInGBs": number,
      "dbServerId": "string",
      "dbSystemId": "string",
      "faultDomain": "string",
      "floatingIpAddress": "string",
      "hostIpId": "string",
      "hostname": "string",
      "maintenanceType": "string",
      "memorySizeInGBs": number,
      "ocid": "string",
      "ociResourceAnchorName": "string",
      "privateIpAddress": "string",
      "softwareStorageSizeInGB": number,
      "status": "string",
      "statusReason": "string",
      "timeMaintenanceWindowEnd": "string",
      "timeMaintenanceWindowStart": "string",
      "totalCpuCoreCount": number,
      "vnic2Id": "string",
      "vnicId": "string"
   }
}
```

## Response Elements
<a name="API_GetDbNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbNode](#API_GetDbNode_ResponseSyntax) **   <a name="odb-GetDbNode-response-dbNode"></a>
Information about a DB node.
Type: [DbNode](API_DbNode.md) object

## Errors
<a name="API_GetDbNode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_GetDbNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/GetDbNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/GetDbNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/GetDbNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/GetDbNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/GetDbNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/GetDbNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/GetDbNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/GetDbNode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/GetDbNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/GetDbNode)
