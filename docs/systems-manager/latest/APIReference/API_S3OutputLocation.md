---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_S3OutputLocation.html
---

# S3OutputLocation
<a name="API_S3OutputLocation"></a>

An S3 bucket where you want to store the results of this request.

## Contents
<a name="API_S3OutputLocation_Contents"></a>

 ** OutputS3BucketName **   <a name="systemsmanager-Type-S3OutputLocation-OutputS3BucketName"></a>
The name of the S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** OutputS3KeyPrefix **   <a name="systemsmanager-Type-S3OutputLocation-OutputS3KeyPrefix"></a>
The S3 bucket subfolder.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** OutputS3Region **   <a name="systemsmanager-Type-S3OutputLocation-OutputS3Region"></a>
The AWS Region of the S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20.
Required: No

## See Also
<a name="API_S3OutputLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/S3OutputLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/S3OutputLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/S3OutputLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
