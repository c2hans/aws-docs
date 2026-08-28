---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanFilePath.html
---

# ScanFilePath
<a name="API_ScanFilePath"></a>

Contains details of infected file including name, file path and hash.

## Contents
<a name="API_ScanFilePath_Contents"></a>

 ** fileName **   <a name="guardduty-Type-ScanFilePath-fileName"></a>
File name of the infected file.
Type: String
Required: No

 ** filePath **   <a name="guardduty-Type-ScanFilePath-filePath"></a>
The file path of the infected file.
Type: String
Required: No

 ** hash **   <a name="guardduty-Type-ScanFilePath-hash"></a>
The hash value of the infected file.
Type: String
Required: No

 ** volumeArn **   <a name="guardduty-Type-ScanFilePath-volumeArn"></a>
EBS volume ARN details of the infected file.
Type: String
Required: No

## See Also
<a name="API_ScanFilePath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanFilePath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanFilePath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanFilePath)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
