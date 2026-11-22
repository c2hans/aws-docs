---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DisassociateTableReplication.html
---

# DisassociateTableReplication

Disassociates a replica table from replication, making it a standalone writable table. Any in-progress replication to the table stops, and in-flight commits fail without being committed to the table. Disassociating a table from replication is permanent and can't be reversed.

You can only disassociate a replica table. If you call this operation on a table that isn't a replica table, including a table that you have already disassociated, the request fails.

After you disassociate a table from replication, you can write to the table as you do any other table. `GetTable` no longer returns `managedByService` and `managedTableInformation` for the table, and `ListTables` no longer returns `managedByService` for it. On the source table, `GetTableReplicationStatus` reports a failure for this destination the next time replication to it is attempted.

Disassociating a table from replication doesn't change its maintenance configuration. Review the maintenance settings of the table, such as compaction, after you disassociate it.

Permissions
You must have the `s3tables:DisassociateTableReplication` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_DisassociateTableReplication_RequestSyntax"></a>

```
PUT /table-replication/disassociate?tableArn={{tableArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_DisassociateTableReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_DisassociateTableReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_DisassociateTableReplication-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the replica table to disassociate from replication.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## Request Body
<a name="API_s3Buckets_DisassociateTableReplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_DisassociateTableReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_s3Buckets_DisassociateTableReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_DisassociateTableReplication_Errors"></a>

 ** AccessDeniedException **
The action cannot be performed because you do not have the required permission.
HTTP Status Code: 403

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

 ** ConflictException **
The request failed because there is a conflict with a previous write. You can retry the request.
HTTP Status Code: 409

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** InternalServerErrorException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified resource could not be found.
HTTP Status Code: 404

 ** TooManyRequestsException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

## See Also
<a name="API_s3Buckets_DisassociateTableReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/DisassociateTableReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/DisassociateTableReplication)
