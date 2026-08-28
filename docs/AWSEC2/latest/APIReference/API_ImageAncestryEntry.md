---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageAncestryEntry.html
---

# ImageAncestryEntry
<a name="API_ImageAncestryEntry"></a>

Information about a single AMI in the ancestry chain and its source (parent) AMI.

## Contents
<a name="API_ImageAncestryEntry_Contents"></a>

 ** creationDate **
The date and time when this AMI was created.
Type: Timestamp
Required: No

 ** imageId **
The ID of this AMI.
Type: String
Required: No

 ** imageOwnerAlias **
The owner alias (`amazon` \| `aws-backup-vault` \| `aws-marketplace` ) of this AMI, if one is assigned. Otherwise, the value is `null`.
Type: String
Required: No

 ** sourceImageId **
The ID of the parent AMI.
Type: String
Required: No

 ** sourceImageRegion **
The AWS Region of the parent AMI.
Type: String
Required: No

## See Also
<a name="API_ImageAncestryEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageAncestryEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageAncestryEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageAncestryEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
