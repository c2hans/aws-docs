---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_GetService.html
---

# GetService
<a name="API_GetService"></a>

Gets the settings for a specified service.

## Request Syntax
<a name="API_GetService_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_GetService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_GetService_RequestSyntax) **   <a name="cloudmap-GetService-request-Id"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to get settings for. For services created by consumers in a shared namespace, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_GetService_ResponseSyntax"></a>

```
{
   "Service": {
      "Arn": "string",
      "CreateDate": number,
      "CreatedByAccount": "string",
      "CreatorRequestId": "string",
      "Description": "string",
      "DnsConfig": {
         "DnsRecords": [
            {
               "TTL": number,
               "Type": "string"
            }
         ],
         "NamespaceId": "string",
         "RoutingPolicy": "string"
      },
      "HealthCheckConfig": {
         "FailureThreshold": number,
         "ResourcePath": "string",
         "Type": "string"
      },
      "HealthCheckCustomConfig": {
         "FailureThreshold": number
      },
      "Id": "string",
      "InstanceCount": number,
      "Name": "string",
      "NamespaceId": "string",
      "ResourceOwner": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_GetService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Service](#API_GetService_ResponseSyntax) **   <a name="cloudmap-GetService-response-Service"></a>
A complex type that contains information about the service.
Type: [Service](API_Service.md) object

## Errors
<a name="API_GetService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_GetService_Examples"></a>

### GetService Example
<a name="API_GetService_Example_1"></a>

This example request retrieves information about the specified service.

#### Sample Request
<a name="API_GetService_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211709Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetService_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Service": {
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
        "CreateDate": "20181118T211707Z",
        "CreatorRequestId": "example-creator-request-id-0004",
        "Description": "Example.com AWS Cloud Map HTTP Service",
        "HealthCheckConfig": {
            "FailureThreshold": 1,
            "ResourcePath": "/",
            "Type": "HTTPS"
        },
        "Id": "srv-e4anhexample0004",
        "Name": "example-http-service",
        "NamespaceId": "ns-e4anhexample0004",
        "ResourceOwner": "123456789012",
        "CreatedByAccount": "123456789012"
    }
}
```

### GetService Example using ARN
<a name="API_GetService_Example_2"></a>

This example request retrieves information about a service in a shared namespace using its ARN. The service was created by account `11112222333` in a namespace shared by `123456789012`.

#### Sample Request
<a name="API_GetService_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211709Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetService_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Service": {
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
        "CreateDate": "20181118T211707Z",
        "CreatorRequestId": "example-creator-request-id-0004",
        "Description": "Example.com AWS Cloud Map HTTP Service",
        "HealthCheckConfig": {
            "FailureThreshold": 1,
            "ResourcePath": "/",
            "Type": "HTTPS"
        },
        "Id": "srv-e4anhexample0004",
        "Name": "example-http-service",
        "NamespaceId": "ns-e4anhexample0004",
        "ResourceOwner": "123456789012",
        "CreatedByAccount": "111122223333"
    }
}
```

## See Also
<a name="API_GetService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/GetService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/GetService)
