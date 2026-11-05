---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTableMigrations.html
---

# ListTableMigrations
<a name="API_s3Buckets_ListTableMigrations"></a>

Lists the migrations whose destination is in a table bucket, a namespace or a table. Specify a `tableBucketARN` to list the migrations into a table bucket, and add a `namespace`, or a `namespace` and a `name`, to narrow the list. Or specify a `tableARN` to list the migrations into a table.

Migrations are listed newest first. Results are paginated: use `maxResults` to set the page size, and pass the `nextToken` from a response to retrieve the next page of results. A page can contain fewer migrations than `maxResults`, or none, and still return a `nextToken`. Continue until a response has no `nextToken`.

Permissions
+ You must have the `s3tables:ListTableMigrations` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_ListTableMigrations_RequestSyntax"></a>

```
GET /list-table-migrations?hasValidPlan={{hasValidPlan}}&maxResults={{maxResults}}&name={{name}}&namespace={{namespace}}&nextToken={{nextToken}}&state={{state}}&tableARN={{tableARN}}&tableBucketARN={{tableBucketARN}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_ListTableMigrations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [hasValidPlan](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-hasValidPlan"></a>
The `hasValidPlan` value to filter the list by. Migrations that are still planning aren't listed, whichever value you specify.

 ** [maxResults](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-maxResults"></a>
The maximum number of migrations to return, from 1 to 1,000. If you don't specify a value, the default is 100.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [name](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-name"></a>
The name of the table to list migrations for. Requires `tableBucketARN` and `namespace`.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`

 ** [namespace](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-namespace"></a>
The namespace to list migrations for. Requires `tableBucketARN`.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`

 ** [nextToken](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-nextToken"></a>
The `nextToken` from a previous response, to get the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [state](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-state"></a>
The state to filter the list by. For the valid values, see the `state` member of `GetTableMigration`.
Valid Values: `new | planning | pendingReview | queued | migrating | succeeded | failed | cancelling | cancelled`

 ** [tableARN](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-tableARN"></a>
The Amazon Resource Name (ARN) of the table to list migrations for. The list includes the migrations into this table. To also list migrations into an earlier table of the same name, specify `tableBucketARN`, `namespace` and `name` instead. Specify either `tableARN` or `tableBucketARN`, not both.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

 ** [tableBucketARN](#API_s3Buckets_ListTableMigrations_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket to list migrations for.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`

## Request Body
<a name="API_s3Buckets_ListTableMigrations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_ListTableMigrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "migrations": [
      {
         "createdAt": "string",
         "hasValidPlan": boolean,
         "migrationId": "string",
         "name": "string",
         "namespace": "string",
         "state": "string",
         "stateUpdatedAt": "string",
         "tableARN": "string",
         "tableBucketARN": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_s3Buckets_ListTableMigrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [migrations](#API_s3Buckets_ListTableMigrations_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-response-migrations"></a>
The migrations, newest first.
Type: Array of [MigrationSummary](API_s3Buckets_MigrationSummary.md) objects

 ** [nextToken](#API_s3Buckets_ListTableMigrations_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListTableMigrations-response-nextToken"></a>
A token to pass as `nextToken` to get the next page of results. If there are no more results, this value isn't returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_s3Buckets_ListTableMigrations_Errors"></a>

 ** AccessDeniedException **
The action cannot be performed because you do not have the required permission.
HTTP Status Code: 403

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

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
<a name="API_s3Buckets_ListTableMigrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/ListTableMigrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ListTableMigrations)
