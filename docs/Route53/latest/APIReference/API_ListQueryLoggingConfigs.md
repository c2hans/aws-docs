---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html
---

# ListQueryLoggingConfigs
<a name="API_ListQueryLoggingConfigs"></a>

Lists the configurations for DNS query logging that are associated with the current AWS account or the configuration that is associated with a specified hosted zone.

For more information about DNS query logs, see [CreateQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html). Additional information, including the format of DNS query logs, appears in [Logging DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html) in the *Amazon Route 53 Developer Guide*.

## Request Syntax
<a name="API_ListQueryLoggingConfigs_RequestSyntax"></a>

```
GET /2013-04-01/queryloggingconfig?hostedzoneid={{HostedZoneId}}&maxresults={{MaxResults}}&nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListQueryLoggingConfigs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [hostedzoneid](#API_ListQueryLoggingConfigs_RequestSyntax) **   <a name="Route53-ListQueryLoggingConfigs-request-uri-HostedZoneId"></a>
(Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in `HostedZoneId`.
If you don't specify a hosted zone ID, `ListQueryLoggingConfigs` returns all of the configurations that are associated with the current AWS account.
Length Constraints: Maximum length of 32.

 ** [maxresults](#API_ListQueryLoggingConfigs_RequestSyntax) **   <a name="Route53-ListQueryLoggingConfigs-request-uri-MaxResults"></a>
(Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current AWS account has more than `MaxResults` configurations, use the value of [NextToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html#API_ListQueryLoggingConfigs_RequestSyntax) in the response to get the next page of results.
If you don't specify a value for `MaxResults`, Route 53 returns up to 100 configurations.

 ** [nexttoken](#API_ListQueryLoggingConfigs_RequestSyntax) **   <a name="Route53-ListQueryLoggingConfigs-request-uri-NextToken"></a>
(Optional) If the current AWS account has more than `MaxResults` query logging configurations, use `NextToken` to get the second and subsequent pages of results.
For the first `ListQueryLoggingConfigs` request, omit this value.
For the second and subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request.
Length Constraints: Maximum length of 1024.

## Request Body
<a name="API_ListQueryLoggingConfigs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListQueryLoggingConfigs_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListQueryLoggingConfigsResponse>
   <NextToken>string</NextToken>
   <QueryLoggingConfigs>
      <QueryLoggingConfig>
         <CloudWatchLogsLogGroupArn>string</CloudWatchLogsLogGroupArn>
         <HostedZoneId>string</HostedZoneId>
         <Id>string</Id>
      </QueryLoggingConfig>
   </QueryLoggingConfigs>
</ListQueryLoggingConfigsResponse>
```

## Response Elements
<a name="API_ListQueryLoggingConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListQueryLoggingConfigsResponse](#API_ListQueryLoggingConfigs_ResponseSyntax) **   <a name="Route53-ListQueryLoggingConfigs-response-ListQueryLoggingConfigsResponse"></a>
Root level tag for the ListQueryLoggingConfigsResponse parameters.
Required: Yes

 ** [NextToken](#API_ListQueryLoggingConfigs_ResponseSyntax) **   <a name="Route53-ListQueryLoggingConfigs-response-NextToken"></a>
If a response includes the last of the query logging configurations that are associated with the current AWS account, `NextToken` doesn't appear in the response.
If a response doesn't include the last of the configurations, you can get more configurations by submitting another [ListQueryLoggingConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html) request. Get the value of `NextToken` that Amazon Route 53 returned in the previous response and include it in `NextToken` in the next request.
Type: String
Length Constraints: Maximum length of 1024.

 ** [QueryLoggingConfigs](#API_ListQueryLoggingConfigs_ResponseSyntax) **   <a name="Route53-ListQueryLoggingConfigs-response-QueryLoggingConfigs"></a>
An array that contains one [QueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html) element for each configuration for DNS query logging that is associated with the current AWS account.
Type: Array of [QueryLoggingConfig](API_QueryLoggingConfig.md) objects

## Errors
<a name="API_ListQueryLoggingConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidPaginationToken **
The value that you specified to get the second or subsequent page of results is invalid.
HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_ListQueryLoggingConfigs_Examples"></a>

### Example Request
<a name="API_ListQueryLoggingConfigs_Example_1"></a>

The following request gets the configuration that is associated with the hosted zone `Z1D633PJN98FT9`.

```
GET /2013-04-01/queryloggingconfig HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListQueryLoggingConfigsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
   <MaxResults>1</MaxResults>
</ListQueryLoggingConfigsRequest>
```

### Example Response
<a name="API_ListQueryLoggingConfigs_Example_2"></a>

This example illustrates one usage of ListQueryLoggingConfigs.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListQueryLoggingConfigsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <NextToken>87654321-dcba-1234-abcd-1a2b3c4d5e70</NextToken>
   <QueryLoggingConfigs>
      <QueryLoggingConfig>
         <Id>87654321-dcba-1234-abcd-1a2b3c4d5e6f</Id>
         <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
         <CloudWatchLogsLogGroupArn>arn:aws:logs:us-east-1:111111111111:log-group:example.com:*</CloudWatchLogsLogGroupArn>
      </QueryLoggingConfig>
   </QueryLoggingConfigs>
</ListQueryLoggingConfigsResponse>
```

## See Also
<a name="API_ListQueryLoggingConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListQueryLoggingConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListQueryLoggingConfigs)
