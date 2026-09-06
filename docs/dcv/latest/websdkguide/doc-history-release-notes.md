---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/doc-history-release-notes.html
---

# Release Notes and Document History for Amazon DCV Web Client SDK
<a name="doc-history-release-notes"></a>

This page provides the release notes and document history for Amazon DCV Web Client SDK.

**Topics**
+ [Release Notes](#release-notes)
+ [Document History](#doc-history)

## Amazon DCV Web Client SDK Release Notes
<a name="release-notes"></a>

This section provides release notes for the Amazon DCV Web Client SDK by release date.

**Topics**
+ [1.13.2 — February 19, 2026](#1.13.2)
+ [1.10.1 — October 22, 2025](#1.10.1)
+ [1.9.100 — July 2, 2025](#1.9.100)
+ [1.8.7 — October 31, 2024](#1.8.7)
+ [1.8.4 — October 1, 2024](#1.8.4)
+ [1.5.10 — December 19, 2023](#1.5.10)
+ [1.5.6 — November 9, 2023](#1.5.6)
+ [1.4.4 — June 29, 2023](#1.4.4)
+ [1.4.0 — March 28, 2023](#1.4.0)
+ [1.3.1 — December 9, 2022](#1.3.1)
+ [1.3.0 — November 11, 2022](#1.3.0)
+ [1.2.1 — July 21, 2022](#1.2.1)
+ [1.2.0 — June 29, 2022](#1.2.0)
+ [1.1.3 — May 23, 2022](#1.1.3)
+ [1.1.2 — May 19, 2022](#1.1.2)
+ [1.1.1 — March 23, 2022](#1.1.1)
+ [1.1.0 — February 23, 2022](#1.1.0)
+ [1.0.4 — December 20, 2021](#1.0.4)
+ [1.0.3 — September 01, 2021](#1.0.3)
+ [1.0.2 — July 30, 2021](#1.0.2)
+ [1.0.1 — May 31, 2021](#1.0.1)
+ [1.0.0 — March 24, 2021](#1.0.0)

### 1.13.2 — February 19, 2026
<a name="1.13.2"></a>

| Build numbers | New features |
| --- | --- |
|  +  Semantic version: 1.13.2 <br />+  Build: 1074   |  +  Added `observers` object parameter to include httpExtraHeadersCallback and httpExtraSearchParamsCallback definitions for DCVViewer component. <br />+  Added `getMaxAllowedMonitorDimensions` api call in connection component to request the display dimension limits supported from the Amazon DCV server.   |

### 1.10.1 — October 22, 2025
<a name="1.10.1"></a>

| Build numbers | New features | Changes and bug fixes |
| --- | --- | --- |
|  +  Semantic version: 1.10.1 <br />+  Build: 1011   | The following features were added: +  Added mobile browser support (Chrome on Android, Chrome and Safari on iOS) <br />+  Added `gestureEvent` connection config callback function <br />+  New API `setTrackpadMode` to Enable/disable touch as trackpad mode  <br />+  New API `probe` to probe endpoints <br />+  Added gamepad support   |  +  Microphone is now grabbed and processed only when there is a remote application using it (needs 2025.0 sever) <br />+  Fixed a bug with Alt key and Firefox <br />+  Improved wheel scroll experience <br />+  Enabled webcam support in Firefox <br />+  Added audio stats in logs at info level <br />+  Fixed cursor resize when size not supported   |

### 1.9.100 — July 2, 2025
<a name="1.9.100"></a>

| Build numbers | New features |
| --- | --- |
|  +  Semantic version: 1.9.100 <br />+  Build: 952   |  +  Added `httpExtraSearchParamsCallback` connection config callback function to customize the URL when establishing a WebSocket connection to the Amazon DCV server (eg adding SigV4). <br />+  Added `httpExtraHeadersCallback` connection config callback function to add custom headers to the HTTP request (eg SigV4).   |

### 1.8.7 — October 31, 2024
<a name="1.8.7"></a>

| Build numbers | Changes and bug fixes |
| --- | --- |
|  +  Semantic version: 1.8.7 <br />+  Build: 858   |  +  Fixed rendering on Firefox 130 and newer   |

### 1.8.4 — October 1, 2024
<a name="1.8.4"></a>

| Build numbers | New features | Changes and bug fixes |
| --- | --- | --- |
|  +  Semantic version: 1.8.4 <br />+  Build: 840   | The following features were added: +  Renamed to “Amazon DCV Web Client SDK” <br />+  Added new API enableHighPixelDensity for high dpi displays <br />+  Added an experimental API setMicrophone to select the microphone in compatible browsers <br />+  Added new Connection Errors GATEWAY\_BUSY, UNSUPPORTED\_CREDENTIAL, and TRANSPORT\_ERROR <br />+  Added new Closing Reasons EXTERNAL\_PROTOCOL\_CONNECTION\_EVICTED, and DISCONNECTION\_REQUESTED   |  +  Improved Webcam handling <br />+  Improved audio playback handling <br />+  Improved WebCodecs handling <br />+  Improved plug and unplug of microphone and webcam <br />+  Improved remote window dragging when multimonitor <br />+  File storage upload and download permissions are now correctly propagated <br />+  Minor fixes on rendering   |

### 1.5.10 — December 19, 2023
<a name="1.5.10"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.5.10 <br />+  Build: 684   | Changes and bug fixes+  Fix stream decoding errors  |

### 1.5.6 — November 9, 2023
<a name="1.5.6"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.5.6 <br />+  Build: 659   | Changes and bug fixes+  Performance improvements in the stream decoding and rendering <br />+  Removed support for Internet Explorer 11  |

### 1.4.4 — June 29, 2023
<a name="1.4.4"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.4.4 <br />+  Build: 573   | Changes and bug fixes+  The viewer UI compoenent now uses the `navigator.keyboard.lock` API on browsers that support it to handle special keys in full screen. <br />+  Fixed a problem which could cause wrong colors when using Chrome 114 or newer. <br />+  Improved WebCodecs detection. <br />+  Fixed a problem with the mouse button state when entering the window. <br />+  Fixed a problem which could cause the modifier keys to remain pressed on macOS. <br />+  Improved audio robustness to degraded network conditions. <br />+  Fixed memory leaks. <br />+  Improved logs to include time and level.  |

### 1.4.0 — March 28, 2023
<a name="1.4.0"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.4.0 <br />+  Build: 476   | New features+  Added a new `uploadFiles` method to the `FileStorage` object to upload multiple files. <br />+  The viewer UI component now supports drag and drop to initiate file upload. <br />+  The WebCodecs browser API is now used also for audio and webcam. <br />Changes and bug fixes+  Fixed memory leaks related to repeated connections from the same page. <br />+  `setUploadBandwidth` now allows values up to 1 Gbps. <br />+  Optimized rendering of UI components. <br />+  Fixed support for animated cursors on Windows. <br />+  Fixed a problem with clipboard support when both text and image data are present for the same operation. <br />+  Improved robustness of the Webcam API: settings cannot be changed while a request is already in progress, `webcam.setEnabled` now keeps track of device ID for the request is in progress and returns a Promise. The viewer UI component shows notification in case of error.  |

### 1.3.1 — December 9, 2022
<a name="1.3.1"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.3.1 <br />+  Build: 413   | Changes and bug fixes+  Fixed a problem which could cause the Time Zone redirection UI to go out of synchronization with the server. <br />+  Fixed a memory leak after multiple reconnections. <br />+  Fixed a problem which caused a blank page on disconnetion. <br />+  Fixed a bug causing console warnings on audio decoder close.  |

### 1.3.0 — November 11, 2022
<a name="1.3.0"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.3.0 <br />+  Build: 407   | New features+  Adopted Cloudscape (https://cloudscape.design) for the UI Viewer component. <br />+  Added support for Time Zone redirection. <br />Changes and bug fixes+  Fixed missing update on asynchronous clipboard when the DCV viewer is focused. <br />+  The `setDisplayScale` function is not needed anymore when scaling the display on client side. <br />+  The `DCVViewer` component now automatically calls `disconnect()` when it is unmounted.  |

### 1.2.1 — July 21, 2022
<a name="1.2.1"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.2.1 <br />+  Build: 358   | Changes and bug fixes+  Fixed a problem that resulted in a failure to connect to Amazon DCV server 2019.1 and older.  |

### 1.2.0 — June 29, 2022
<a name="1.2.0"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.2.0 <br />+  Build: 352   | Changes and bug fixes+  Fixed crashing bug when the frames received are larger than the maximum supported resolution (4096x2160). <br />+  Resource objects (passed as arguments to `fileDownload` and `filePrinted` observers) now have the `accept` and `decline` methods that can be called on the object to download and discard the resource respectively. <br />+  Minor bug fix on automatic clipboard synchronization when disconnecting.  |

### 1.1.3 — May 23, 2022
<a name="1.1.3"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.1.3 <br />+  Build: 329   | Changes and bug fixes+  Fixed a problem preventing successful connection when specifying the web-url-path option.  |

### 1.1.2 — May 19, 2022
<a name="1.1.2"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.1.2 <br />+  Build: 322   | Changes and bug fixes+  Fixed a problem that could cause input to not work correctly after connection. <br />+  Fixed mouse coordinates when scale ratio is greater than 1.  |

### 1.1.1 — March 23, 2022
<a name="1.1.1"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.1.1 <br />+  Build: 309   | Changes and bug fixes+  Report `Transport Error` when communication with the server times out. <br />+  Fixed a recurring decoding error when streaming large resolutions.  |

### 1.1.0 — February 23, 2022
<a name="1.1.0"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.1.0 <br />+  Build: 295   | New features+  Release Amazon DCV Web UI SDK library with `DCVViewer` React component. <br />+  Export Amazon DCV Web Client SDK both as UMD and ES modules. <br />+  Added high color accuracy support. <br />+  Added the ability to list and interact with clients connected to a session. Added notifications for connection and disconnection. <br />Changes and bug fixes+  Improved webcodecs decoding support. <br />+  Various keyboard improvements. <br />+  Fix a bug that was preventing to open a second screen when the clipboard was disabled.  |

### 1.0.4 — December 20, 2021
<a name="1.0.4"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.0.4 <br />+  Build: 249   | New features+  Support opening multiple connections from the same page. <br />+  Support loading the SDK from a CDN.  |

### 1.0.3 — September 01, 2021
<a name="1.0.3"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.0.3 <br />+  Build: 202   | New features+  Experimental support for WebCodecs. This is disabled by default and must be enabled via the `ConnectionConfig` object using the new property `enableWebCodecs`. <br />+  Clipboard: added support for `image/png` data type on Chromium based browsers. <br />+  Added observer/callback to get the server’s screenshot as a PNG image (requires Amazon DCV server 2021.2). <br />Changes and bug fixes+ Improved handling of keyboard modifiers. |

### 1.0.2 — July 30, 2021
<a name="1.0.2"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.0.2 <br />+  Build: 167   |  +  Fixed pressure detection for stylus events. <br />+  Improved support for Korean keyboard layout on Chrome.   |

### 1.0.1 — May 31, 2021
<a name="1.0.1"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.0.1 <br />+  Build: 141   |  +  Fixed propagation of connection errors and close reasons <br />+  Fixed filestorage chunk progress update <br />+  Improved webcam handling <br />+  Improved audio-in processing   |

### 1.0.0 — March 24, 2021
<a name="1.0.0"></a>

| Version | Release notes |
| --- | --- |
|  +  Semantic version: 1.0.0 <br />+  Build: 81   | Initial release of the Amazon DCV Web Client SDK. |

## Document History
<a name="doc-history"></a>

The following table describes the documentation for this release of Amazon DCV Web Client SDK.

| Change | Description | Date |
| --- | --- | --- |
| Amazon DCV Web Client SDK version 1.13.2 | Amazon DCV Web Client SDK 1.13.2 is now available. For more information, see [SDK v.1.13.2](#1.13.2). | February 19, 2026 |
| Amazon DCV Web Client SDK version 1.10.1 | Amazon DCV Web Client SDK 1.10.1 is now available. For more information, see [SDK v.1.10.1](#1.10.1). | October 22, 2025 |
| Amazon DCV Web Client SDK version 1.9.100 | Amazon DCV Web Client SDK 1.9.100 is now available. For more information, see [SDK v.1.9.100](#1.9.100). | July 2, 2025 |
| Amazon DCV Web Client SDK version 1.8.7 | Amazon DCV Web Client SDK 1.8.7 is now available. For more information, see [SDK v.1.8.7](#1.8.7). | October 31, 2024 |
| Amazon DCV Web Client SDK version 1.8.4 | Amazon DCV Web Client SDK 1.8.4 is now available. For more information, see [SDK v.1.8.4](#1.8.4). | October 1, 2024 |
| Amazon DCV Web Client SDK version 1.5.6 | Amazon DCV Web Client SDK 1.5.6 is now available. For more information, see [SDK v.1.5.6](#1.5.6). | November 9, 2023 |
| Amazon DCV Web Client SDK version 1.4.4 | Amazon DCV Web Client SDK 1.4.4 is now available. For more information, see [SDK v.1.4.4](#1.4.4). | June 29, 2023 |
| Amazon DCV Web Client SDK version 1.4.0 | Amazon DCV Web Client SDK 1.4.0 is now available. For more information, see [SDK v.1.4.0](#1.4.0). | March 28, 2023 |
| Amazon DCV Web Client SDK version 1.3.1 | Amazon DCV Web Client SDK 1.3.1 is now available. For more information, see [SDK v.1.3.1](#1.3.1). | December 9, 2022 |
| Amazon DCV Web Client SDK version 1.3.0 | Amazon DCV Web Client SDK 1.3.0 is now available. For more information, see [SDK v.1.3.0](#1.3.0). | November 11, 2022 |
| Amazon DCV Web Client SDK version 1.2.0 | Amazon DCV Web Client SDK 1.2.0 is now available. For more information, see [SDK v.1.2.0](#1.2.0). | June 29, 2022 |
| Amazon DCV Web Client SDK version 1.1.0 | Amazon DCV Web Client SDK 1.1.0 is now available. For more information, see [SDK v.1.1.0](#1.1.0). | February 23, 2022 |
| Amazon DCV Web Client SDK version 1.0.1 | Fixed some typos. Minor bugs fixed, see [SDK v.1.0.1](#1.0.1). | May 31, 2021 |
| Initial release | First publication of this content. | March 24, 2021 |
