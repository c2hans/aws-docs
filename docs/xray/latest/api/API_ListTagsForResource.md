---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Returns a list of tags that are applied to the specified AWS X-Ray group or sampling rule.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
POST /ListTagsForResource HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}",
   "ResourceARN": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="xray-ListTagsForResource-request-NextToken"></a>
A pagination token. If multiple pages of results are returned, use the `NextToken` value returned with the current page of results as the value of this parameter to get the next page of results.
Type: String
Required: No

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="xray-ListTagsForResource-request-ResourceARN"></a>
The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="xray-ListTagsForResource-response-NextToken"></a>
A pagination token. If multiple pages of results are returned, use the `NextToken` value returned with the current page of results to get the next page of results.
Type: String

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="xray-ListTagsForResource-response-Tags"></a>
A list of tags, as key and value pairs, that is associated with the specified X-Ray group or sampling rule.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.
HTTP Status Code: 404

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ListTagsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
