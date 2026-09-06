---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AssessmentTarget.html
---

# AssessmentTarget
<a name="API_AssessmentTarget"></a>

Defines the criteria of assessment.

## Contents
<a name="API_AssessmentTarget_Contents"></a>

 ** condition **   <a name="migrationhubstrategy-Type-AssessmentTarget-condition"></a>
Condition of an assessment.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | CONTAINS | NOT_CONTAINS`
Required: Yes

 ** name **   <a name="migrationhubstrategy-Type-AssessmentTarget-name"></a>
Name of an assessment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** values **   <a name="migrationhubstrategy-Type-AssessmentTarget-values"></a>
Values of an assessment.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_AssessmentTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/AssessmentTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/AssessmentTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/AssessmentTarget)
