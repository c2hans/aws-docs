---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableRecordExpirationConfiguration.html
---

# PutTableRecordExpirationConfiguration
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration"></a>

Creates or updates the expiration configuration settings for records in a table, including the status of the configuration. If you enable record expiration for a table, records expire and are automatically removed from the table after the number of days that you specify.

Permissions
You must have the `s3tables:PutTableRecordExpirationConfiguration` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_RequestSyntax"></a>

```
PUT /table-record-expiration?tableArn={{tableArn}} HTTP/1.1
Content-type: application/json

{
   "value": {
      "settings": {
         "days": {{number}}
      },
      "status": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_PutTableRecordExpirationConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableRecordExpirationConfiguration-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the table.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## Request Body
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [value](#API_s3Buckets_PutTableRecordExpirationConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableRecordExpirationConfiguration-request-value"></a>
The record expiration configuration to apply to the table, including the status (`enabled` or `disabled`) and retention period in days.
Type: [TableRecordExpirationConfigurationValue](API_s3Buckets_TableRecordExpirationConfigurationValue.md) object
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_Errors"></a>

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** InternalServerErrorException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.
HTTP Status Code: 405

 ** NotFoundException **
The request was rejected because the specified resource could not be found.
HTTP Status Code: 404

 ** TooManyRequestsException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

## See Also
<a name="API_s3Buckets_PutTableRecordExpirationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableRecordExpirationConfiguration)
