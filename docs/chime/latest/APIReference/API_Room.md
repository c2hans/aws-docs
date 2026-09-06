---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_Room.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Room
<a name="API_Room"></a>

The Amazon Chime chat room details.

## Contents
<a name="API_Room_Contents"></a>

 ** AccountId **   <a name="chime-Type-Room-AccountId"></a>
The Amazon Chime account ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedBy **   <a name="chime-Type-Room-CreatedBy"></a>
The identifier of the room creator.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedTimestamp **   <a name="chime-Type-Room-CreatedTimestamp"></a>
The room creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Name **   <a name="chime-Type-Room-Name"></a>
The room name.
Type: String
Required: No

 ** RoomId **   <a name="chime-Type-Room-RoomId"></a>
The room ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedTimestamp **   <a name="chime-Type-Room-UpdatedTimestamp"></a>
The room update timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_Room_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/Room)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/Room)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/Room)
