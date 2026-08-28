---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstancesRevision.html
---

# DiscoverInstancesRevision
<a name="API_DiscoverInstancesRevision"></a>

Discovers the increasing revision associated with an instance.

## Request Syntax
<a name="API_DiscoverInstancesRevision_RequestSyntax"></a>

```
{
   "NamespaceName": "{{string}}",
   "OwnerAccount": "{{string}}",
   "ServiceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DiscoverInstancesRevision_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NamespaceName](#API_DiscoverInstancesRevision_RequestSyntax) **   <a name="cloudmap-DiscoverInstancesRevision-request-NamespaceName"></a>
The `HttpName` name of the namespace. The `HttpName` is found in the `HttpProperties` member of the `Properties` member of the namespace.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[!-~]{1,1024}$`
Required: Yes

 ** [OwnerAccount](#API_DiscoverInstancesRevision_RequestSyntax) **   <a name="cloudmap-DiscoverInstancesRevision-request-OwnerAccount"></a>
The ID of the AWS account that owns the namespace associated with the instance, as specified in the namespace `ResourceOwner` field. For instances associated with namespaces that are shared with your account, you must specify an `OwnerAccount`. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** [ServiceName](#API_DiscoverInstancesRevision_RequestSyntax) **   <a name="cloudmap-DiscoverInstancesRevision-request-ServiceName"></a>
The name of the service that you specified when you registered the instance.
Type: String
Pattern: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`
Required: Yes

## Response Syntax
<a name="API_DiscoverInstancesRevision_ResponseSyntax"></a>

```
{
   "InstancesRevision": number
}
```

## Response Elements
<a name="API_DiscoverInstancesRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstancesRevision](#API_DiscoverInstancesRevision_ResponseSyntax) **   <a name="cloudmap-DiscoverInstancesRevision-response-InstancesRevision"></a>
The increasing revision associated to the response Instances list. If a new instance is registered or deregistered, the `InstancesRevision` updates. The health status updates don't update `InstancesRevision`.
Type: Long

## Errors
<a name="API_DiscoverInstancesRevision_Errors"></a>

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
<a name="API_DiscoverInstancesRevision_Examples"></a>

### DiscoverInstancesRevision Example
<a name="API_DiscoverInstancesRevision_Example_1"></a>

This example lists the increasing revision associated with instances registered to the specified service in the specified namespace.

#### Sample Request
<a name="API_DiscoverInstancesRevision_Example_1_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20230607T233508Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20230607/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DiscoverInstancesRevision
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
    "NamespaceName": "example-public-dns.com",
    "ServiceName": "example-dns-pub-service"
}
```

#### Sample Response
<a name="API_DiscoverInstancesRevision_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "InstancesRevision": 1001
}
```

### DiscoverInstancesRevision Example using OwnerAccount
<a name="API_DiscoverInstancesRevision_Example_2"></a>

This example lists the increasing revision associated with instances registered to a service in a shared namespace by specifying the `OwnerAccount`.

#### Sample Request
<a name="API_DiscoverInstancesRevision_Example_2_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20230607T233508Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20230607/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DiscoverInstancesRevision
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "NamespaceName": "example-public-dns.com",
    "ServiceName": "example-dns-pub-service",
    "OwnerAccount": "123456789012"
}
```

#### Sample Response
<a name="API_DiscoverInstancesRevision_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "InstancesRevision": 1001
}
```

## See Also
<a name="API_DiscoverInstancesRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/DiscoverInstancesRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DiscoverInstancesRevision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
