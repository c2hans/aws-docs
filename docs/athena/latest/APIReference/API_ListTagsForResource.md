---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags associated with an Athena resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTagsForResource_RequestSyntax) **   <a name="athena-ListTagsForResource-request-MaxResults"></a>
The maximum number of results to be returned per request that lists the tags for the resource.
Type: Integer
Valid Range: Minimum value of 75.
Required: No

 ** [NextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="athena-ListTagsForResource-request-NextToken"></a>
The token for the next set of results, or null if there are no additional results for this request, where the request lists the tags for the resource with the specified ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="athena-ListTagsForResource-request-ResourceARN"></a>
Lists the tags for the resource with the specified ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

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
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="athena-ListTagsForResource-response-NextToken"></a>
A token to be used by the next request if this request is truncated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="athena-ListTagsForResource-response-Tags"></a>
The list of tags associated with the specified resource.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ListTagsForResource)
