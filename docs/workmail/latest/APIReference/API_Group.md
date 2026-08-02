---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_Group.html
---

# Group
<a name="API_Group"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The representation of an WorkMail group.

## Contents
<a name="API_Group_Contents"></a>

 ** DisabledDate **   <a name="workmail-Type-Group-DisabledDate"></a>
The date indicating when the group was disabled from WorkMail use.
Type: Timestamp
Required: No

 ** Email **   <a name="workmail-Type-Group-Email"></a>
The email of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`
Required: No

 ** EnabledDate **   <a name="workmail-Type-Group-EnabledDate"></a>
The date indicating when the group was enabled for WorkMail use.
Type: Timestamp
Required: No

 ** Id **   <a name="workmail-Type-Group-Id"></a>
The identifier of the group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** Name **   <a name="workmail-Type-Group-Name"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** State **   <a name="workmail-Type-Group-State"></a>
The state of the group, which can be ENABLED, DISABLED, or DELETED.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/Group)
