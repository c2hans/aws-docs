---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_query_ListTagsForResource"></a>

List all tags on a Timestream query resource.

## Request Syntax
<a name="API_query_ListTagsForResource_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_query_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_query_ListTagsForResource_RequestSyntax) **   <a name="timestream-query_ListTagsForResource-request-MaxResults"></a>
The maximum number of tags to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_query_ListTagsForResource_RequestSyntax) **   <a name="timestream-query_ListTagsForResource-request-NextToken"></a>
A pagination token to resume pagination.
Type: String
Required: No

 ** [ResourceARN](#API_query_ListTagsForResource_RequestSyntax) **   <a name="timestream-query_ListTagsForResource-request-ResourceARN"></a>
The Timestream resource with tags to be listed. This value is an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_query_ListTagsForResource_ResponseSyntax"></a>

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
<a name="API_query_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_query_ListTagsForResource_ResponseSyntax) **   <a name="timestream-query_ListTagsForResource-response-NextToken"></a>
A pagination token to resume pagination with a subsequent call to `ListTagsForResourceResponse`.
Type: String

 ** [Tags](#API_query_ListTagsForResource_ResponseSyntax) **   <a name="timestream-query_ListTagsForResource-response-Tags"></a>
The tags currently associated with the Timestream resource.
Type: Array of [Tag](API_query_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_query_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidEndpointException **
The requested endpoint is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** ScheduledQueryArn **
The ARN of the scheduled query.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_query_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ListTagsForResource)
