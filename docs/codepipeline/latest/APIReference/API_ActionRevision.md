---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ActionRevision.html
---

# ActionRevision
<a name="API_ActionRevision"></a>

Represents information about the version (or revision) of an action.

## Contents
<a name="API_ActionRevision_Contents"></a>

 ** created **   <a name="CodePipeline-Type-ActionRevision-created"></a>
The date and time when the most recent version of the action was created, in timestamp format.
Type: Timestamp
Required: Yes

 ** revisionChangeId **   <a name="CodePipeline-Type-ActionRevision-revisionChangeId"></a>
The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** revisionId **   <a name="CodePipeline-Type-ActionRevision-revisionId"></a>
The system-generated unique ID that identifies the revision number of the action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: Yes

## See Also
<a name="API_ActionRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionRevision)
