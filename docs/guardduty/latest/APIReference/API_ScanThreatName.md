---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanThreatName.html
---

# ScanThreatName
<a name="API_ScanThreatName"></a>

Contains files infected with the given threat providing details of malware name and severity.

## Contents
<a name="API_ScanThreatName_Contents"></a>

 ** filePaths **   <a name="guardduty-Type-ScanThreatName-filePaths"></a>
List of infected files in EBS volume with details.
Type: Array of [ScanFilePath](API_ScanFilePath.md) objects
Required: No

 ** itemCount **   <a name="guardduty-Type-ScanThreatName-itemCount"></a>
Total number of files infected with given threat.
Type: Integer
Required: No

 ** name **   <a name="guardduty-Type-ScanThreatName-name"></a>
The name of the identified threat.
Type: String
Required: No

 ** severity **   <a name="guardduty-Type-ScanThreatName-severity"></a>
Severity of threat identified as part of the malware scan.
Type: String
Required: No

## See Also
<a name="API_ScanThreatName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanThreatName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanThreatName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanThreatName)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
