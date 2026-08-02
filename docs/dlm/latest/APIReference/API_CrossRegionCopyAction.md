---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyAction.html
---

# CrossRegionCopyAction
<a name="API_CrossRegionCopyAction"></a>

 **[Event-based policies only]** Specifies a cross-Region copy action for event-based policies.

**Note**
To specify a cross-Region copy rule for snapshot and AMI policies, use [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html).

## Contents
<a name="API_CrossRegionCopyAction_Contents"></a>

 ** EncryptionConfiguration **   <a name="dlm-Type-CrossRegionCopyAction-EncryptionConfiguration"></a>
The encryption settings for the copied snapshot.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: Yes

 ** Target **   <a name="dlm-Type-CrossRegionCopyAction-Target"></a>
The target Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^[\w:\-\/\*]+$`
Required: Yes

 ** RetainRule **   <a name="dlm-Type-CrossRegionCopyAction-RetainRule"></a>
Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies. After the retention period expires, the cross-Region copy is deleted.
Type: [CrossRegionCopyRetainRule](API_CrossRegionCopyRetainRule.md) object
Required: No

## See Also
<a name="API_CrossRegionCopyAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/CrossRegionCopyAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/CrossRegionCopyAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/CrossRegionCopyAction)
