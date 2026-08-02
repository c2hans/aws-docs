---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckStatus.html
---

# GetHealthCheckStatus
<a name="API_GetHealthCheckStatus"></a>

Gets status of a specified health check.

**Important**
This API is intended for use during development to diagnose behavior. It doesn’t support production use-cases with high query rates that require immediate and actionable responses.

## Request Syntax
<a name="API_GetHealthCheckStatus_RequestSyntax"></a>

```
GET /2013-04-01/healthcheck/{{HealthCheckId}}/status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHealthCheckStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckId](#API_GetHealthCheckStatus_RequestSyntax) **   <a name="Route53-GetHealthCheckStatus-request-uri-HealthCheckId"></a>
The ID for the health check that you want the current status for. When you created the health check, `CreateHealthCheck` returned the ID in the response, in the `HealthCheckId` element.
If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use `GetHealthCheckStatus` to get the status of a calculated health check.
Length Constraints: Maximum length of 64.
Required: Yes

## Request Body
<a name="API_GetHealthCheckStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHealthCheckStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckStatusResponse>
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
</GetHealthCheckStatusResponse>
```

## Response Elements
<a name="API_GetHealthCheckStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHealthCheckStatusResponse](#API_GetHealthCheckStatus_ResponseSyntax) **   <a name="Route53-GetHealthCheckStatus-response-GetHealthCheckStatusResponse"></a>
Root level tag for the GetHealthCheckStatusResponse parameters.
Required: Yes

 ** [HealthCheckObservations](#API_GetHealthCheckStatus_ResponseSyntax) **   <a name="Route53-GetHealthCheckStatus-response-HealthCheckObservations"></a>
A list that contains one `HealthCheckObservation` element for each Amazon Route 53 health checker that is reporting a status about the health check endpoint.
Type: Array of [HealthCheckObservation](API_HealthCheckObservation.md) objects

## Errors
<a name="API_GetHealthCheckStatus_Errors"></a>

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
<a name="API_GetHealthCheckStatus_Examples"></a>

### Example Request
<a name="API_GetHealthCheckStatus_Example_1"></a>

This example illustrates one usage of GetHealthCheckStatus.

```
GET /2013-04-01/healthcheck/018927304987/status
```

### Example Response
<a name="API_GetHealthCheckStatus_Example_2"></a>

This example illustrates one usage of GetHealthCheckStatus.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckStatusResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheckObservations>
      <HealthCheckObservation>
         <IPAddress>192.0.2.226</IPAddress>
         <Region>us-east-2</Region>
         <StatusReport>
            <Status>Success: HTTP Status Code: 200. Resolved IP: 192.0.2.2. OK</Status>
            <CheckedTime>2014-10-27T17:48:25.038Z</CheckedTime>
         </StatusReport>
      </HealthCheckObservation>
      <HealthCheckObservation>
         <IPAddress>192.0.2.56</IPAddress>
         <Region>us-west-1</Region>
         <StatusReport>
            <Status>Success: HTTP Status Code: 200. Resolved IP: 192.0.2.14. OK</Status>
            <CheckedTime>2014-10-27T17:48:16.751Z</CheckedTime>
         </StatusReport>
      </HealthCheckObservation>
      ...
   </HealthCheckObservations>
</GetHealthCheckStatusResponse>
```

## See Also
<a name="API_GetHealthCheckStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHealthCheckStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHealthCheckStatus)
