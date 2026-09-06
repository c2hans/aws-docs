---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_route53resolver_ListTagsForResource"></a>

Lists the tags that you associated with the specified resource.

## Request Syntax
<a name="API_route53resolver_ListTagsForResource_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_route53resolver_ListTagsForResource_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListTagsForResource-request-MaxResults"></a>
The maximum number of tags that you want to return in the response to a `ListTagsForResource` request. If you don't specify a value for `MaxResults`, Resolver returns up to 100 tags.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListTagsForResource_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListTagsForResource-request-NextToken"></a>
For the first `ListTagsForResource` request, omit this value.
If you have more than `MaxResults` tags, you can submit another `ListTagsForResource` request to get the next group of tags for the resource. In the next request, specify the value of `NextToken` from the previous response.
Type: String
Required: No

 ** [ResourceArn](#API_route53resolver_ListTagsForResource_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListTagsForResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) for the resource that you want to list tags for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_route53resolver_ListTagsForResource_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53resolver_ListTagsForResource_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListTagsForResource-response-NextToken"></a>
If more than `MaxResults` tags match the specified criteria, you can submit another `ListTagsForResource` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [Tags](#API_route53resolver_ListTagsForResource_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListTagsForResource-response-Tags"></a>
The tags that are associated with the resource that you specified in the `ListTagsForResource` request.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.

## Errors
<a name="API_route53resolver_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The value that you specified for `NextToken` in a `List` request isn't valid.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_ListTagsForResource_Examples"></a>

### ListTagsForResource Example
<a name="API_route53resolver_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

#### Sample Request
<a name="API_route53resolver_ListTagsForResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 134
X-Amz-Target: Route53Resolver.ListTagsForResource
X-Amz-Date: 20181101T185222Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "MaxResults": 10,
    "ResourceArn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample"
}
```

#### Sample Response
<a name="API_route53resolver_ListTagsForResource_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 18:52:22 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 107
x-amzn-RequestId: bda80f7b-0f2c-41d1-9043-f36d3example
Connection: keep-alive

{
    "Tags": [
        {
            "Key": "account-id",
            "Value": "12345"
        }
    ]
}
```

## See Also
<a name="API_route53resolver_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListTagsForResource)
