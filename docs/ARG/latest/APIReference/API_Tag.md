---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Adds tags to a resource group with the specified Amazon resource name (ARN). Existing tags on a resource group are not changed if they are not specified in the request parameters.

**Important**
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:Tag`

## Request Syntax
<a name="API_Tag_RequestSyntax"></a>

```
PUT /resources/{{Arn}}/tags HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_Tag_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_Tag_RequestSyntax) **   <a name="ARG-Tag-request-uri-Arn"></a>
The Amazon resource name (ARN) of the resource group to which to add tags.
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: Yes

## Request Body
<a name="API_Tag_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_Tag_RequestSyntax) **   <a name="ARG-Tag-request-Tags"></a>
The tags to add to the specified resource group. A tag is a string-to-string map of key-value pairs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_Tag_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_Tag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_Tag_ResponseSyntax) **   <a name="ARG-Tag-response-Arn"></a>
The Amazon resource name (ARN) of the tagged resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`

 ** [Tags](#API_Tag_ResponseSyntax) **   <a name="ARG-Tag-response-Tags"></a>
The tags that have been added to the specified resource group.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_Tag_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** NotFoundException **
One or more of the specified resources don't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

## Examples
<a name="API_Tag_Examples"></a>

### Example
<a name="API_Tag_Example_1"></a>

The following example attaches two tags to the specified resource group. The first tag has a key of `Department` and a value of `Finance`, and the second has a key of `Env` and a value of `Prod`. Note that this tags only the group itself; it doesn't tag any members of the group.

The ARN in the PUT element must be [URL encoded](https://wikipedia.org/wiki/Percent-encoding).

#### Sample Request
<a name="API_Tag_Example_1_Request"></a>

```
PUT /resources/arn%3Aaws%3Aresource-groups%3Aus-west-2%3A123456789012%3Agroup%2FMyTest/tags HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.tag
X-Amz-Date: 20220120T220458Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 50

{
    "Tags": {
        "Department": "Finance",
        "Env": "Prod"
    }
}
```

#### Sample Response
<a name="API_Tag_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 22:04:58 GMT
Content-Type: application/json
Content-Length: 114
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "Arn":"arn:aws:resource-groups:us-west-2:123456789012:group/MyTest",
    "Tags":{
        "Department":"Finance",
        "Env":"Prod"
    }
}
```

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/Tag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/Tag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/Tag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/Tag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/Tag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/Tag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/Tag)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/Tag)
