---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstanceTaskDetails.html
---

# ImportInstanceTaskDetails
<a name="API_ImportInstanceTaskDetails"></a>

Describes an import instance task.

## Contents
<a name="API_ImportInstanceTaskDetails_Contents"></a>

 ** description **
A description of the task.
Type: String
Required: No

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** platform **
The instance operating system.
Type: String
Valid Values: `Windows`
Required: No

 ** Volumes.N **
The volumes.
Type: Array of [ImportInstanceVolumeDetailItem](API_ImportInstanceVolumeDetailItem.md) objects
Required: No

## See Also
<a name="API_ImportInstanceTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportInstanceTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportInstanceTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportInstanceTaskDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
