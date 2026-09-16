---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHealthCheck.html
---

# CreateHealthCheck
<a name="API_CreateHealthCheck"></a>

Creates a new health check.

For information about adding health checks to resource record sets, see [HealthCheckId](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html#Route53-Type-ResourceRecordSet-HealthCheckId) in [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html).

 **ELB Load Balancers**

If you're registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to a Route 53 health check.

 **Private Hosted Zones**

You can associate health checks with failover resource record sets in a private hosted zone. Note the following:
+ Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.
+ You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server.
+ You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 `StatusCheckFailed` metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html).

## Request Syntax
<a name="API_CreateHealthCheck_RequestSyntax"></a>

```
POST /2013-04-01/healthcheck HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>{{string}}</CallerReference>
   <HealthCheckConfig>
      <AlarmIdentifier>
         <Name>{{string}}</Name>
         <Region>{{string}}</Region>
      </AlarmIdentifier>
      <ChildHealthChecks>
         <ChildHealthCheck>{{string}}</ChildHealthCheck>
      </ChildHealthChecks>
      <Disabled>{{boolean}}</Disabled>
      <EnableSNI>{{boolean}}</EnableSNI>
      <FailureThreshold>{{integer}}</FailureThreshold>
      <FullyQualifiedDomainName>{{string}}</FullyQualifiedDomainName>
      <HealthThreshold>{{integer}}</HealthThreshold>
      <InsufficientDataHealthStatus>{{string}}</InsufficientDataHealthStatus>
      <Inverted>{{boolean}}</Inverted>
      <IPAddress>{{string}}</IPAddress>
      <MeasureLatency>{{boolean}}</MeasureLatency>
      <Port>{{integer}}</Port>
      <Regions>
         <Region>{{string}}</Region>
      </Regions>
      <RequestInterval>{{integer}}</RequestInterval>
      <ResourcePath>{{string}}</ResourcePath>
      <RoutingControlArn>{{string}}</RoutingControlArn>
      <SearchString>{{string}}</SearchString>
      <Type>{{string}}</Type>
   </HealthCheckConfig>
</CreateHealthCheckRequest>
```

