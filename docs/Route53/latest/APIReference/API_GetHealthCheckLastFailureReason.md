---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckLastFailureReason.html
---

# GetHealthCheckLastFailureReason
<a name="API_GetHealthCheckLastFailureReason"></a>

Gets the reason that a specified health check failed most recently.

## Request Syntax
<a name="API_GetHealthCheckLastFailureReason_RequestSyntax"></a>

```
GET /2013-04-01/healthcheck/{{HealthCheckId}}/lastfailurereason HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHealthCheckLastFailureReason_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckId](#API_GetHealthCheckLastFailureReason_RequestSyntax) **   <a name="Route53-GetHealthCheckLastFailureReason-request-uri-HealthCheckId"></a>
The ID for the health check for which you want the last failure reason. When you created the health check, `CreateHealthCheck` returned the ID in the response, in the `HealthCheckId` element.
If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use `GetHealthCheckLastFailureReason` for a calculated health check.
Length Constraints: Maximum length of 64.
Required: Yes

## Request Body
<a name="API_GetHealthCheckLastFailureReason_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHealthCheckLastFailureReason_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckLastFailureReasonResponse>
   <HealthCheckObservations>
      <HealthCheckObservation>
         <IPAddress>string</IPAddress>
         <Region>string</Region>
         <StatusReport>
            <CheckedTime>timestamp</CheckedTime>
            <Status>string</Status>
         </StatusReport>
      </HealthCheckObservation>
   </HealthCheckObservations>
</GetHealthCheckLastFailureReasonResponse>
```

## Response Elements
<a name="API_GetHealthCheckLastFailureReason_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHealthCheckLastFailureReasonResponse](#API_GetHealthCheckLastFailureReason_ResponseSyntax) **   <a name="Route53-GetHealthCheckLastFailureReason-response-GetHealthCheckLastFailureReasonResponse"></a>
Root level tag for the GetHealthCheckLastFailureReasonResponse parameters.
Required: Yes

 ** [HealthCheckObservations](#API_GetHealthCheckLastFailureReason_ResponseSyntax) **   <a name="Route53-GetHealthCheckLastFailureReason-response-HealthCheckObservations"></a>
A list that contains one `Observation` element for each Amazon Route 53 health checker that is reporting a last failure reason.
Type: Array of [HealthCheckObservation](API_HealthCheckObservation.md) objects

## Errors
<a name="API_GetHealthCheckLastFailureReason_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheck **
No health check exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_GetHealthCheckLastFailureReason_Examples"></a>

### Example Request
<a name="API_GetHealthCheckLastFailureReason_Example_1"></a>

This example illustrates one usage of GetHealthCheckLastFailureReason.

```
GET /2013-04-01/healthcheck/018927304987/lastfailurereason
```

### Example Response
<a name="API_GetHealthCheckLastFailureReason_Example_2"></a>

This example illustrates one usage of GetHealthCheckLastFailureReason.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckLastFailureReasonResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheckObservations>
      <HealthCheckObservation>
         <IPAddress>192.0.2.197</IPAddress>
         <StatusReport>
            <Status>Failure: The health checker could not establish a connection within the timeout limit.</Status>
            <CheckedTime>2014-10-25T23:51:20.603Z</CheckedTime>
         </StatusReport>
      </HealthCheckObservation>
      <HealthCheckObservation>
         <IPAddress>192.0.2.226</IPAddress>
         <StatusReport>
            <Status>The health check endpoint has not failed since the Route 53 health checker for this endpoint restarted at 2014-10-24T02:55:12.106+00:00</Status>
            <CheckedTime>2014-10-24T03:02:48.809Z</CheckedTime>
         </StatusReport>
      </HealthCheckObservation>
      ...
   </HealthCheckObservations>
<GetHealthCheckLastFailureReasonResponse>
```

## See Also
<a name="API_GetHealthCheckLastFailureReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHealthCheckLastFailureReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHealthCheckLastFailureReason)
