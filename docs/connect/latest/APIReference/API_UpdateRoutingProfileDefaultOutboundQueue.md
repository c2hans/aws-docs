---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateRoutingProfileDefaultOutboundQueue.html
---

# UpdateRoutingProfileDefaultOutboundQueue
<a name="API_UpdateRoutingProfileDefaultOutboundQueue"></a>

Updates the default outbound queue of a routing profile.

## Request Syntax
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_RequestSyntax"></a>

```
POST /routing-profiles/{{InstanceId}}/{{RoutingProfileId}}/default-outbound-queue HTTP/1.1
Content-type: application/json

{
   "DefaultOutboundQueueId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateRoutingProfileDefaultOutboundQueue_RequestSyntax) **   <a name="connect-UpdateRoutingProfileDefaultOutboundQueue-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [RoutingProfileId](#API_UpdateRoutingProfileDefaultOutboundQueue_RequestSyntax) **   <a name="connect-UpdateRoutingProfileDefaultOutboundQueue-request-uri-RoutingProfileId"></a>
The identifier of the routing profile.
Required: Yes

## Request Body
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DefaultOutboundQueueId](#API_UpdateRoutingProfileDefaultOutboundQueue_RequestSyntax) **   <a name="connect-UpdateRoutingProfileDefaultOutboundQueue-request-DefaultOutboundQueueId"></a>
The identifier for the default outbound queue.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_Errors"></a>

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
<a name="API_UpdateRoutingProfileDefaultOutboundQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateRoutingProfileDefaultOutboundQueue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
