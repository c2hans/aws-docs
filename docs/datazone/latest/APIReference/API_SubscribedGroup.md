---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedGroup.html
---

# SubscribedGroup
<a name="API_SubscribedGroup"></a>

The group that subscribes to the asset.

## Contents
<a name="API_SubscribedGroup_Contents"></a>

 ** id **   <a name="datazone-Type-SubscribedGroup-id"></a>
The ID of the subscribed group.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** name **   <a name="datazone-Type-SubscribedGroup-name"></a>
The name of the subscribed group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9+=,.@-]+`
Required: No

## See Also
<a name="API_SubscribedGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedGroup)
