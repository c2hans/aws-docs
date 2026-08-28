---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VolumeAttachment.html
---

# AwsEc2VolumeAttachment
<a name="API_AwsEc2VolumeAttachment"></a>

An attachment to an Amazon EC2 volume.

## Contents
<a name="API_AwsEc2VolumeAttachment_Contents"></a>

 ** AttachTime **   <a name="securityhub-Type-AwsEc2VolumeAttachment-AttachTime"></a>
The datetime when the attachment initiated.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeleteOnTermination **   <a name="securityhub-Type-AwsEc2VolumeAttachment-DeleteOnTermination"></a>
Whether the EBS volume is deleted when the EC2 instance is terminated.
Type: Boolean
Required: No

 ** InstanceId **   <a name="securityhub-Type-AwsEc2VolumeAttachment-InstanceId"></a>
The identifier of the EC2 instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsEc2VolumeAttachment-Status"></a>
The attachment state of the volume. Valid values are as follows:
+  `attaching`
+  `attached`
+  `busy`
+  `detaching`
+  `detached`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VolumeAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VolumeAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VolumeAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VolumeAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
