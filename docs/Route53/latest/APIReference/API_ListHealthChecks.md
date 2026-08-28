---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHealthChecks.html
---

# ListHealthChecks
<a name="API_ListHealthChecks"></a>

Retrieve a list of the health checks that are associated with the current AWS account.

## Request Syntax
<a name="API_ListHealthChecks_RequestSyntax"></a>

```
GET /2013-04-01/healthcheck?marker={{Marker}}&maxitems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHealthChecks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [marker](#API_ListHealthChecks_RequestSyntax) **   <a name="Route53-ListHealthChecks-request-uri-Marker"></a>
If the value of `IsTruncated` in the previous response was `true`, you have more health checks. To get another group, submit another `ListHealthChecks` request.
For the value of `marker`, specify the value of `NextMarker` from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.
If the value of `IsTruncated` in the previous response was `false`, there are no more health checks to get.
Length Constraints: Maximum length of 64.

 ** [maxitems](#API_ListHealthChecks_RequestSyntax) **   <a name="Route53-ListHealthChecks-request-uri-MaxItems"></a>
The maximum number of health checks that you want `ListHealthChecks` to return in response to the current request. Amazon Route 53 returns a maximum of 1000 items. If you set `MaxItems` to a value greater than 1000, Route 53 returns only the first 1000 health checks.

## Request Body
<a name="API_ListHealthChecks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHealthChecks_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListHealthChecksResponse>
   <HealthChecks>
      <HealthCheck>
         <CallerReference>string</CallerReference>
         <CloudWatchAlarmConfiguration>
            <ComparisonOperator>string</ComparisonOperator>
            <Dimensions>
               <Dimension>
                  <Name>string</Name>
                  <Value>string</Value>
               </Dimension>
            </Dimensions>
            <EvaluationPeriods>integer</EvaluationPeriods>
            <MetricName>string</MetricName>
            <Namespace>string</Namespace>
            <Period>integer</Period>
            <Statistic>string</Statistic>
            <Threshold>double</Threshold>
         </CloudWatchAlarmConfiguration>
         <HealthCheckConfig>
            <AlarmIdentifier>
               <Name>string</Name>
               <Region>string</Region>
            </AlarmIdentifier>
            <ChildHealthChecks>
               <ChildHealthCheck>string</ChildHealthCheck>
            </ChildHealthChecks>
            <Disabled>boolean</Disabled>
            <EnableSNI>boolean</EnableSNI>
            <FailureThreshold>integer</FailureThreshold>
            <FullyQualifiedDomainName>string</FullyQualifiedDomainName>
            <HealthThreshold>integer</HealthThreshold>
            <InsufficientDataHealthStatus>string</InsufficientDataHealthStatus>
            <Inverted>boolean</Inverted>
            <IPAddress>string</IPAddress>
            <MeasureLatency>boolean</MeasureLatency>
            <Port>integer</Port>
            <Regions>
               <Region>string</Region>
            </Regions>
            <RequestInterval>integer</RequestInterval>
            <ResourcePath>string</ResourcePath>
            <RoutingControlArn>string</RoutingControlArn>
            <SearchString>string</SearchString>
            <Type>string</Type>
         </HealthCheckConfig>
         <HealthCheckVersion>long</HealthCheckVersion>
         <Id>string</Id>
         <LinkedService>
            <Description>string</Description>
            <ServicePrincipal>string</ServicePrincipal>
         </LinkedService>
      </HealthCheck>
   </HealthChecks>
   <IsTruncated>boolean</IsTruncated>
   <Marker>string</Marker>
   <MaxItems>string</MaxItems>
   <NextMarker>string</NextMarker>
</ListHealthChecksResponse>
```

## Response Elements
<a name="API_ListHealthChecks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListHealthChecksResponse](#API_ListHealthChecks_ResponseSyntax) **   <a name="Route53-ListHealthChecks-response-ListHealthChecksResponse"></a>
Root level tag for the ListHealthChecksResponse parameters.
Required: Yes

 ** [HealthChecks](#API_ListHealthChecks_ResponseSyntax) **   <a name="Route53-ListHealthChecks-response-HealthChecks"></a>
A complex type that contains one `HealthCheck` element for each health check that is associated with the current AWS account.
Type: Array of [HealthCheck](API_HealthCheck.md) objects

 ** [IsTruncated](#API_ListHealthChecks_ResponseSyntax) **   <a name="Route53-ListHealthChecks-response-IsTruncated"></a>
A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another `ListHealthChecks` request and specifying the value of `NextMarker` in the `marker` parameter.
Type: Boolean

 ** [Marker](#API_ListHealthChecks_ResponseSyntax) **   <a name="Route53-ListHealthChecks-response-Marker"></a>
For the second and subsequent calls to `ListHealthChecks`, `Marker` is the value that you specified for the `marker` parameter in the previous request.
Type: String
Length Constraints: Maximum length of 64.

 ** [MaxItems](#API_ListHealthChecks_ResponseSyntax) **   <a name="Route53-ListHealthChecks-response-MaxItems"></a>
The value that you specified for the `maxitems` parameter in the call to `ListHealthChecks` that produced the current response.
Type: String

 ** [NextMarker](#API_ListHealthChecks_ResponseSyntax) **   <a name="Route53-ListHealthChecks-response-NextMarker"></a>
If `IsTruncated` is `true`, the value of `NextMarker` identifies the first health check that Amazon Route 53 returns if you submit another `ListHealthChecks` request and specify the value of `NextMarker` in the `marker` parameter.
Type: String
Length Constraints: Maximum length of 64.

## Errors
<a name="API_ListHealthChecks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IncompatibleVersion **
The resource you're trying to access is unsupported on this Amazon Route 53 endpoint.
HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListHealthChecks_Examples"></a>

### Example Request
<a name="API_ListHealthChecks_Example_1"></a>

This example illustrates one usage of ListHealthChecks.

```
GET /2013-04-01/healthcheck?maxitems=1
```

### Example Response
<a name="API_ListHealthChecks_Example_2"></a>

This example illustrates one usage of ListHealthChecks.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListHealthChecksResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthChecks>
      <HealthCheck>
         <Id>abcdef11-2222-3333-4444-555555fedcba</Id>
         <CallerReference>example.com 192.0.2.17</CallerReference>
         <HealthCheckConfig>
            <IPAddress>192.0.2.17</IPAddress>
            <Port>80</Port>
            <Type>HTTP</Type>
            <ResourcePath>/docs/route-53-health-check.html</ResourcePath>
            <FullyQualifiedDomainName>example.com</FullyQualifiedDomainName>
            <RequestInterval>30</RequestInterval>
            <FailureThreshold>3</FailureThreshold>
            <MeasureLatency>true</MeasureLatency>
            <EnableSNI>true</EnableSNI>
            <Inverted>false</Inverted>
         </HealthCheckConfig>
         <HealthCheckVersion>2</HealthCheckVersion>
      </HealthCheck>
   </HealthChecks>
   <IsTruncated>true</IsTruncated>
   <NextMarker>aaaaaaaa-1234-5678-9012-bbbbbbcccccc</NextMarker>
   <MaxItems>1</MaxItems>
</ListHealthChecksResponse>
```

## See Also
<a name="API_ListHealthChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListHealthChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListHealthChecks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
