---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHealthChecksBySource.html
---

# ListHealthChecksBySource

Retrieves a list of the health checks that use a specified health check source.

Results are paginated. If `IsTruncated` is `true`, specify the `NextMarker` value for `marker` to get more results.

## Request Syntax
<a name="API_ListHealthChecksBySource_RequestSyntax"></a>

```
GET /2013-04-01/healthchecks/source/{{HealthCheckSourceId}}?marker={{Marker}}&maxitems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHealthChecksBySource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckSourceId](#API_ListHealthChecksBySource_RequestSyntax) **   <a name="Route53-ListHealthChecksBySource-request-uri-HealthCheckSourceId"></a>
The ID of the health check source whose health checks you want to list.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [marker](#API_ListHealthChecksBySource_RequestSyntax) **   <a name="Route53-ListHealthChecksBySource-request-uri-Marker"></a>
The `NextMarker` value from the previous response, if the value of `IsTruncated` was `true`. Specify it to get the next group of health checks. If `IsTruncated` was `false`, there are no more health checks to get.
Length Constraints: Maximum length of 64.

 ** [maxitems](#API_ListHealthChecksBySource_RequestSyntax) **   <a name="Route53-ListHealthChecksBySource-request-uri-MaxItems"></a>
The maximum number of health checks that you want `ListHealthChecksBySource` to return. Route 53 returns a maximum of 1000 health checks. If you specify a value greater than 1000, Route 53 returns only the first 1000.

## Request Body
<a name="API_ListHealthChecksBySource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHealthChecksBySource_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListHealthChecksBySourceResponse>
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
            <EndpointType>string</EndpointType>
            <FailureThreshold>integer</FailureThreshold>
            <FullyQualifiedDomainName>string</FullyQualifiedDomainName>
            <HealthCheckSourceId>string</HealthCheckSourceId>
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
</ListHealthChecksBySourceResponse>
```

## Response Elements
<a name="API_ListHealthChecksBySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListHealthChecksBySourceResponse](#API_ListHealthChecksBySource_ResponseSyntax) **   <a name="Route53-ListHealthChecksBySource-response-ListHealthChecksBySourceResponse"></a>
Root level tag for the ListHealthChecksBySourceResponse parameters.
Required: Yes

 ** [HealthChecks](#API_ListHealthChecksBySource_ResponseSyntax) **   <a name="Route53-ListHealthChecksBySource-response-HealthChecks"></a>
A complex type that contains one `HealthCheck` element for each health check that uses the specified health check source.
Type: Array of [HealthCheck](API_HealthCheck.md) objects

 ** [IsTruncated](#API_ListHealthChecksBySource_ResponseSyntax) **   <a name="Route53-ListHealthChecksBySource-response-IsTruncated"></a>
Specifies whether there are more health checks to list. If the value is `true`, specify the `NextMarker` value for `marker` to get the next group of health checks.
Type: Boolean

 ** [Marker](#API_ListHealthChecksBySource_ResponseSyntax) **   <a name="Route53-ListHealthChecksBySource-response-Marker"></a>
The value that you specified for the `marker` parameter in the call to `ListHealthChecksBySource` that produced the current response. This value is present for the second and subsequent calls to `ListHealthChecksBySource`.
Type: String
Length Constraints: Maximum length of 64.

 ** [MaxItems](#API_ListHealthChecksBySource_ResponseSyntax) **   <a name="Route53-ListHealthChecksBySource-response-MaxItems"></a>
The value that you specified for the `maxitems` parameter in the call to `ListHealthChecksBySource` that produced the current response.
Type: String

 ** [NextMarker](#API_ListHealthChecksBySource_ResponseSyntax) **   <a name="Route53-ListHealthChecksBySource-response-NextMarker"></a>
The identifier of the first health check in the next group of health checks. If `IsTruncated` is `true`, specify this value in the `marker` parameter of another `ListHealthChecksBySource` request.
Type: String
Length Constraints: Maximum length of 64.

## Errors
<a name="API_ListHealthChecksBySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheckSource **
No health check source exists with the specified ID. Verify that the ID is correct and that the health check source hasn't been deleted.
HTTP Status Code: 404

## See Also
<a name="API_ListHealthChecksBySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListHealthChecksBySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListHealthChecksBySource)
