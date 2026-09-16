---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePrivateDnsNamespace.html
---

# CreatePrivateDnsNamespace
<a name="API_CreatePrivateDnsNamespace"></a>

Creates a private namespace based on DNS, which is visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace `example.com` and name your service `backend`, the resulting DNS name for the service is `backend.example.com`. Service instances that are registered using a private DNS namespace can be discovered using either a `DiscoverInstances` request or using DNS. For the current quota on the number of namespaces that you can create using the same AWS account, see [AWS Cloud Map quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html) in the * AWS Cloud Map Developer Guide*.

## Request Syntax
<a name="API_CreatePrivateDnsNamespace_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Properties": {
      "DnsProperties": {
         "SOA": {
            "TTL": {{number}}
         }
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Vpc": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePrivateDnsNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_CreatePrivateDnsNamespace_RequestSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed `CreatePrivateDnsNamespace` requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string (for example, a date/timestamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** [Description](#API_CreatePrivateDnsNamespace_RequestSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-request-Description"></a>
A description for the namespace.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Name](#API_CreatePrivateDnsNamespace_RequestSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-request-Name"></a>
The name that you want to assign to this namespace. When you create a private DNS namespace, AWS Cloud Map automatically creates an Amazon Route 53 private hosted zone that has the same name as the namespace.
Type: String
Length Constraints: Maximum length of 253.
Pattern: `^(?!arn:)[!-~]{1,253}$`
Required: Yes

 ** [Properties](#API_CreatePrivateDnsNamespace_RequestSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-request-Properties"></a>
Properties for the private DNS namespace.
Type: [PrivateDnsNamespaceProperties](API_PrivateDnsNamespaceProperties.md) object
Required: No

 ** [Tags](#API_CreatePrivateDnsNamespace_RequestSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-request-Tags"></a>
The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Vpc](#API_CreatePrivateDnsNamespace_RequestSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-request-Vpc"></a>
The ID of the Amazon VPC that you want to associate the namespace with.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_CreatePrivateDnsNamespace_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_CreatePrivateDnsNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_CreatePrivateDnsNamespace_ResponseSyntax) **   <a name="cloudmap-CreatePrivateDnsNamespace-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_CreatePrivateDnsNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The operation is already in progress.
 ** DuplicateOperationId **
The ID of the operation that's already in progress.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** NamespaceAlreadyExists **
The namespace that you're trying to create already exists.
 ** CreatorRequestId **
The `CreatorRequestId` that was used to create the namespace.
 ** NamespaceId **
The ID of the existing namespace.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
The resource can't be created because you've reached the quota on the number of resources.
HTTP Status Code: 400

 ** TooManyTagsException **
The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.
 ** ResourceName **
The name of the resource.
HTTP Status Code: 400

## Examples
<a name="API_CreatePrivateDnsNamespace_Examples"></a>

### CreatePrivateDnsNamespace Example
<a name="API_CreatePrivateDnsNamespace_Example_1"></a>

This example creates a private DNS namespace called `example-private-dns.com` that's visible only in the specified VPC.

#### Sample Request
<a name="API_CreatePrivateDnsNamespace_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211704Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.CreatePrivateDnsNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "CreatorRequestId": "example-creator-request-id-0002",
    "Name": "example-private-dns.com",
    "Description": "Example.com AWS Cloud Map Private DNS Namespace",
    "Vpc": "vpc-12345678"
}
```

#### Sample Response
<a name="API_CreatePrivateDnsNamespace_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "OperationId":"dns1voqozuhfet5kzxoxg-a-response-example"
}
```

## See Also
<a name="API_CreatePrivateDnsNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)
