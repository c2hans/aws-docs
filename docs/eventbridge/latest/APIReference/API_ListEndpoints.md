---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEndpoints.html
---

# ListEndpoints
<a name="API_ListEndpoints"></a>

List the global endpoints associated with this account. For more information about global endpoints, see [Making applications Regional-fault tolerant with global endpoints and event replication](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html) in the * *Amazon EventBridge User Guide* *.

## Request Syntax
<a name="API_ListEndpoints_RequestSyntax"></a>

```
{
   "HomeRegion": "{{string}}",
   "MaxResults": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HomeRegion](#API_ListEndpoints_RequestSyntax) **   <a name="eventbridge-ListEndpoints-request-HomeRegion"></a>
The primary Region of the endpoints associated with this account. For example `"HomeRegion": "us-east-1"`.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 20.
Pattern: `^[\-a-z0-9]+$`
Required: No

 ** [MaxResults](#API_ListEndpoints_RequestSyntax) **   <a name="eventbridge-ListEndpoints-request-MaxResults"></a>
The maximum number of results returned by the call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListEndpoints_RequestSyntax) **   <a name="eventbridge-ListEndpoints-request-NamePrefix"></a>
A value that will return a subset of the endpoints associated with this account. For example, `"NamePrefix": "ABC"` will return all endpoints with "ABC" in the name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListEndpoints_RequestSyntax) **   <a name="eventbridge-ListEndpoints-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListEndpoints_ResponseSyntax"></a>

```
{
   "Endpoints": [
      {
         "Arn": "string",
         "CreationTime": number,
         "Description": "string",
         "EndpointId": "string",
         "EndpointUrl": "string",
         "EventBuses": [
            {
               "EventBusArn": "string"
            }
         ],
         "LastModifiedTime": number,
         "Name": "string",
         "ReplicationConfig": {
            "State": "string"
         },
         "RoleArn": "string",
         "RoutingConfig": {
            "FailoverConfig": {
               "Primary": {
                  "HealthCheck": "string"
               },
               "Secondary": {
                  "Route": "string"
               }
            }
         },
         "State": "string",
         "StateReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoints](#API_ListEndpoints_ResponseSyntax) **   <a name="eventbridge-ListEndpoints-response-Endpoints"></a>
The endpoints returned by the call.
Type: Array of [Endpoint](API_Endpoint.md) objects

 ** [NextToken](#API_ListEndpoints_ResponseSyntax) **   <a name="eventbridge-ListEndpoints-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## See Also
<a name="API_ListEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
