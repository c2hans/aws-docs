---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2Metadata.html
---

# Ec2Metadata
<a name="API_Ec2Metadata"></a>

Meta data details of an Amazon EC2 instance.

## Contents
<a name="API_Ec2Metadata_Contents"></a>

 ** amiId **   <a name="inspector2-Type-Ec2Metadata-amiId"></a>
The ID of the Amazon Machine Image (AMI) used to launch the instance.
Type: String
Pattern: `ami-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

 ** platform **   <a name="inspector2-Type-Ec2Metadata-platform"></a>
The platform of the instance.
Type: String
Valid Values: `WINDOWS | LINUX | UNKNOWN | MACOS`
Required: No

 ** tags **   <a name="inspector2-Type-Ec2Metadata-tags"></a>
The tags attached to the instance.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Ec2Metadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Ec2Metadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Ec2Metadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Ec2Metadata)
