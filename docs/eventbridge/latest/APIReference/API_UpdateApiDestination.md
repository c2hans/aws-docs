---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateApiDestination.html
---

# UpdateApiDestination
<a name="API_UpdateApiDestination"></a>

Updates an API destination.

## Request Syntax
<a name="API_UpdateApiDestination_RequestSyntax"></a>

```
{
   "ConnectionArn": "{{string}}",
   "Description": "{{string}}",
   "HttpMethod": "{{string}}",
   "InvocationEndpoint": "{{string}}",
   "InvocationRateLimitPerSecond": {{number}},
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApiDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_UpdateApiDestination_RequestSyntax) **   <a name="eventbridge-UpdateApiDestination-request-ConnectionArn"></a>
The ARN of the connection to use for the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`
Required: No

 ** [Description](#API_UpdateApiDestination_RequestSyntax) **   <a name="eventbridge-UpdateApiDestination-request-Description"></a>
The name of the API destination to update.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [HttpMethod](#API_UpdateApiDestination_RequestSyntax) **   <a name="eventbridge-UpdateApiDestination-request-HttpMethod"></a>
The method to use for the API destination.
Type: String
Valid Values: `POST | GET | HEAD | OPTIONS | PUT | PATCH | DELETE`
Required: No

 ** [InvocationEndpoint](#API_UpdateApiDestination_RequestSyntax) **   <a name="eventbridge-UpdateApiDestination-request-InvocationEndpoint"></a>
The URL to the endpoint to use for the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`
Required: No

 ** [InvocationRateLimitPerSecond](#API_UpdateApiDestination_RequestSyntax) **   <a name="eventbridge-UpdateApiDestination-request-InvocationRateLimitPerSecond"></a>
The maximum number of invocations per second to send to the API destination.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Name](#API_UpdateApiDestination_RequestSyntax) **   <a name="eventbridge-UpdateApiDestination-request-Name"></a>
The name of the API destination to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_UpdateApiDestination_ResponseSyntax"></a>

```
{
   "ApiDestinationArn": "string",
   "ApiDestinationState": "string",
   "CreationTime": number,
   "LastModifiedTime": number
}
```

## Response Elements
<a name="API_UpdateApiDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApiDestinationArn](#API_UpdateApiDestination_ResponseSyntax) **   <a name="eventbridge-UpdateApiDestination-response-ApiDestinationArn"></a>
The ARN of the API destination that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:api-destination\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ApiDestinationState](#API_UpdateApiDestination_ResponseSyntax) **   <a name="eventbridge-UpdateApiDestination-response-ApiDestinationState"></a>
The state of the API destination that was updated.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [CreationTime](#API_UpdateApiDestination_ResponseSyntax) **   <a name="eventbridge-UpdateApiDestination-response-CreationTime"></a>
A time stamp for the time that the API destination was created.
Type: Timestamp

 ** [LastModifiedTime](#API_UpdateApiDestination_ResponseSyntax) **   <a name="eventbridge-UpdateApiDestination-response-LastModifiedTime"></a>
A time stamp for the time that the API destination was last modified.
Type: Timestamp

## Errors
<a name="API_UpdateApiDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApiDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/UpdateApiDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/UpdateApiDestination)
