---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{ResourceArn}} HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="appconfig-TagResource-request-uri-ResourceArn"></a>
The ARN of the resource for which to retrieve tags.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="appconfig-TagResource-request-Tags"></a>
The key-value string map. The valid character set is [a-zA-Z\+-=.\_:/]. The tag key can be up to 128 characters and must not start with `aws:`. The tag value can be up to 256 characters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_TagResource_Examples"></a>

### Example
<a name="API_TagResource_Example_1"></a>

This example illustrates one usage of TagResource.

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
POST /tags/arn%3Aaws%3Aappconfig%3Aus-east-1%3A111122223333%3Aapplication%abc1234 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.tag-resource
X-Amz-Date: 20210920T185502Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 25

{
	"Tags": {"group1": "1"}
}
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/TagResource)
