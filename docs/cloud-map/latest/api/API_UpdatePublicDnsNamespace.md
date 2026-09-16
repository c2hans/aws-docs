---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePublicDnsNamespace.html
---

# UpdatePublicDnsNamespace
<a name="API_UpdatePublicDnsNamespace"></a>

Updates a public DNS namespace.

## Request Syntax
<a name="API_UpdatePublicDnsNamespace_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "Namespace": {
      "Description": "{{string}}",
      "Properties": {
         "DnsProperties": {
            "SOA": {
               "TTL": {{number}}
            }
         }
      }
   },
   "UpdaterRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePublicDnsNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_UpdatePublicDnsNamespace_RequestSyntax) **   <a name="cloudmap-UpdatePublicDnsNamespace-request-Id"></a>
The ID or Amazon Resource Name (ARN) of the namespace being updated.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Namespace](#API_UpdatePublicDnsNamespace_RequestSyntax) **   <a name="cloudmap-UpdatePublicDnsNamespace-request-Namespace"></a>
Updated properties for the public DNS namespace.
Type: [PublicDnsNamespaceChange](API_PublicDnsNamespaceChange.md) object
Required: Yes

 ** [UpdaterRequestId](#API_UpdatePublicDnsNamespace_RequestSyntax) **   <a name="cloudmap-UpdatePublicDnsNamespace-request-UpdaterRequestId"></a>
A unique string that identifies the request and that allows failed `UpdatePublicDnsNamespace` requests to be retried without the risk of running the operation twice. `UpdaterRequestId` can be any unique string (for example, a date/timestamp).
Type: String
Length Constraints: Maximum length of 64.
Required: No

## Response Syntax
<a name="API_UpdatePublicDnsNamespace_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_UpdatePublicDnsNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_UpdatePublicDnsNamespace_ResponseSyntax) **   <a name="cloudmap-UpdatePublicDnsNamespace-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_UpdatePublicDnsNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The operation is already in progress.
 ** DuplicateOperationId **
The ID of the operation that's already in progress.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** NamespaceNotFound **
No namespace exists with the specified ID.
HTTP Status Code: 400

 ** ResourceInUse **
The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.
HTTP Status Code: 400

## Examples
<a name="API_UpdatePublicDnsNamespace_Examples"></a>

### UpdatePublicDnsNamespace Example
<a name="API_UpdatePublicDnsNamespace_Example_1"></a>

This example updates the description for the specified public DNS namespace.

#### Sample Request
<a name="API_UpdatePublicDnsNamespace_Example_1_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211819Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdatePublicDNSNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
  "Id": "ns-e4anhexample0004",
  "UpdaterRequestId": "example-id",
  "Namespace": { "Description": "The updated namespace description" }
 }
```

#### Sample Response
<a name="API_UpdatePublicDnsNamespace_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "OperationId":"httpvoqozuhfet5kzxoxg-a-response-example"
}
```

### UpdatePublicDnsNamespace Example using ARN
<a name="API_UpdatePublicDnsNamespace_Example_2"></a>

This example updates the description for a shared public DNS namespace using its ARN.

#### Sample Request
<a name="API_UpdatePublicDnsNamespace_Example_2_Request"></a>

```
POST / HTTP/1.1
host:data-servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211819Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdatePublicDNSNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
  "Id": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e4anhexample0004",
  "UpdaterRequestId": "example-id",
  "Namespace": { "Description": "The updated namespace description" }
 }
```

#### Sample Response
<a name="API_UpdatePublicDnsNamespace_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "OperationId":"httpvoqozuhfet5kzxoxg-a-response-example"
}
```

## See Also
<a name="API_UpdatePublicDnsNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/UpdatePublicDnsNamespace)
