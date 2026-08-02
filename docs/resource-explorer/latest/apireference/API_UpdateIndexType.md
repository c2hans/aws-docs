---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UpdateIndexType.html
---

# UpdateIndexType
<a name="API_UpdateIndexType"></a>

Changes the type of the index from one of the following types to the other. For more information about indexes and the role they perform in AWS Resource Explorer, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the * AWS Resource Explorer User Guide*.
+  ** `AGGREGATOR` index type**

  The index contains information about resources from all AWS Regions in the AWS account in which you've created a Resource Explorer index. Resource information from all other Regions is replicated to this Region's index.

  When you change the index type to `AGGREGATOR`, Resource Explorer turns on replication of all discovered resource information from the other AWS Regions in your account to this index. You can then, from this Region only, perform resource search queries that span all AWS Regions in the AWS account. Turning on replication from all other Regions is performed by asynchronous background tasks. You can check the status of the asynchronous tasks by using the [GetIndex](API_GetIndex.md) operation. When the asynchronous tasks complete, the `Status` response of that operation changes from `UPDATING` to `ACTIVE`. After that, you can start to see results from other AWS Regions in query results. However, it can take several hours for replication from all other Regions to complete.
**Important**
You can have only one aggregator index per AWS account. Before you can promote a different index to be the aggregator index for the account, you must first demote the existing aggregator index to type `LOCAL`.
+  ** `LOCAL` index type**

  The index contains information about resources in only the AWS Region in which the index exists. If an aggregator index in another Region exists, then information in this local index is replicated to the aggregator index.

  When you change the index type to `LOCAL`, Resource Explorer turns off the replication of resource information from all other AWS Regions in the AWS account to this Region. The aggregator index remains in the `UPDATING` state until all replication with other Regions successfully stops. You can check the status of the asynchronous task by using the [GetIndex](API_GetIndex.md) operation. When Resource Explorer successfully stops all replication with other Regions, the `Status` response of that operation changes from `UPDATING` to `ACTIVE`. Separately, the resource information from other Regions that was previously stored in the index is deleted within 30 days by another background task. Until that asynchronous task completes, some results from other Regions can continue to appear in search results.
**Important**
After you demote an aggregator index to a local index, you must wait 24 hours before you can promote another index to be the new aggregator index for the account.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  **Action**: `resource-explorer-2:UpdateIndexType`

   **Resource**: The ARN of the index in the AWS Region in which you call this operation.

   [This action supports using condition keys to check the tags attached to the index to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To create an index and turn on Resource Explorer in an AWS Region, use [CreateIndex](API_CreateIndex.md).
+ To delete an index and turn off Resource Explorer in an AWS Region, use [DeleteIndex](API_DeleteIndex.md).

## Request Syntax
<a name="API_UpdateIndexType_RequestSyntax"></a>

```
POST /UpdateIndexType HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIndexType_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIndexType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_UpdateIndexType_RequestSyntax) **   <a name="resourceexplorer-UpdateIndexType-request-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index that you want to update.
Type: String
Required: Yes

 ** [Type](#API_UpdateIndexType_RequestSyntax) **   <a name="resourceexplorer-UpdateIndexType-request-Type"></a>
The type of the index. To understand the difference between `LOCAL` and `AGGREGATOR`, see [Turning on cross-Region search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the * AWS Resource Explorer User Guide*.
Type: String
Valid Values: `LOCAL | AGGREGATOR`
Required: Yes

## Response Syntax
<a name="API_UpdateIndexType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "LastUpdatedAt": "string",
   "State": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_UpdateIndexType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateIndexType_ResponseSyntax) **   <a name="resourceexplorer-UpdateIndexType-response-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index that you updated.
Type: String

 ** [LastUpdatedAt](#API_UpdateIndexType_ResponseSyntax) **   <a name="resourceexplorer-UpdateIndexType-response-LastUpdatedAt"></a>
The date and timestamp when the index was last updated.
Type: Timestamp

 ** [State](#API_UpdateIndexType_ResponseSyntax) **   <a name="resourceexplorer-UpdateIndexType-response-State"></a>
Indicates the state of the request to update the index. This operation is asynchronous. Call the [GetIndex](API_GetIndex.md) operation to check for changes.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | UPDATING`

 ** [Type](#API_UpdateIndexType_ResponseSyntax) **   <a name="resourceexplorer-UpdateIndexType-response-Type"></a>
Specifies the type of the specified index after the operation completes.
Type: String
Valid Values: `LOCAL | AGGREGATOR`

## Errors
<a name="API_UpdateIndexType_Errors"></a>

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

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request failed because it exceeds a service quota.
 ** Name **
The name of the service quota that was exceeded by the request.
 ** Value **
The current value for the quota that the request tried to exceed.
HTTP Status Code: 402

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_UpdateIndexType_Examples"></a>

### Example
<a name="API_UpdateIndexType_Example_1"></a>

The following example converts the specified index from type `LOCAL` to type `AGGREGATOR`. This turns on the ability to search for resources across all AWS Regions in the account. You must send the request to the AWS Region that contains the index you want to update.

#### Sample Request
<a name="API_UpdateIndexType_Example_1_Request"></a>

```
POST /UpdateIndexType HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "Type": "AGGREGATOR"
}
```

#### Sample Response
<a name="API_UpdateIndexType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Arn":"arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "LastUpdatedAt":"2022-07-13T18:41:58.799Z",
    "State":"UPDATING",
    "Type":"AGGREGATOR"
}
```

## See Also
<a name="API_UpdateIndexType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/UpdateIndexType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/UpdateIndexType)
