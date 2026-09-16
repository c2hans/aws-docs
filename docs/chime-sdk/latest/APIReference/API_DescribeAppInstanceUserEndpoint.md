---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceUserEndpoint.html
---

# DescribeAppInstanceUserEndpoint
<a name="API_DescribeAppInstanceUserEndpoint"></a>

Returns the full details of an `AppInstanceUserEndpoint`.

## Request Syntax
<a name="API_DescribeAppInstanceUserEndpoint_RequestSyntax"></a>

```
GET /app-instance-users/{{appInstanceUserArn}}/endpoints/{{endpointId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAppInstanceUserEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceUserArn](#API_DescribeAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-DescribeAppInstanceUserEndpoint-request-uri-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `.*`
Required: Yes

 ** [endpointId](#API_DescribeAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-DescribeAppInstanceUserEndpoint-request-uri-EndpointId"></a>
The unique identifier of the `AppInstanceUserEndpoint`.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `.*`
Required: Yes

## Request Body
<a name="API_DescribeAppInstanceUserEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAppInstanceUserEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceUserEndpoint": {
      "AllowMessages": "string",
      "AppInstanceUserArn": "string",
      "CreatedTimestamp": number,
      "EndpointAttributes": {
         "DeviceToken": "string",
         "VoipDeviceToken": "string"
      },
      "EndpointId": "string",
      "EndpointState": {
         "Status": "string",
         "StatusReason": "string"
      },
      "LastUpdatedTimestamp": number,
      "Name": "string",
      "ResourceArn": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeAppInstanceUserEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceUserEndpoint](#API_DescribeAppInstanceUserEndpoint_ResponseSyntax) **   <a name="chimesdk-DescribeAppInstanceUserEndpoint-response-AppInstanceUserEndpoint"></a>
The full details of an `AppInstanceUserEndpoint`: the `AppInstanceUserArn`, ID, name, type, resource ARN, attributes, allow messages, state, and created and last updated timestamps. All timestamps use epoch milliseconds.
Type: [AppInstanceUserEndpoint](API_AppInstanceUserEndpoint.md) object

## Errors
<a name="API_DescribeAppInstanceUserEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_DescribeAppInstanceUserEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/DescribeAppInstanceUserEndpoint)
