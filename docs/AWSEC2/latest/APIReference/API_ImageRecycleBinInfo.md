---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageRecycleBinInfo.html
---

# ImageRecycleBinInfo
<a name="API_ImageRecycleBinInfo"></a>

Information about an AMI that is currently in the Recycle Bin.

## Contents
<a name="API_ImageRecycleBinInfo_Contents"></a>

 ** description **
The description of the AMI.
Type: String
Required: No

 ** imageId **
The ID of the AMI.
Type: String
Required: No

 ** name **
The name of the AMI.
Type: String
Required: No

 ** recycleBinEnterTime **
The date and time when the AMI entered the Recycle Bin.
Type: Timestamp
Required: No

 ** recycleBinExitTime **
The date and time when the AMI is to be permanently deleted from the Recycle Bin.
Type: Timestamp
Required: No

## See Also
<a name="API_ImageRecycleBinInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageRecycleBinInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageRecycleBinInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageRecycleBinInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
