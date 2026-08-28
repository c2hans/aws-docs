---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Threat.html
---

# Threat
<a name="API_Threat"></a>

Provides information about the threat detected in a security finding and the file paths that were affected by the threat.

## Contents
<a name="API_Threat_Contents"></a>

 ** FilePaths **   <a name="securityhub-Type-Threat-FilePaths"></a>
Provides information about the file paths that were affected by the threat.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Type: Array of [FilePaths](API_FilePaths.md) objects
Required: No

 ** ItemCount **   <a name="securityhub-Type-Threat-ItemCount"></a>
This total number of items in which the threat has been detected.
Type: Integer
Required: No

 ** Name **   <a name="securityhub-Type-Threat-Name"></a>
The name of the threat.
Length Constraints: Minimum of 1 length. Maximum of 128 length.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Severity **   <a name="securityhub-Type-Threat-Severity"></a>
The severity of the threat.
Length Constraints: Minimum of 1 length. Maximum of 128 length.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Threat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Threat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Threat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Threat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
