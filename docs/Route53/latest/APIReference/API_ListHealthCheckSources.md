---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHealthCheckSources.html
---

# ListHealthCheckSources

Retrieves a list of the health check sources that are associated with the current AWS account.

Results are paginated. To get more results, specify the `NextToken` value from the previous response for `NextToken`.

## Request Syntax
<a name="API_ListHealthCheckSources_RequestSyntax"></a>

```
GET /2013-04-01/healthchecksource?maxresults={{MaxResults}}&nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHealthCheckSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxresults](#API_ListHealthCheckSources_RequestSyntax) **   <a name="Route53-ListHealthCheckSources-request-uri-MaxResults"></a>
The maximum number of health check sources that you want `ListHealthCheckSources` to return. Route 53 returns a maximum of 100 health check sources. If you specify a value greater than 100, Route 53 returns only the first 100.

 ** [nexttoken](#API_ListHealthCheckSources_RequestSyntax) **   <a name="Route53-ListHealthCheckSources-request-uri-NextToken"></a>
The `NextToken` value from the previous response, if it included one. Specify it to get the next group of health check sources.
Length Constraints: Maximum length of 64.

## Request Body
<a name="API_ListHealthCheckSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHealthCheckSources_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListHealthCheckSourcesResponse>
   <HealthCheckSources>
      <HealthCheckSource>
         <HealthCheckSourceConfig>
            <SubnetConfigurationList>
               <SubnetConfiguration>
                  <AvailabilityZoneId>string</AvailabilityZoneId>
                  <SecurityGroupIdList>
                     <SecurityGroupId>string</SecurityGroupId>
                  </SecurityGroupIdList>
                  <SubnetId>string</SubnetId>
               </SubnetConfiguration>
            </SubnetConfigurationList>
            <VpcId>string</VpcId>
         </HealthCheckSourceConfig>
         <HealthCheckSourceId>string</HealthCheckSourceId>
         <HealthCheckSourceStatus>string</HealthCheckSourceStatus>
         <StatusReason>string</StatusReason>
         <StatusReasonCode>string</StatusReasonCode>
      </HealthCheckSource>
   </HealthCheckSources>
   <NextToken>string</NextToken>
</ListHealthCheckSourcesResponse>
```

## Response Elements
<a name="API_ListHealthCheckSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListHealthCheckSourcesResponse](#API_ListHealthCheckSources_ResponseSyntax) **   <a name="Route53-ListHealthCheckSources-response-ListHealthCheckSourcesResponse"></a>
Root level tag for the ListHealthCheckSourcesResponse parameters.
Required: Yes

 ** [HealthCheckSources](#API_ListHealthCheckSources_ResponseSyntax) **   <a name="Route53-ListHealthCheckSources-response-HealthCheckSources"></a>
A complex type that contains one `HealthCheckSource` element for each health check source that is associated with the current AWS account.
Type: Array of [HealthCheckSource](API_HealthCheckSource.md) objects

 ** [NextToken](#API_ListHealthCheckSources_ResponseSyntax) **   <a name="Route53-ListHealthCheckSources-response-NextToken"></a>
A pagination token. If there are more health check sources to list, specify this value for `NextToken` in the next request.
Type: String
Length Constraints: Maximum length of 64.

## Errors
<a name="API_ListHealthCheckSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ListHealthCheckSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListHealthCheckSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListHealthCheckSources)
