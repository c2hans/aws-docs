---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_GetDbServer.html
---

# GetDbServer
<a name="API_GetDbServer"></a>

Returns information about the specified database server.

## Request Syntax
<a name="API_GetDbServer_RequestSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "{{string}}",
   "dbServerId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDbServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudExadataInfrastructureId](#API_GetDbServer_RequestSyntax) **   <a name="odb-GetDbServer-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Oracle Exadata infrastructure that contains the database server.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [dbServerId](#API_GetDbServer_RequestSyntax) **   <a name="odb-GetDbServer-request-dbServerId"></a>
The unique identifier of the database server to retrieve information about.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

## Response Syntax
<a name="API_GetDbServer_ResponseSyntax"></a>

```
{
   "dbServer": {
      "autonomousVirtualMachineIds": [ "string" ],
      "autonomousVmClusterIds": [ "string" ],
      "computeModel": "string",
      "cpuCoreCount": number,
      "createdAt": "string",
      "dbNodeStorageSizeInGBs": number,
      "dbServerId": "string",
      "dbServerPatchingDetails": {
         "estimatedPatchDuration": number,
         "patchingStatus": "string",
         "timePatchingEnded": "string",
         "timePatchingStarted": "string"
      },
      "displayName": "string",
      "exadataInfrastructureId": "string",
      "maxCpuCount": number,
      "maxDbNodeStorageInGBs": number,
      "maxMemoryInGBs": number,
      "memorySizeInGBs": number,
      "ocid": "string",
      "ociResourceAnchorName": "string",
      "shape": "string",
      "status": "string",
      "statusReason": "string",
      "vmClusterIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetDbServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbServer](#API_GetDbServer_ResponseSyntax) **   <a name="odb-GetDbServer-response-dbServer"></a>
The details of the requested database server.
Type: [DbServer](API_DbServer.md) object

## Errors
<a name="API_GetDbServer_Errors"></a>

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
<a name="API_GetDbServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/GetDbServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/GetDbServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/GetDbServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/GetDbServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/GetDbServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/GetDbServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/GetDbServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/GetDbServer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/GetDbServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/GetDbServer)
