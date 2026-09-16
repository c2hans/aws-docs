---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_RegisterAccount.html
---

# RegisterAccount
<a name="API_RegisterAccount"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

**Important**
This API operation contains deprecated parameters. Register your account again without the Timestream resources parameter so that AWS IoT FleetWise can remove the Timestream metadata stored. You should then pass the data destination into the [CreateCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateCampaign.html) API operation.
You must delete any existing campaigns that include an empty data destination before you register your account again. For more information, see the [DeleteCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteCampaign.html) API operation.
If you want to delete the Timestream inline policy from the service-linked role, such as to mitigate an overly permissive policy, you must first delete any existing campaigns. Then delete the service-linked role and register your account again to enable CloudWatch metrics. For more information, see [DeleteServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html) in the * AWS Identity and Access Management API Reference*.

Registers your AWS account, IAM, and Amazon Timestream resources so AWS IoT FleetWise can transfer your vehicle data to the AWS Cloud. For more information, including step-by-step procedures, see [Setting up AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html).

**Note**
An AWS account is **not** the same thing as a "user." An [AWS user](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html#intro-identity-users) is an identity that you create using AWS Identity and Access Management (IAM) and takes the form of either an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) or an [IAM role, both with credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). A single AWS account can, and typically does, contain many users and roles.

## Request Syntax
<a name="API_RegisterAccount_RequestSyntax"></a>

```
{
   "iamResources": {
      "roleArn": "{{string}}"
   },
   "timestreamResources": {
      "timestreamDatabaseName": "{{string}}",
      "timestreamTableName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_RegisterAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [iamResources](#API_RegisterAccount_RequestSyntax) **   <a name="iotfleetwise-RegisterAccount-request-iamResources"></a>
 *This parameter has been deprecated.*
The IAM resource that allows AWS IoT FleetWise to send data to Amazon Timestream.
Type: [IamResources](API_IamResources.md) object
Required: No

 ** [timestreamResources](#API_RegisterAccount_RequestSyntax) **   <a name="iotfleetwise-RegisterAccount-request-timestreamResources"></a>
 *This parameter has been deprecated.*
The registered Amazon Timestream resources that AWS IoT FleetWise edge agent software can transfer your vehicle data to.
Type: [TimestreamResources](API_TimestreamResources.md) object
Required: No

## Response Syntax
<a name="API_RegisterAccount_ResponseSyntax"></a>

```
{
   "creationTime": number,
   "iamResources": {
      "roleArn": "string"
   },
   "lastModificationTime": number,
   "registerAccountStatus": "string",
   "timestreamResources": {
      "timestreamDatabaseName": "string",
      "timestreamTableName": "string"
   }
}
```

## Response Elements
<a name="API_RegisterAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_RegisterAccount_ResponseSyntax) **   <a name="iotfleetwise-RegisterAccount-response-creationTime"></a>
 The time the account was registered, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [iamResources](#API_RegisterAccount_ResponseSyntax) **   <a name="iotfleetwise-RegisterAccount-response-iamResources"></a>
 The registered IAM resource that allows AWS IoT FleetWise to send data to Amazon Timestream.
Type: [IamResources](API_IamResources.md) object

 ** [lastModificationTime](#API_RegisterAccount_ResponseSyntax) **   <a name="iotfleetwise-RegisterAccount-response-lastModificationTime"></a>
 The time this registration was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [registerAccountStatus](#API_RegisterAccount_ResponseSyntax) **   <a name="iotfleetwise-RegisterAccount-response-registerAccountStatus"></a>
 The status of registering your AWS account, IAM role, and Timestream resources.
Type: String
Valid Values: `REGISTRATION_PENDING | REGISTRATION_SUCCESS | REGISTRATION_FAILURE`

 ** [timestreamResources](#API_RegisterAccount_ResponseSyntax) **   <a name="iotfleetwise-RegisterAccount-response-timestreamResources"></a>
The registered Amazon Timestream resources that AWS IoT FleetWise edge agent software can transfer your vehicle data to.
Type: [TimestreamResources](API_TimestreamResources.md) object

## Errors
<a name="API_RegisterAccount_Errors"></a>

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
<a name="API_RegisterAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/RegisterAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/RegisterAccount)
