---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeAuthenticationProfile.html
---

# DescribeAuthenticationProfile
<a name="API_DescribeAuthenticationProfile"></a>

This API is in preview release for Connect Customer and is subject to change. To request access to this API, contact Support.

Describes the target authentication profile.

## Request Syntax
<a name="API_DescribeAuthenticationProfile_RequestSyntax"></a>

```
GET /authentication-profiles/{{InstanceId}}/{{AuthenticationProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAuthenticationProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AuthenticationProfileId](#API_DescribeAuthenticationProfile_RequestSyntax) **   <a name="connect-DescribeAuthenticationProfile-request-uri-AuthenticationProfileId"></a>
A unique identifier for the authentication profile.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [InstanceId](#API_DescribeAuthenticationProfile_RequestSyntax) **   <a name="connect-DescribeAuthenticationProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeAuthenticationProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAuthenticationProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthenticationProfile": {
      "AllowedIps": [ "string" ],
      "Arn": "string",
      "BlockedIps": [ "string" ],
      "CreatedTime": number,
      "Description": "string",
      "Id": "string",
      "IsDefault": boolean,
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "MaxSessionDuration": number,
      "Name": "string",
      "PeriodicSessionDuration": number,
      "SessionInactivityDuration": number,
      "SessionInactivityHandlingEnabled": boolean
   }
}
```

## Response Elements
<a name="API_DescribeAuthenticationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationProfile](#API_DescribeAuthenticationProfile_ResponseSyntax) **   <a name="connect-DescribeAuthenticationProfile-response-AuthenticationProfile"></a>
The authentication profile object being described.
Type: [AuthenticationProfile](API_AuthenticationProfile.md) object

## Errors
<a name="API_DescribeAuthenticationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeAuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeAuthenticationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeAuthenticationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
