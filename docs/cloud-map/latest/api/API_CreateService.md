---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html
---

# CreateService
<a name="API_CreateService"></a>

Creates a service. This action defines the configuration for the following entities:
+ For public and private DNS namespaces, one of the following combinations of DNS records in Amazon Route 53:
  +  `A`
  +  `AAAA`
  +  `A` and `AAAA`
  +  `SRV`
  +  `CNAME`
+ Optionally, a health check

After you create the service, you can submit a [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) request, and AWS Cloud Map uses the values in the configuration to create the specified entities.

For the current quota on the number of instances that you can register using the same namespace and using the same service, see [AWS Cloud Map quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html) in the * AWS Cloud Map Developer Guide*.

## Request Syntax
<a name="API_CreateService_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "Description": "{{string}}",
   "DnsConfig": {
      "DnsRecords": [
         {
            "TTL": {{number}},
            "Type": "{{string}}"
         }
      ],
      "NamespaceId": "{{string}}",
      "RoutingPolicy": "{{string}}"
   },
   "HealthCheckConfig": {
      "FailureThreshold": {{number}},
      "ResourcePath": "{{string}}",
      "Type": "{{string}}"
   },
   "HealthCheckCustomConfig": {
      "FailureThreshold": {{number}}
   },
   "Name": "{{string}}",
   "NamespaceId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed `CreateService` requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string (for example, a date/timestamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** [Description](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-Description"></a>
A description for the service.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [DnsConfig](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-DnsConfig"></a>
A complex type that contains information about the Amazon Route 53 records that you want AWS Cloud Map to create when you register an instance.
Type: [DnsConfig](API_DnsConfig.md) object
Required: No

 ** [HealthCheckConfig](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-HealthCheckConfig"></a>
 *Public DNS and HTTP namespaces only.* A complex type that contains settings for an optional Route 53 health check. If you specify settings for a health check, AWS Cloud Map associates the health check with all the Route 53 DNS records that you specify in `DnsConfig`.
If you specify a health check configuration, you can specify either `HealthCheckCustomConfig` or `HealthCheckConfig` but not both.
For information about the charges for health checks, see [AWS Cloud Map Pricing](http://aws.amazon.com/cloud-map/pricing/).
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: No

 ** [HealthCheckCustomConfig](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-HealthCheckCustomConfig"></a>
A complex type that contains information about an optional custom health check.
If you specify a health check configuration, you can specify either `HealthCheckCustomConfig` or `HealthCheckConfig` but not both.
You can't add, update, or delete a `HealthCheckCustomConfig` configuration from an existing service.
Type: [HealthCheckCustomConfig](API_HealthCheckCustomConfig.md) object
Required: No

 ** [Name](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-Name"></a>
The name that you want to assign to the service.
Do not include sensitive information in the name if the namespace is discoverable by public DNS queries.
If you want AWS Cloud Map to create an `SRV` record when you register an instance and you're using a system that requires a specific `SRV` format, such as [HAProxy](http://www.haproxy.org/), specify the following for `Name`:
+ Start the name with an underscore (\_), such as `_exampleservice`.
+ End the name with *.\_protocol*, such as `._tcp`.
When you register an instance, AWS Cloud Map creates an `SRV` record and assigns a name to the record by concatenating the service name and the namespace name (for example,
 `_exampleservice._tcp.example.com`).
For services that are accessible by DNS queries, you can't create multiple services with names that differ only by case (such as EXAMPLE and example). Otherwise, these services have the same DNS name and can't be distinguished. However, if you use a namespace that's only accessible by API calls, then you can create services that with names that differ only by case.
Type: String
Pattern: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`
Required: Yes

 ** [NamespaceId](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-NamespaceId"></a>
The ID or Amazon Resource Name (ARN) of the namespace that you want to use to create the service. For namespaces shared with your AWS account, specify the namespace ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** [Tags](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-Tags"></a>
The tags to add to the service. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Type](#API_CreateService_RequestSyntax) **   <a name="cloudmap-CreateService-request-Type"></a>
If present, specifies that the service instances are only discoverable using the `DiscoverInstances` API operation. No DNS records is registered for the service instances. The only valid value is `HTTP`.
Type: String
Valid Values: `HTTP`
Required: No

## Response Syntax
<a name="API_CreateService_ResponseSyntax"></a>

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
<a name="API_CreateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Service](#API_CreateService_ResponseSyntax) **   <a name="cloudmap-CreateService-response-Service"></a>
A complex type that contains information about the new service.
Type: [Service](API_Service.md) object

## Errors
<a name="API_CreateService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** NamespaceNotFound **
No namespace exists with the specified ID.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
The resource can't be created because you've reached the quota on the number of resources.
HTTP Status Code: 400

 ** ServiceAlreadyExists **
The service can't be created because a service with the same name already exists.
 ** CreatorRequestId **
The `CreatorRequestId` that was used to create the service.
 ** ServiceArn **
The ARN of the existing service.
 ** ServiceId **
The ID of the existing service.
HTTP Status Code: 400

 ** TooManyTagsException **
The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.
 ** ResourceName **
The name of the resource.
HTTP Status Code: 400

## Examples
<a name="API_CreateService_Examples"></a>

### Creating a service with Amazon Route 53 health check
<a name="API_CreateService_Example_1"></a>

The example creates a service with a Amazon Route 53 health check configured.

#### Sample Request
<a name="API_CreateService_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211706Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.CreateService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "CreatorRequestId": "example-creator-request-id-0004",
    "NamespaceId": "ns-e4anhexample0004",
    "Name": "example-http-service",
    "HealthCheckConfig": {
        "Type": "HTTPS",
        "ResourcePath": "/",
        "FailureThreshold": 1
    },
    "Description": "Example.com AWS Cloud Map HTTP Service"
}
```

#### Sample Response
<a name="API_CreateService_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Service": {
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
        "CreateDate": "20181118T211707Z",
        "CreatedByAccount" "123456789012",
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
        "ResourceOwner": "123456789012"
    }
}
```

### Creating a service using namespace ARN
<a name="API_CreateService_Example_2"></a>

In this example, the `CreateService` request involves a namespace that is shared with the account `111122223333` by account `123456789012`. As a consumer of the shared namespace, the requester must include the namespace ARN in the request.

#### Sample Request
<a name="API_CreateService_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211706Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.CreateService
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "CreatorRequestId": "example-creator-request-id-0007",
    "NamespaceId": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e1tpmexample0001",
    "Name": "example-http-service",
    "HealthCheckConfig": {
        "Type": "HTTPS",
        "ResourcePath": "/",
        "FailureThreshold": 1
    },
    "Description": "Example.com AWS Cloud Map HTTP Service"
}
```

#### Sample Response
<a name="API_CreateService_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Service": {
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0001",
        "CreateDate": "20181118T211707Z",
        "CreatedByAccount": "111122223333"
        "CreatorRequestId": "example-creator-request-id-0007",
        "Description": "Example.com AWS Cloud Map HTTP Service",
        "HealthCheckConfig": {
            "FailureThreshold": 1,
            "ResourcePath": "/",
            "Type": "HTTPS"
        },
        "Id": "srv-e4anhexample0001",
        "Name": "example-http-service",
        "NamespaceId": "ns-e1tpmexample0001",
        "ResourceOwner": "123456789012"
    }
}
```

## See Also
<a name="API_CreateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/CreateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/CreateService)
