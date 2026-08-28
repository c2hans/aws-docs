---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html
---

# RegisterInstance
<a name="API_RegisterInstance"></a>

Creates or updates one or more records and, optionally, creates a health check based on the settings in a specified service. When you submit a `RegisterInstance` request, the following occurs:
+ For each DNS record that you define in the service that's specified by `ServiceId`, a record is created or updated in the hosted zone that's associated with the corresponding namespace.
+ If the service includes `HealthCheckConfig`, a health check is created based on the settings in the health check configuration.
+ The health check, if any, is associated with each of the new or updated records.

**Important**
One `RegisterInstance` request must complete before you can submit another request and specify the same service ID and instance ID.

For more information, see [CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html).

When AWS Cloud Map receives a DNS query for the specified DNS name, it returns the applicable value:
+  **If the health check is healthy**: returns all the records
+  **If the health check is unhealthy**: returns the applicable value for the last healthy instance
+  **If you didn't specify a health check configuration**: returns all the records

For the current quota on the number of instances that you can register using the same namespace and using the same service, see [AWS Cloud Map quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html) in the * AWS Cloud Map Developer Guide*.

## Request Syntax
<a name="API_RegisterInstance_RequestSyntax"></a>

```
{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "CreatorRequestId": "{{string}}",
   "InstanceId": "{{string}}",
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attributes](#API_RegisterInstance_RequestSyntax) **   <a name="cloudmap-RegisterInstance-request-Attributes"></a>
A string map that contains the following information for the service that you specify in `ServiceId`:
+ The attributes that apply to the records that are defined in the service.
+ For each attribute, the applicable value.
Do not include sensitive information in the attributes if the namespace is discoverable by public DNS queries.
The following are the supported attribute keys.
AWS\_ALIAS\_DNS\_NAME
If you want AWS Cloud Map to create an Amazon Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that's associated with the load balancer. For information about how to get the DNS name, see "DNSName" in the topic [AliasTarget](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html) in the *Route 53 API Reference*.
Note the following:
+ The configuration for the service that's specified by `ServiceId` must include settings for an `A` record, an `AAAA` record, or both.
+ In the service that's specified by `ServiceId`, the value of `RoutingPolicy` must be `WEIGHTED`.
+ If the service that's specified by `ServiceId` includes `HealthCheckConfig` settings, AWS Cloud Map will create the Route 53 health check, but it doesn't associate the health check with the alias record.
+  AWS Cloud Map currently doesn't support creating alias records that route traffic to AWS resources other than Elastic Load Balancing load balancers.
+ If you specify a value for `AWS_ALIAS_DNS_NAME`, don't specify values for any of the `AWS_INSTANCE` attributes.
+ The `AWS_ALIAS_DNS_NAME` is not supported in the GovCloud (US) Regions.
AWS\_EC2\_INSTANCE\_ID
 *HTTP namespaces only.* The Amazon EC2 instance ID for the instance. If the `AWS_EC2_INSTANCE_ID` attribute is specified, then the only other attribute that can be specified is `AWS_INIT_HEALTH_STATUS`. When the `AWS_EC2_INSTANCE_ID` attribute is specified, then the `AWS_INSTANCE_IPV4` attribute will be filled out with the primary private IPv4 address.
AWS\_INIT\_HEALTH\_STATUS
If the service configuration includes `HealthCheckCustomConfig`, you can optionally use `AWS_INIT_HEALTH_STATUS` to specify the initial status of the custom health check, `HEALTHY` or `UNHEALTHY`. If you don't specify a value for `AWS_INIT_HEALTH_STATUS`, the initial status is `HEALTHY`.
AWS\_INSTANCE\_CNAME
If the service configuration includes a `CNAME` record, the domain name that you want Route 53 to return in response to DNS queries (for example, `example.com`).
This value is required if the service specified by `ServiceId` includes settings for an `CNAME` record.
AWS\_INSTANCE\_IPV4
If the service configuration includes an `A` record, the IPv4 address that you want Route 53 to return in response to DNS queries (for example, `192.0.2.44`).
This value is required if the service specified by `ServiceId` includes settings for an `A` record. If the service includes settings for an `SRV` record, you must specify a value for `AWS_INSTANCE_IPV4`, `AWS_INSTANCE_IPV6`, or both.
AWS\_INSTANCE\_IPV6
If the service configuration includes an `AAAA` record, the IPv6 address that you want Route 53 to return in response to DNS queries (for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345`).
This value is required if the service specified by `ServiceId` includes settings for an `AAAA` record. If the service includes settings for an `SRV` record, you must specify a value for `AWS_INSTANCE_IPV4`, `AWS_INSTANCE_IPV6`, or both.
AWS\_INSTANCE\_PORT
If the service includes an `SRV` record, the value that you want Route 53 to return for the port.
If the service includes `HealthCheckConfig`, the port on the endpoint that you want Route 53 to send requests to.
This value is required if you specified settings for an `SRV` record or a Route 53 health check when you created the service.
Custom attributes
You can add up to 30 custom attributes. For each key-value pair, the maximum length of the attribute name is 255 characters, and the maximum length of the attribute value is 1,024 characters. The total size of all provided attributes (sum of all keys and values) must not exceed 5,000 characters.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9!-~]+$`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
Required: Yes

 ** [CreatorRequestId](#API_RegisterInstance_RequestSyntax) **   <a name="cloudmap-RegisterInstance-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed `RegisterInstance` requests to be retried without the risk of executing the operation twice. You must use a unique `CreatorRequestId` string every time you submit a `RegisterInstance` request if you're registering additional instances for the same namespace and service. `CreatorRequestId` can be any unique string (for example, a date/time stamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** [InstanceId](#API_RegisterInstance_RequestSyntax) **   <a name="cloudmap-RegisterInstance-request-InstanceId"></a>
An identifier that you want to associate with the instance. Note the following:
+ If the service that's specified by `ServiceId` includes settings for an `SRV` record, the value of `InstanceId` is automatically included as part of the value for the `SRV` record. For more information, see [DnsRecord > Type](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsRecord.html#cloudmap-Type-DnsRecord-Type).
+ You can use this value to update an existing instance.
+ To register a new instance, you must specify a value that's unique among instances that you register by using the same service.
+ If you specify an existing `InstanceId` and `ServiceId`, AWS Cloud Map updates the existing DNS records, if any. If there's also an existing health check, AWS Cloud Map deletes the old health check and creates a new one.
**Note**
The health check isn't deleted immediately, so it will still appear for a while if you submit a `ListHealthChecks` request, for example.
Do not include sensitive information in `InstanceId` if the namespace is discoverable by public DNS queries and any `Type` member of `DnsRecord` for the service contains `SRV` because the `InstanceId` is discoverable by public DNS queries.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[0-9a-zA-Z_/:.@-]+$`
Required: Yes

 ** [ServiceId](#API_RegisterInstance_RequestSyntax) **   <a name="cloudmap-RegisterInstance-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to use for settings for the instance. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_RegisterInstance_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_RegisterInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_RegisterInstance_ResponseSyntax) **   <a name="cloudmap-RegisterInstance-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_RegisterInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The operation is already in progress.
 ** DuplicateOperationId **
The ID of the operation that's already in progress.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ResourceInUse **
The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
The resource can't be created because you've reached the quota on the number of resources.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_RegisterInstance_Examples"></a>

### RegisterInstance Example
<a name="API_RegisterInstance_Example_1"></a>

This example request registers an instance in the specified service.

#### Sample Request
<a name="API_RegisterInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211815Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.RegisterInstance
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "CreatorRequestId": "example-creator-request-id-0001",
    "InstanceId": "i-abcd1234",
    "Attributes": {
        "AWS_INSTANCE_IPV4": "192.0.2.44",
        "AWS_INSTANCE_PORT": "80",
        "color": "green",
        "region": "us-west-2",
        "stage": "beta"
    },
    "ServiceId": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_RegisterInstance_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "OperationId":"dns1voqozuhfet5kzxoxg-a-response-example"
}
```

### RegisterInstance Example using service ARN
<a name="API_RegisterInstance_Example_2"></a>

This example request registers an instance in a service within a shared namespace using the service ARN.

#### Sample Request
<a name="API_RegisterInstance_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211815Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.RegisterInstance
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "CreatorRequestId": "example-creator-request-id-0001",
    "InstanceId": "i-abcd1234",
    "Attributes": {
        "AWS_INSTANCE_IPV4": "192.0.2.44",
        "AWS_INSTANCE_PORT": "80",
        "color": "green",
        "region": "us-west-2",
        "stage": "beta"
    },
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_RegisterInstance_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "OperationId":"dns1voqozuhfet5kzxoxg-a-response-example"
}
```

## See Also
<a name="API_RegisterInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/RegisterInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/RegisterInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
