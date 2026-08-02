---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_LineageObject.html
---

# LineageObject
<a name="API_LineageObject"></a>

Information about the runtime process details.

## Contents
<a name="API_LineageObject_Contents"></a>

 ** euid **   <a name="guardduty-Type-LineageObject-euid"></a>
The effective user ID that was used to execute the process.
Type: Integer
Required: No

 ** executablePath **   <a name="guardduty-Type-LineageObject-executablePath"></a>
The absolute path of the process executable file.
Type: String
Required: No

 ** name **   <a name="guardduty-Type-LineageObject-name"></a>
The name of the process.
Type: String
Required: No

 ** namespacePid **   <a name="guardduty-Type-LineageObject-namespacePid"></a>
The process ID of the child process.
Type: Integer
Required: No

 ** parentUuid **   <a name="guardduty-Type-LineageObject-parentUuid"></a>
The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.
Type: String
Required: No

 ** pid **   <a name="guardduty-Type-LineageObject-pid"></a>
The ID of the process.
Type: Integer
Required: No

 ** startTime **   <a name="guardduty-Type-LineageObject-startTime"></a>
The time when the process started. This is in UTC format.
Type: Timestamp
Required: No

 ** userId **   <a name="guardduty-Type-LineageObject-userId"></a>
The user ID of the user that executed the process.
Type: Integer
Required: No

 ** uuid **   <a name="guardduty-Type-LineageObject-uuid"></a>
The unique ID assigned to the process by GuardDuty.
Type: String
Required: No

## See Also
<a name="API_LineageObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/LineageObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/LineageObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/LineageObject)
