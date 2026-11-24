---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorRelationshipPolicy.html
---

# SnapmirrorRelationshipPolicy

Describes the SnapMirror policy that an Amazon FSx for NetApp ONTAP SnapMirror relationship uses.

## Contents
<a name="API_SnapmirrorRelationshipPolicy_Contents"></a>

 ** PolicyId **   <a name="FSx-Type-SnapmirrorRelationshipPolicy-PolicyId"></a>
The ID of the SnapMirror policy.
Type: String
Pattern: `^(snapmirrorpol-[0-9a-f]{17})$`
Required: No

 ** PolicyName **   <a name="FSx-Type-SnapmirrorRelationshipPolicy-PolicyName"></a>
The name of the SnapMirror policy in ONTAP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_SnapmirrorRelationshipPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorRelationshipPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorRelationshipPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorRelationshipPolicy)
