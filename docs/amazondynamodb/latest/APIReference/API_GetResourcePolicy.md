---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetResourcePolicy.html
---

# GetResourcePolicy
<a name="API_GetResourcePolicy"></a>

Returns the resource-based policy document attached to the resource, which can be a table or stream, in JSON format.

 `GetResourcePolicy` follows an [*eventually consistent*](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html) model. The following list describes the outcomes when you issue the `GetResourcePolicy` request immediately after issuing another request:
+ If you issue a `GetResourcePolicy` request immediately after a `PutResourcePolicy` request, DynamoDB might return a `PolicyNotFoundException`.
+ If you issue a `GetResourcePolicy`request immediately after a `DeleteResourcePolicy` request, DynamoDB might return the policy that was present before the deletion request.
+ If you issue a `GetResourcePolicy` request immediately after a `CreateTable` request, which includes a resource-based policy, DynamoDB might return a `ResourceNotFoundException` or a `PolicyNotFoundException`.

Because `GetResourcePolicy` uses an *eventually consistent* query, the metadata for your policy or table might not be available at that moment. Wait for a few seconds, and then retry the `GetResourcePolicy` request.

After a `GetResourcePolicy` request returns a policy created using the `PutResourcePolicy` request, the policy will be applied in the authorization of requests to the resource. Because this process is eventually consistent, it will take some time to apply the policy to all requests to a resource. Policies that you attach while creating a table using the `CreateTable` request will always be applied to all requests for that table.

## Request Syntax
<a name="API_GetResourcePolicy_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourcePolicy_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceArn](#API_GetResourcePolicy_RequestSyntax) **   <a name="DDB-GetResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the DynamoDB resource to which the policy is attached. The resources you can specify include tables and streams.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: Yes

## Response Syntax
<a name="API_GetResourcePolicy_ResponseSyntax"></a>

```
{
   "Policy": "string",
   "RevisionId": "string"
}
```

## Response Elements
<a name="API_GetResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetResourcePolicy_ResponseSyntax) **   <a name="DDB-GetResourcePolicy-response-Policy"></a>
The resource-based policy document attached to the resource, which can be a table or stream, in JSON format.
Type: String

 ** [RevisionId](#API_GetResourcePolicy_ResponseSyntax) **   <a name="DDB-GetResourcePolicy-response-RevisionId"></a>
A unique string that represents the revision ID of the policy. If you're comparing revision IDs, make sure to always use string comparison logic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_GetResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** PolicyNotFoundException **
The operation tried to access a nonexistent resource-based policy.
If you specified an `ExpectedRevisionId`, it's possible that a policy is present for the resource but its revision ID didn't match the expected value.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## Examples
<a name="API_GetResourcePolicy_Examples"></a>

### Get the resource-based policy of a table
<a name="API_GetResourcePolicy_Example_1"></a>

The following example retrieves the resource-based policy of a table named `Thread`.

#### Sample Request
<a name="API_GetResourcePolicy_Example_1_Request"></a>

```
GET / HTTP/1.1
Host: dynamodb.<region>.<domain>;
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: DynamoDB_20120810.GetResourcePolicy
{
    "ResourceArn": "arn:aws:dynamodb:us-west-2:123456789012:table/Thread"
}
```

#### Sample Response
<a name="API_GetResourcePolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":[\"arn:aws:iam::111122223333:root\",\"arn:aws:iam::444455556666:root\"]},\"Action\":[\"dynamodb:GetItem\"],\"Resource\":\"arn:aws:dynamodb:us-west-2:123456789012:table/Thread\"}}",
    "RevisionId": "1683717331354"
}
```

## See Also
<a name="API_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/GetResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GetResourcePolicy)
