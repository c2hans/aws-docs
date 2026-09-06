---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateService.html
---

# UpdateService
<a name="API_UpdateService"></a>

Submits a request to perform the following operations:
+ Update the TTL setting for existing `DnsRecords` configurations
+ Add, update, or delete `HealthCheckConfig` for a specified service
**Note**
You can't add, update, or delete a `HealthCheckCustomConfig` configuration.

For public and private DNS namespaces, note the following:
+ If you omit any existing `DnsRecords` or `HealthCheckConfig` configurations from an `UpdateService` request, the configurations are deleted from the service.
+ If you omit an existing `HealthCheckCustomConfig` configuration from an `UpdateService` request, the configuration isn't deleted from the service.

**Note**
You can't call `UpdateService` and update settings in the following scenarios:
When the service is associated with an HTTP namespace
When the service is associated with a shared namespace and contains instances that were registered by AWS accounts other than the account making the `UpdateService` call

When you update settings for a service, AWS Cloud Map also updates the corresponding settings in all the records and health checks that were created by using the specified service.

## Request Syntax
<a name="API_UpdateService_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "Service": {
      "Description": "{{string}}",
      "DnsConfig": {
         "DnsRecords": [
            {
               "TTL": {{number}},
               "Type": "{{string}}"
            }
         ]
      },
      "HealthCheckConfig": {
         "FailureThreshold": {{number}},
         "ResourcePath": "{{string}}",
         "Type": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_UpdateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_UpdateService_RequestSyntax) **   <a name="cloudmap-UpdateService-request-Id"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to update. If the namespace associated with the service is shared with your AWS account, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Service](#API_UpdateService_RequestSyntax) **   <a name="cloudmap-UpdateService-request-Service"></a>
A complex type that contains the new settings for the service. You can specify a maximum of 30 attributes (key-value pairs).
Type: [ServiceChange](API_ServiceChange.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateService_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_UpdateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_UpdateService_ResponseSyntax) **   <a name="cloudmap-UpdateService-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_UpdateService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The operation is already in progress.
 ** DuplicateOperationId **
The ID of the operation that's already in progress.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_UpdateService_Examples"></a>

### UpdateService Example
<a name="API_UpdateService_Example_1"></a>

This example updates the `TTL` and the `HealthCheckConfig` settings of the specified service.

#### Sample Request
<a name="API_UpdateService_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211814Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdateService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "srv-e4anhexample0004",
    "Service": {
        "HealthCheckConfig": {
            "Type": "HTTP",
            "ResourcePath": "/",
            "FailureThreshold": 1
        },
        "DnsConfig": {
            "DnsRecords": [
                {
                    "Type": "A",
                    "TTL": 60
                }
            ]
        }
    }
}
```

#### Sample Response
<a name="API_UpdateService_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "OperationId":"m35hsdrkxwjffm3xef4bxyy6vc3ewakx-jdn3y5g5"
}
```

### UpdateService Example using ARN
<a name="API_UpdateService_Example_2"></a>

This example updates the `TTL` and the `HealthCheckConfig` settings of a service in a shared namespace using its ARN.

#### Sample Request
<a name="API_UpdateService_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211814Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdateService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
    "Service": {
        "HealthCheckConfig": {
            "Type": "HTTP",
            "ResourcePath": "/",
            "FailureThreshold": 1
        },
        "DnsConfig": {
            "DnsRecords": [
                {
                    "Type": "A",
                    "TTL": 60
                }
            ]
        }
    }
}
```

#### Sample Response
<a name="API_UpdateService_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "OperationId":"m35hsdrkxwjffm3xef4bxyy6vc3ewakx-jdn3y5g5"
}
```

## See Also
<a name="API_UpdateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/UpdateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/UpdateService)
