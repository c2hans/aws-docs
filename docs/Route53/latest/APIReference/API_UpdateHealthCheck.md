---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html
---

# UpdateHealthCheck
<a name="API_UpdateHealthCheck"></a>

Updates an existing health check. Note that some values can't be updated.

For more information about updating health checks, see [Creating, Updating, and Deleting Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html) in the *Amazon Route 53 Developer Guide*.

## Request Syntax
<a name="API_UpdateHealthCheck_RequestSyntax"></a>

```
POST /2013-04-01/healthcheck/{{HealthCheckId}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
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
   <HealthCheckVersion>{{long}}</HealthCheckVersion>
   <HealthThreshold>{{integer}}</HealthThreshold>
   <InsufficientDataHealthStatus>{{string}}</InsufficientDataHealthStatus>
   <Inverted>{{boolean}}</Inverted>
   <IPAddress>{{string}}</IPAddress>
   <Port>{{integer}}</Port>
   <Regions>
      <Region>{{string}}</Region>
   </Regions>
   <ResetElements>
      <ResettableElementName>{{string}}</ResettableElementName>
   </ResetElements>
   <ResourcePath>{{string}}</ResourcePath>
   <SearchString>{{string}}</SearchString>
</UpdateHealthCheckRequest>
```

## URI Request Parameters
<a name="API_UpdateHealthCheck_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckId](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-uri-HealthCheckId"></a>
The ID for the health check for which you want detailed information. When you created the health check, `CreateHealthCheck` returned the ID in the response, in the `HealthCheckId` element.
Length Constraints: Maximum length of 64.
Required: Yes

