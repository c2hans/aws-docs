---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_Untag.html
---

# Untag
<a name="API_Untag"></a>

Deletes tags from a specified resource group.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:Untag`

## Request Syntax
<a name="API_Untag_RequestSyntax"></a>

```
PATCH /resources/{{Arn}}/tags HTTP/1.1
Content-type: application/json

{
   "Keys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_Untag_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_Untag_RequestSyntax) **   <a name="ARG-Untag-request-uri-Arn"></a>
The Amazon resource name (ARN) of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys.
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: Yes

## Request Body
<a name="API_Untag_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Keys](#API_Untag_RequestSyntax) **   <a name="ARG-Untag-request-Keys"></a>
The keys of the tags to be removed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_Untag_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Keys": [ "string" ]
}
```

## Response Elements
<a name="API_Untag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_Untag_ResponseSyntax) **   <a name="ARG-Untag-response-Arn"></a>
The Amazon resource name (ARN) of the resource group from which tags have been removed.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`

 ** [Keys](#API_Untag_ResponseSyntax) **   <a name="ARG-Untag-response-Keys"></a>
The keys of the tags that were removed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_Untag_Errors"></a>

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
<a name="API_Untag_Examples"></a>

### Example
<a name="API_Untag_Example_1"></a>

The following example removes the tag with the key Department from the specified resource group. Note that this updates the tags on only the group itself; it doesn't touch the tags on any group members.

The ARN in the PATCH element must be [URL encoded](https://wikipedia.org/wiki/Percent-encoding).

#### Sample Request
<a name="API_Untag_Example_1_Request"></a>

```
PATCH /resources/arn%3Aaws%3Aresource-groups%3Aus-west-2%3A123456789012%3Agroup%2FMyTest/tags HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.untag
X-Amz-Date: 20220120T221301Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 24

{
    "Keys": [
        "Department"
    ]
}
```

#### Sample Response
<a name="API_Untag_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 22:13:01 GMT
Content-Type: application/json
Content-Length: 91
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "Arn":"arn:aws:resource-groups:us-west-2:123456789012:group/MyTest",
    "Keys":[
        "Department"
    ]
}
```

## See Also
<a name="API_Untag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/Untag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/Untag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/Untag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/Untag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/Untag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/Untag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/Untag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/Untag)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/Untag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/Untag)
