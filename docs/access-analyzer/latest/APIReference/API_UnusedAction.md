---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAction.html
---

# UnusedAction
<a name="API_UnusedAction"></a>

Contains information about an unused access finding for an action. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents
<a name="API_UnusedAction_Contents"></a>

 ** action **   <a name="accessanalyzer-Type-UnusedAction-action"></a>
The action for which the unused access finding was generated.
Type: String
Required: Yes

 ** lastAccessed **   <a name="accessanalyzer-Type-UnusedAction-lastAccessed"></a>
The time at which the action was last accessed.
Type: Timestamp
Required: No

## See Also
<a name="API_UnusedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAction)
