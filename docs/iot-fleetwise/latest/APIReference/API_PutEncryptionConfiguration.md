---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_PutEncryptionConfiguration.html
---

# PutEncryptionConfiguration
<a name="API_PutEncryptionConfiguration"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Creates or updates the encryption configuration. AWS IoT FleetWise can encrypt your data and resources using an AWS managed key. Or, you can use a KMS key that you own and manage. For more information, see [Data encryption](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/data-encryption.html) in the * AWS IoT FleetWise Developer Guide*.

## Request Syntax
<a name="API_PutEncryptionConfiguration_RequestSyntax"></a>

```
{
   "encryptionType": "{{string}}",
   "kmsKeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutEncryptionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [encryptionType](#API_PutEncryptionConfiguration_RequestSyntax) **   <a name="iotfleetwise-PutEncryptionConfiguration-request-encryptionType"></a>
The type of encryption. Choose `KMS_BASED_ENCRYPTION` to use a KMS key or `FLEETWISE_DEFAULT_ENCRYPTION` to use an AWS managed key.
Type: String
Valid Values: `KMS_BASED_ENCRYPTION | FLEETWISE_DEFAULT_ENCRYPTION`
Required: Yes

 ** [kmsKeyId](#API_PutEncryptionConfiguration_RequestSyntax) **   <a name="iotfleetwise-PutEncryptionConfiguration-request-kmsKeyId"></a>
The ID of the KMS key that is used for encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_PutEncryptionConfiguration_ResponseSyntax"></a>

```
{
   "encryptionStatus": "string",
   "encryptionType": "string",
   "kmsKeyId": "string"
}
```

## Response Elements
<a name="API_PutEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [encryptionStatus](#API_PutEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-PutEncryptionConfiguration-response-encryptionStatus"></a>
The encryption status.
Type: String
Valid Values: `PENDING | SUCCESS | FAILURE`

 ** [encryptionType](#API_PutEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-PutEncryptionConfiguration-response-encryptionType"></a>
The type of encryption. Set to `KMS_BASED_ENCRYPTION` to use an KMS key that you own and manage. Set to `FLEETWISE_DEFAULT_ENCRYPTION` to use an AWS managed key that is owned by the AWS IoT FleetWise service account.
Type: String
Valid Values: `KMS_BASED_ENCRYPTION | FLEETWISE_DEFAULT_ENCRYPTION`

 ** [kmsKeyId](#API_PutEncryptionConfiguration_ResponseSyntax) **   <a name="iotfleetwise-PutEncryptionConfiguration-response-kmsKeyId"></a>
The ID of the KMS key that is used for encryption.
Type: String

## Errors
<a name="API_PutEncryptionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resource **
The resource on which there are conflicting operations.
 ** resourceType **
The type of resource on which there are conflicting operations..
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
<a name="API_PutEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/PutEncryptionConfiguration)
