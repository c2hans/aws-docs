---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DefaultApplication.html
---

# DefaultApplication
<a name="API_DefaultApplication"></a>

Represents the default Amazon GameLift Streams application that a stream group hosts.

## Contents
<a name="API_DefaultApplication_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="gameliftstreams-Type-DefaultApplication-Arn"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: No

 ** Id **   <a name="gameliftstreams-Type-DefaultApplication-Id"></a>
An ID that uniquely identifies the application resource. Example ID: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_DefaultApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/DefaultApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/DefaultApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/DefaultApplication)
