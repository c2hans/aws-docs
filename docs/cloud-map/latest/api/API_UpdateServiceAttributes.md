---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html
---

# UpdateServiceAttributes
<a name="API_UpdateServiceAttributes"></a>

Submits a request to update a specified service to add service-level attributes.

## Request Syntax
<a name="API_UpdateServiceAttributes_RequestSyntax"></a>

```
{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateServiceAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attributes](#API_UpdateServiceAttributes_RequestSyntax) **   <a name="cloudmap-UpdateServiceAttributes-request-Attributes"></a>
A string map that contains attribute key-value pairs.
Type: String to string map
Map Entries: Maximum number of 30 items.
Key Length Constraints: Maximum length of 255.
Value Length Constraints: Maximum length of 1024.
Required: Yes

 ** [ServiceId](#API_UpdateServiceAttributes_RequestSyntax) **   <a name="cloudmap-UpdateServiceAttributes-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to update. For services created in a namespace shared with your AWS account, specify the service ARN.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Elements
<a name="API_UpdateServiceAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateServiceAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceAttributesLimitExceededException **
The attribute can't be added to the service because you've exceeded the quota for the number of attributes you can add to a service.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_UpdateServiceAttributes_Examples"></a>

### UpdateServiceAttributes Example
<a name="API_UpdateServiceAttributes_Example_1"></a>

This example API request updates the service `srv-e4anhexample0004` to add an attribute `Port` with value `80`.

#### Sample Request
<a name="API_UpdateServiceAttributes_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdateServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "srv-e4anhexample0004",
    "Attributes": {
       "Port":"80"
    }
}
```

#### Sample Response
<a name="API_UpdateServiceAttributes_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

### UpdateServiceAttributes Example using ARN
<a name="API_UpdateServiceAttributes_Example_2"></a>

This example API request updates a service in a shared namespace using its ARN to add an attribute `Port` with value `80`.

#### Sample Request
<a name="API_UpdateServiceAttributes_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.UpdateServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
    "Attributes": {
       "Port":"80"
    }
}
```

#### Sample Response
<a name="API_UpdateServiceAttributes_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{}
```

## See Also
<a name="API_UpdateServiceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/UpdateServiceAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/UpdateServiceAttributes)
