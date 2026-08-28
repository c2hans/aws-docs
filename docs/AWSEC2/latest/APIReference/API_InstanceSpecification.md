---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceSpecification.html
---

# InstanceSpecification
<a name="API_InstanceSpecification"></a>

The instance details to specify which volumes should be snapshotted.

## Contents
<a name="API_InstanceSpecification_Contents"></a>

 ** InstanceId **
The instance to specify which volumes should be snapshotted.
Type: String
Required: Yes

 ** ExcludeBootVolume **
Excludes the root volume from being snapshotted.
Type: Boolean
Required: No

 ** ExcludeDataVolumeId.N **
The IDs of the data (non-root) volumes to exclude from the multi-volume snapshot set. If you specify the ID of the root volume, the request fails. To exclude the root volume, use **ExcludeBootVolume**.
You can specify up to 40 volume IDs per request.
Type: Array of strings
Required: No

## See Also
<a name="API_InstanceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
