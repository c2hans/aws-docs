---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Describes a tag.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key ** (request), ** key ** (response)
The key of the tag.
Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:`.
Type: String
Required: No

 ** Value ** (request), ** value ** (response)
The value of the tag.
Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.
Type: String
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Tag)
