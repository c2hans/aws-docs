---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisaData.html
---

# CisaData
<a name="API_CisaData"></a>

The Cybersecurity and Infrastructure Security Agency (CISA) details for a specific vulnerability.

## Contents
<a name="API_CisaData_Contents"></a>

 ** action **   <a name="inspector2-Type-CisaData-action"></a>
The remediation action recommended by CISA for this vulnerability.
Type: String
Length Constraints: Minimum length of 0.
Required: No

 ** dateAdded **   <a name="inspector2-Type-CisaData-dateAdded"></a>
The date and time CISA added this vulnerability to their catalogue.
Type: Timestamp
Required: No

 ** dateDue **   <a name="inspector2-Type-CisaData-dateDue"></a>
The date and time CISA expects a fix to have been provided vulnerability.
Type: Timestamp
Required: No

## See Also
<a name="API_CisaData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisaData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisaData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisaData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