## URI Request Parameters
<a name="API_CreateHealthCheck_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateHealthCheck_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateHealthCheckRequest](#API_CreateHealthCheck_RequestSyntax) **   <a name="Route53-CreateHealthCheck-request-CreateHealthCheckRequest"></a>
Root level tag for the CreateHealthCheckRequest parameters.
Required: Yes

 ** [CallerReference](#API_CreateHealthCheck_RequestSyntax) **   <a name="Route53-CreateHealthCheck-request-CallerReference"></a>
A unique string that identifies the request and that allows you to retry a failed `CreateHealthCheck` request without the risk of creating two identical health checks:
+ If you send a `CreateHealthCheck` request with the same `CallerReference` and settings as a previous request, and if the health check doesn't exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the health check configuration in the response.
+ If you send a `CreateHealthCheck` request with the same `CallerReference` as a deleted health check, regardless of the settings, Route 53 returns a `HealthCheckAlreadyExists` error.
+ If you send a `CreateHealthCheck` request with the same `CallerReference` as an existing health check but with different settings, Route 53 returns a `HealthCheckAlreadyExists` error.
+ If you send a `CreateHealthCheck` request with a unique `CallerReference` but settings identical to an existing health check, Route 53 creates the health check.
 Route 53 does not store the `CallerReference` for a deleted health check indefinitely. The `CallerReference` for a deleted health check will be deleted after a number of days.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [HealthCheckConfig](#API_CreateHealthCheck_RequestSyntax) **   <a name="Route53-CreateHealthCheck-request-HealthCheckConfig"></a>
A complex type that contains settings for a new health check.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: Yes

## Response Syntax
<a name="API_CreateHealthCheck_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckResponse>
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
</CreateHealthCheckResponse>
```

## Response Elements
<a name="API_CreateHealthCheck_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateHealthCheck_ResponseSyntax) **   <a name="Route53-CreateHealthCheck-response-Location"></a>
The unique URL representing the new health check.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateHealthCheckResponse](#API_CreateHealthCheck_ResponseSyntax) **   <a name="Route53-CreateHealthCheck-response-CreateHealthCheckResponse"></a>
Root level tag for the CreateHealthCheckResponse parameters.
Required: Yes

 ** [HealthCheck](#API_CreateHealthCheck_ResponseSyntax) **   <a name="Route53-CreateHealthCheck-response-HealthCheck"></a>
A complex type that contains identifying information about the health check.
Type: [HealthCheck](API_HealthCheck.md) object

## Errors
<a name="API_CreateHealthCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HealthCheckAlreadyExists **
 The health check you're attempting to create already exists. Amazon Route 53 returns this error when you submit a request that has the following values:
+ The same value for `CallerReference` as an existing health check, and one or more values that differ from the existing health check that has the same caller reference.
+ The same value for `CallerReference` as a health check that you created and later deleted, regardless of the other settings in the request.
 ** message **

HTTP Status Code: 409

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** TooManyHealthChecks **
This health check can't be created because the current account has reached the limit on the number of active health checks.
For information about default limits, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*.
For information about how to get the current limit for an account, see [GetAccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html). To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
You have reached the maximum number of active health checks for an AWS account. To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
HTTP Status Code: 400

## Examples
<a name="API_CreateHealthCheck_Examples"></a>

### Request Syntax for HTTP[S], HTTP[S]\_STR\_MATCH, and TCP Health Checks
<a name="API_CreateHealthCheck_Example_1"></a>

This example illustrates one usage of CreateHealthCheck.

```
POST /2013-04-01/healthcheck HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>unique description</CallerReference>
   <HealthCheckConfig>
      <EnableSNI>true | false</EnableSNI>
      <FailureThreshold>number of health checks that must pass or fail to change the status of the health check</FailureThreshold>
      <FullyQualifiedDomainName>domain name of the endpoint to check</FullyQualifiedDomainName>
      <Inverted>true | false</Inverted>
      <IPAddress>IP address of the endpoint to check</IPAddress>
      <MeasureLatency>true | false</MeasureLatency>
      <Port>port on the endpoint to check</Port>
      <Regions>
         <Region>us-west-1 | us-west-2 | us-east-1 | eu-west-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1</Region>
         ...
      </Regions>
      <RequestInterval>10 | 30</RequestInterval>
      <ResourcePath>path of the file that you want Route 53 to request</ResourcePath>
      <SearchString>if Type is HTTP_STR_MATCH or HTTPS_STR_MATCH, the string to search for in the response body from the specified resource</SearchString>
      <Type>HTTP | HTTPS | HTTP_STR_MATCH | HTTPS_STR_MATCH | TCP</Type>
   </HealthCheckConfig>
</CreateHealthCheckRequest>
```

### Response Syntax for HTTP[S], HTTP[S]\_STR\_MATCH, and TCP Health Checks
<a name="API_CreateHealthCheck_Example_2"></a>

This example illustrates one usage of CreateHealthCheck.

```
HTTP/1.1 201 Created
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheck>
      <Id>ID that Route 53 assigned to the new health check</Id>
      <CallerReference>unique description</CallerReference>
      <HealthCheckConfig>
         <EnableSNI>true | false</EnableSNI>
         <FailureThreshold>number of health checks that must pass or fail to change the status of the health check</FailureThreshold>
         <FullyQualifiedDomainName>domain name of the endpoint to check</FullyQualifiedDomainName>
         <Inverted>true | false</Inverted>
         <IPAddress>IP address of the endpoint to check</IPAddress>
         <MeasureLatency>true | false</MeasureLatency>
         <Port>port on the endpoint to check</Port>
         <Regions>
            <Region>us-west-1 | us-west-2 | us-east-1 | eu-west-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1</Region>
            ...
         </Regions>
         <RequestInterval>10 | 30</RequestInterval>
         <ResourcePath>path of the file that you want Route 53 to request</ResourcePath>
         <SearchString>if Type is HTTP_STR_MATCH or HTTPS_STR_MATCH, the string to search for in the response body from the specified resource</SearchString>
         <Type>HTTP | HTTPS | HTTP_STR_MATCH | HTTPS_STR_MATCH | TCP</Type>
      </HealthCheckConfig>
      <HealthCheckVersion>sequential counter</HealthCheckVersion>
   </HealthCheck>
</CreateHealthCheckResponse>
```

### Request Syntax for CLOUDWATCH\_METRIC Health Checks
<a name="API_CreateHealthCheck_Example_3"></a>

This example illustrates one usage of CreateHealthCheck.

```
POST /2013-04-01/healthcheck HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>unique description</CallerReference>
   <HealthCheckConfig>
      <AlarmIdentifier>
         <Name>name of CloudWatch alarm</Name>
         <Region>region that CloudWatch alarm was created in</Region>
      </AlarmIdentifier>
      <InsufficientDataHealthStatus>Healthy | Unhealthy | LastKnownStatus</InsufficientDataHealthStatus>
      <Inverted>true | false</Inverted>
      <Type>CLOUDWATCH_METRIC</Type>
   </HealthCheckConfig>
</CreateHealthCheckRequest>
```

### Response Syntax for CLOUDWATCH\_METRIC Health Checks
<a name="API_CreateHealthCheck_Example_4"></a>

This example illustrates one usage of CreateHealthCheck.

```
POST /2013-04-01/healthcheck HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheck>
      <Id>ID that Route 53 assigned to the new health check</Id>
      <CallerReference>unique description</CallerReference>
      <HealthCheckConfig>
         <AlarmIdentifier>
            <Name>name of CloudWatch alarm</Name>
            <Region>region of CloudWatch alarm</Region>
         </AlarmIdentifier>
         <InsufficientDataHealthStatus>Healthy | Unhealthy | LastKnownStatus</InsufficientDataHealthStatus>
         <Inverted>true | false</Inverted>
         <Type>CLOUDWATCH_METRIC</Type>
      </HealthCheckConfig>
      <CloudWatchAlarmConfiguration>
         <ComparisonOperator>GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold</ComparisonOperator>
         <Dimensions>
            <Dimension>
               <Name>name of a dimension for the metric</Name>
               <Value>value of a dimension for the metric</Value>
            </Dimension>
            ...
         </Dimensions>
         <EvaluationPeriods>number of periods that metric is compared to threshold</EvaluationPeriods>
         <MetricName>name of the metric that's associated with the alarm</MetricName>
         <Namespace>namespace of the metric that the alarm is associated with</Namespace>
         <Period>duration of a period in seconds</Period>
         <Statistic>statistic applied to the CloudWatch metric</Statistic>
         <Threshold>value the metric is compared with</Threshold>
      </CloudWatchAlarmConfiguration>
      <HealthCheckVersion>sequential counter</HealthCheckVersion>
   </HealthCheck>
</CreateHealthCheckResponse>
```

### Request Syntax for CALCULATED Health Checks
<a name="API_CreateHealthCheck_Example_5"></a>

This example illustrates one usage of CreateHealthCheck.

```
POST /2013-04-01/healthcheck HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>unique description</CallerReference>
   <HealthCheckConfig>
      <ChildHealthChecks>
         <ChildHealthCheck>health check ID</ChildHealthCheck>
         ...
      </ChildHealthChecks>
      <HealthThreshold>number of the health checks that are associated with a CALCULATED health check that must be healthy</HealthThreshold>
      <Inverted>true | false</Inverted>
      <Type>CALCULATED</Type>
   </HealthCheckConfig>
</CreateHealthCheckRequest>
```

### Response Syntax for CALCULATED Health Checks
<a name="API_CreateHealthCheck_Example_6"></a>

This example illustrates one usage of CreateHealthCheck.

```
HTTP/1.1 201 Created
<?xml version="1.0" encoding="UT2F-8"?>
<CreateHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheck>
      <Id>ID that Route 53 assigned to the new health check</Id>
      <CallerReference>unique description</CallerReference>
      <HealthCheckConfig>
         <ChildHealthChecks>
            <ChildHealthCheck>health check ID</ChildHealthCheck>
            ...
         </ChildHealthChecks>
         <HealthThreshold>number of health checks that are associated with a CALCULATED health check that must be healthy</HealthThreshold>
         <Inverted>true | false</Inverted>
         <Type>CALCULATED</Type>
      </HealthCheckConfig>
      <HealthCheckVersion>sequential counter</HealthCheckVersion>
   </HealthCheck>
</CreateHealthCheckResponse>
```

## See Also
<a name="API_CreateHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateHealthCheck)
