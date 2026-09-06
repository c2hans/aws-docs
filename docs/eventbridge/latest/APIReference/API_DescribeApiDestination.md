---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeApiDestination.html
---

# DescribeApiDestination
<a name="API_DescribeApiDestination"></a>

Retrieves details about an API destination.

## Request Syntax
<a name="API_DescribeApiDestination_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApiDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeApiDestination_RequestSyntax) **   <a name="eventbridge-DescribeApiDestination-request-Name"></a>
The name of the API destination to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeApiDestination_ResponseSyntax"></a>

```
{
   "ApiDestinationArn": "string",
   "ApiDestinationState": "string",
   "ConnectionArn": "string",
   "CreationTime": number,
   "Description": "string",
   "HttpMethod": "string",
   "InvocationEndpoint": "string",
   "InvocationRateLimitPerSecond": number,
   "LastModifiedTime": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_DescribeApiDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApiDestinationArn](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-ApiDestinationArn"></a>
The ARN of the API destination retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:api-destination\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ApiDestinationState](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-ApiDestinationState"></a>
The state of the API destination retrieved.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [ConnectionArn](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-ConnectionArn"></a>
The ARN of the connection specified for the API destination retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [CreationTime](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-CreationTime"></a>
A time stamp for the time that the API destination was created.
Type: Timestamp

 ** [Description](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-Description"></a>
The description for the API destination retrieved.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

 ** [HttpMethod](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-HttpMethod"></a>
The method to use to connect to the HTTP endpoint.
Type: String
Valid Values: `POST | GET | HEAD | OPTIONS | PUT | PATCH | DELETE`

 ** [InvocationEndpoint](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-InvocationEndpoint"></a>
The URL to use to connect to the HTTP endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`

 ** [InvocationRateLimitPerSecond](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-InvocationRateLimitPerSecond"></a>
The maximum number of invocations per second to specified for the API destination. Note that if you set the invocation rate maximum to a value lower the rate necessary to send all events received on to the destination HTTP endpoint, some events may not be delivered within the 24-hour retry window. If you plan to set the rate lower than the rate necessary to deliver all events, consider using a dead-letter queue to catch events that are not delivered within 24 hours.
Type: Integer
Valid Range: Minimum value of 1.

 ** [LastModifiedTime](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-LastModifiedTime"></a>
A time stamp for the time that the API destination was last modified.
Type: Timestamp

 ** [Name](#API_DescribeApiDestination_ResponseSyntax) **   <a name="eventbridge-DescribeApiDestination-response-Name"></a>
The name of the API destination retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

## Errors
<a name="API_DescribeApiDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApiDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeApiDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeApiDestination)
