---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_LoggingInfo.html
---

# LoggingInfo
<a name="API_LoggingInfo"></a>

Information about an Amazon Simple Storage Service (Amazon S3) bucket to write managed node-level logs to.

**Note**
 `LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how AWS Systems Manager handles these options for the supported maintenance window task types, see [MaintenanceWindowTaskInvocationParameters](API_MaintenanceWindowTaskInvocationParameters.md).

## Contents
<a name="API_LoggingInfo_Contents"></a>

 ** S3BucketName **   <a name="systemsmanager-Type-LoggingInfo-S3BucketName"></a>
The name of an S3 bucket where execution logs are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** S3Region **   <a name="systemsmanager-Type-LoggingInfo-S3Region"></a>
The AWS Region where the S3 bucket is located.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20.
Required: Yes

 ** S3KeyPrefix **   <a name="systemsmanager-Type-LoggingInfo-S3KeyPrefix"></a>
(Optional) The S3 bucket subfolder.
Type: String
Length Constraints: Maximum length of 500.
Required: No

## See Also
<a name="API_LoggingInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/LoggingInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/LoggingInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/LoggingInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
