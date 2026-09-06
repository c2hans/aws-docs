---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_Member.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Member
<a name="API_Member"></a>

The member details, such as email address, name, member ID, and member type.

## Contents
<a name="API_Member_Contents"></a>

 ** AccountId **   <a name="chime-Type-Member-AccountId"></a>
The Amazon Chime account ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Email **   <a name="chime-Type-Member-Email"></a>
The member email address.
Type: String
Required: No

 ** FullName **   <a name="chime-Type-Member-FullName"></a>
The member name.
Type: String
Required: No

 ** MemberId **   <a name="chime-Type-Member-MemberId"></a>
The member ID (user ID or bot ID).
Type: String
Pattern: `.*\S.*`
Required: No

 ** MemberType **   <a name="chime-Type-Member-MemberType"></a>
The member type.
Type: String
Valid Values: `User | Bot | Webhook`
Required: No

## See Also
<a name="API_Member_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/Member)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/Member)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/Member)
