---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentFrameworkControlSet.html
---

# UpdateAssessmentFrameworkControlSet
<a name="API_UpdateAssessmentFrameworkControlSet"></a>

 A `controlSet` entity that represents a collection of controls in AWS Audit Manager. This doesn't contain the control set ID.

## Contents
<a name="API_UpdateAssessmentFrameworkControlSet_Contents"></a>

 ** controls **   <a name="auditmanager-Type-UpdateAssessmentFrameworkControlSet-controls"></a>
 The list of controls that are contained within the control set.
Type: Array of [CreateAssessmentFrameworkControl](API_CreateAssessmentFrameworkControl.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** name **   <a name="auditmanager-Type-UpdateAssessmentFrameworkControlSet-name"></a>
 The name of the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\\_]*$`
Required: Yes

 ** id **   <a name="auditmanager-Type-UpdateAssessmentFrameworkControlSet-id"></a>
 The unique identifier for the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\\_]*$`
Required: No

## See Also
<a name="API_UpdateAssessmentFrameworkControlSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/UpdateAssessmentFrameworkControlSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/UpdateAssessmentFrameworkControlSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/UpdateAssessmentFrameworkControlSet)
