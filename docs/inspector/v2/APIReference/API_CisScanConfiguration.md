---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanConfiguration.html
---

# CisScanConfiguration
<a name="API_CisScanConfiguration"></a>

The CIS scan configuration.

## Contents
<a name="API_CisScanConfiguration_Contents"></a>

 ** scanConfigurationArn **   <a name="inspector2-Type-CisScanConfiguration-scanConfigurationArn"></a>
The CIS scan configuration's scan configuration ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-[0-9]{1}:[0-9]{12}:owner/(o-[a-z0-9]+|[0-9]{12})/cis-configuration/[0-9a-fA-F-]+`
Required: Yes

 ** ownerId **   <a name="inspector2-Type-CisScanConfiguration-ownerId"></a>
The CIS scan configuration's owner ID.
Type: String
Pattern: `\d{12}|o-[a-z0-9]{10,32}`
Required: No

 ** scanName **   <a name="inspector2-Type-CisScanConfiguration-scanName"></a>
The name of the CIS scan configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** schedule **   <a name="inspector2-Type-CisScanConfiguration-schedule"></a>
The CIS scan configuration's schedule.
Type: [Schedule](API_Schedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** securityLevel **   <a name="inspector2-Type-CisScanConfiguration-securityLevel"></a>
The CIS scan configuration's security level.
Type: String
Valid Values: `LEVEL_1 | LEVEL_2`
Required: No

 ** tags **   <a name="inspector2-Type-CisScanConfiguration-tags"></a>
The CIS scan configuration's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** targets **   <a name="inspector2-Type-CisScanConfiguration-targets"></a>
The CIS scan configuration's targets.
Type: [CisTargets](API_CisTargets.md) object
Required: No

## See Also
<a name="API_CisScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisScanConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
