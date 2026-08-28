---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html
---

# PutMessagingStreamingConfigurations
<a name="API_messaging-chime_PutMessagingStreamingConfigurations"></a>

Sets the data streaming configuration for an `AppInstance`. For more information, see [Streaming messaging data](https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html) in the *Amazon Chime SDK Developer Guide*.

## Request Syntax
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_RequestSyntax"></a>

```
PUT /app-instances/{{appInstanceArn}}/streaming-configurations HTTP/1.1
Content-type: application/json

{
   "StreamingConfigurations": [
      {
         "DataType": "{{string}}",
         "ResourceArn": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceArn](#API_messaging-chime_PutMessagingStreamingConfigurations_RequestSyntax) **   <a name="chimesdk-messaging-chime_PutMessagingStreamingConfigurations-request-uri-AppInstanceArn"></a>
The ARN of the streaming configuration.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StreamingConfigurations](#API_messaging-chime_PutMessagingStreamingConfigurations_RequestSyntax) **   <a name="chimesdk-messaging-chime_PutMessagingStreamingConfigurations-request-StreamingConfigurations"></a>
The streaming configurations.
Type: Array of [StreamingConfiguration](API_messaging-chime_StreamingConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## Response Syntax
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamingConfigurations": [
      {
         "DataType": "string",
         "ResourceArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamingConfigurations](#API_messaging-chime_PutMessagingStreamingConfigurations_ResponseSyntax) **   <a name="chimesdk-messaging-chime_PutMessagingStreamingConfigurations-response-StreamingConfigurations"></a>
The requested streaming configurations.
Type: Array of [StreamingConfiguration](API_messaging-chime_StreamingConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

## Errors
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

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
<a name="API_messaging-chime_PutMessagingStreamingConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/PutMessagingStreamingConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
