---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateInstanceCustomHealthStatus.html
---

# UpdateInstanceCustomHealthStatus
<a name="API_UpdateInstanceCustomHealthStatus"></a>

Submits a request to change the health status of a custom health check to healthy or unhealthy.

You can use `UpdateInstanceCustomHealthStatus` to change the status only for custom health checks, which you define using `HealthCheckCustomConfig` when you create a service. You can't use it to change the status for Route 53 health checks, which you define using `HealthCheckConfig`.

For more information, see [HealthCheckCustomConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html).

## Request Syntax
<a name="API_UpdateInstanceCustomHealthStatus_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "ServiceId": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateInstanceCustomHealthStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_UpdateInstanceCustomHealthStatus_RequestSyntax) **   <a name="cloudmap-UpdateInstanceCustomHealthStatus-request-InstanceId"></a>
The ID of the instance that you want to change the health status for.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** [ServiceId](#API_UpdateInstanceCustomHealthStatus_RequestSyntax) **   <a name="cloudmap-UpdateInstanceCustomHealthStatus-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that includes the configuration for the custom health check that you want to change the status for. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Status](#API_UpdateInstanceCustomHealthStatus_RequestSyntax) **   <a name="cloudmap-UpdateInstanceCustomHealthStatus-request-Status"></a>
The new status of the instance, `HEALTHY` or `UNHEALTHY`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: Yes

## Response Elements
<a name="API_UpdateInstanceCustomHealthStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInstanceCustomHealthStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomHealthNotFound **
The health check for the instance that's specified by `ServiceId` and `InstanceId` isn't a custom health check.
HTTP Status Code: 400

 ** InstanceNotFound **
No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_UpdateInstanceCustomHealthStatus_Examples"></a>

### UpdateInstanceCustomHealthStatus Example
<a name="API_UpdateInstanceCustomHealthStatus_Example_1"></a>

This example updates the custom health status for the specified instance to `HEALTHY`.

#### Sample Request
<a name="API_UpdateInstanceCustomHealthStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211819Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdateInstanceCustomHealthStatus
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "InstanceId": "i-abcd1234",
    "ServiceId": "srv-e4anhexample0004",
    "Status": "HEALTHY"
}
```

#### Sample Response
<a name="API_UpdateInstanceCustomHealthStatus_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

### UpdateInstanceCustomHealthStatus Example using service ARN
<a name="API_UpdateInstanceCustomHealthStatus_Example_2"></a>

This example updates the custom health status for an instance in a service within a shared namespace using the service ARN.

#### Sample Request
<a name="API_UpdateInstanceCustomHealthStatus_Example_2_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211819Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdateInstanceCustomHealthStatus
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "InstanceId": "i-abcd1234",
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
    "Status": "HEALTHY"
}
```

#### Sample Response
<a name="API_UpdateInstanceCustomHealthStatus_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

## See Also
<a name="API_UpdateInstanceCustomHealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/UpdateInstanceCustomHealthStatus)
