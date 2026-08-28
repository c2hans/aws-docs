---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.html
---

# AdminListDevices
<a name="API_AdminListDevices"></a>

Lists a user's registered devices. Remembered devices are used in authentication services where you offer a "Remember me" option for users who you want to permit to sign in without MFA from a trusted device. Users can bypass MFA while your application performs device SRP authentication on the back end. For more information, see [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminListDevices_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "PaginationToken": "{{string}}",
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminListDevices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_AdminListDevices_RequestSyntax) **   <a name="CognitoUserPools-AdminListDevices-request-Limit"></a>
The maximum number of devices that you want Amazon Cognito to return in the response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** [PaginationToken](#API_AdminListDevices_RequestSyntax) **   <a name="CognitoUserPools-AdminListDevices-request-PaginationToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`
Required: No

 ** [Username](#API_AdminListDevices_RequestSyntax) **   <a name="CognitoUserPools-AdminListDevices-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminListDevices_RequestSyntax) **   <a name="CognitoUserPools-AdminListDevices-request-UserPoolId"></a>
The ID of the user pool where the device owner is a user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_AdminListDevices_ResponseSyntax"></a>

```
{
   "Devices": [
      {
         "DeviceAttributes": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "DeviceCreateDate": number,
         "DeviceKey": "string",
         "DeviceLastAuthenticatedDate": number,
         "DeviceLastModifiedDate": number
      }
   ],
   "PaginationToken": "string"
}
```

## Response Elements
<a name="API_AdminListDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Devices](#API_AdminListDevices_ResponseSyntax) **   <a name="CognitoUserPools-AdminListDevices-response-Devices"></a>
An array of devices and their information. Each entry that's returned includes device information, last-accessed and created dates, and the device key.
Type: Array of [DeviceType](API_DeviceType.md) objects

 ** [PaginationToken](#API_AdminListDevices_ResponseSyntax) **   <a name="CognitoUserPools-AdminListDevices-response-PaginationToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`

## Errors
<a name="API_AdminListDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** InvalidUserPoolConfigurationException **
This exception is thrown when the user pool configuration is not valid.
 ** message **
The message returned when the user pool configuration is not valid.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_AdminListDevices_Examples"></a>

### Example
<a name="API_AdminListDevices_Example_1"></a>

The following example API request retrieves information about the first two devices that belong to the user "testuser."

#### Sample Request
<a name="API_AdminListDevices_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminListDevices
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser" ,
  "Limit": 2
}
```

#### Sample Response
<a name="API_AdminListDevices_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
	"Devices": [
		{
			"DeviceAttributes": [
				{
					"Name": "device_status",
					"Value": "valid"
				},
				{
					"Name": "device_name",
					"Value": "Dart-device"
				},
				{
					"Name": "dev:device_arn",
					"Value": "arn:aws:cognito-idp:us-west-2:123456789012:owner/testuser.us-west-2_EXAMPLE/device/us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
				},
				{
					"Name": "dev:device_owner",
					"Value": "testuser.us-west-2_EXAMPLE"
				},
				{
					"Name": "last_ip_used",
					"Value": "192.0.2.1"
				},
				{
					"Name": "dev:device_remembered_status",
					"Value": "remembered"
				},
				{
					"Name": "dev:device_sdk",
					"Value": "aws-sdk-unknown-unknown"
				}
			],
			"DeviceCreateDate": 1715100742.022,
			"DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
			"DeviceLastAuthenticatedDate": 1715100742.0,
			"DeviceLastModifiedDate": 1715100742.022
		},
		{
			"DeviceAttributes": [
				{
					"Name": "device_status",
					"Value": "valid"
				},
				{
					"Name": "device_name",
					"Value": "Mobile-device"
				},
				{
					"Name": "dev:device_arn",
					"Value": "arn:aws:cognito-idp:us-west-2:123456789012:owner/testuser.us-west-2_EXAMPLE/device/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
				},
				{
					"Name": "dev:device_owner",
					"Value": "testuser.us-west-2_EXAMPLE"
				},
				{
					"Name": "last_ip_used",
					"Value": "192.0.2.99"
				},
				{
					"Name": "dev:device_remembered_status",
					"Value": "remembered"
				},
				{
					"Name": "dev:device_sdk",
					"Value": "aws-sdk-unknown-unknown"
				}
			],
			"DeviceCreateDate": 1715100742.022,
			"DeviceKey": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
			"DeviceLastAuthenticatedDate": 1715100742.0,
			"DeviceLastModifiedDate": 1715100742.022
		}
	]
}
```

## See Also
<a name="API_AdminListDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminListDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminListDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
