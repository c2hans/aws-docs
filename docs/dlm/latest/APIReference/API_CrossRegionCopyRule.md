---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html
---

# CrossRegionCopyRule
<a name="API_CrossRegionCopyRule"></a>

 **[Custom snapshot and AMI policies only]** Specifies a cross-Region copy rule for a snapshot and AMI policies.

**Note**
To specify a cross-Region copy action for event-based polices, use [CrossRegionCopyAction](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyAction.html).

## Contents
<a name="API_CrossRegionCopyRule_Contents"></a>

 ** Encrypted **   <a name="dlm-Type-CrossRegionCopyRule-Encrypted"></a>
To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.
Type: Boolean
Required: Yes

 ** CmkArn **   <a name="dlm-Type-CrossRegionCopyRule-CmkArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,4}){0,2}:kms:([a-z]+-){2,3}\d:\d+:key/.*`
Required: No

 ** CopyTags **   <a name="dlm-Type-CrossRegionCopyRule-CopyTags"></a>
Indicates whether to copy all user-defined tags from the source snapshot or AMI to the cross-Region copy.
Type: Boolean
Required: No

 ** DeprecateRule **   <a name="dlm-Type-CrossRegionCopyRule-DeprecateRule"></a>
 **[Custom AMI policies only]** The AMI deprecation rule for cross-Region AMI copies created by the rule.
Type: [CrossRegionCopyDeprecateRule](API_CrossRegionCopyDeprecateRule.md) object
Required: No

 ** RetainRule **   <a name="dlm-Type-CrossRegionCopyRule-RetainRule"></a>
The retention rule that indicates how long the cross-Region snapshot or AMI copies are to be retained in the destination Region.
Type: [CrossRegionCopyRetainRule](API_CrossRegionCopyRetainRule.md) object
Required: No

 ** Target **   <a name="dlm-Type-CrossRegionCopyRule-Target"></a>
Use this parameter for snapshot policies only. For AMI policies, use **TargetRegion** instead.
 **[Custom snapshot policies only]** The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^[\w:\-\/\*]+$`
Required: No

 ** TargetRegion **   <a name="dlm-Type-CrossRegionCopyRule-TargetRegion"></a>
Use this parameter for AMI policies only. For snapshot policies, use **Target** instead. For snapshot policies created before the **Target** parameter was introduced, this parameter indicates the target Region for snapshot copies.

 **[Custom AMI policies only]** The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `([a-z]+-){2,3}\d`
Required: No

## See Also
<a name="API_CrossRegionCopyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/CrossRegionCopyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/CrossRegionCopyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/CrossRegionCopyRule)
