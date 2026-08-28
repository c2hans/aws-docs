---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTemplate.html
---

# AssessmentTemplate
<a name="API_AssessmentTemplate"></a>

Contains information about an Amazon Inspector Classic assessment template. This data type is used as the response element in the [DescribeAssessmentTemplates](API_DescribeAssessmentTemplates.md) action.

## Contents
<a name="API_AssessmentTemplate_Contents"></a>

 ** arn **   <a name="Inspector-Type-AssessmentTemplate-arn"></a>
The ARN of the assessment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** assessmentRunCount **   <a name="Inspector-Type-AssessmentTemplate-assessmentRunCount"></a>
The number of existing assessment runs associated with this assessment template. This value can be zero or a positive integer.
Type: Integer
Required: Yes

 ** assessmentTargetArn **   <a name="Inspector-Type-AssessmentTemplate-assessmentTargetArn"></a>
The ARN of the assessment target that corresponds to this assessment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** createdAt **   <a name="Inspector-Type-AssessmentTemplate-createdAt"></a>
The time at which the assessment template is created.
Type: Timestamp
Required: Yes

 ** durationInSeconds **   <a name="Inspector-Type-AssessmentTemplate-durationInSeconds"></a>
The duration in seconds specified for this assessment template. The default value is 3600 seconds (one hour). The maximum value is 86400 seconds (one day).
Type: Integer
Valid Range: Minimum value of 180. Maximum value of 86400.
Required: Yes

 ** name **   <a name="Inspector-Type-AssessmentTemplate-name"></a>
The name of the assessment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: Yes

 ** rulesPackageArns **   <a name="Inspector-Type-AssessmentTemplate-rulesPackageArns"></a>
The rules packages that are specified for this assessment template.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** userAttributesForFindings **   <a name="Inspector-Type-AssessmentTemplate-userAttributesForFindings"></a>
The user-defined attributes that are assigned to every generated finding from the assessment run that uses this assessment template.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** lastAssessmentRunArn **   <a name="Inspector-Type-AssessmentTemplate-lastAssessmentRunArn"></a>
The Amazon Resource Name (ARN) of the most recent assessment run associated with this assessment template. This value exists only when the value of assessmentRunCount is greaterpa than zero.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_AssessmentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
