---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RuntimeContext.html
---

# RuntimeContext
<a name="API_RuntimeContext"></a>

Additional information about the suspicious activity.

## Contents
<a name="API_RuntimeContext_Contents"></a>

 ** addressFamily **   <a name="guardduty-Type-RuntimeContext-addressFamily"></a>
Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IP version of 4 protocol.
Type: String
Required: No

 ** commandLineExample **   <a name="guardduty-Type-RuntimeContext-commandLineExample"></a>
Example of the command line involved in the suspicious activity.
Type: String
Required: No

 ** fileOperation **   <a name="guardduty-Type-RuntimeContext-fileOperation"></a>
Represents the type of file operation that triggered the finding, such as Write, Delete, Rename, Link, or Symlink.
Type: String
Required: No

 ** filePath **   <a name="guardduty-Type-RuntimeContext-filePath"></a>
The path of the sensitive file that was modified. Modification includes write, delete, rename, link, or symlink operations. This field is indexed for filtering.
Type: String
Required: No

 ** fileSystemType **   <a name="guardduty-Type-RuntimeContext-fileSystemType"></a>
Represents the type of mounted fileSystem.
Type: String
Required: No

 ** flags **   <a name="guardduty-Type-RuntimeContext-flags"></a>
Represents options that control the behavior of a runtime operation or action. For example, a filesystem mount operation may contain a read-only flag.
Type: Array of strings
Required: No

 ** ianaProtocolNumber **   <a name="guardduty-Type-RuntimeContext-ianaProtocolNumber"></a>
Specifies a particular protocol within the address family. Usually there is a single protocol in address families. For example, the address family `AF_INET` only has the IP protocol.
Type: Integer
Required: No

 ** ldPreloadValue **   <a name="guardduty-Type-RuntimeContext-ldPreloadValue"></a>
The value of the LD\_PRELOAD environment variable.
Type: String
Required: No

 ** libraryPath **   <a name="guardduty-Type-RuntimeContext-libraryPath"></a>
The path to the new library that was loaded.
Type: String
Required: No

 ** memoryRegions **   <a name="guardduty-Type-RuntimeContext-memoryRegions"></a>
Specifies the Region of a process's address space such as stack and heap.
Type: Array of strings
Required: No

 ** modifiedAt **   <a name="guardduty-Type-RuntimeContext-modifiedAt"></a>
The timestamp at which the process modified the current process. The timestamp is in UTC date string format.
Type: Timestamp
Required: No

 ** modifyingProcess **   <a name="guardduty-Type-RuntimeContext-modifyingProcess"></a>
Information about the process that modified the current process. This is available for multiple finding types.
Type: [ProcessDetails](API_ProcessDetails.md) object
Required: No

 ** moduleFilePath **   <a name="guardduty-Type-RuntimeContext-moduleFilePath"></a>
The path to the module loaded into the kernel.
Type: String
Required: No

 ** moduleName **   <a name="guardduty-Type-RuntimeContext-moduleName"></a>
The name of the module loaded into the kernel.
Type: String
Required: No

 ** moduleSha256 **   <a name="guardduty-Type-RuntimeContext-moduleSha256"></a>
The `SHA256` hash of the module.
Type: String
Required: No

 ** mountSource **   <a name="guardduty-Type-RuntimeContext-mountSource"></a>
The path on the host that is mounted by the container.
Type: String
Required: No

 ** mountTarget **   <a name="guardduty-Type-RuntimeContext-mountTarget"></a>
The path in the container that is mapped to the host directory.
Type: String
Required: No

 ** relatedFilePaths **   <a name="guardduty-Type-RuntimeContext-relatedFilePaths"></a>
All file paths modified by the same process that triggered the finding, up to a maximum of 25 paths.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** releaseAgentPath **   <a name="guardduty-Type-RuntimeContext-releaseAgentPath"></a>
The path in the container that modified the release agent file.
Type: String
Required: No

 ** runcBinaryPath **   <a name="guardduty-Type-RuntimeContext-runcBinaryPath"></a>
The path to the leveraged `runc` implementation.
Type: String
Required: No

 ** scriptPath **   <a name="guardduty-Type-RuntimeContext-scriptPath"></a>
The path to the script that was executed.
Type: String
Required: No

 ** serviceName **   <a name="guardduty-Type-RuntimeContext-serviceName"></a>
Name of the security service that has been potentially disabled.
Type: String
Required: No

 ** shellHistoryFilePath **   <a name="guardduty-Type-RuntimeContext-shellHistoryFilePath"></a>
The path to the modified shell history file.
Type: String
Required: No

 ** socketPath **   <a name="guardduty-Type-RuntimeContext-socketPath"></a>
The path to the docket socket that was accessed.
Type: String
Required: No

 ** targetProcess **   <a name="guardduty-Type-RuntimeContext-targetProcess"></a>
Information about the process that had its memory overwritten by the current process.
Type: [ProcessDetails](API_ProcessDetails.md) object
Required: No

 ** threatFilePath **   <a name="guardduty-Type-RuntimeContext-threatFilePath"></a>
The suspicious file path for which the threat intelligence details were found.
Type: String
Required: No

 ** toolCategory **   <a name="guardduty-Type-RuntimeContext-toolCategory"></a>
Category that the tool belongs to. Some of the examples are Backdoor Tool, Pentest Tool, Network Scanner, and Network Sniffer.
Type: String
Required: No

 ** toolName **   <a name="guardduty-Type-RuntimeContext-toolName"></a>
Name of the potentially suspicious tool.
Type: String
Required: No

## See Also
<a name="API_RuntimeContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RuntimeContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RuntimeContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RuntimeContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
