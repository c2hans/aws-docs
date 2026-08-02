---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateApiDestination.html
---

# CreateApiDestination
<a name="API_CreateApiDestination"></a>

Creates an API destination, which is an HTTP invocation endpoint configured as a target for events.

API destinations do not support private destinations, such as interface VPC endpoints.

For more information, see [API destinations](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html) in the *EventBridge User Guide*.

## Request Syntax
<a name="API_CreateApiDestination_RequestSyntax"></a>

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
<a name="API_CreateApiDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_CreateApiDestination_RequestSyntax) **   <a name="eventbridge-CreateApiDestination-request-ConnectionArn"></a>
The ARN of the connection to use for the API destination. The destination endpoint must support the authorization type specified for the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`
Required: Yes

 ** [Description](#API_CreateApiDestination_RequestSyntax) **   <a name="eventbridge-CreateApiDestination-request-Description"></a>
A description for the API destination to create.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [HttpMethod](#API_CreateApiDestination_RequestSyntax) **   <a name="eventbridge-CreateApiDestination-request-HttpMethod"></a>
The method to use for the request to the HTTP invocation endpoint.
Type: String
Valid Values: `POST | GET | HEAD | OPTIONS | PUT | PATCH | DELETE`
Required: Yes

 ** [InvocationEndpoint](#API_CreateApiDestination_RequestSyntax) **   <a name="eventbridge-CreateApiDestination-request-InvocationEndpoint"></a>
The URL to the HTTP invocation endpoint for the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`
Required: Yes

 ** [InvocationRateLimitPerSecond](#API_CreateApiDestination_RequestSyntax) **   <a name="eventbridge-CreateApiDestination-request-InvocationRateLimitPerSecond"></a>
The maximum number of requests per second to send to the HTTP invocation endpoint.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Name](#API_CreateApiDestination_RequestSyntax) **   <a name="eventbridge-CreateApiDestination-request-Name"></a>
The name for the API destination to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CreateApiDestination_ResponseSyntax"></a>

```
{
   "ApiDestinationArn": "string",
   "ApiDestinationState": "string",
   "CreationTime": number,
   "LastModifiedTime": number
}
```

## Response Elements
<a name="API_CreateApiDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApiDestinationArn](#API_CreateApiDestination_ResponseSyntax) **   <a name="eventbridge-CreateApiDestination-response-ApiDestinationArn"></a>
The ARN of the API destination that was created by the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:api-destination\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ApiDestinationState](#API_CreateApiDestination_ResponseSyntax) **   <a name="eventbridge-CreateApiDestination-response-ApiDestinationState"></a>
The state of the API destination that was created by the request.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [CreationTime](#API_CreateApiDestination_ResponseSyntax) **   <a name="eventbridge-CreateApiDestination-response-CreationTime"></a>
A time stamp indicating the time that the API destination was created.
Type: Timestamp

 ** [LastModifiedTime](#API_CreateApiDestination_ResponseSyntax) **   <a name="eventbridge-CreateApiDestination-response-LastModifiedTime"></a>
A time stamp indicating the time that the API destination was last modified.
Type: Timestamp

## Errors
<a name="API_CreateApiDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_CreateApiDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CreateApiDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateApiDestination)
