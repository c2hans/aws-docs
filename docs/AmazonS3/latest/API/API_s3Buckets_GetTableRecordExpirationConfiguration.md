---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableRecordExpirationConfiguration.html
---

# GetTableRecordExpirationConfiguration
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration"></a>

Retrieves the expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is `enabled`, records expire and are automatically removed from the table after the specified number of days.

Permissions
You must have the `s3tables:GetTableRecordExpirationConfiguration` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_RequestSyntax"></a>

```
GET /table-record-expiration?tableArn={{tableArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_GetTableRecordExpirationConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationConfiguration-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the table.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "settings": {
         "days": number
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_s3Buckets_GetTableRecordExpirationConfiguration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationConfiguration-response-configuration"></a>
The record expiration configuration for the table, including the status and retention settings.
Type: [TableRecordExpirationConfigurationValue](API_s3Buckets_TableRecordExpirationConfigurationValue.md) object

## Errors
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_Errors"></a>

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
<a name="API_s3Buckets_GetTableRecordExpirationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableRecordExpirationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
