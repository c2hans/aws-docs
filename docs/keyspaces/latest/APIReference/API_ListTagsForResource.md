---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Returns a list of all tags associated with the specified Amazon Keyspaces resource.

To read keyspace metadata using `ListTagsForResource`, the IAM principal needs `Select` action permissions for the specified resource and the system keyspace.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTagsForResource_RequestSyntax) **   <a name="keyspaces-ListTagsForResource-request-maxResults"></a>
The total number of tags to return in the output. If the total number of tags available is more than the value specified, a `NextToken` is provided in the output. To resume pagination, provide the `NextToken` value as an argument of a subsequent API invocation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="keyspaces-ListTagsForResource-request-nextToken"></a>
The pagination token. To resume pagination, provide the `NextToken` value as argument of a subsequent API invocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="keyspaces-ListTagsForResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the Amazon Keyspaces resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="keyspaces-ListTagsForResource-response-nextToken"></a>
A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="keyspaces-ListTagsForResource-response-tags"></a>
A list of tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 60 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
HTTP Status Code: 400

 [InternalServerException](API_InternalServerException.md)
Amazon Keyspaces was unable to fully process this request because of an internal server error.
 ** message **
An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The specified resource was not found. Verify the resource identifier and ensure the resource exists and is in an ACTIVE state.
 ** resourceArn **
The unique identifier in the format of Amazon Resource Name (ARN) for the resource couldn't be found.
HTTP Status Code: 400

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The operation exceeded the service quota for this resource. For more information on service quotas, see [Quotas](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html) in the *Amazon Keyspaces Developer Guide*.
 ** message **
The requested operation would exceed the service quota for this resource. Review the service quotas and adjust your request accordingly.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The operation failed due to an invalid or malformed request.
 ** message **
The request parameters are invalid or malformed. Review the API documentation and correct the request format.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ListTagsForResource)
