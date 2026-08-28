---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_FileSystemEndpoints.html
---

# FileSystemEndpoints
<a name="API_FileSystemEndpoints"></a>

An Amazon FSx for NetApp ONTAP file system has the following endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.

## Contents
<a name="API_FileSystemEndpoints_Contents"></a>

 ** Intercluster **   <a name="FSx-Type-FileSystemEndpoints-Intercluster"></a>
An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.
Type: [FileSystemEndpoint](API_FileSystemEndpoint.md) object
Required: No

 ** Management **   <a name="FSx-Type-FileSystemEndpoints-Management"></a>
An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.
Type: [FileSystemEndpoint](API_FileSystemEndpoint.md) object
Required: No

## See Also
<a name="API_FileSystemEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileSystemEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileSystemEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileSystemEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
