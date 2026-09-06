---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Identity.html
---

# Identity
<a name="API_Identity"></a>

Contains an identity that can access an AWS IoT SiteWise Monitor resource.

**Note**
Currently, you can't use AWS API operations to retrieve IAM Identity Center identity IDs. You can find the IAM Identity Center identity IDs in the URL of user and group pages in the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

## Contents
<a name="API_Identity_Contents"></a>

 ** group **   <a name="iotsitewise-Type-Identity-group"></a>
An IAM Identity Center group identity.
Type: [GroupIdentity](API_GroupIdentity.md) object
Required: No

 ** iamRole **   <a name="iotsitewise-Type-Identity-iamRole"></a>
An IAM role identity.
Type: [IAMRoleIdentity](API_IAMRoleIdentity.md) object
Required: No

 ** iamUser **   <a name="iotsitewise-Type-Identity-iamUser"></a>
An IAM user identity.
Type: [IAMUserIdentity](API_IAMUserIdentity.md) object
Required: No

 ** user **   <a name="iotsitewise-Type-Identity-user"></a>
An IAM Identity Center user identity.
Type: [UserIdentity](API_UserIdentity.md) object
Required: No

## See Also
<a name="API_Identity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Identity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Identity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Identity)
