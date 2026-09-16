---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds one or more tags to the specified resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_TagResource_RequestSyntax) **   <a name="cloudmap-TagResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="cloudmap-TagResource-request-Tags"></a>
The tags to add to the specified resource. Specifying the tag key is required. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation can't be completed because the resource was not found.
HTTP Status Code: 400

 ** TooManyTagsException **
The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.
 ** ResourceName **
The name of the resource.
HTTP Status Code: 400

## Examples
<a name="API_TagResource_Examples"></a>

### TagResource Example
<a name="API_TagResource_Example_1"></a>

This example request tags the specified resource.

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: servicediscovery.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: Route53AutoNaming_v20170314.TagResource
Content-Type: application/x-amz-json-1.1
X-Amz-Date: 20200521T192626Z
X-Amz-Security-Token: [security-token]
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20200521/us-east-1/servicediscovery/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-security-token;x-amz-target,
               Signature=[calculated-signature]
Content-Length: [number of characters in the JSON string]

{
    "ResourceARN": "arn:aws:servicediscovery:us-east-1:123456789012:namespace/ns-ylexjili4cdxy3xm",
    "Tags": [{
        "Key": "Department",
        "Value": "Engineering"
    }, {
        "Key": "Project",
        "Value": "Zeta"
    }]
}
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Type: application/x-amz-json-1.1
Date: Thu, 21 May 2020 19:26:29 GMT
x-amzn-RequestId: [request-id]
Content-Length: 2
Connection: keep-alive

{}
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/TagResource)
