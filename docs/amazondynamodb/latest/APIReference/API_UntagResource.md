---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes the association of tags from an Amazon DynamoDB resource. You can call `UntagResource` up to five times per second, per account.
+  `UntagResource` is an asynchronous operation. If you issue a [ListTagsOfResource](API_ListTagsOfResource.md) request immediately after an `UntagResource` request, DynamoDB might return your previous tag set, if there was one, or an empty tag set. This is because `ListTagsOfResource` uses an eventually consistent query, and the metadata for your tags or table might not be available at that moment. Wait for a few seconds, and then try the `ListTagsOfResource` request again.
+ The application or removal of tags using `TagResource` and `UntagResource` APIs is eventually consistent. `ListTagsOfResource` API will only reflect the changes after a few seconds.

For an overview on tagging DynamoDB resources, see [Tagging for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html) in the *Amazon DynamoDB Developer Guide*.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="DDB-UntagResource-request-ResourceArn"></a>
The DynamoDB resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="DDB-UntagResource-request-TagKeys"></a>
A list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the DynamoDB resource.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

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

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UntagResource)
