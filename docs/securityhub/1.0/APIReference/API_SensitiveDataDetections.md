---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SensitiveDataDetections.html
---

# SensitiveDataDetections
<a name="API_SensitiveDataDetections"></a>

The list of detected instances of sensitive data.

## Contents
<a name="API_SensitiveDataDetections_Contents"></a>

 ** Count **   <a name="securityhub-Type-SensitiveDataDetections-Count"></a>
The total number of occurrences of sensitive data that were detected.
Type: Long
Required: No

 ** Occurrences **   <a name="securityhub-Type-SensitiveDataDetections-Occurrences"></a>
Details about the sensitive data that was detected.
Type: [Occurrences](API_Occurrences.md) object
Required: No

 ** Type **   <a name="securityhub-Type-SensitiveDataDetections-Type"></a>
The type of sensitive data that was detected. For example, the type might indicate that the data is an email address.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SensitiveDataDetections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SensitiveDataDetections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SensitiveDataDetections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SensitiveDataDetections)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
