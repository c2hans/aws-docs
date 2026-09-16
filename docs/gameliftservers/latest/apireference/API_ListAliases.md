---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListAliases.html
---

# ListAliases
<a name="API_ListAliases"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves all aliases for this AWS account. You can filter the result set by alias name and/or routing strategy type. Use the pagination parameters to retrieve results in sequential pages.

**Note**
Returned aliases are not listed in any particular order.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_ListAliases_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}",
   "RoutingStrategyType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_ListAliases_RequestSyntax) **   <a name="gameliftservers-ListAliases-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Name](#API_ListAliases_RequestSyntax) **   <a name="gameliftservers-ListAliases-request-Name"></a>
A descriptive label that is associated with an alias. Alias names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [NextToken](#API_ListAliases_RequestSyntax) **   <a name="gameliftservers-ListAliases-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [RoutingStrategyType](#API_ListAliases_RequestSyntax) **   <a name="gameliftservers-ListAliases-request-RoutingStrategyType"></a>
The routing type to filter results on. Use this parameter to retrieve only aliases with a certain routing type. To retrieve all aliases, leave this parameter empty.
Possible routing types include the following:
+  **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
+  **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the [RoutingStrategy](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RoutingStrategy.html) message embedded.
Type: String
Valid Values: `SIMPLE | TERMINAL`
Required: No

## Response Syntax
<a name="API_ListAliases_ResponseSyntax"></a>

```
{
   "Aliases": [
      {
         "AliasArn": "string",
         "AliasId": "string",
         "CreationTime": number,
         "Description": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "RoutingStrategy": {
            "FleetId": "string",
            "Message": "string",
            "Type": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_ListAliases_ResponseSyntax) **   <a name="gameliftservers-ListAliases-response-Aliases"></a>
A collection of alias resources that match the request parameters.
Type: Array of [Alias](API_Alias.md) objects

 ** [NextToken](#API_ListAliases_ResponseSyntax) **   <a name="gameliftservers-ListAliases-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListAliases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_ListAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListAliases)
