---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetEncryptionConfiguration.html
---

# GetEncryptionConfiguration
<a name="API_GetEncryptionConfiguration"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Retrieves the encryption configuration for resources and data in AWS IoT FleetWise.

## Response Syntax
<a name="API_GetEncryptionConfiguration_ResponseSyntax"></a>

```
{
   "creationTime": number,
   "encryptionStatus": "string",
   "encryptionType": "string",
   "errorMessage": "string",
   "kmsKeyId": "string",
   "lastModificationTime": number
}
```

## Response Elements
<a name="API_GetEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-GetEncryptionConfiguration-response-creationTime"></a>
The time when encryption was configured in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [encryptionStatus](#API_GetEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-GetEncryptionConfiguration-response-encryptionStatus"></a>
The encryption status.
Type: String
Valid Values: `PENDING | SUCCESS | FAILURE`

 ** [encryptionType](#API_GetEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-GetEncryptionConfiguration-response-encryptionType"></a>
The type of encryption. Set to `KMS_BASED_ENCRYPTION` to use a KMS key that you own and manage. Set to `FLEETWISE_DEFAULT_ENCRYPTION` to use an AWS managed key that is owned by the AWS IoT FleetWise service account.
Type: String
Valid Values: `KMS_BASED_ENCRYPTION | FLEETWISE_DEFAULT_ENCRYPTION`

 ** [errorMessage](#API_GetEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-GetEncryptionConfiguration-response-errorMessage"></a>
The error message that describes why encryption settings couldn't be configured, if applicable.
Type: String

 ** [kmsKeyId](#API_GetEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-GetEncryptionConfiguration-response-kmsKeyId"></a>
The ID of the KMS key that is used for encryption.
Type: String

 ** [lastModificationTime](#API_GetEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-GetEncryptionConfiguration-response-lastModificationTime"></a>
The time when encryption was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

## Errors
<a name="API_GetEncryptionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetEncryptionConfiguration)
