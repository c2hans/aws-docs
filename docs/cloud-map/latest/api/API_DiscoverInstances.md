---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html
---

# DiscoverInstances
<a name="API_DiscoverInstances"></a>

Discovers registered instances for a specified namespace and service. You can use `DiscoverInstances` to discover instances for any type of namespace. `DiscoverInstances` returns a randomized list of instances allowing customers to distribute traffic evenly across instances. For public and private DNS namespaces, you can also use DNS queries to discover instances.

## Request Syntax
<a name="API_DiscoverInstances_RequestSyntax"></a>

```
{
   "HealthStatus": "{{string}}",
   "MaxResults": {{number}},
   "NamespaceName": "{{string}}",
   "OptionalParameters": {
      "{{string}}" : "{{string}}"
   },
   "OwnerAccount": "{{string}}",
   "QueryParameters": {
      "{{string}}" : "{{string}}"
   },
   "ServiceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DiscoverInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HealthStatus](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-HealthStatus"></a>
The health status of the instances that you want to discover. This parameter is ignored for services that don't have a health check configured, and all instances are returned.
HEALTHY
Returns healthy instances.
UNHEALTHY
Returns unhealthy instances.
ALL
Returns all instances.
HEALTHY\_OR\_ELSE\_ALL
Returns healthy instances, unless none are reporting a healthy state. In that case, return all instances. This is also called failing open.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | ALL | HEALTHY_OR_ELSE_ALL`
Required: No

 ** [MaxResults](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-MaxResults"></a>
The maximum number of instances that you want AWS Cloud Map to return in the response to a `DiscoverInstances` request. If you don't specify a value for `MaxResults`, AWS Cloud Map returns up to 100 instances.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NamespaceName](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-NamespaceName"></a>
The `HttpName` name of the namespace. The `HttpName` is found in the `HttpProperties` member of the `Properties` member of the namespace. In most cases, `Name` and `HttpName` match. However, if you reuse `Name` for namespace creation, a generated hash is added to `HttpName` to distinguish the two.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[!-~]{1,1024}$`
Required: Yes

 ** [OptionalParameters](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-OptionalParameters"></a>
Opportunistic filters to scope the results based on custom attributes. If there are instances that match both the filters specified in both the `QueryParameters` parameter and this parameter, all of these instances are returned. Otherwise, the filters are ignored, and only instances that match the filters that are specified in the `QueryParameters` parameter are returned.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9!-~]+$`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
Required: No

 ** [OwnerAccount](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-OwnerAccount"></a>
The ID of the AWS account that owns the namespace associated with the instance, as specified in the namespace `ResourceOwner` field. For instances associated with namespaces that are shared with your account, you must specify an `OwnerAccount`.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** [QueryParameters](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-QueryParameters"></a>
Filters to scope the results based on custom attributes for the instance (for example, `{version=v1, az=1a}`). Only instances that match all the specified key-value pairs are returned.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9!-~]+$`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
Required: No

 ** [ServiceName](#API_DiscoverInstances_RequestSyntax) **   <a name="cloudmap-DiscoverInstances-request-ServiceName"></a>
The name of the service that you specified when you registered the instance.
Type: String
Pattern: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`
Required: Yes

## Response Syntax
<a name="API_DiscoverInstances_ResponseSyntax"></a>

```
{
   "Instances": [
      {
         "Attributes": {
            "string" : "string"
         },
         "HealthStatus": "string",
         "InstanceId": "string",
         "NamespaceName": "string",
         "ServiceName": "string"
      }
   ],
   "InstancesRevision": number
}
```

## Response Elements
<a name="API_DiscoverInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_DiscoverInstances_ResponseSyntax) **   <a name="cloudmap-DiscoverInstances-response-Instances"></a>
A complex type that contains one `HttpInstanceSummary` for each registered instance.
Type: Array of [HttpInstanceSummary](API_HttpInstanceSummary.md) objects

 ** [InstancesRevision](#API_DiscoverInstances_ResponseSyntax) **   <a name="cloudmap-DiscoverInstances-response-InstancesRevision"></a>
The increasing revision associated to the response Instances list. If a new instance is registered or deregistered, the `InstancesRevision` updates. The health status updates don't update `InstancesRevision`.
Type: Long

## Errors
<a name="API_DiscoverInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** NamespaceNotFound **
No namespace exists with the specified ID.
HTTP Status Code: 400

 ** RequestLimitExceeded **
The operation can't be completed because you've reached the quota for the number of requests. For more information, see [AWS Cloud Map API request throttling quota](https://docs.aws.amazon.com/cloud-map/latest/dg/throttling.html) in the * AWS Cloud Map Developer Guide*.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_DiscoverInstances_Examples"></a>

### DiscoverInstances Example
<a name="API_DiscoverInstances_Example_1"></a>

This example discovers registered instances for the specified service and namespace.

#### Sample Request
<a name="API_DiscoverInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211819Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DiscoverInstances
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "NamespaceName": "example-public-dns.com",
    "ServiceName": "example-dns-pub-service"
}
```

#### Sample Response
<a name="API_DiscoverInstances_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Instances": [
        {
            "Attributes": {
                "AWS_INSTANCE_IPV4": "192.0.2.44",
                "AWS_INSTANCE_PORT": "80",
                "color": "green",
                "region": "us-west-2",
                "stage": "beta"
            },
            "HealthStatus": "HEALTHY",
            "InstanceId": "i-abcd1234",
            "NamespaceName": "example-public-dns.com",
            "ServiceName": "example-dns-pub-service"
        }
    ],
    "InstancesRevision": 2
}
```

### DiscoverInstances Example using OwnerAccount
<a name="API_DiscoverInstances_Example_2"></a>

This example discovers registered instances for a service in a shared namespace by specifying the OwnerAccount.

#### Sample Request
<a name="API_DiscoverInstances_Example_2_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211819Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DiscoverInstances
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "NamespaceName": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e1tpmexample0001",
    "ServiceName": "example-dns-pub-service",
    "OwnerAccount": "123456789012"
}
```

#### Sample Response
<a name="API_DiscoverInstances_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Instances": [
        {
            "Attributes": {
                "AWS_INSTANCE_IPV4": "192.0.2.44",
                "AWS_INSTANCE_PORT": "80",
                "color": "green",
                "region": "us-west-2",
                "stage": "beta"
            },
            "HealthStatus": "HEALTHY",
            "InstanceId": "i-abcd1234",
            "NamespaceName": "example-public-dns.com",
            "ServiceName": "example-dns-pub-service"
        }
    ],
    "InstancesRevision": 2
}
```

## See Also
<a name="API_DiscoverInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/DiscoverInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DiscoverInstances)
