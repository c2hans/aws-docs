---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListApiDestinations.html
---

# ListApiDestinations
<a name="API_ListApiDestinations"></a>

Retrieves a list of API destination in the account in the current Region.

## Request Syntax
<a name="API_ListApiDestinations_RequestSyntax"></a>

```
{
   "ConnectionArn": "{{string}}",
   "Limit": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApiDestinations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_ListApiDestinations_RequestSyntax) **   <a name="eventbridge-ListApiDestinations-request-ConnectionArn"></a>
The ARN of the connection specified for the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`
Required: No

 ** [Limit](#API_ListApiDestinations_RequestSyntax) **   <a name="eventbridge-ListApiDestinations-request-Limit"></a>
The maximum number of API destinations to include in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListApiDestinations_RequestSyntax) **   <a name="eventbridge-ListApiDestinations-request-NamePrefix"></a>
A name prefix to filter results returned. Only API destinations with a name that starts with the prefix are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListApiDestinations_RequestSyntax) **   <a name="eventbridge-ListApiDestinations-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListApiDestinations_ResponseSyntax"></a>

```
{
   "ApiDestinations": [
      {
         "ApiDestinationArn": "string",
         "ApiDestinationState": "string",
         "ConnectionArn": "string",
         "CreationTime": number,
         "HttpMethod": "string",
         "InvocationEndpoint": "string",
         "InvocationRateLimitPerSecond": number,
         "LastModifiedTime": number,
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApiDestinations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApiDestinations](#API_ListApiDestinations_ResponseSyntax) **   <a name="eventbridge-ListApiDestinations-response-ApiDestinations"></a>
An array that includes information about each API destination.
Type: Array of [ApiDestination](API_ApiDestination.md) objects

 ** [NextToken](#API_ListApiDestinations_ResponseSyntax) **   <a name="eventbridge-ListApiDestinations-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListApiDestinations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## See Also
<a name="API_ListApiDestinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListApiDestinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListApiDestinations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
