---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListIndexes.html
---

# ListIndexes
<a name="API_ListIndexes"></a>

Retrieves a list of all of the indexes in AWS Regions that are currently collecting resource information for AWS Resource Explorer.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:ListIndexes`

   **Resource**: No specific resource (\*).

 **Related operations**
+ To turn on Resource Explorer in an AWS Region, use [CreateIndex](API_CreateIndex.md).
+ To turn off Resource Explorer in an AWS Region, use [DeleteIndex](API_DeleteIndex.md).
+ To retrieve the details for an index and check its state or its type, use [GetIndex](API_GetIndex.md).
+ To convert a local index to an aggregator index, use [UpdateIndexType](API_UpdateIndexType.md).

## Request Syntax
<a name="API_ListIndexes_RequestSyntax"></a>

```
POST /ListIndexes HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Regions": [ "{{string}}" ],
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListIndexes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListIndexes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListIndexes_RequestSyntax) **   <a name="resourceexplorer-ListIndexes-request-MaxResults"></a>
The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListIndexes_RequestSyntax) **   <a name="resourceexplorer-ListIndexes-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Regions](#API_ListIndexes_RequestSyntax) **   <a name="resourceexplorer-ListIndexes-request-Regions"></a>
If specified, limits the response to only information about the index in the specified list of AWS Regions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[a-z-]+-[a-z]+-[0-9]`
Required: No

 ** [Type](#API_ListIndexes_RequestSyntax) **   <a name="resourceexplorer-ListIndexes-request-Type"></a>
If specified, limits the output to only indexes of the specified Type, either `LOCAL` or `AGGREGATOR`.
Use this option to discover the aggregator index for your account.
Type: String
Valid Values: `LOCAL | AGGREGATOR`
Required: No

## Response Syntax
<a name="API_ListIndexes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Indexes": [
      {
         "Arn": "string",
         "Region": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIndexes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Indexes](#API_ListIndexes_ResponseSyntax) **   <a name="resourceexplorer-ListIndexes-response-Indexes"></a>
A structure that contains the details and status of each index.
Type: Array of [Index](API_Index.md) objects

 ** [NextToken](#API_ListIndexes_ResponseSyntax) **   <a name="resourceexplorer-ListIndexes-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String

## Errors
<a name="API_ListIndexes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_ListIndexes_Examples"></a>

### Example
<a name="API_ListIndexes_Example_1"></a>

The following example shows how to list the Resource Explorer indexes in the current AWS account. In this example, only two AWS Regions have indexes.

#### Sample Request
<a name="API_ListIndexes_Example_1_Request"></a>

```
POST /ListIndexes HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{}
```

#### Sample Response
<a name="API_ListIndexes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Indexes": [
        {
            "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
            "Region": "us-east-1",
            "Type": "LOCAL"
        },
        {
            "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222",
            "Region":"us-west-2",
            "Type":"LOCAL"
        }
    ]
}
```

## See Also
<a name="API_ListIndexes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListIndexes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListIndexes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
