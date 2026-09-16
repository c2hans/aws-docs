---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstance.html
---

# GetInstance
<a name="API_GetInstance"></a>

Gets information about a specified instance.

## Request Syntax
<a name="API_GetInstance_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_GetInstance_RequestSyntax) **   <a name="cloudmap-GetInstance-request-InstanceId"></a>
The ID of the instance that you want to get information about.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** [ServiceId](#API_GetInstance_RequestSyntax) **   <a name="cloudmap-GetInstance-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_GetInstance_ResponseSyntax"></a>

```
{
   "Instance": {
      "Attributes": {
         "string" : "string"
      },
      "CreatedByAccount": "string",
      "CreatorRequestId": "string",
      "Id": "string"
   },
   "ResourceOwner": "string"
}
```

## Response Elements
<a name="API_GetInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instance](#API_GetInstance_ResponseSyntax) **   <a name="cloudmap-GetInstance-response-Instance"></a>
A complex type that contains information about a specified instance.
Type: [Instance](API_Instance.md) object

 ** [ResourceOwner](#API_GetInstance_ResponseSyntax) **   <a name="cloudmap-GetInstance-response-ResourceOwner"></a>
The ID of the AWS account that created the namespace that contains the service that the instance is associated with. If this isn't your account ID, it's the ID of the account that shared the namespace with your account.
Type: String
Length Constraints: Fixed length of 12.

## Errors
<a name="API_GetInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceNotFound **
No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.
HTTP Status Code: 400

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_GetInstance_Examples"></a>

### GetInstance Example
<a name="API_GetInstance_Example_1"></a>

This example retrieves information about the specified instance.

#### Sample Request
<a name="API_GetInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211816Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetInstance
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "InstanceId": "i-abcd1234",
    "ServiceId": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetInstance_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Instance": {
        "Id": "i-abcd1234",
        "Attributes": {
            "AWS_INSTANCE_IPV4": "192.0.2.44",
            "AWS_INSTANCE_PORT": "80",
            "color": "green",
            "region": "us-west-2",
            "stage": "beta"
        },
        "CreatedByAccount": "123456789012"
    }
    "ResourceOwner": "123456789012"
}
```

### GetInstance Example using service ARN
<a name="API_GetInstance_Example_2"></a>

This example retrieves information about an instance registered by account `111122223333` in a namespace shared by account `123456789012` using the service ARN.

#### Sample Request
<a name="API_GetInstance_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211816Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetInstance
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "InstanceId": "i-abcd1234",
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetInstance_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Instance": {
        "Id": "i-abcd1234",
        "Attributes": {
            "AWS_INSTANCE_IPV4": "192.0.2.44",
            "AWS_INSTANCE_PORT": "80",
            "color": "green",
            "region": "us-west-2",
            "stage": "beta"
        },
        "CreatedByAccount": "111122223333"
    }
    "ResourceOwner": "123456789012"
}
```

## See Also
<a name="API_GetInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/GetInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/GetInstance)
