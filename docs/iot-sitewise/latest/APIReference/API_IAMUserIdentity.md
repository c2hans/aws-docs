---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_IAMUserIdentity.html
---

# IAMUserIdentity
<a name="API_IAMUserIdentity"></a>

Contains information about an AWS Identity and Access Management user.

## Contents
<a name="API_IAMUserIdentity_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-IAMUserIdentity-arn"></a>
The ARN of the IAM user. For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
If you delete the IAM user, access policies that contain this identity include an empty `arn`. You can delete the access policy for the IAM user that no longer exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`
Required: Yes

## See Also
<a name="API_IAMUserIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/IAMUserIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/IAMUserIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/IAMUserIdentity)
