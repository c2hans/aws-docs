---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_NeptuneSettings.html
---

# NeptuneSettings
<a name="API_NeptuneSettings"></a>

Provides information that defines an Amazon Neptune endpoint.

## Contents
<a name="API_NeptuneSettings_Contents"></a>

 ** S3BucketFolder **   <a name="DMS-Type-NeptuneSettings-S3BucketFolder"></a>
A folder path where you want AWS DMS to store migrated graph data in the S3 bucket specified by `S3BucketName`
Type: String
Required: Yes

 ** S3BucketName **   <a name="DMS-Type-NeptuneSettings-S3BucketName"></a>
The name of the Amazon S3 bucket where AWS DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these .csv files.
Type: String
Required: Yes

 ** ErrorRetryDuration **   <a name="DMS-Type-NeptuneSettings-ErrorRetryDuration"></a>
The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.
Type: Integer
Required: No

 ** IamAuthEnabled **   <a name="DMS-Type-NeptuneSettings-IamAuthEnabled"></a>
If you want AWS Identity and Access Management (IAM) authorization enabled for this endpoint, set this parameter to `true`. Then attach the appropriate IAM policy document to your service role specified by `ServiceAccessRoleArn`. The default is `false`.
Type: Boolean
Required: No

 ** MaxFileSize **   <a name="DMS-Type-NeptuneSettings-MaxFileSize"></a>
The maximum size in kilobytes of migrated graph data stored in a .csv file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.
Type: Integer
Required: No

 ** MaxRetryCount **   <a name="DMS-Type-NeptuneSettings-MaxRetryCount"></a>
The number of times for AWS DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error. The default is 5.
Type: Integer
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-NeptuneSettings-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint. The role must allow the `iam:PassRole` action. For more information, see [Creating an IAM Service Role for Accessing Amazon Neptune as a Target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole) in the * AWS Database Migration Service User Guide. *
Type: String
Required: No

## See Also
<a name="API_NeptuneSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/NeptuneSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/NeptuneSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/NeptuneSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
