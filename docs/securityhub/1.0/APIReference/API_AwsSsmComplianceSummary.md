---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSsmComplianceSummary.html
---

# AwsSsmComplianceSummary
<a name="API_AwsSsmComplianceSummary"></a>

Provides the details about the compliance status for a patch.

## Contents
<a name="API_AwsSsmComplianceSummary_Contents"></a>

 ** ComplianceType **   <a name="securityhub-Type-AwsSsmComplianceSummary-ComplianceType"></a>
The type of resource for which the compliance was determined. For `AwsSsmPatchCompliance`, `ComplianceType` is `Patch`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CompliantCriticalCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-CompliantCriticalCount"></a>
For the patches that are compliant, the number that have a severity of `CRITICAL`.
Type: Integer
Required: No

 ** CompliantHighCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-CompliantHighCount"></a>
For the patches that are compliant, the number that have a severity of `HIGH`.
Type: Integer
Required: No

 ** CompliantInformationalCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-CompliantInformationalCount"></a>
For the patches that are compliant, the number that have a severity of `INFORMATIONAL`.
Type: Integer
Required: No

 ** CompliantLowCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-CompliantLowCount"></a>
For the patches that are compliant, the number that have a severity of `LOW`.
Type: Integer
Required: No

 ** CompliantMediumCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-CompliantMediumCount"></a>
For the patches that are compliant, the number that have a severity of `MEDIUM`.
Type: Integer
Required: No

 ** CompliantUnspecifiedCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-CompliantUnspecifiedCount"></a>
For the patches that are compliant, the number that have a severity of `UNSPECIFIED`.
Type: Integer
Required: No

 ** ExecutionType **   <a name="securityhub-Type-AwsSsmComplianceSummary-ExecutionType"></a>
The type of execution that was used determine compliance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NonCompliantCriticalCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-NonCompliantCriticalCount"></a>
For the patch items that are noncompliant, the number of items that have a severity of `CRITICAL`.
Type: Integer
Required: No

 ** NonCompliantHighCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-NonCompliantHighCount"></a>
For the patches that are noncompliant, the number that have a severity of `HIGH`.
Type: Integer
Required: No

 ** NonCompliantInformationalCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-NonCompliantInformationalCount"></a>
For the patches that are noncompliant, the number that have a severity of `INFORMATIONAL`.
Type: Integer
Required: No

 ** NonCompliantLowCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-NonCompliantLowCount"></a>
For the patches that are noncompliant, the number that have a severity of `LOW`.
Type: Integer
Required: No

 ** NonCompliantMediumCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-NonCompliantMediumCount"></a>
For the patches that are noncompliant, the number that have a severity of `MEDIUM`.
Type: Integer
Required: No

 ** NonCompliantUnspecifiedCount **   <a name="securityhub-Type-AwsSsmComplianceSummary-NonCompliantUnspecifiedCount"></a>
For the patches that are noncompliant, the number that have a severity of `UNSPECIFIED`.
Type: Integer
Required: No

 ** OverallSeverity **   <a name="securityhub-Type-AwsSsmComplianceSummary-OverallSeverity"></a>
The highest severity for the patches. Valid values are as follows:
+  `CRITICAL`
+  `HIGH`
+  `MEDIUM`
+  `LOW`
+  `INFORMATIONAL`
+  `UNSPECIFIED`
Type: String
Pattern: `.*\S.*`
Required: No

 ** PatchBaselineId **   <a name="securityhub-Type-AwsSsmComplianceSummary-PatchBaselineId"></a>
The identifier of the patch baseline. The patch baseline lists the patches that are approved for installation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PatchGroup **   <a name="securityhub-Type-AwsSsmComplianceSummary-PatchGroup"></a>
The identifier of the patch group for which compliance was determined. A patch group uses tags to group EC2 instances that should have the same patch compliance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsSsmComplianceSummary-Status"></a>
The current patch compliance status. Valid values are as follows:
+  `COMPLIANT`
+  `NON_COMPLIANT`
+  `UNSPECIFIED_DATA`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsSsmComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsSsmComplianceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsSsmComplianceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsSsmComplianceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
