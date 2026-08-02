---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GroupIdentifier.html
---

# GroupIdentifier
<a name="API_GroupIdentifier"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The identifier that contains the Group ID and name of a group.

## Contents
<a name="API_GroupIdentifier_Contents"></a>

 ** GroupId **   <a name="workmail-Type-GroupIdentifier-GroupId"></a>
Group ID that matched the group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** GroupName **   <a name="workmail-Type-GroupIdentifier-GroupName"></a>
Group name that matched the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

## See Also
<a name="API_GroupIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GroupIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GroupIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GroupIdentifier)
