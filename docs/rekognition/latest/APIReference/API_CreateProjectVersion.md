---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html
---

# CreateProjectVersion
<a name="API_CreateProjectVersion"></a>

Creates a new version of Amazon Rekognition project (like a Custom Labels model or a custom adapter) and begins training. Models and adapters are managed as part of a Rekognition project. The response from `CreateProjectVersion` is an Amazon Resource Name (ARN) for the project version.

The FeatureConfig operation argument allows you to configure specific model or adapter settings. You can provide a description to the project version by using the VersionDescription argment. Training can take a while to complete. You can get the current status by calling [DescribeProjectVersions](API_DescribeProjectVersions.md). Training completed successfully if the value of the `Status` field is `TRAINING_COMPLETED`. Once training has successfully completed, call [DescribeProjectVersions](API_DescribeProjectVersions.md) to get the training results and evaluate the model.

This operation requires permissions to perform the `rekognition:CreateProjectVersion` action.

**Note**
 *The following applies only to projects with Amazon Rekognition Custom Labels as the chosen feature:*
For Custom Labels projects, training uses the training and test datasets associated with the project. For more information, see [Creating training and test datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html). After evaluating the model, you start the model by calling [StartProjectVersion](API_StartProjectVersion.md). If training fails, see [ Debugging a failed model training](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-debugging.html). For more information, see [Improving a trained Amazon Rekognition Custom Labels model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/improving-model.html).
You can train a model in a project that doesn't have associated datasets by specifying manifest files in the `TrainingData` and `TestingData` fields.
If you open the console after training a model with manifest files, Amazon Rekognition Custom Labels creates the datasets for you using the most recent manifest files. You can no longer train a model version for the project by specifying manifest files.
Instead of training with a project without associated datasets, we recommend that you use the manifest files to create training and test datasets for the project.

## Request Syntax
<a name="API_CreateProjectVersion_RequestSyntax"></a>

```
{
   "FeatureConfig": {
      "ContentModeration": {
         "ConfidenceThreshold": {{number}}
      }
   },
   "KmsKeyId": "{{string}}",
   "OutputConfig": {
      "S3Bucket": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   },
   "ProjectArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TestingData": {
      "Assets": [
         {
            "GroundTruthManifest": {
               "S3Object": {
                  "Bucket": "{{string}}",
                  "Name": "{{string}}",
                  "Version": "{{string}}"
               }
            }
         }
      ],
      "AutoCreate": {{boolean}}
   },
   "TrainingData": {
      "Assets": [
         {
            "GroundTruthManifest": {
               "S3Object": {
                  "Bucket": "{{string}}",
                  "Name": "{{string}}",
                  "Version": "{{string}}"
               }
            }
         }
      ]
   },
   "VersionDescription": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateProjectVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FeatureConfig](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-FeatureConfig"></a>
Feature-specific configuration of the training job. If the job configuration does not match the feature type associated with the project, an InvalidParameterException is returned.
Type: [CustomizationFeatureConfig](API_CustomizationFeatureConfig.md) object
Required: No

 ** [KmsKeyId](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-KmsKeyId"></a>
The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training images, test images, and manifest files copied into the service for the project version. Your source images are unaffected. The key is also used to encrypt training results and manifest files written to the output Amazon S3 bucket (`OutputConfig`).
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

 ** [OutputConfig](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-OutputConfig"></a>
The Amazon S3 bucket location to store the results of training. The bucket can be any S3 bucket in your AWS account. You need `s3:PutObject` permission on the bucket.
Type: [OutputConfig](API_OutputConfig.md) object
Required: Yes

 ** [ProjectArn](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-ProjectArn"></a>
The ARN of the Amazon Rekognition project that will manage the project version you want to train.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

 ** [Tags](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-Tags"></a>
 A set of tags (key-value pairs) that you want to attach to the project version.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [TestingData](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-TestingData"></a>
Specifies an external manifest that the service uses to test the project version. If you specify `TestingData` you must also specify `TrainingData`. The project must not have any associated datasets.
Type: [TestingData](API_TestingData.md) object
Required: No

 ** [TrainingData](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-TrainingData"></a>
Specifies an external manifest that the services uses to train the project version. If you specify `TrainingData` you must also specify `TestingData`. The project must not have any associated datasets.
Type: [TrainingData](API_TrainingData.md) object
Required: No

 ** [VersionDescription](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-VersionDescription"></a>
A description applied to the project version being created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_. ()':,;?]+`
Required: No

 ** [VersionName](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-VersionName"></a>
A name for the version of the project version. This value must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

## Response Syntax
<a name="API_CreateProjectVersion_ResponseSyntax"></a>

```
{
   "ProjectVersionArn": "string"
}
```

## Response Elements
<a name="API_CreateProjectVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProjectVersionArn](#API_CreateProjectVersion_ResponseSyntax) **   <a name="rekognition-CreateProjectVersion-response-ProjectVersionArn"></a>
The ARN of the model or the project version that was created. Use `DescribeProjectVersion` to get the current status of the training operation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`

## Errors
<a name="API_CreateProjectVersion_Errors"></a>

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
<a name="API_CreateProjectVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateProjectVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateProjectVersion)
