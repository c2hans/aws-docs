---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html
---

# GetTagValues
<a name="API_GetTagValues"></a>

Returns all tag values for the specified key that are used in the specified AWS Region for the calling account.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

## Request Syntax
<a name="API_GetTagValues_RequestSyntax"></a>

```
{
   "Key": "{{string}}",
   "PaginationToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTagValues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Key](#API_GetTagValues_RequestSyntax) **   <a name="resourcegrouptagging-GetTagValues-request-Key"></a>
Specifies the tag key for which you want to list all existing values that are currently used in the specified AWS Region for the calling account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: Yes

 ** [PaginationToken](#API_GetTagValues_RequestSyntax) **   <a name="resourcegrouptagging-GetTagValues-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_GetTagValues_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "TagValues": [ "string" ]
}
```

## Response Elements
<a name="API_GetTagValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetTagValues_ResponseSyntax) **   <a name="resourcegrouptagging-GetTagValues-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [TagValues](#API_GetTagValues_ResponseSyntax) **   <a name="resourcegrouptagging-GetTagValues-response-TagValues"></a>
A list of all tag values for the specified key currently used in the specified AWS Region for the calling account.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

## Errors
<a name="API_GetTagValues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The request processing failed because of an unknown error, exception, or failure. You can retry the request.
HTTP Status Code: 500

 ** InvalidParameterException **
The request failed because of one of the following reasons:
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide.
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.
HTTP Status Code: 400

 ** ThrottledException **
The request failed because it exceeded the allowed frequency of submitted requests.
HTTP Status Code: 400

## Examples
<a name="API_GetTagValues_Examples"></a>

### Example
<a name="API_GetTagValues_Example_1"></a>

This example illustrates one usage of GetTagValues.

#### Sample Request
<a name="API_GetTagValues_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 18
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetTagValues
X-Amz-Date: 20170421T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "Key": "Example_key"
}
```

#### Sample Response
<a name="API_GetTagValues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Content-Length: 42
Date: Fri, 21 Apr 2017 21:45:25 GMT

{
    "PaginationToken": "",
    "TagValues": [
        "Example_value"
    ]
}
```

## See Also
<a name="API_GetTagValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetTagValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetTagValues)
