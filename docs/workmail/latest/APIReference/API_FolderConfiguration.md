---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_FolderConfiguration.html
---

# FolderConfiguration
<a name="API_FolderConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The configuration applied to an organization's folders by its retention policy.

## Contents
<a name="API_FolderConfiguration_Contents"></a>

 ** Action **   <a name="workmail-Type-FolderConfiguration-Action"></a>
The action to take on the folder contents at the end of the folder configuration period.
Type: String
Valid Values: `NONE | DELETE | PERMANENTLY_DELETE`
Required: Yes

 ** Name **   <a name="workmail-Type-FolderConfiguration-Name"></a>
The folder name.
Type: String
Valid Values: `INBOX | DELETED_ITEMS | SENT_ITEMS | DRAFTS | JUNK_EMAIL`
Required: Yes

 ** Period **   <a name="workmail-Type-FolderConfiguration-Period"></a>
The number of days for which the folder-configuration action applies.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 730.
Required: No

## See Also
<a name="API_FolderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/FolderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/FolderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/FolderConfiguration)
