---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CustomDataIdentifiersDetections.html
---

# CustomDataIdentifiersDetections
<a name="API_CustomDataIdentifiersDetections"></a>

The list of detected instances of sensitive data.

## Contents
<a name="API_CustomDataIdentifiersDetections_Contents"></a>

 ** Arn **   <a name="securityhub-Type-CustomDataIdentifiersDetections-Arn"></a>
The ARN of the custom identifier that was used to detect the sensitive data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Count **   <a name="securityhub-Type-CustomDataIdentifiersDetections-Count"></a>
The total number of occurrences of sensitive data that were detected.
Type: Long
Required: No

 ** Name **   <a name="securityhub-Type-CustomDataIdentifiersDetections-Name"></a>
he name of the custom identifier that detected the sensitive data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Occurrences **   <a name="securityhub-Type-CustomDataIdentifiersDetections-Occurrences"></a>
Details about the sensitive data that was detected.
Type: [Occurrences](API_Occurrences.md) object
Required: No

## See Also
<a name="API_CustomDataIdentifiersDetections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CustomDataIdentifiersDetections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CustomDataIdentifiersDetections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CustomDataIdentifiersDetections)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
