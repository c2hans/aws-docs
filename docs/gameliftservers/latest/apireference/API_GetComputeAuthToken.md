---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAuthToken.html
---

# GetComputeAuthToken
<a name="API_GetComputeAuthToken"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Requests an authentication token from Amazon GameLift Servers for a compute resource in an Amazon GameLift Servers fleet. Game servers that are running on the compute use this token to communicate with the Amazon GameLift Servers service, such as when calling the Amazon GameLift Servers server SDK action `InitSDK()`. Authentication tokens are valid for a limited time span, so you need to request a fresh token before the current token expires.

 **Request options**
+ For managed EC2 fleets (compute type `EC2`), auth token retrieval and refresh is handled automatically. All game servers that are running on all fleet instances have access to a valid auth token.
+ For Anywhere fleets (compute type `ANYWHERE`), if you're using the Amazon GameLift Servers Agent, auth token retrieval and refresh is handled automatically for any compute where the Agent is running. If you're not using the Agent, create a mechanism to retrieve and refresh auth tokens for computes that are running game server processes.
+ For managed container fleets, if you're using the Amazon GameLift Servers Agent, auth token retrieval and refresh is handled automatically for any container or Anywhere compute where the Agent is running. If you're not using the Agent, use the alternative authentication method instead of using this operation.

 **Learn more**
+  [Create an Anywhere fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html)
+  [Test your integration](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-testing.html)
+  [Server SDK reference guides](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html) (for version 5.x)

## Request Syntax
<a name="API_GetComputeAuthToken_RequestSyntax"></a>

```
{
   "ComputeName": "{{string}}",
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComputeAuthToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ComputeName](#API_GetComputeAuthToken_RequestSyntax) **   <a name="gameliftservers-GetComputeAuthToken-request-ComputeName"></a>
The name of the compute resource you are requesting the authentication token for. For an Anywhere fleet compute, use the registered compute name. For an EC2 fleet instance, use the instance ID.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: Yes

 ** [FleetId](#API_GetComputeAuthToken_RequestSyntax) **   <a name="gameliftservers-GetComputeAuthToken-request-FleetId"></a>
A unique identifier for the fleet that the compute is registered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Syntax
<a name="API_GetComputeAuthToken_ResponseSyntax"></a>

```
{
   "AuthToken": "string",
   "ComputeArn": "string",
   "ComputeName": "string",
   "ExpirationTimestamp": number,
   "FleetArn": "string",
   "FleetId": "string"
}
```

## Response Elements
<a name="API_GetComputeAuthToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthToken](#API_GetComputeAuthToken_ResponseSyntax) **   <a name="gameliftservers-GetComputeAuthToken-response-AuthToken"></a>
A valid temporary authentication token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9\-]+`

 ** [ComputeArn](#API_GetComputeAuthToken_ResponseSyntax) **   <a name="gameliftservers-GetComputeAuthToken-response-ComputeArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to an Amazon GameLift Servers compute resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::compute/compute-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`

 ** [ComputeName](#API_GetComputeAuthToken_ResponseSyntax) **   <a name="gameliftservers-GetComputeAuthToken-response-ComputeName"></a>
The name of the compute resource that the authentication token is issued to.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`

 ** [ExpirationTimestamp](#API_GetComputeAuthToken_ResponseSyntax) **   <a name="gameliftservers-GetComputeAuthToken-response-ExpirationTimestamp"></a>
The amount of time until the authentication token is no longer valid.
Type: Timestamp

 ** [FleetArn](#API_GetComputeAuthToken_ResponseSyntax) **   <a name="gameliftservers-GetComputeAuthToken-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_GetComputeAuthToken_ResponseSyntax) **   <a name="gameliftservers-GetComputeAuthToken-response-FleetId"></a>
A unique identifier for the fleet that the compute is registered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

## Errors
<a name="API_GetComputeAuthToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_GetComputeAuthToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/GetComputeAuthToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GetComputeAuthToken)
