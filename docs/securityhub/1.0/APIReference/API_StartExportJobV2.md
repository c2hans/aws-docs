---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartExportJobV2.html
---

# StartExportJobV2
<a name="API_StartExportJobV2"></a>

Starts an ad hoc export job that writes Security Hub findings to an Amazon Simple Storage Service (Amazon S3) bucket that you own. Because the export runs asynchronously, this operation returns only the `ExportJobId` of the new job; it doesn't wait for the export to finish. Use `GetExportJobV2` to poll the job, and `ListExportJobsV2` to view the export jobs in your account.

Security Hub allows only one export job in the `RUNNING` state per account at a time. If an export job is already running, this operation returns a `ServiceQuotaExceededException`. Wait for the running job to finish, or cancel it with `CancelExportJobV2`, before you start a new one.

Specify the destination bucket and AWS Key Management Service (AWS KMS) key in the `Destination` parameter, and the output format (`CSV` or `OCSF_JSON`), optional filters, and field selection in the `OutputConfiguration` parameter. Before you call this operation, you must grant Security Hub permission to write to your bucket and use your AWS KMS key by adding the bucket policy and key policy statements shown in the Examples section.

Two identities use your AWS KMS key, and each needs its own permission. Security Hub uses the key when it writes the export objects to your bucket. The IAM principal that calls `StartExportJobV2` must also have `kms:GenerateDataKey` and `kms:Decrypt` permissions on the key. The Examples section shows both grants.

A delegated administrator can use the optional `Scopes` parameter to export findings for specific organizations or organizational units (OUs).

To make the request idempotent, provide a `ClientToken`. If you retry a `StartExportJobV2` request with the same `ClientToken` and the same request parameters, Security Hub returns the `ExportJobId` of the original job instead of starting a new one. If you reuse a `ClientToken` with different request parameters, this operation returns a `ConflictException`.

## Request Syntax
<a name="API_StartExportJobV2_RequestSyntax"></a>

