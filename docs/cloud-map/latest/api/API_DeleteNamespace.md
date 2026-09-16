---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteNamespace.html
---

# DeleteNamespace
<a name="API_DeleteNamespace"></a>

Deletes a namespace from the current account. If the namespace still contains one or more services, the request fails.

## Request Syntax
<a name="API_DeleteNamespace_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_DeleteNamespace_RequestSyntax) **   <a name="cloudmap-DeleteNamespace-request-Id"></a>
The ID or Amazon Resource Name (ARN) of the namespace that you want to delete.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_DeleteNamespace_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_DeleteNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_DeleteNamespace_ResponseSyntax) **   <a name="cloudmap-DeleteNamespace-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_DeleteNamespace_Errors"></a>

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
<a name="API_DeleteNamespace_Examples"></a>

### DeleteNamespace Example
<a name="API_DeleteNamespace_Example_1"></a>

This example deletes the specified namespace.

#### Sample Request
<a name="API_DeleteNamespace_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211707Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeleteNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "ns-e4anhexample0004"
}
```

#### Sample Response
<a name="API_DeleteNamespace_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "OperationId":"deleteelozuhfet5kzxoxg-a-response-example"
}
```

### DeleteNamespace Example using ARN
<a name="API_DeleteNamespace_Example_2"></a>

This example deletes a shared namespace using its ARN.

#### Sample Request
<a name="API_DeleteNamespace_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211707Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeleteNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e4anhexample0004"
}
```

#### Sample Response
<a name="API_DeleteNamespace_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "OperationId":"deleteelozuhfet5kzxoxg-a-response-example"
}
```

## See Also
<a name="API_DeleteNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/DeleteNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DeleteNamespace)
