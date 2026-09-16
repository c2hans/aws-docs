---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteIndex.html
---

# DeleteIndex
<a name="API_DeleteIndex"></a>

Deletes the specified index and turns off AWS Resource Explorer in the specified AWS Region. When you delete an index, Resource Explorer stops discovering and indexing resources in that Region. Resource Explorer also deletes all views in that Region. These actions occur as asynchronous background tasks. You can check to see when the actions are complete by using the [GetIndex](API_GetIndex.md) operation and checking the `Status` response value.

**Note**
If the index you delete is the aggregator index for the AWS account, you must wait 24 hours before you can promote another local index to be the aggregator index for the account. Users can't perform account-wide searches using Resource Explorer until another aggregator index is configured.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:DeleteIndex`

   **Resource**: The ARN of the index in the AWS Region in which you call this operation.

   [This action supports using condition keys to check the tags attached to the index to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To turn on Resource Explorer in an AWS Region by creating an index, use [CreateIndex](API_CreateIndex.md).
+ To retrieve the details for an index and check its state or its type, use [GetIndex](API_GetIndex.md).
+ To list all of the indexes in the AWS account, use [ListIndexes](API_ListIndexes.md).
+ To switch an index between being a local index or an aggregator index, use [UpdateIndexType](API_UpdateIndexType.md).

## Request Syntax
<a name="API_DeleteIndex_RequestSyntax"></a>

```
POST /DeleteIndex HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteIndex_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_DeleteIndex_RequestSyntax) **   <a name="resourceexplorer-DeleteIndex-request-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index that you want to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "LastUpdatedAt": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DeleteIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteIndex_ResponseSyntax) **   <a name="resourceexplorer-DeleteIndex-response-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index that you successfully started the deletion process.
This operation is asynchronous. To check its status, call the [GetIndex](API_GetIndex.md) operation.
Type: String

 ** [LastUpdatedAt](#API_DeleteIndex_ResponseSyntax) **   <a name="resourceexplorer-DeleteIndex-response-LastUpdatedAt"></a>
The date and time when you last updated this index.
Type: Timestamp

 ** [State](#API_DeleteIndex_ResponseSyntax) **   <a name="resourceexplorer-DeleteIndex-response-State"></a>
Indicates the current state of the index.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | UPDATING`

## Errors
<a name="API_DeleteIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_DeleteIndex_Examples"></a>

The following example deletes the Resource Explorer index in an AWS Region. In addition to specifying the ARN of the index, you must also call this operation from the Region in which the index exists. This turns off Resource Explorer in that Region, and users can no longer search for resources in that Region. You can get the ARN of the index by calling the [ListIndexes](API_ListIndexes.md) operation.

### Example
<a name="API_DeleteIndex_Example_1"></a>

This example illustrates one usage of DeleteIndex.

#### Sample Request
<a name="API_DeleteIndex_Example_1_Request"></a>

```
POST /DeleteIndex HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_DeleteIndex_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Arn":"arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "State":"deleting"
}
```

## See Also
<a name="API_DeleteIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/DeleteIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/DeleteIndex)
