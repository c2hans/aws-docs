---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists tags for a resource. Tagging is currently supported for detectors, finding filters, IP sets, threat intel sets, and publishing destination, with a limit of 50 tags per resource. When invoked, this operation returns all assigned tags for a given resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /tags/{{ResourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="guardduty-ListTagsForResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) for the given GuardDuty resource.
Pattern: `arn:[A-Za-z_.-]{1,20}:guardduty:[A-Za-z0-9_/.-]{0,63}:\d+:detector/[A-Za-z0-9_/.-]{32,264}`
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="guardduty-ListTagsForResource-response-tags"></a>
The tags associated with the resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An access denied exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 403

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListTagsForResource)
