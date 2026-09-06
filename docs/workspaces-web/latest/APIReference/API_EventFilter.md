---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_EventFilter.html
---

# EventFilter
<a name="API_EventFilter"></a>

The filter that specifies the events to monitor.

## Contents
<a name="API_EventFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** all **   <a name="workspacesweb-Type-EventFilter-all"></a>
The filter that monitors all of the available events, including any new events emitted in the future.
Type: Structure
Required: No

 ** include **   <a name="workspacesweb-Type-EventFilter-include"></a>
The filter that monitors only the listed set of events. New events are not auto-monitored.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Values: `WebsiteInteract | FileDownloadFromSecureBrowserToRemoteDisk | FileTransferFromRemoteToLocalDisk | FileTransferFromLocalToRemoteDisk | FileUploadFromRemoteDiskToSecureBrowser | ContentPasteToWebsite | ContentTransferFromLocalToRemoteClipboard | ContentCopyFromWebsite | UrlLoad | TabOpen | TabClose | PrintJobSubmit | SessionConnect | SessionStart | SessionDisconnect | SessionEnd | UrlBlockByContentFilter`
Required: No

## See Also
<a name="API_EventFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/EventFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/EventFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/EventFilter)
