---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketLogging.html
---

# GetTableBucketLogging
<a name="API_s3Buckets_GetTableBucketLogging"></a>

Gets the server access logging configuration for a table bucket. For more information, see [Server access logging for table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-server-logs.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:GetTableBucketLogging` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableBucketLogging_RequestSyntax"></a>

```
GET /buckets/{{tableBucketARN}}/logging HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableBucketLogging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_GetTableBucketLogging_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableBucketLogging-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableBucketLogging_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableBucketLogging_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tableBucketLoggingStatus": {
      "loggingEnabled": {
         "targetBucket": "string",
         "targetObjectKeyFormat": {
            "partitionedPrefix": {
               "partitionDateSource": "string"
            }
         },
         "targetPrefix": "string"
      }
   }
}
```

## Response Elements
<a name="API_s3Buckets_GetTableBucketLogging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tableBucketLoggingStatus](#API_s3Buckets_GetTableBucketLogging_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableBucketLogging-response-tableBucketLoggingStatus"></a>
The logging status of the table bucket. If logging is disabled, `loggingEnabled` is absent.
Type: [TableBucketLoggingStatus](API_s3Buckets_TableBucketLoggingStatus.md) object

## Errors
<a name="API_s3Buckets_GetTableBucketLogging_Errors"></a>

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
<a name="API_s3Buckets_GetTableBucketLogging_Examples"></a>

### Sample Request
<a name="API_s3Buckets_GetTableBucketLogging_Example_1"></a>

This request gets the server access logging configuration of the table bucket `arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket`.

```
GET /buckets/<URL-encoded table bucket ARN>/logging HTTP/1.1
Host: s3tables.us-east-1.amazonaws.com
Date: Wed, 04 Nov 2026 12:00:00 GMT
Authorization: authorization string
```

### Sample Response: Logging enabled
<a name="API_s3Buckets_GetTableBucketLogging_Example_2"></a>

This example illustrates one usage of GetTableBucketLogging.

```
HTTP/1.1 200 OK
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

### Sample Response: Logging disabled
<a name="API_s3Buckets_GetTableBucketLogging_Example_3"></a>

This example illustrates one usage of GetTableBucketLogging.

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "tableBucketLoggingStatus": {}
}
```

## See Also
<a name="API_s3Buckets_GetTableBucketLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableBucketLogging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableBucketLogging)
