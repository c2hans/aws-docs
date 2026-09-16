---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListIndexesForMembers.html
---

# ListIndexesForMembers
<a name="API_ListIndexesForMembers"></a>

Retrieves a list of a member's indexes in all AWS Regions that are currently collecting resource information for AWS Resource Explorer. Only the management account or a delegated administrator with service access enabled can invoke this API call.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:ListIndexesForMembers`

   **Resource**: No specific resource (\*).

 **Related operations**
+ To turn on Resource Explorer in an AWS Region, use [CreateIndex](API_CreateIndex.md).
+ To turn off Resource Explorer in an AWS Region, use [DeleteIndex](API_DeleteIndex.md).
+ To retrieve the details for an index and check its state or its type, use [GetIndex](API_GetIndex.md).
+ To list all of the indexes in the AWS account, use [ListIndexes](API_ListIndexes.md).
+ To convert a local index to an aggregator index, use [UpdateIndexType](API_UpdateIndexType.md).

## Request Syntax
<a name="API_ListIndexesForMembers_RequestSyntax"></a>

```
POST /ListIndexesForMembers HTTP/1.1
Content-type: application/json

{
   "AccountIdList": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListIndexesForMembers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListIndexesForMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIdList](#API_ListIndexesForMembers_RequestSyntax) **   <a name="resourceexplorer-ListIndexesForMembers-request-AccountIdList"></a>
The account IDs will limit the output to only indexes from these accounts.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [MaxResults](#API_ListIndexesForMembers_RequestSyntax) **   <a name="resourceexplorer-ListIndexesForMembers-request-MaxResults"></a>
The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [NextToken](#API_ListIndexesForMembers_RequestSyntax) **   <a name="resourceexplorer-ListIndexesForMembers-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListIndexesForMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Indexes": [
      {
         "AccountId": "string",
         "Arn": "string",
         "Region": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIndexesForMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Indexes](#API_ListIndexesForMembers_ResponseSyntax) **   <a name="resourceexplorer-ListIndexesForMembers-response-Indexes"></a>
A structure that contains the details and status of each index.
Type: Array of [MemberIndex](API_MemberIndex.md) objects

 ** [NextToken](#API_ListIndexesForMembers_ResponseSyntax) **   <a name="resourceexplorer-ListIndexesForMembers-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String

## Errors
<a name="API_ListIndexesForMembers_Errors"></a>

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
<a name="API_ListIndexesForMembers_Examples"></a>

### Example
<a name="API_ListIndexesForMembers_Example_1"></a>

The following example shows how to list the existing Resource Explorer indexes in each Region for a specific account.

#### Sample Request
<a name="API_ListIndexesForMembers_Example_1_Request"></a>

```
POST /ListIndexesForMembers HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "AccountidList": [
        "123456789012"
    ]
}
```

#### Sample Response
<a name="API_ListIndexesForMembers_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Indexes": [
        {
            "AccountId": "123456789012",
            "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
            "Region": "us-east-1",
            "Type": "LOCAL"
        },
        {
            "AccountId": "123456789012",
            "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222",
            "Region":"us-west-2",
            "Type":"LOCAL"
        }
    ]
}
```

## See Also
<a name="API_ListIndexesForMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListIndexesForMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListIndexesForMembers)
