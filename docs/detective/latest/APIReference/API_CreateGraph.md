---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateGraph.html
---

# CreateGraph
<a name="API_CreateGraph"></a>

Creates a new behavior graph for the calling account, and sets that account as the administrator account. This operation is called by the account that is enabling Detective.

The operation also enables Detective for the calling account in the currently selected Region. It returns the ARN of the new behavior graph.

 `CreateGraph` triggers a process to create the corresponding data tables for the new behavior graph.

An account can only be the administrator account for one behavior graph within a Region. If the same account calls `CreateGraph` with the same administrator account, it always returns the same behavior graph ARN. It does not create a new behavior graph.

## Request Syntax
<a name="API_CreateGraph_RequestSyntax"></a>

```
POST /graph HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateGraph_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGraph_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_CreateGraph_RequestSyntax) **   <a name="detective-CreateGraph-request-Tags"></a>
The tags to assign to the new behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateGraph_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GraphArn": "string"
}
```

## Response Elements
<a name="API_CreateGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GraphArn](#API_CreateGraph_ResponseSyntax) **   <a name="detective-CreateGraph-response-GraphArn"></a>
The ARN of the new behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`

## Errors
<a name="API_CreateGraph_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request attempted an invalid action.
HTTP Status Code: 409

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
This request cannot be completed for one of the following reasons.
+ This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.
+ This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.
 ** Resources **
The type of resource that has exceeded the service quota.
HTTP Status Code: 402

## Examples
<a name="API_CreateGraph_Examples"></a>

### Example
<a name="API_CreateGraph_Example_1"></a>

This example illustrates one usage of CreateGraph.

#### Sample Request
<a name="API_CreateGraph_Example_1_Request"></a>

```
POST /graph HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 50
Authorization: AUTHPARAMS
X-Amz-Date: 20200122T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
   "Tags": {
      "Department" : "Finance"
   }
}
```

### Example
<a name="API_CreateGraph_Example_2"></a>

This example illustrates one usage of CreateGraph.

#### Sample Response
<a name="API_CreateGraph_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 94
Date: Wed, 22 Jan 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive

{
 "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
}
```

## See Also
<a name="API_CreateGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/CreateGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/CreateGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/CreateGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/CreateGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/CreateGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/CreateGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/CreateGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/CreateGraph)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/CreateGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/CreateGraph)
