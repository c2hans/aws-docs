---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Severity.html
---

# Severity
<a name="API_Severity"></a>

The severity of the finding.

The finding provider can provide the initial severity. The finding provider can only update the severity if it hasn't been updated using `BatchUpdateFindings`.

The finding must have either `Label` or `Normalized` populated. If only one of these attributes is populated, then Security Hub CSPM automatically populates the other one. If neither attribute is populated, then the finding is invalid. `Label` is the preferred attribute.

## Contents
<a name="API_Severity_Contents"></a>

 ** Label **   <a name="securityhub-Type-Severity-Label"></a>
The severity value of the finding. The allowed values are the following.
+  `INFORMATIONAL` - No issue was found.
+  `LOW` - The issue does not require action on its own.
+  `MEDIUM` - The issue must be addressed but not urgently.
+  `HIGH` - The issue must be addressed as a priority.
+  `CRITICAL` - The issue must be remediated immediately to avoid it escalating.
If you provide `Normalized` and don't provide `Label`, then `Label` is set automatically as follows.
+ 0 - `INFORMATIONAL`
+ 1–39 - `LOW`
+ 40–69 - `MEDIUM`
+ 70–89 - `HIGH`
+ 90–100 - `CRITICAL`
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** Normalized **   <a name="securityhub-Type-Severity-Normalized"></a>
Deprecated. The normalized severity of a finding. Instead of providing `Normalized`, provide `Label`.
The value of `Normalized` can be an integer between `0` and `100`.
If you provide `Label` and don't provide `Normalized`, then `Normalized` is set automatically as follows.
+  `INFORMATIONAL` - 0
+  `LOW` - 1
+  `MEDIUM` - 40
+  `HIGH` - 70
+  `CRITICAL` - 90
Type: Integer
Required: No

 ** Original **   <a name="securityhub-Type-Severity-Original"></a>
The native severity from the finding product that generated the finding.
Length Constraints: Minimum length of 1. Maximum length of 64.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Product **   <a name="securityhub-Type-Severity-Product"></a>
Deprecated. This attribute isn't included in findings. Instead of providing `Product`, provide `Original`.
The native severity as defined by the AWS service or integrated partner product that generated the finding.
Type: Double
Required: No

## See Also
<a name="API_Severity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Severity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Severity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Severity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
