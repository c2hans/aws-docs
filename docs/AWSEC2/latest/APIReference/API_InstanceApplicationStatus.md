---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceApplicationStatus.html
---

# InstanceApplicationStatus
<a name="API_InstanceApplicationStatus"></a>

Describes the application status for an instance.

## Contents
<a name="API_InstanceApplicationStatus_Contents"></a>

 ** applicationStatus **
The application status for the instance.
Type: [ApplicationStatus](API_ApplicationStatus.md) object
Required: No

 ** availabilityZone **
The Availability Zone of the instance.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone of the instance.
Type: String
Required: No

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceApplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceApplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceApplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceApplicationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
