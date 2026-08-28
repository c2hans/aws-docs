---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_RoomMembership.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# RoomMembership
<a name="API_RoomMembership"></a>

The room membership details.

## Contents
<a name="API_RoomMembership_Contents"></a>

 ** InvitedBy **   <a name="chime-Type-RoomMembership-InvitedBy"></a>
The identifier of the user that invited the room member.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Member **   <a name="chime-Type-RoomMembership-Member"></a>
The member details, such as email address, name, member ID, and member type.
Type: [Member](API_Member.md) object
Required: No

 ** Role **   <a name="chime-Type-RoomMembership-Role"></a>
The membership role.
Type: String
Valid Values: `Administrator | Member`
Required: No

 ** RoomId **   <a name="chime-Type-RoomMembership-RoomId"></a>
The room ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedTimestamp **   <a name="chime-Type-RoomMembership-UpdatedTimestamp"></a>
The room membership update timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_RoomMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/RoomMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/RoomMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/RoomMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
