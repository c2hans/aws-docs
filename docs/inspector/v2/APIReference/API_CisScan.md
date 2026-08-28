---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScan.html
---

# CisScan
<a name="API_CisScan"></a>

The CIS scan.

## Contents
<a name="API_CisScan_Contents"></a>

 ** scanArn **   <a name="inspector2-Type-CisScan-scanArn"></a>
The CIS scan's ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** scanConfigurationArn **   <a name="inspector2-Type-CisScan-scanConfigurationArn"></a>
The CIS scan's configuration ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-[0-9]{1}:[0-9]{12}:owner/(o-[a-z0-9]+|[0-9]{12})/cis-configuration/[0-9a-fA-F-]+`
Required: Yes

 ** failedChecks **   <a name="inspector2-Type-CisScan-failedChecks"></a>
The CIS scan's failed checks.
Type: Integer
Required: No

 ** scanDate **   <a name="inspector2-Type-CisScan-scanDate"></a>
The CIS scan's date.
Type: Timestamp
Required: No

 ** scanName **   <a name="inspector2-Type-CisScan-scanName"></a>
The the name of the scan configuration that's associated with this scan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** scheduledBy **   <a name="inspector2-Type-CisScan-scheduledBy"></a>
The account or organization that schedules the CIS scan.
Type: String
Required: No

 ** securityLevel **   <a name="inspector2-Type-CisScan-securityLevel"></a>
 The security level for the CIS scan. Security level refers to the Benchmark levels that CIS assigns to a profile.
Type: String
Valid Values: `LEVEL_1 | LEVEL_2`
Required: No

 ** status **   <a name="inspector2-Type-CisScan-status"></a>
The CIS scan's status.
Type: String
Valid Values: `FAILED | COMPLETED | CANCELLED | IN_PROGRESS`
Required: No

 ** targets **   <a name="inspector2-Type-CisScan-targets"></a>
The CIS scan's targets.
Type: [CisTargets](API_CisTargets.md) object
Required: No

 ** totalChecks **   <a name="inspector2-Type-CisScan-totalChecks"></a>
The CIS scan's total checks.
Type: Integer
Required: No

## See Also
<a name="API_CisScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisScan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
