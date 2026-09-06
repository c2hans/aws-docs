---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_MembershipItem.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# MembershipItem
<a name="API_MembershipItem"></a>

Membership details, such as member ID and member role.

## Contents
<a name="API_MembershipItem_Contents"></a>

 ** MemberId **   <a name="chime-Type-MembershipItem-MemberId"></a>
The member ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Role **   <a name="chime-Type-MembershipItem-Role"></a>
The member role.
Type: String
Valid Values: `Administrator | Member`
Required: No

## See Also
<a name="API_MembershipItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/MembershipItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/MembershipItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/MembershipItem)
