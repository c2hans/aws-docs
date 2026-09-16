---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PutDataExportConfiguration.html
---

# PutDataExportConfiguration
<a name="API_PutDataExportConfiguration"></a>

Creates data export configuration details.

If you want to temporarily disable export and later re-enable it for the same domain, use the `--no-enable-export` flag to disable and the `--enable-export` flag to re-enable. This preserves the configuration and allows you to re-enable export without deleting S3 table.

**Note**
You can enable asset metadata export for only one domain per account per Region. To enable export for a different domain, complete the following steps:
Delete the export configuration for the currently enabled domain using the DeleteDataExportConfiguration operation.
Delete the asset S3 table under the aws-sagemaker-catalog S3 table bucket. We recommend backing up the S3 table before deletion.
Call the PutDataExportConfiguration API to enable export for the new domain.

## Request Syntax
<a name="API_PutDataExportConfiguration_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/data-export-configuration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "enableExport": {{boolean}},
   "encryptionConfiguration": {
      "kmsKeyArn": "{{string}}",
      "sseAlgorithm": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutDataExportConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_PutDataExportConfiguration_RequestSyntax) **   <a name="datazone-PutDataExportConfiguration-request-uri-domainIdentifier"></a>
The domain ID for which you want to create data export configuration details.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_PutDataExportConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutDataExportConfiguration_RequestSyntax) **   <a name="datazone-PutDataExportConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [enableExport](#API_PutDataExportConfiguration_RequestSyntax) **   <a name="datazone-PutDataExportConfiguration-request-enableExport"></a>
Specifies that the export is to be enabled as part of creating data export configuration details.
Type: Boolean
Required: Yes

 ** [encryptionConfiguration](#API_PutDataExportConfiguration_RequestSyntax) **   <a name="datazone-PutDataExportConfiguration-request-encryptionConfiguration"></a>
The encryption configuration as part of creating data export configuration details.
The KMS key provided here as part of encryptionConfiguration must have the required permissions as described in [KMS permissions for exporting asset metadata in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.html).
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

## Response Syntax
<a name="API_PutDataExportConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutDataExportConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDataExportConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_PutDataExportConfiguration_Examples"></a>

### Example
<a name="API_PutDataExportConfiguration_Example_1"></a>

Enable data export:

#### Sample Request
<a name="API_PutDataExportConfiguration_Example_1_Request"></a>

```
aws datazone put-data-export-configuration  --domain-identifier dzd-440699i00ezy21 --region us-east-2 --enable-export
```

### Example
<a name="API_PutDataExportConfiguration_Example_2"></a>

Disable data export:

#### Sample Request
<a name="API_PutDataExportConfiguration_Example_2_Request"></a>

```
aws datazone put-data-export-configuration --domain-identifier dzd-440699i00ezy21 --region us-east-2 --no-enable-export
```

### Example
<a name="API_PutDataExportConfiguration_Example_3"></a>

With KMS key encryption configuration:

#### Sample Request
<a name="API_PutDataExportConfiguration_Example_3_Request"></a>

```
aws datazone put-data-export-configuration --encryption-configuration kmsKeyArn=arn:aws:kms:us-east-2:651673343886:key/292fedfe-c9h6-40fa-961b-87393584195c,sseAlgorithm=aws:kms --enable-export --region us-east-2 --domain-identifier dzd-440699i00ezy21
```

### Example
<a name="API_PutDataExportConfiguration_Example_4"></a>

With KMS key encryption configuration when KMS key is disabled:

#### Sample Response
<a name="API_PutDataExportConfiguration_Example_4_Response"></a>

```
An error occurred (ValidationException) when calling the PutDataExportConfiguration operation: The specified KMS key ARN is disabled. (Service: S3Tables, Status Code: 400, Request ID: 07bdfab7-6336-4145-b5ec-277a6a77a4e0) (SDK Attempt Count: 1)
```

### Example
<a name="API_PutDataExportConfiguration_Example_5"></a>

With KMS key encryption configuration when KMS key is missing permission for systemtables.sagemaker-catalog.amazonaws.com service principal:

#### Sample Response
<a name="API_PutDataExportConfiguration_Example_5_Response"></a>

```
An error occurred (AccessDeniedException) when calling the PutDataExportConfiguration operation: User: arn:aws:sts::750784792897:assumed-role/SageMakerCatalogDataSetPublisherRole/AWSSageMakerCatalog-S3TablesRole-651393378886 is not authorized to perform: kms:DescribeKey on this resource because the resource does not exist in this Region, no resource-based policies allow access, or a resource-based policy explicitly denies access (Service: S3Tables, Status Code: 403, Request ID: 86f5d9f9-62a6-4af9-8177-69edbb2992f4) (SDK Attempt Count: 1)
```

### Example
<a name="API_PutDataExportConfiguration_Example_6"></a>

With KMS key encryption configuration when SSE algorithm is not provided along with KMS key:

#### Sample Response
<a name="API_PutDataExportConfiguration_Example_6_Response"></a>

```
An error occurred (ValidationException) when calling the PutDataExportConfiguration operation: The specified SSE algorithm is invalid. (Service: S3Tables, Status Code: 400, Request ID: 678df137-aa8e-47aa-b485-a8971a3f2f3c) (SDK Attempt Count: 1)
```

### Example
<a name="API_PutDataExportConfiguration_Example_7"></a>

Enable export failing with conflict exception. Provide --client-token parameter with a different client token to resolve this error.

#### Sample Response
<a name="API_PutDataExportConfiguration_Example_7_Response"></a>

```
An error occurred (ConflictException) when calling the PutDataExportConfiguration operation: Conflict exception occurred while putting data export configuration for domain:dzd-cslg7hs0m6k4fd
```

### Example
<a name="API_PutDataExportConfiguration_Example_8"></a>

When configuration already exists for another domain:

#### Sample Response
<a name="API_PutDataExportConfiguration_Example_8_Response"></a>

```
An error occurred (ConflictException) when calling the PutDataExportConfiguration operation: Data Export Configuration exists for another domain with id: dzd-cslg7hs0m6k4fd
```

## See Also
<a name="API_PutDataExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/PutDataExportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PutDataExportConfiguration)
