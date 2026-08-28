---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageMetadata.html
---

# ImageMetadata
<a name="API_ImageMetadata"></a>

Information about the AMI.

## Contents
<a name="API_ImageMetadata_Contents"></a>

 ** creationDate **
The date and time the AMI was created.
Type: String
Required: No

 ** deprecationTime **
The deprecation date and time of the AMI, in UTC, in the following format: *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z.
Type: String
Required: No

 ** imageAllowed **
If `true`, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If `false`, the AMI can't be discovered or used in the account.
For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** imageId **
The ID of the AMI.
Type: String
Required: No

 ** imageOwnerAlias **
The alias of the AMI owner.
Valid values: `amazon` \| `aws-backup-vault` \| `aws-marketplace`
Type: String
Required: No

 ** imageOwnerId **
The ID of the AWS account that owns the AMI.
Type: String
Required: No

 ** imageState **
The current state of the AMI. If the state is `available`, the AMI is successfully registered and can be used to launch an instance.
Type: String
Valid Values: `pending | available | invalid | deregistered | transient | failed | error | disabled`
Required: No

 ** ImageWatermarkSet.N **
The watermarks attached to the AMI.
Type: Array of [ImageWatermark](API_ImageWatermark.md) objects
Required: No

 ** isPublic **
Indicates whether the AMI has public launch permissions. A value of `true` means this AMI has public launch permissions, while `false` means it has only implicit (AMI owner) or explicit (shared with your account) launch permissions.
Type: Boolean
Required: No

 ** name **
The name of the AMI.
Type: String
Required: No

## See Also
<a name="API_ImageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
