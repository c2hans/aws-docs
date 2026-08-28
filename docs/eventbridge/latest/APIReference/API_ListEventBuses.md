---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventBuses.html
---

# ListEventBuses
<a name="API_ListEventBuses"></a>

Lists all the event buses in your account, including the default event bus, custom event buses, and partner event buses.

## Request Syntax
<a name="API_ListEventBuses_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEventBuses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListEventBuses_RequestSyntax) **   <a name="eventbridge-ListEventBuses-request-Limit"></a>
Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListEventBuses_RequestSyntax) **   <a name="eventbridge-ListEventBuses-request-NamePrefix"></a>
Specifying this limits the results to only those event buses with names that start with the specified prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[/\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListEventBuses_RequestSyntax) **   <a name="eventbridge-ListEventBuses-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListEventBuses_ResponseSyntax"></a>

```
{
   "EventBuses": [
      {
         "Arn": "string",
         "CreationTime": number,
         "Description": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "Policy": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEventBuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventBuses](#API_ListEventBuses_ResponseSyntax) **   <a name="eventbridge-ListEventBuses-response-EventBuses"></a>
This list of event buses.
Type: Array of [EventBus](API_EventBus.md) objects

 ** [NextToken](#API_ListEventBuses_ResponseSyntax) **   <a name="eventbridge-ListEventBuses-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListEventBuses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## See Also
<a name="API_ListEventBuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListEventBuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListEventBuses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
