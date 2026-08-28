---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ComprehendMedicalAsyncJobProperties.html
---

# ComprehendMedicalAsyncJobProperties
<a name="API_ComprehendMedicalAsyncJobProperties"></a>

Provides information about a detection job.

## Contents
<a name="API_ComprehendMedicalAsyncJobProperties_Contents"></a>

 ** DataAccessRoleArn **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) that gives Comprehend Medical; read access to your input data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** EndTime **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-EndTime"></a>
The time that the detection job completed.
Type: Timestamp
Required: No

 ** ExpirationTime **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-ExpirationTime"></a>
The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the `ListEntitiesDetectionV2Job` or the `ListPHIDetectionJobs` operation.
Type: Timestamp
Required: No

 ** InputDataConfig **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-InputDataConfig"></a>
The input data configuration that you supplied when you created the detection job.
Type: [InputDataConfig](API_InputDataConfig.md) object
Required: No

 ** JobId **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-JobId"></a>
The identifier assigned to the detection job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobName **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-JobName"></a>
The name that you assigned to the detection job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobStatus **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-JobStatus"></a>
The current status of the detection job. If the status is `FAILED`, the `Message` field shows the reason for the failure.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | PARTIAL_SUCCESS | FAILED | STOP_REQUESTED | STOPPED`
Required: No

 ** KMSKey **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-KMSKey"></a>
The AWS Key Management Service key, if any, used to encrypt the output files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** LanguageCode **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-LanguageCode"></a>
The language code of the input documents.
Type: String
Valid Values: `en`
Required: No

 ** ManifestFilePath **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-ManifestFilePath"></a>
The path to the file that describes the results of a batch job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Message **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-Message"></a>
A description of the status of a job.
Type: String
Required: No

 ** ModelVersion **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-ModelVersion"></a>
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.
Type: String
Required: No

 ** OutputDataConfig **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-OutputDataConfig"></a>
The output data configuration that you supplied when you created the detection job.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: No

 ** SubmitTime **   <a name="comprehendmedical-Type-ComprehendMedicalAsyncJobProperties-SubmitTime"></a>
The time that the detection job was submitted for processing.
Type: Timestamp
Required: No

## See Also
<a name="API_ComprehendMedicalAsyncJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/ComprehendMedicalAsyncJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/ComprehendMedicalAsyncJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/ComprehendMedicalAsyncJobProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
