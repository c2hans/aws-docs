---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketLogging.html
---

# PutTableBucketLogging
<a name="API_s3Buckets_PutTableBucketLogging"></a>

Sets, updates, or removes the server access logging configuration for a table bucket. When logging is enabled, Amazon S3 delivers a record of the requests made to the table bucket and its tables to the target general purpose bucket that you specify. To disable logging, call this operation with an empty `tableBucketLoggingStatus`. For more information, see [Server access logging for table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-server-logs.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:PutTableBucketLogging` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_PutTableBucketLogging_RequestSyntax"></a>

```
PUT /buckets/{{tableBucketARN}}/logging HTTP/1.1
Content-type: application/json

{
   "tableBucketLoggingStatus": {
      "loggingEnabled": {
         "targetBucket": "{{string}}",
         "targetObjectKeyFormat": {
            "partitionedPrefix": {
               "partitionDateSource": "{{string}}"
            }
         },
         "targetPrefix": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_s3Buckets_PutTableBucketLogging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_PutTableBucketLogging_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketLogging-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_PutTableBucketLogging_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tableBucketLoggingStatus](#API_s3Buckets_PutTableBucketLogging_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketLogging-request-tableBucketLoggingStatus"></a>
The logging status to apply to the table bucket. To disable logging, specify an empty `tableBucketLoggingStatus`.
Type: [TableBucketLoggingStatus](API_s3Buckets_TableBucketLoggingStatus.md) object
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableBucketLogging_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_s3Buckets_PutTableBucketLogging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_PutTableBucketLogging_Errors"></a>

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

## Examples
<a name="API_s3Buckets_PutTableBucketLogging_Examples"></a>

### Sample Request: Enabling logging
<a name="API_s3Buckets_PutTableBucketLogging_Example_1"></a>

This request enables server access logging for the table bucket `arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket`. Logs are delivered to the general purpose bucket `amzn-s3-demo-destination-bucket` under the prefix `logs/`, with object keys partitioned by the time of the logged events.

```
PUT /buckets/<URL-encoded table bucket ARN>/logging HTTP/1.1
Host: s3tables.us-east-1.amazonaws.com
Date: Wed, 04 Nov 2026 12:00:00 GMT
Authorization: authorization string
Content-Type: application/json

{
  "tableBucketLoggingStatus": {
    "loggingEnabled": {
      "targetBucket": "amzn-s3-demo-destination-bucket",
      "targetPrefix": "logs/",
      "targetObjectKeyFormat": {
        "partitionedPrefix": {
          "partitionDateSource": "EventTime"
        }
      }
    }
  }
}
```

### Sample Response
<a name="API_s3Buckets_PutTableBucketLogging_Example_2"></a>

This example illustrates one usage of PutTableBucketLogging.

```
HTTP/1.1 204 No Content
```

### Sample Request: Disabling logging
<a name="API_s3Buckets_PutTableBucketLogging_Example_3"></a>

This request disables server access logging for the table bucket `arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket`.

```
PUT /buckets/<URL-encoded table bucket ARN>/logging HTTP/1.1
Host: s3tables.us-east-1.amazonaws.com
Date: Wed, 04 Nov 2026 12:00:00 GMT
Authorization: authorization string
Content-Type: application/json

{
  "tableBucketLoggingStatus": {}
}
```

### Sample Response
<a name="API_s3Buckets_PutTableBucketLogging_Example_4"></a>

This example illustrates one usage of PutTableBucketLogging.

```
HTTP/1.1 204 No Content
```

## See Also
<a name="API_s3Buckets_PutTableBucketLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketLogging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketLogging)
