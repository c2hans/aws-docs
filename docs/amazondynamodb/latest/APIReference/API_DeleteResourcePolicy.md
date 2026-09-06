---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes the resource-based policy attached to the resource, which can be a table or stream.

 `DeleteResourcePolicy` is an idempotent operation; running it multiple times on the same resource *doesn't* result in an error response, unless you specify an `ExpectedRevisionId`, which will then return a `PolicyNotFoundException`.

**Important**
To make sure that you don't inadvertently lock yourself out of your own resources, the root principal in your AWS account can perform `DeleteResourcePolicy` requests, even if your resource-based policy explicitly denies the root principal's access.

**Note**
 `DeleteResourcePolicy` is an asynchronous operation. If you issue a `GetResourcePolicy` request immediately after running the `DeleteResourcePolicy` request, DynamoDB might still return the deleted policy. This is because the policy for your resource might not have been deleted yet. Wait for a few seconds, and then try the `GetResourcePolicy` request again.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
{
   "ExpectedRevisionId": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="DDB-DeleteResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the DynamoDB resource from which the policy will be removed. The resources you can specify include tables and streams. If you remove the policy of a table, it will also remove the permissions for the table's indexes defined in that policy document. This is because index permissions are defined in the table's policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: Yes

 ** [ExpectedRevisionId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="DDB-DeleteResourcePolicy-request-ExpectedRevisionId"></a>
A string value that you can use to conditionally delete your policy. When you provide an expected revision ID, if the revision ID of the existing policy on the resource doesn't match or if there's no policy attached to the resource, the request will fail and return a `PolicyNotFoundException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_DeleteResourcePolicy_ResponseSyntax"></a>

```
{
   "RevisionId": "string"
}
```

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RevisionId](#API_DeleteResourcePolicy_ResponseSyntax) **   <a name="DDB-DeleteResourcePolicy-response-RevisionId"></a>
A unique string that represents the revision ID of the policy. If you're comparing revision IDs, make sure to always use string comparison logic.
This value will be empty if you make a request against a resource without a policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** LimitExceededException **
There is no limit to the number of daily on-demand backups that can be taken.
For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include `CreateTable`, `UpdateTable`, `DeleteTable`,`UpdateTimeToLive`, `RestoreTableFromBackup`, and `RestoreTableToPointInTime`.
When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.
When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.
There is a soft account quota of 2,500 tables.
GetRecords was called with a value of more than 1000 for the limit request parameter.
More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.
 ** message **
Too many operations for a given subscriber.
HTTP Status Code: 400

 ** PolicyNotFoundException **
The operation tried to access a nonexistent resource-based policy.
If you specified an `ExpectedRevisionId`, it's possible that a policy is present for the resource but its revision ID didn't match the expected value.
HTTP Status Code: 400

 ** ResourceInUseException **
The operation conflicts with the resource's availability. For example:
+ You attempted to recreate an existing table.
+ You tried to delete a table currently in the `CREATING` state.
+ You tried to update a resource that was already being updated.
When appropriate, wait for the ongoing update to complete and attempt the request again.
 ** message **
The resource which is being attempted to be changed is in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DeleteResourcePolicy_Examples"></a>

### Delete the resource-based policy of a table
<a name="API_DeleteResourcePolicy_Example_1"></a>

The following example deletes the resource-based policy of a table named `Thread`.

#### Sample Request
<a name="API_DeleteResourcePolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dynamodb.<region>.<domain>;
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: DynamoDB_20120810.DeleteResourcePolicy
{
    "ResourceArn": "arn:aws:dynamodb:us-west-2:123456789012:table/Thread"
}
```

#### Sample Response
<a name="API_DeleteResourcePolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "RevisionId": "1683717331354"
}
```

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DeleteResourcePolicy)
