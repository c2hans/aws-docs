---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_AssessmentSummary.html
---

# AssessmentSummary
<a name="API_AssessmentSummary"></a>

Summarized information about an assessment.

## Contents
<a name="API_AssessmentSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssessmentArn **   <a name="AWSMarketplaceService-Type-AssessmentSummary-AssessmentArn"></a>
The ARN associated with the assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`
Required: No

 ** AssessmentId **   <a name="AWSMarketplaceService-Type-AssessmentSummary-AssessmentId"></a>
The unique ID of the assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

 ** AssessmentResult **   <a name="AWSMarketplaceService-Type-AssessmentSummary-AssessmentResult"></a>
The overall result of the assessment.
Type: String
Valid Values: `PASS | FAIL`
Required: No

 ** AssessmentTargetSummary **   <a name="AWSMarketplaceService-Type-AssessmentSummary-AssessmentTargetSummary"></a>
Identifies the entity or change set that was assessed.
Type: [AssessmentTargetSummary](API_AssessmentTargetSummary.md) object
Required: No

 ** CreatedAt **   <a name="AWSMarketplaceService-Type-AssessmentSummary-CreatedAt"></a>
The date and time the assessment was created, in ISO 8601 format (`2018-02-27T13:45:22Z`).
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** ExpiresAt **   <a name="AWSMarketplaceService-Type-AssessmentSummary-ExpiresAt"></a>
The date and time the assessment expires, in ISO 8601 format (`2018-02-27T13:45:22Z`).
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** FrameworkId **   <a name="AWSMarketplaceService-Type-AssessmentSummary-FrameworkId"></a>
The identifier of the framework that was evaluated by this assessment, in the format `frameworkId@version` (for example, `AMISecurity@1.0`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@.]+$`
Required: No

 ** FrameworkSummary **   <a name="AWSMarketplaceService-Type-AssessmentSummary-FrameworkSummary"></a>
The framework-specific details of the assessed resource. The set member corresponds to the framework identified by `FrameworkId`.
Type: [FrameworkSummary](API_FrameworkSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_AssessmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/AssessmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/AssessmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/AssessmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
