---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetRegisterAccountStatus.html
---

# GetRegisterAccountStatus
<a name="API_GetRegisterAccountStatus"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Retrieves information about the status of registering your AWS account, IAM, and Amazon Timestream resources so that AWS IoT FleetWise can transfer your vehicle data to the AWS Cloud.

For more information, including step-by-step procedures, see [Setting up AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html).

**Note**
This API operation doesn't require input parameters.

## Response Syntax
<a name="API_GetRegisterAccountStatus_ResponseSyntax"></a>

```
{
   "accountStatus": "string",
   "creationTime": number,
   "customerAccountId": "string",
   "iamRegistrationResponse": {
      "errorMessage": "string",
      "registrationStatus": "string",
      "roleArn": "string"
   },
   "lastModificationTime": number,
   "timestreamRegistrationResponse": {
      "errorMessage": "string",
      "registrationStatus": "string",
      "timestreamDatabaseArn": "string",
      "timestreamDatabaseName": "string",
      "timestreamTableArn": "string",
      "timestreamTableName": "string"
   }
}
```

## Response Elements
<a name="API_GetRegisterAccountStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountStatus](#API_GetRegisterAccountStatus_ResponseSyntax) **   <a name="iotfleetwise-GetRegisterAccountStatus-response-accountStatus"></a>
 The status of registering your account and resources. The status can be one of:
+  `REGISTRATION_SUCCESS` - The AWS resource is successfully registered.
+  `REGISTRATION_PENDING` - AWS IoT FleetWise is processing the registration request. This process takes approximately five minutes to complete.
+  `REGISTRATION_FAILURE` - AWS IoT FleetWise can't register the AWS resource. Try again later.
Type: String
Valid Values: `REGISTRATION_PENDING | REGISTRATION_SUCCESS | REGISTRATION_FAILURE`

 ** [creationTime](#API_GetRegisterAccountStatus_ResponseSyntax) **   <a name="iotfleetwise-GetRegisterAccountStatus-response-creationTime"></a>
 The time the account was registered, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [customerAccountId](#API_GetRegisterAccountStatus_ResponseSyntax) **   <a name="iotfleetwise-GetRegisterAccountStatus-response-customerAccountId"></a>
 The unique ID of the AWS account, provided at account creation.
Type: String

 ** [iamRegistrationResponse](#API_GetRegisterAccountStatus_ResponseSyntax) **   <a name="iotfleetwise-GetRegisterAccountStatus-response-iamRegistrationResponse"></a>
 Information about the registered IAM resources or errors, if any.
Type: [IamRegistrationResponse](API_IamRegistrationResponse.md) object

 ** [lastModificationTime](#API_GetRegisterAccountStatus_ResponseSyntax) **   <a name="iotfleetwise-GetRegisterAccountStatus-response-lastModificationTime"></a>
 The time this registration was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [timestreamRegistrationResponse](#API_GetRegisterAccountStatus_ResponseSyntax) **   <a name="iotfleetwise-GetRegisterAccountStatus-response-timestreamRegistrationResponse"></a>
 Information about the registered Amazon Timestream resources or errors, if any.
Type: [TimestreamRegistrationResponse](API_TimestreamRegistrationResponse.md) object

## Errors
<a name="API_GetRegisterAccountStatus_Errors"></a>

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
<a name="API_GetRegisterAccountStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetRegisterAccountStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetRegisterAccountStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
