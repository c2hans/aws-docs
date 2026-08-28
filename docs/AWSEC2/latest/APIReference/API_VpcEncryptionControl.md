---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcEncryptionControl.html
---

# VpcEncryptionControl
<a name="API_VpcEncryptionControl"></a>

Describes the configuration and state of VPC encryption controls.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_VpcEncryptionControl_Contents"></a>

 ** mode **
The encryption mode for the VPC Encryption Control configuration.
Type: String
Valid Values: `monitor | enforce`
Required: No

 ** resourceExclusions **
Information about resource exclusions for the VPC Encryption Control configuration.
Type: [VpcEncryptionControlExclusions](API_VpcEncryptionControlExclusions.md) object
Required: No

 ** state **
The current state of the VPC Encryption Control configuration.
Type: String
Valid Values: `enforce-in-progress | monitor-in-progress | enforce-failed | monitor-failed | deleting | deleted | available | creating | delete-failed`
Required: No

 ** stateMessage **
A message providing additional information about the encryption control state.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the VPC Encryption Control configuration.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcEncryptionControlId **
The ID of the VPC Encryption Control configuration.
Type: String
Required: No

 ** vpcId **
The ID of the VPC associated with the encryption control configuration.
Type: String
Required: No

## See Also
<a name="API_VpcEncryptionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcEncryptionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcEncryptionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcEncryptionControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
