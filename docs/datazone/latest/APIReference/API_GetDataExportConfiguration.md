---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDataExportConfiguration.html
---

# GetDataExportConfiguration
<a name="API_GetDataExportConfiguration"></a>

Gets data export configuration details.

## Request Syntax
<a name="API_GetDataExportConfiguration_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-export-configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataExportConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetDataExportConfiguration_RequestSyntax) **   <a name="datazone-GetDataExportConfiguration-request-uri-domainIdentifier"></a>
The ID of the domain where you want to get the data export configuration details.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetDataExportConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataExportConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "encryptionConfiguration": {
      "kmsKeyArn": "string",
      "sseAlgorithm": "string"
   },
   "isExportEnabled": boolean,
   "s3TableBucketArn": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetDataExportConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDataExportConfiguration_ResponseSyntax) **   <a name="datazone-GetDataExportConfiguration-response-createdAt"></a>
The timestamp at which the data export configuration report was created.
Type: Timestamp

 ** [encryptionConfiguration](#API_GetDataExportConfiguration_ResponseSyntax) **   <a name="datazone-GetDataExportConfiguration-response-encryptionConfiguration"></a>
The encryption configuration as part of the data export configuration details.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [isExportEnabled](#API_GetDataExportConfiguration_ResponseSyntax) **   <a name="datazone-GetDataExportConfiguration-response-isExportEnabled"></a>
Specifies whether the export is enabled.
Type: Boolean

 ** [s3TableBucketArn](#API_GetDataExportConfiguration_ResponseSyntax) **   <a name="datazone-GetDataExportConfiguration-response-s3TableBucketArn"></a>
The Amazon S3 table bucket ARN as part of the data export configuration details.
Type: String

 ** [status](#API_GetDataExportConfiguration_ResponseSyntax) **   <a name="datazone-GetDataExportConfiguration-response-status"></a>
The status of the data export configuration.
Type: String
Valid Values: `COMPLETED | FAILED`

 ** [updatedAt](#API_GetDataExportConfiguration_ResponseSyntax) **   <a name="datazone-GetDataExportConfiguration-response-updatedAt"></a>
The timestamp at which the data export configuration report was updated.
Type: Timestamp

## Errors
<a name="API_GetDataExportConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_GetDataExportConfiguration_Examples"></a>

### Example
<a name="API_GetDataExportConfiguration_Example_1"></a>

Get data export configuration:

#### Sample Request
<a name="API_GetDataExportConfiguration_Example_1_Request"></a>

```
aws datazone get-data-export-configuration --domain-identifier dzd-440699i00ezy21 --region us-east-2
```

#### Sample Response
<a name="API_GetDataExportConfiguration_Example_1_Response"></a>

```
{
    "isExportEnabled": true,
    "status": "COMPLETED",
    "s3TableBucketArn": "arn:aws:s3tables:us-east-2:651393673886:bucket/aws-sagemaker-catalog",
    "createdAt": "2025-11-26T06:17:32.580000+05:30",
    "updatedAt": "2025-11-26T06:17:32.580000+05:30"
}
```

### Example
<a name="API_GetDataExportConfiguration_Example_2"></a>

When export is disabled:

#### Sample Response
<a name="API_GetDataExportConfiguration_Example_2_Response"></a>

```
{
    "isExportEnabled": false,
    "status": "COMPLETED",
    "createdAt": "2025-11-26T06:17:32.580000+05:30",
    "updatedAt": "2025-11-26T06:17:32.580000+05:30"
}
```

### Example
<a name="API_GetDataExportConfiguration_Example_3"></a>

When export is enabled with KMS key provided:

#### Sample Response
<a name="API_GetDataExportConfiguration_Example_3_Response"></a>

```
{
    "isExportEnabled": true,
    "status": "COMPLETED",
    "encryptionConfiguration": {
        "kmsKeyArn": "arn:aws:kms:us-east-2:651393343886:key/292fedfe-c4b6-40fa-961b-87393584195c",
        "sseAlgorithm": "aws:kms"
    },
    "s3TableBucketArn": "arn:aws:s3tables:us-east-2:651393343886:bucket/aws-sagemaker-catalog",
    "createdAt": "2025-11-26T06:17:32.580000+05:30",
    "updatedAt": "2025-11-26T06:17:32.580000+05:30"
}
```

## See Also
<a name="API_GetDataExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetDataExportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetDataExportConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
