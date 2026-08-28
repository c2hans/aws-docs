---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateIndex.html
---

# CreateIndex
<a name="API_CreateIndex"></a>

Turns on AWS Resource Explorer in the AWS Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the [Search](API_Search.md) operation. You can create only one index in a Region.

**Note**
This operation creates only a *local* index. To promote the local index in one AWS Region into the aggregator index for the AWS account, use the [UpdateIndexType](API_UpdateIndexType.md) operation. For more information, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the * AWS Resource Explorer User Guide*.

For more details about what happens when you turn on Resource Explorer in an AWS Region, see [Turn on Resource Explorer to index your resources in an AWS Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html) in the * AWS Resource Explorer User Guide*.

If this is the first AWS Region in which you've created an index for Resource Explorer, then this operation also [creates a service-linked role](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html) in your AWS account that allows Resource Explorer to enumerate your resources to populate the index.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  **Action**: `resource-explorer-2:CreateIndex`

   **Resource**: The ARN of the index (as it will exist after the operation completes) in the AWS Region and account in which you're trying to create the index. Use the wildcard character (`*`) at the end of the string to match the eventual UUID. For example, the following `Resource` element restricts the role or user to creating an index in only the `us-east-2` Region of the specified account.

   `"Resource": "arn:aws:resource-explorer-2:us-west-2:<account-id>:index/*"`

  Alternatively, you can use `"Resource": "*"` to allow the role or user to create an index in any Region.
+  **Action**: `iam:CreateServiceLinkedRole`

   **Resource**: No specific resource (\*).

  This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the [service-linked role needed to index the resources in your account](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html). Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.

 **Related operations**
+ To turn off Resource Explorer in an AWS Region, use [DeleteIndex](API_DeleteIndex.md).
+ To retrieve the details for an index and check its state or its type, use [GetIndex](API_GetIndex.md).
+ To list all of the indexes in the AWS account, use [ListIndexes](API_ListIndexes.md).
+ To convert a local index to an aggregator index, use [UpdateIndexType](API_UpdateIndexType.md).

## Request Syntax
<a name="API_CreateIndex_RequestSyntax"></a>

```
POST /CreateIndex HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateIndex_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateIndex_RequestSyntax) **   <a name="resourceexplorer-CreateIndex-request-ClientToken"></a>
This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a [UUID-type value](https://wikipedia.org/wiki/Universally_unique_identifier) to ensure the uniqueness of your index.
Type: String
Required: No

 ** [Tags](#API_CreateIndex_RequestSyntax) **   <a name="resourceexplorer-CreateIndex-request-Tags"></a>
The specified tags are attached only to the index created in this AWS Region. The tags aren't attached to any of the resources listed in the index.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_CreateIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateIndex_ResponseSyntax) **   <a name="resourceexplorer-CreateIndex-response-Arn"></a>
The ARN of the new local index for the Region. You can reference this ARN in IAM permission policies to authorize the following operations: [DeleteIndex](API_DeleteIndex.md) \| [GetIndex](API_GetIndex.md) \| [UpdateIndexType](API_UpdateIndexType.md) \| [CreateView](API_CreateView.md)
Type: String

 ** [CreatedAt](#API_CreateIndex_ResponseSyntax) **   <a name="resourceexplorer-CreateIndex-response-CreatedAt"></a>
The date and timestamp when the index was created.
Type: Timestamp

 ** [State](#API_CreateIndex_ResponseSyntax) **   <a name="resourceexplorer-CreateIndex-response-State"></a>
Indicates the current state of the index. You can check for changes to the state for asynchronous operations by calling the [GetIndex](API_GetIndex.md) operation.
The state can remain in the `CREATING` or `UPDATING` state for several hours as Resource Explorer discovers the information about your resources and populates the index.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | UPDATING`

## Errors
<a name="API_CreateIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** ConflictException **
If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this AWS Region.
If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current AWS Region.
If you attempted to update an index type to `AGGREGATOR`, then the request failed because you already have an `AGGREGATOR` index in a different AWS Region.
HTTP Status Code: 409

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
<a name="API_CreateIndex_Examples"></a>

### Example
<a name="API_CreateIndex_Example_1"></a>

The following example creates a local index in the AWS Region in which you call the operation. In this example, the Region is `us-east-1`. The specified `ClientToken` is a randomly generated UUID.

#### Sample Request
<a name="API_CreateIndex_Example_1_Request"></a>

```
POST /CreateIndex HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{"ClientToken": "EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"}
```

#### Sample Response
<a name="API_CreateIndex_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Arn":"arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222",
    "CreatedAt":"2022-11-01T20:00:59.149Z",
    "State":"CREATING"
}
```

## See Also
<a name="API_CreateIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/CreateIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/CreateIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
