---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ProcessDetails.html
---

# ProcessDetails
<a name="API_ProcessDetails"></a>

Information about the observed process.

## Contents
<a name="API_ProcessDetails_Contents"></a>

 ** euid **   <a name="guardduty-Type-ProcessDetails-euid"></a>
The effective user ID of the user that executed the process.
Type: Integer
Required: No

 ** executablePath **   <a name="guardduty-Type-ProcessDetails-executablePath"></a>
The absolute path of the process executable file.
Type: String
Required: No

 ** executableSha256 **   <a name="guardduty-Type-ProcessDetails-executableSha256"></a>
The `SHA256` hash of the process executable.
Type: String
Required: No

 ** lineage **   <a name="guardduty-Type-ProcessDetails-lineage"></a>
Information about the process's lineage.
Type: Array of [LineageObject](API_LineageObject.md) objects
Required: No

 ** name **   <a name="guardduty-Type-ProcessDetails-name"></a>
The name of the process.
Type: String
Required: No

 ** namespacePid **   <a name="guardduty-Type-ProcessDetails-namespacePid"></a>
The ID of the child process.
Type: Integer
Required: No

 ** parentUuid **   <a name="guardduty-Type-ProcessDetails-parentUuid"></a>
The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.
Type: String
Required: No

 ** pid **   <a name="guardduty-Type-ProcessDetails-pid"></a>
The ID of the process.
Type: Integer
Required: No

 ** pwd **   <a name="guardduty-Type-ProcessDetails-pwd"></a>
The present working directory of the process.
Type: String
Required: No

 ** startTime **   <a name="guardduty-Type-ProcessDetails-startTime"></a>
The time when the process started. This is in UTC format.
Type: Timestamp
Required: No

 ** user **   <a name="guardduty-Type-ProcessDetails-user"></a>
The user that executed the process.
Type: String
Required: No

 ** userId **   <a name="guardduty-Type-ProcessDetails-userId"></a>
The unique ID of the user that executed the process.
Type: Integer
Required: No

 ** uuid **   <a name="guardduty-Type-ProcessDetails-uuid"></a>
The unique ID assigned to the process by GuardDuty.
Type: String
Required: No

## See Also
<a name="API_ProcessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ProcessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ProcessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ProcessDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
