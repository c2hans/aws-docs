---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateVPCConnection.html
---

# UpdateVPCConnection
<a name="API_UpdateVPCConnection"></a>

Updates a VPC connection.

## Request Syntax
<a name="API_UpdateVPCConnection_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/vpc-connections/{{VPCConnectionId}} HTTP/1.1
Content-type: application/json

{
   "DnsResolvers": [ "{{string}}" ],
   "Name": "{{string}}",
   "RoleArn": "{{string}}",
   "SecurityGroupIds": [ "{{string}}" ],
   "SubnetIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateVPCConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-uri-AwsAccountId"></a>
The AWS account ID of the account that contains the VPC connection that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [VPCConnectionId](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-uri-VPCConnectionId"></a>
The ID of the VPC connection that you're updating. This ID is a unique identifier for each AWS Region in an AWS account.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_UpdateVPCConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-Name"></a>
The display name for the VPC connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [RoleArn](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-RoleArn"></a>
An IAM role associated with the VPC connection.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [SecurityGroupIds](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-SecurityGroupIds"></a>
A list of security group IDs for the VPC connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^sg-[0-9a-z]*$`
Required: Yes

 ** [SubnetIds](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-SubnetIds"></a>
A list of subnet IDs for the VPC connection.
Type: Array of strings
Array Members: Minimum number of 2 items. Maximum number of 15 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^subnet-[0-9a-z]*$`
Required: Yes

 ** [DnsResolvers](#API_UpdateVPCConnection_RequestSyntax) **   <a name="QS-UpdateVPCConnection-request-DnsResolvers"></a>
A list of IP addresses of DNS resolver endpoints for the VPC connection.
Type: Array of strings
Array Members: Maximum number of 15 items.
Length Constraints: Minimum length of 7. Maximum length of 15.
Required: No

## Response Syntax
<a name="API_UpdateVPCConnection_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AvailabilityStatus": "string",
   "RequestId": "string",
   "UpdateStatus": "string",
   "VPCConnectionId": "string"
}
```

## Response Elements
<a name="API_UpdateVPCConnection_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateVPCConnection_ResponseSyntax) **   <a name="QS-UpdateVPCConnection-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateVPCConnection_ResponseSyntax) **   <a name="QS-UpdateVPCConnection-response-Arn"></a>
The Amazon Resource Name (ARN) of the VPC connection.
Type: String

 ** [AvailabilityStatus](#API_UpdateVPCConnection_ResponseSyntax) **   <a name="QS-UpdateVPCConnection-response-AvailabilityStatus"></a>
The availability status of the VPC connection.
Type: String
Valid Values: `AVAILABLE | UNAVAILABLE | PARTIALLY_AVAILABLE`

 ** [RequestId](#API_UpdateVPCConnection_ResponseSyntax) **   <a name="QS-UpdateVPCConnection-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [UpdateStatus](#API_UpdateVPCConnection_ResponseSyntax) **   <a name="QS-UpdateVPCConnection-response-UpdateStatus"></a>
The update status of the VPC connection's last update.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETION_IN_PROGRESS | DELETION_FAILED | DELETED`

 ** [VPCConnectionId](#API_UpdateVPCConnection_ResponseSyntax) **   <a name="QS-UpdateVPCConnection-response-VPCConnectionId"></a>
The ID of the VPC connection that you are updating. This ID is a unique identifier for each AWS Region in anAWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_UpdateVPCConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateVPCConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateVPCConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateVPCConnection)