```
POST /exportjobsv2 HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Destination": { ... },
   "Name": "{{string}}",
   "OutputConfiguration": { ... },
   "Scopes": {
      "AwsOrganizations": [
         {
            "OrganizationalUnitId": "{{string}}",
            "OrganizationId": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_StartExportJobV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartExportJobV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartExportJobV2_RequestSyntax) **   <a name="securityhub-StartExportJobV2-request-ClientToken"></a>
A unique identifier used to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[\x21-\x7E]{1,64}$`
Required: No

 ** [Destination](#API_StartExportJobV2_RequestSyntax) **   <a name="securityhub-StartExportJobV2-request-Destination"></a>
The destination that Security Hub writes the export to. You must specify exactly one destination type. Currently, the only supported type is Amazon S3.
Type: [ExportDestination](API_ExportDestination.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Name](#API_StartExportJobV2_RequestSyntax) **   <a name="securityhub-StartExportJobV2-request-Name"></a>
An optional, user-provided name for the export job that helps you identify it in `ListExportJobsV2` results. The value can be 1–256 characters. Alphanumeric characters, spaces, and the following ASCII characters are permitted: `. _ , : ( ) / + -`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [OutputConfiguration](#API_StartExportJobV2_RequestSyntax) **   <a name="securityhub-StartExportJobV2-request-OutputConfiguration"></a>
Specifies what data to export and how to format it. You must specify exactly one output type. Currently, the only supported type is `Findings`.
Type: [ExportOutput](API_ExportOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Scopes](#API_StartExportJobV2_RequestSyntax) **   <a name="securityhub-StartExportJobV2-request-Scopes"></a>
Limits the export to findings from specific organizational units (OUs) or from the delegated administrator's organization. Only the delegated administrator account can use this parameter; other accounts that specify it receive an `AccessDeniedException`.
This parameter is optional. If you omit it, the delegated administrator exports findings from all accounts across the entire organization, and other accounts export only their own findings.
You can specify up to 10 entries in `Scopes.AwsOrganizations`. If you specify multiple entries, Security Hub combines them using OR logic.
Type: [ExportScopes](API_ExportScopes.md) object
Required: No

## Response Syntax
<a name="API_StartExportJobV2_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "ExportJobId": "string"
}
```

## Response Elements
<a name="API_StartExportJobV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ExportJobId](#API_StartExportJobV2_ResponseSyntax) **   <a name="securityhub-StartExportJobV2-response-ExportJobId"></a>
The unique identifier of the export job that Security Hub started. Use this value with `GetExportJobV2` or `CancelExportJobV2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`

## Errors
<a name="API_StartExportJobV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** OrganizationalUnitNotFoundException **
The request failed because one or more organizational units specified in the request don't exist within the caller's organization.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed the service quota limit.
HTTP Status Code: 402

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## Examples
<a name="API_StartExportJobV2_Examples"></a>

### Example – Grant Security Hub permission to write to your S3 bucket
<a name="API_StartExportJobV2_Example_1"></a>

Before you start an export, attach a policy like the following to the destination Amazon S3 bucket. It allows the Security Hub export service principal (`exportv2.securityhub.amazonaws.com`) to write export objects to your bucket. The `aws:SourceAccount` condition key restricts access to export jobs that your own account starts. This protects against the confused deputy problem.

Each permission in the statement is required for the following reasons:
+  `s3:PutObject` – Writes the export objects, including the individual parts of a multipart upload.
+  `s3:GetObject` and `s3:ListBucket` – The export job needs these permissions when it writes its output. Exports fail without them.
+  `s3:AbortMultipartUpload` – Lets Security Hub clean up an incomplete multipart upload. Without this permission, exports can leave incomplete multipart uploads in your bucket, and those uploads continue to accrue storage charges until you remove them.

Specify both the bucket ARN and the object ARN in the `Resource` element. `s3:ListBucket` acts on the bucket itself and matches only the bucket ARN. The remaining permissions act on objects and match only the ARN that ends with `/*`.

In the following example, replace `amzn-s3-demo-bucket` with the name of your destination bucket, and `111122223333` with your AWS account ID.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSecurityHubExportsWrite",
            "Effect": "Allow",
            "Principal": {
                "Service": "exportv2.securityhub.amazonaws.com"
            },
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                }
            }
        }
    ]
}
```

### Example – Grant Security Hub permission to use your KMS key
<a name="API_StartExportJobV2_Example_2"></a>

Add a statement like the following to the key policy of the AWS KMS key that you specify in `KmsKeyArn`. It allows the Security Hub export service principal to use the key, through Amazon S3 only, to write export objects to your bucket with server-side encryption. In a key policy, a `Resource` value of `*` refers to the key that the policy is attached to, not to all keys.

Each permission and condition key in the statement is required for the following reasons:
+  `kms:GenerateDataKey` – Amazon S3 requests a data key from your AWS KMS key to encrypt the export objects with SSE-KMS.
+  `kms:Decrypt` – Amazon S3 requires this permission for the `UploadPart` operation of a multipart upload. Large exports use multipart uploads, and the writes fail without it.
+  `kms:ViaService` – Restricts the export service principal to using the key through Amazon S3 only, in the Region that you specify. In the `aws-cn` and `aws-us-gov` partitions, use the Amazon S3 service name for that partition.
+  `aws:SourceAccount` – Restricts use of the key to export jobs that your own account starts, which protects against the confused deputy problem.
+  `kms:EncryptionContext:aws:s3:arn` – Binds key use to a single bucket. Export writes use Amazon S3 Bucket Keys, so the encryption context value is the bucket ARN rather than an object ARN.

In the following example, replace `aa-example-1` with your AWS Region, `111122223333` with your AWS account ID, and `amzn-s3-demo-bucket` with the name of your destination bucket.

```
{
    "Sid": "AllowSecurityHubExportSseKmsWriteViaS3",
    "Effect": "Allow",
    "Principal": {
        "Service": "exportv2.securityhub.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "s3.aa-example-1.amazonaws.com",
            "aws:SourceAccount": "111122223333",
            "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-bucket"
        }
    }
}
```

### Example – Grant the calling principal permission to use your KMS key
<a name="API_StartExportJobV2_Example_3"></a>

Any principal that assigns a customer managed AWS KMS key to an export job must have permission to generate and decrypt data keys for that key. This requirement applies to the `StartExportJobV2` operation.

Add a statement like the following to the key policy of the AWS KMS key that you specify in `KmsKeyArn`.

Each permission and condition key in the statement is required for the following reasons:
+  `kms:GenerateDataKey` and `kms:Decrypt` – The two operations that the calling principal must be allowed to perform on the key.
+  `kms:EncryptionContext:aws:s3:arn` – Binds key use to a single bucket. Set the value to the ARN of your destination bucket.

In the following example, replace `111122223333` with your AWS account ID, `ExportCallerRole` with the name of the role that calls `StartExportJobV2`, and `amzn-s3-demo-bucket` with the name of your destination bucket.

```
{
    "Sid": "AllowSecurityHubExportCallerKeyAccess",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExportCallerRole"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-bucket"
        }
    }
}
```

## See Also
<a name="API_StartExportJobV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/StartExportJobV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StartExportJobV2)
