---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AtigData.html
---

# AtigData
<a name="API_AtigData"></a>

The Amazon Web Services Threat Intel Group (ATIG) details for a specific vulnerability.

## Contents
<a name="API_AtigData_Contents"></a>

 ** firstSeen **   <a name="inspector2-Type-AtigData-firstSeen"></a>
The date and time this vulnerability was first observed.
Type: Timestamp
Required: No

 ** lastSeen **   <a name="inspector2-Type-AtigData-lastSeen"></a>
The date and time this vulnerability was last observed.
Type: Timestamp
Required: No

 ** targets **   <a name="inspector2-Type-AtigData-targets"></a>
The commercial sectors this vulnerability targets.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** ttps **   <a name="inspector2-Type-AtigData-ttps"></a>
The [MITRE ATT&CK](https://attack.mitre.org/) tactics, techniques, and procedures (TTPs) associated with vulnerability.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 0. Maximum length of 30.
Required: No

## See Also
<a name="API_AtigData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AtigData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AtigData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AtigData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
