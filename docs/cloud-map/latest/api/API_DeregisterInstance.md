---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DeregisterInstance.html
---

# DeregisterInstance
<a name="API_DeregisterInstance"></a>

Deletes the Amazon Route 53 DNS records and health check, if any, that AWS Cloud Map created for the specified instance.

## Request Syntax
<a name="API_DeregisterInstance_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_DeregisterInstance_RequestSyntax) **   <a name="cloudmap-DeregisterInstance-request-InstanceId"></a>
The value that you specified for `Id` in the [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) request.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** [ServiceId](#API_DeregisterInstance_RequestSyntax) **   <a name="cloudmap-DeregisterInstance-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. If the namespace associated with the service is shared with your account, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_DeregisterInstance_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_DeregisterInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_DeregisterInstance_ResponseSyntax) **   <a name="cloudmap-DeregisterInstance-response-OperationId"></a>
A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_DeregisterInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The operation is already in progress.
 ** DuplicateOperationId **
The ID of the operation that's already in progress.
HTTP Status Code: 400

 ** InstanceNotFound **
No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ResourceInUse **
The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_DeregisterInstance_Examples"></a>

### DeregisterInstance Example
<a name="API_DeregisterInstance_Example_1"></a>

This example API request deregisters the specified instance.

#### Sample Request
<a name="API_DeregisterInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211816Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeregisterInstance
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "InstanceId": "i-abcd1234",
    "ServiceId": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_DeregisterInstance_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "OperationId":"httpvoqozuhfet5kzxoxg-a-response-example"
}
```

### DeregisterInstance Example using service ARN
<a name="API_DeregisterInstance_Example_2"></a>

This example API request deregisters an instance from a service in a shared namespace using the service ARN.

#### Sample Request
<a name="API_DeregisterInstance_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211816Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.DeregisterInstance
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "InstanceId": "i-abcd1234",
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_DeregisterInstance_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "OperationId":"httpvoqozuhfet5kzxoxg-a-response-example"
}
```

## See Also
<a name="API_DeregisterInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/DeregisterInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DeregisterInstance)
