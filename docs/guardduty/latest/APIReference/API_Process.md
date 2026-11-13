---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Process.html
---

# Process
<a name="API_Process"></a>

Contains information about a process in a process lineage. `ParentUuid` links each process to its parent process.

## Contents
<a name="API_Process_Contents"></a>

 ** uuid **   <a name="guardduty-Type-Process-uuid"></a>
The unique identifier of the process.
Type: String
Required: Yes

 ** findings **   <a name="guardduty-Type-Process-findings"></a>
The findings associated with this process.
Type: Array of [FindingReference](API_FindingReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** name **   <a name="guardduty-Type-Process-name"></a>
The name of the process.
Type: String
Required: No

 ** parentUuid **   <a name="guardduty-Type-Process-parentUuid"></a>
The unique identifier of the parent process. Not set for the root process.
Type: String
Required: No

 ** path **   <a name="guardduty-Type-Process-path"></a>
The path of the process executable.
Type: String
Required: No

## See Also
<a name="API_Process_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Process)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Process)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Process)
