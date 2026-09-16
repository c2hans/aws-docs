---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CopyProjectVersion.html
---

# CopyProjectVersion
<a name="API_CopyProjectVersion"></a>

**Note**
This operation applies only to Amazon Rekognition Custom Labels.

Copies a version of an Amazon Rekognition Custom Labels model from a source project to a destination project. The source and destination projects can be in different AWS accounts but must be in the same AWS Region. You can't copy a model to another AWS service.

To copy a model version to a different AWS account, you need to create a resource-based policy known as a *project policy*. You attach the project policy to the source project by calling [PutProjectPolicy](API_PutProjectPolicy.md). The project policy gives permission to copy the model version from a trusting AWS account to a trusted account.

For more information about creating and attaching a project policy document, see [Attaching a project policy (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-attach-project-policy.html).

If you are copying a model version to a project in the same AWS account, you don't need to create a project policy.

**Note**
Copying project versions is supported only for Custom Labels models.
To copy a model, the destination project, source project, and source model version must already exist.

Copying a model version takes a while to complete. To get the current status, call [DescribeProjectVersions](API_DescribeProjectVersions.md) and check the value of `Status` in the [ProjectVersionDescription](API_ProjectVersionDescription.md) object. The copy operation has finished when the value of `Status` is `COPYING_COMPLETED`.

This operation requires permissions to perform the `rekognition:CopyProjectVersion` action.

## Request Syntax
<a name="API_CopyProjectVersion_RequestSyntax"></a>

```
{
   "DestinationProjectArn": "{{string}}",
   "KmsKeyId": "{{string}}",
   "OutputConfig": {
      "S3Bucket": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   },
   "SourceProjectArn": "{{string}}",
   "SourceProjectVersionArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_CopyProjectVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationProjectArn](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-DestinationProjectArn"></a>
The ARN of the project in the trusted AWS account that you want to copy the model version to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

 ** [KmsKeyId](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-KmsKeyId"></a>
The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training results and manifest files written to the output Amazon S3 bucket (`OutputConfig`).
If you choose to use your own KMS key, you need the following permissions on the KMS key.
+ kms:CreateGrant
+ kms:DescribeKey
+ kms:GenerateDataKey
+ kms:Decrypt
If you don't specify a value for `KmsKeyId`, images copied into the service are encrypted using a key that AWS owns and manages.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

 ** [OutputConfig](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-OutputConfig"></a>
The S3 bucket and folder location where the training output for the source model version is placed.
Type: [OutputConfig](API_OutputConfig.md) object
Required: Yes

 ** [SourceProjectArn](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-SourceProjectArn"></a>
The ARN of the source project in the trusting AWS account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

 ** [SourceProjectVersionArn](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-SourceProjectVersionArn"></a>
The ARN of the model version in the source project that you want to copy to a destination project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

 ** [Tags](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-Tags"></a>
The key-value tags to assign to the model version.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [VersionName](#API_CopyProjectVersion_RequestSyntax) **   <a name="rekognition-CopyProjectVersion-request-VersionName"></a>
A name for the version of the model that's copied to the destination project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

## Response Syntax
<a name="API_CopyProjectVersion_ResponseSyntax"></a>

```
{
   "ProjectVersionArn": "string"
}
```

## Response Elements
<a name="API_CopyProjectVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProjectVersionArn](#API_CopyProjectVersion_ResponseSyntax) **   <a name="rekognition-CopyProjectVersion-response-ProjectVersionArn"></a>
The ARN of the copied model version in the destination project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`

## Errors
<a name="API_CopyProjectVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is already being used.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

The size of the resource exceeds the allowed limit. For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html).
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_CopyProjectVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CopyProjectVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CopyProjectVersion)
