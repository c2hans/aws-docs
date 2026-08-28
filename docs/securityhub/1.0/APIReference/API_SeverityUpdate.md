---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SeverityUpdate.html
---

# SeverityUpdate
<a name="API_SeverityUpdate"></a>

Updates to the severity information for a finding.

## Contents
<a name="API_SeverityUpdate_Contents"></a>

 ** Label **   <a name="securityhub-Type-SeverityUpdate-Label"></a>
The severity value of the finding. The allowed values are the following.
+  `INFORMATIONAL` - No issue was found.
+  `LOW` - The issue does not require action on its own.
+  `MEDIUM` - The issue must be addressed but not urgently.
+  `HIGH` - The issue must be addressed as a priority.
+  `CRITICAL` - The issue must be remediated immediately to avoid it escalating.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** Normalized **   <a name="securityhub-Type-SeverityUpdate-Normalized"></a>
The normalized severity for the finding. This attribute is to be deprecated in favor of `Label`.
If you provide `Normalized` and don't provide `Label`, `Label` is set automatically as follows.
+ 0 - `INFORMATIONAL`
+ 1–39 - `LOW`
+ 40–69 - `MEDIUM`
+ 70–89 - `HIGH`
+ 90–100 - `CRITICAL`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Product **   <a name="securityhub-Type-SeverityUpdate-Product"></a>
The native severity as defined by the AWS service or integrated partner product that generated the finding.
Type: Double
Required: No

## See Also
<a name="API_SeverityUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SeverityUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SeverityUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SeverityUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
