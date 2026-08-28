---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AccountVpcEncryptionControl.html
---

# AccountVpcEncryptionControl
<a name="API_AccountVpcEncryptionControl"></a>

Describes the account-level VPC Encryption Control configuration, including its mode, state, and exclusions.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_AccountVpcEncryptionControl_Contents"></a>

 ** exclusions **
Information about the traffic exclusions for the account-level VPC Encryption Control configuration.
Type: [AccountVpcEncryptionControlExclusions](API_AccountVpcEncryptionControlExclusions.md) object
Required: No

 ** lastUpdateTimestamp **
The date and time when the account-level VPC Encryption Control configuration was last updated.
Type: Timestamp
Required: No

 ** managedBy **
The entity that manages the account-level VPC Encryption Control configuration.
Type: String
Valid Values: `account | declarative-policy`
Required: No

 ** mode **
The encryption mode for the account-level VPC Encryption Control configuration.
Type: String
Valid Values: `unmanaged | attempt-monitor | attempt-enforce`
Required: No

 ** state **
The current state of the account-level VPC Encryption Control configuration.
Type: String
Valid Values: `default-state | transitions-in-progress | transitions-partially-successful | transitions-successful | transitions-failed`
Required: No

## See Also
<a name="API_AccountVpcEncryptionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AccountVpcEncryptionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AccountVpcEncryptionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AccountVpcEncryptionControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