## Request Body
<a name="API_UpdateHealthCheck_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateHealthCheckRequest](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-UpdateHealthCheckRequest"></a>
Root level tag for the UpdateHealthCheckRequest parameters.
Required: Yes

 ** [AlarmIdentifier](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-AlarmIdentifier"></a>
A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
Type: [AlarmIdentifier](API_AlarmIdentifier.md) object
Required: No

 ** [ChildHealthChecks](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-ChildHealthChecks"></a>
A complex type that contains one `ChildHealthCheck` element for each health check that you want to associate with a `CALCULATED` health check.
Type: Array of strings
Array Members: Maximum number of 256 items.
Length Constraints: Maximum length of 64.
Required: No

 ** [Disabled](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-Disabled"></a>
Stops Route 53 from performing health checks. When you disable a health check, here's what happens:
+  **Health checks that check the health of endpoints:** Route 53 stops submitting requests to your application, server, or other resource.
+  **Calculated health checks:** Route 53 stops aggregating the status of the referenced health checks.
+  **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the corresponding CloudWatch metrics.
After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. Additionally, in disabled state, you can also invert the status of the health check to route traffic differently. For more information, see [Inverted](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted).
Charges for a health check still apply when the health check is disabled. For more information, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/).
Type: Boolean
Required: No

 ** [EnableSNI](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-EnableSNI"></a>
Specify whether you want Amazon Route 53 to send the value of `FullyQualifiedDomainName` to the endpoint in the `client_hello` message during `TLS` negotiation. This allows the endpoint to respond to `HTTPS` health check requests with the applicable SSL/TLS certificate.
Some endpoints require that HTTPS requests include the host name in the `client_hello` message. If you don't enable SNI, the status of the health check will be SSL alert `handshake_failure`. A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
The SSL/TLS certificate on your endpoint includes a domain name in the `Common Name` field and possibly several more in the `Subject Alternative Names` field. One of the domain names in the certificate should match the value that you specify for `FullyQualifiedDomainName`. If the endpoint responds to the `client_hello` message with a certificate that does not include the domain name that you specified in `FullyQualifiedDomainName`, a health checker will retry the handshake. In the second attempt, the health checker will omit `FullyQualifiedDomainName` from the `client_hello` message.
Type: Boolean
Required: No

 ** [FailureThreshold](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-FailureThreshold"></a>
The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see [How Amazon Route 53 Determines Whether an Endpoint Is Healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html) in the *Amazon Route 53 Developer Guide*.
Otherwise, if you don't specify a value for `FailureThreshold`, the default value is three health checks.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [FullyQualifiedDomainName](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-FullyQualifiedDomainName"></a>
Amazon Route 53 behavior depends on whether you specify a value for `IPAddress`.
If a health check already has a value for `IPAddress`, you can change the value. However, you can't update an existing health check to add or remove the value of `IPAddress`.
 **If you specify a value for** `IPAddress`:
Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of `FullyQualifiedDomainName` in the `Host` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
When Route 53 checks the health of an endpoint, here is how it constructs the `Host` header:
+ If you specify a value of `80` for `Port` and `HTTP` or `HTTP_STR_MATCH` for `Type`, Route 53 passes the value of `FullyQualifiedDomainName` to the endpoint in the `Host` header.
+ If you specify a value of `443` for `Port` and `HTTPS` or `HTTPS_STR_MATCH` for `Type`, Route 53 passes the value of `FullyQualifiedDomainName` to the endpoint in the `Host` header.
+ If you specify another value for `Port` and any value except `TCP` for `Type`, Route 53 passes * `FullyQualifiedDomainName`:`Port` * to the endpoint in the `Host` header.
If you don't specify a value for `FullyQualifiedDomainName`, Route 53 substitutes the value of `IPAddress` in the `Host` header in each of the above cases.
 **If you don't specify a value for** `IPAddress`:
If you don't specify a value for `IPAddress`, Route 53 sends a DNS request to the domain that you specify in `FullyQualifiedDomainName` at the interval you specify in `RequestInterval`. Using an IPv4 address that is returned by DNS, Route 53 then checks the health of the endpoint.
If you don't specify a value for `IPAddress`, you can’t update the health check to remove the `FullyQualifiedDomainName`; if you don’t specify a value for `IPAddress` on creation, a `FullyQualifiedDomainName` is required.
If you don't specify a value for `IPAddress`, Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for `FullyQualifiedDomainName`, the health check fails with a "DNS resolution failed" error.
If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by `FullyQualifiedDomainName`, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of `FullyQualifiedDomainName`, specify the domain name of the server (such as `us-east-2-www.example.com`), not the name of the resource record sets (www.example.com).
In this configuration, if the value of `FullyQualifiedDomainName` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.
In addition, if the value of `Type` is `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, or `HTTPS_STR_MATCH`, Route 53 passes the value of `FullyQualifiedDomainName` in the `Host` header, as it does when you specify a value for `IPAddress`. If the value of `Type` is `TCP`, Route 53 doesn't pass a `Host` header.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** [HealthCheckVersion](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-HealthCheckVersion"></a>
A sequential counter that Amazon Route 53 sets to `1` when you create a health check and increments by 1 each time you update settings for the health check.
We recommend that you use `GetHealthCheck` or `ListHealthChecks` to get the current value of `HealthCheckVersion` for the health check that you want to update, and that you include that value in your `UpdateHealthCheck` request. This prevents Route 53 from overwriting an intervening update:
+ If the value in the `UpdateHealthCheck` request matches the value of `HealthCheckVersion` in the health check, Route 53 updates the health check with the new settings.
+ If the value of `HealthCheckVersion` in the health check is greater, the health check was changed after you got the version number. Route 53 does not update the health check, and it returns a `HealthCheckVersionMismatch` error.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** [HealthThreshold](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-HealthThreshold"></a>
The number of child health checks that are associated with a `CALCULATED` health that Amazon Route 53 must consider healthy for the `CALCULATED` health check to be considered healthy. To specify the child health checks that you want to associate with a `CALCULATED` health check, use the `ChildHealthChecks` and `ChildHealthCheck` elements.
Note the following:
+ If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
+ If you specify `0`, Route 53 always considers this health check to be healthy.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 256.
Required: No

 ** [InsufficientDataHealthStatus](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-InsufficientDataHealthStatus"></a>
When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
+  `Healthy`: Route 53 considers the health check to be healthy.
+  `Unhealthy`: Route 53 considers the health check to be unhealthy.
+  `LastKnownStatus`: By default, Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the status for the health check is healthy.
Type: String
Valid Values: `Healthy | Unhealthy | LastKnownStatus`
Required: No

 ** [Inverted](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-Inverted"></a>
Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
Type: Boolean
Required: No

 ** [IPAddress](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-IPAddress"></a>
The IPv4 or IPv6 IP address for the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for `IPAddress`, Route 53 sends a DNS request to resolve the domain name that you specify in `FullyQualifiedDomainName` at the interval that you specify in `RequestInterval`. Using an IP address that is returned by DNS, Route 53 then checks the health of the endpoint.
Use one of the following formats for the value of `IPAddress`:
+  **IPv4 address**: four values between 0 and 255, separated by periods (.), for example, `192.0.2.44`.
+  **IPv6 address**: eight groups of four hexadecimal values, separated by colons (:), for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345`. You can also shorten IPv6 addresses as described in RFC 5952, for example, `2001:db8:85a3::abcd:1:2345`.
If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for `IPAddress`. This ensures that the IP address of your instance never changes. For more information, see the applicable documentation:
+ Linux: [Elastic IP Addresses (EIP)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide for Linux Instances*
+ Windows: [Elastic IP Addresses (EIP)](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide for Windows Instances*
If a health check already has a value for `IPAddress`, you can change the value. However, you can't update an existing health check to add or remove the value of `IPAddress`.
For more information, see [FullyQualifiedDomainName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName).
Constraints: Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:
+  [RFC 5735, Special Use IPv4 Addresses](https://tools.ietf.org/html/rfc5735)
+  [RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space](https://tools.ietf.org/html/rfc6598)
+  [RFC 5156, Special-Use IPv6 Addresses](https://tools.ietf.org/html/rfc5156)
Type: String
Length Constraints: Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`
Required: No

 ** [Port](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-Port"></a>
The port on the endpoint that you want Amazon Route 53 to perform health checks on.
Don't specify a value for `Port` when you specify a value for `Type` of `CLOUDWATCH_METRIC` or `CALCULATED`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** [Regions](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-Regions"></a>
A complex type that contains one `Region` element for each region that you want Amazon Route 53 health checkers to check the specified endpoint from.
Type: Array of strings
Array Members: Minimum number of 3 items. Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `us-east-1 | us-west-1 | us-west-2 | eu-west-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1`
Required: No

 ** [ResetElements](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-ResetElements"></a>
A complex type that contains one `ResettableElementName` element for each element that you want to reset to the default value. Valid values for `ResettableElementName` include the following:
+  `ChildHealthChecks`: Amazon Route 53 resets [ChildHealthChecks](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-ChildHealthChecks) to null.
+  `FullyQualifiedDomainName`: Route 53 resets [FullyQualifiedDomainName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName). to null.
+  `Regions`: Route 53 resets the [Regions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions) list to the default set of regions.
+  `ResourcePath`: Route 53 resets [ResourcePath](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-ResourcePath) to null.
Type: Array of strings
Array Members: Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `FullyQualifiedDomainName | Regions | ResourcePath | ChildHealthChecks`
Required: No

 ** [ResourcePath](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-ResourcePath"></a>
The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html. You can also include query string parameters, for example, `/welcome.html?language=jp&login=y`.
Specify this value only if you want to change it.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** [SearchString](#API_UpdateHealthCheck_RequestSyntax) **   <a name="Route53-UpdateHealthCheck-request-SearchString"></a>
If the value of `Type` is `HTTP_STR_MATCH` or `HTTPS_STR_MATCH`, the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy. (You can't change the value of `Type` when you update a health check.)
Type: String
Length Constraints: Maximum length of 255.
Required: No

## Response Syntax
<a name="API_UpdateHealthCheck_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckResponse>
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
</UpdateHealthCheckResponse>
```

## Response Elements
<a name="API_UpdateHealthCheck_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [UpdateHealthCheckResponse](#API_UpdateHealthCheck_ResponseSyntax) **   <a name="Route53-UpdateHealthCheck-response-UpdateHealthCheckResponse"></a>
Root level tag for the UpdateHealthCheckResponse parameters.
Required: Yes

 ** [HealthCheck](#API_UpdateHealthCheck_ResponseSyntax) **   <a name="Route53-UpdateHealthCheck-response-HealthCheck"></a>
A complex type that contains the response to an `UpdateHealthCheck` request.
Type: [HealthCheck](API_HealthCheck.md) object

## Errors
<a name="API_UpdateHealthCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HealthCheckVersionMismatch **
The value of `HealthCheckVersion` in the request doesn't match the value of `HealthCheckVersion` in the health check.
HTTP Status Code: 409

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheck **
No health check exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_UpdateHealthCheck_Examples"></a>

### Request Syntax for HTTP[S], HTTP[S]\_STR\_MATCH, and TCP Health Checks
<a name="API_UpdateHealthCheck_Example_1"></a>

This example illustrates one usage of UpdateHealthCheck.

```
POST /2013-04-01/healthcheck/health check ID HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <EnableSNI>true | false</EnableSNI>
   <FailureThreshold>number of health checks that must pass or fail to change the status of the health check</FailureThreshold>
   <FullyQualifiedDomainName>domain name of the endpoint to check</FullyQualifiedDomainName>
   <HealthCheckVersion>sequential counter</HealthCheckVersion>
   <Inverted>true | false</Inverted>
   <IPAddress>IP address of the endpoint to check</IPAddress>
   <Port>port on the endpoint to check</Port>
   <Regions>
      <Region>us-west-1 | us-west-2 | us-east-1 | eu-west-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1</Region>
      ...
   </Regions>
   <ResourcePath>path of the file that you want Route 53 to request</ResourcePath>
   <SearchString>if Type is HTTP_STR_MATCH or HTTPS_STR_MATCH, the string to search for in the response body from the specified resource</SearchString>
</UpdateHealthCheckRequest>
```

### Response Syntax for HTTP[S], HTTP[S]\_STR\_MATCH, and TCP Health Checks
<a name="API_UpdateHealthCheck_Example_2"></a>

This example illustrates one usage of UpdateHealthCheck.

```
HTTP/1.1 201 Created
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheck>
      <Id>ID that Route 53 assigned to the health check when you created it</Id>
      <CallerReference>unique description</CallerReference>
      <HealthCheckConfig>
         <EnableSNI>true | false</EnableSNI>
         <FailureThreshold>number of health checks that must pass or fail to change the status of the health check</FailureThreshold>
         <FullyQualifiedDomainName>domain name of the endpoint to check</FullyQualifiedDomainName>
         <Inverted>true | false</Inverted>
         <IPAddress>IP address of the endpoint to check</IPAddress>
         <MeasureLatency>true | false</MeasureLatency>
         <Port>port on the endpoint to check</Port>
         <RequestInterval>10 | 30</RequestInterval>
         <ResourcePath>path of the file that you want Route 53 to request</ResourcePath>
         <SearchString>if Type is HTTP_STR_MATCH or HTTPS_STR_MATCH, the string to search for in the response body from the specified resource</SearchString>
         <Type>HTTP | HTTPS | HTTP_STR_MATCH | HTTPS_STR_MATCH | TCP</Type>
      </HealthCheckConfig>
      <HealthCheckVersion>sequential counter</HealthCheckVersion>
   </HealthCheck>
</UpdateHealthCheckResponse>
```

### Request Syntax for CLOUDWATCH\_METRIC Health Checks
<a name="API_UpdateHealthCheck_Example_3"></a>

This example illustrates one usage of UpdateHealthCheck.

```
POST /2013-04-01/healthcheck/health check ID HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <AlarmIdentifier>
      <Name>name of CloudWatch alarm</Name>
      <Region>region that CloudWatch alarm was created in</Region>
   </AlarmIdentifier>
   <HealthCheckVersion>sequential counter</HealthCheckVersion>
   <InsufficientDataHealthStatus>Healthy | Unhealthy | LastKnownStatus</InsufficientDataHealthStatus>
   <Inverted>true | false</Inverted>
</UpdateHealthCheckRequest>
```

### Response Syntax for CLOUDWATCH\_METRIC Health Checks
<a name="API_UpdateHealthCheck_Example_4"></a>

This example illustrates one usage of UpdateHealthCheck.

```
POST /2013-04-01/healthcheck HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheck>
      <Id>ID that Route 53 assigned to the health check when you created it</Id>
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
         <EvaluationPeriods>number of periods that metric is compared to threshold</EvaluationPeriods>
         <Threshold>value the metric is compared with</Threshold>
         <ComparisonOperator>GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold</ComparisonOperator>
         <Period>duration of a period in seconds</Period>
         <MetricName>name of the metric that's associated with the alarm</MetricName>
         <Namespace>namespace of the metric that the alarm is associated with</Namespace>
         <Statistic>statistic applied to the CloudWatch metric</Statistic>
         <Dimensions>
            <Dimension>
               <Name>name of a dimension for the metric</Name>
               <Value>value of a dimension for the metric</Value>
            </Dimension>
            ...
         </Dimensions>
      </CloudWatchAlarmConfiguration>
      <HealthCheckVersion>sequential counter</HealthCheckVersion>
   </HealthCheck>
</UpdateHealthCheckResponse>
```

### Request Syntax for CALCULATED Health Checks
<a name="API_UpdateHealthCheck_Example_5"></a>

This example illustrates one usage of UpdateHealthCheck.

```
POST /2013-04-01/healthcheck/health check ID HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ChildHealthChecks>
      <ChildHealthCheck>health check ID</ChildHealthCheck>
      ...
   </ChildHealthChecks>
   <HealthCheckVersion>sequential counter</HealthCheckVersion>
   <HealthThreshold>number of health checks that are associated with a CALCULATED health check that must be healthy</HealthThreshold>
   <Inverted>true | false</Inverted>
</UpdateHealthCheckRequest>
```

### Response Syntax for CALCULATED Health Checks
<a name="API_UpdateHealthCheck_Example_6"></a>

This example illustrates one usage of UpdateHealthCheck.

```
HTTP/1.1 201 Created
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHealthCheckResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheck>
      <Id>ID that Route 53 assigned to the health check when you created it</Id>
      <CallerReference>unique description</CallerReference>
      <HealthCheckConfig>
         <ChildHealthChecks>
            <ChildHealthCheck>health check ID</ChildHealthCheck>
            ...
         </ChildHealthChecks>
         <HealthThreshold>number of health checks associated with a CALCULATED health check that must be healthy</HealthThreshold>
         <Inverted>true | false</Inverted>
         <Type>CALCULATED</Type>
      </HealthCheckConfig>
      <HealthCheckVersion>sequential counter</HealthCheckVersion>
   </HealthCheck>
</UpdateHealthCheckResponse>
```

## See Also
<a name="API_UpdateHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/UpdateHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/UpdateHealthCheck)
