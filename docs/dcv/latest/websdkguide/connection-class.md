---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/connection-class.html
---

# Connection Class
<a name="connection-class"></a>

The Connection Class obtained by calling the [`connect` method](dcv-module.md#connect) of the `dcv` module. For an example showing how to use it, see the [Getting started](establish-connection.md#auth-conn) section.

**Topics**
+ [Methods](#methods)

## Methods
<a name="methods"></a>

**Topics**
+ [attachDisplay(win, displayConf) → {Promise.<number>\|Promise.<{code: [MultiMonitorErrorCode](dcv-module.md#MultiMonitorErrorCode), message: string}>}](#attachDisplay)
+ [captureClipboardEvents(enabled, win, displayId) → {void}](#captureClipboardEvents)
+ [detachDisplay(displayId) → {void}](#detachDisplay)
+ [disconnect() → {void}](#disconnect)
+ [disconnectCollaborator(connectionId) → {void}](#disconnectCollaborator)
+ [enableDisplayQualityUpdates(enable) → {void}](#enableDisplayQualityUpdates)
+ [enableHighPixelDensity(enable) → {void}](#enableHighPixelDensity)
+ [enableTimezoneRedirection(enable) → {Promise\|Promise.<{code: [TimezoneRedirectionErrorCode](dcv-module.md#TimezoneRedirectionErrorCode), message: string}>}](#enableTimezoneRedirection)
+ [enterRelativeMouseMode() → {void}](#enterRelativeMouseMode)
+ [getConnectedDevices() → {Promise.<Array.<MediaDeviceInfo>>\|Promise.<{message: string}>}](#getConnectedDevices)
+ [getFileExplorer() → {Promise.<[filestorage](dcv-module.md#filestorage)>\|Promise.<{code: [ChannelErrorCode](dcv-module.md#ChannelErrorCode), message: string}>}](#getFileExplorer)
+ [getMaxAllowedMonitorDimensions() {[MaxDimensionLimits](dcv-module.md#MaxDimensionLimits)}](#getMaxAllowedMonitorDimensions)
+ [getServerInfo() → {[serverInfo](dcv-module.md#serverInfo)}](#getServerInfo)
+ [getScreenshot() → {Promise\|Promise.<{code: [ScreenshotErrorCode](dcv-module.md#ScreenshotErrorCode), message: string}>}](#getScreenshot)
+ [getStats() → {[stats](dcv-module.md#stats)}](#getStats)
+ [latchModifierKey(key, location, isDown) → {boolean}](#latchModifierKey)
+ [openChannel(name, authToken, callbacks, namespace) → {Promise\|Promise.<{code: [ChannelErrorCode](dcv-module.md#ChannelErrorCode), message: string}>}](#openChannel)
+ [queryFeature(featureName) → {Promise.<{enabled: boolean, remote?: string, autoCopy?: boolean, autoPaste?: boolean, serviceStatus?: string, available?: boolean}>\|Promise.<{message: string}>}](#queryFeature)
+ [registerKeyboardShortcuts(shortcuts) → {void}](#registerKeyboardShortcuts)
+ [requestDisplayConfig(highColorAccuracy) → {Promise\|Promise.<{code: [DisplayConfigErrorCode](dcv-module.md#DisplayConfigErrorCode), message: string}>}](#requestDisplayConfig)
+ [requestDisplayLayout(layout) → {Promise\|Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>}](#requestDisplayLayout)
+ [requestResolution(width, height) → {Promise\|Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>}](#requestResolution)
+ [sendKeyboardEvent(event) → {boolean}](#sendKeyboardEvent)
+ [sendKeyboardShortcut(shortcut) → {void}](#sendKeyboardShortcut)
+ [setDisplayQuality(min, maxopt) → {void}](#setDisplayQuality)
+ [setDisplayScale(scaleRatio, displayId) → {Promise\|Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>} (DEPRECATED)](#setDisplayScale)
+ [setKeyboardQuirks(quirks) → {void}](#setKeyboardQuirks)
+ [setMaxDisplayResolution(maxWidth, maxHeight) → {void}](#setMaxDisplayResolution)
+ [setMicrophone(enable) → {Promise\|Promise.<{code: [AudioErrorCode](dcv-module.md#AudioErrorCode), message: string}>}](#setMicrophone)
+ [setMinDisplayResolution(minWidth, minHeight) → {void}](#setMinDisplayResolution)
+ [setUploadBandwidth(value) → {number}](#setUploadBandwidth)
+ [setVolume(volume) → {void}](#setVolume)
+ [setMicrophone(enable, deviceId) → {Promise\|Promise.<{code: [AudioErrorCode](dcv-module.md#AudioErrorCode), message: string}>}](#setMicrophone)
+ [setWebcam(enable, deviceId) → {Promise\|Promise.<{code: [WebcamErrorCode](dcv-module.md#WebcamErrorCode), message: string}>}](#setWebcam)
+ [syncClipboards() → {boolean}](#syncClipboards)

### attachDisplay(win, displayConf) → {Promise.<number>\|Promise.<{code: [MultiMonitorErrorCode](dcv-module.md#MultiMonitorErrorCode), message: string}>}
<a name="attachDisplay"></a>

 Attaches a specific display to a window. You can't attach the main display. If successful, the function returns the `displayId`.

#### Parameters:
<a name="parameters-1"></a>

<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>win</code> </td><td> Object </td><td> The window to which the display must be attached. </td></tr>
  <tr><td> <code>displayConf</code> </td><td> Object </td><td> The configuration of the display.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Attributes </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>displayId</code> </td><td> number </td><td> &lt;optional&gt; </td><td> The ID of the display. </td></tr>
  <tr><td> <code>displayDivName</code> </td><td> </td><td> </td><td> The name of the display div. </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>

#### Returns:
<a name="returns"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise.<number> \| Promise.<{code: [MultiMonitorErrorCode](dcv-module.md#MultiMonitorErrorCode), message: string}>

### captureClipboardEvents(enabled, win, displayId) → {void}
<a name="captureClipboardEvents"></a>

 Starts or stops listening to copy-paste events. In the case of interactive clipboards (always in the case of paste) we need to start listening to the copy/paste events. It could be useful to start and stop listening only when it is needed, for example, when a modal is shown.

#### Parameters:
<a name="parameters-2"></a>

|  Name  |  Type  |  Attributes  |  Description  |
| --- | --- | --- | --- |
|  enabled  |  boolean  |   |  To start listening to events, specify true. To stop listening to events, specify false.  |
|  win  |  Object  |  <optional>  |  The window in which to listen for events. If omitted, the default window is used.  |
|  displayId  |  number  |  <optional>  |  The ID of the display that should listen the events. If omitted, the default display of the window is used.  |

#### Returns:
<a name="returns-1"></a>

 Type
 void

### detachDisplay(displayId) → {void}
<a name="detachDisplay"></a>

 Detaches a specific display. The main display cannot be detached.

#### Parameters:
<a name="parameters-3"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  displayId  |  number  |  The ID of the display to detach.  |

#### Returns:
<a name="returns-2"></a>

 Type
 void

### disconnect() → {void}
<a name="disconnect"></a>

 Disconnects from the Amazon DCV server and closes the connection.

#### Returns:
<a name="returns-3"></a>

 Type
 void

### disconnectCollaborator(connectionId) → {void}
<a name="disconnectCollaborator"></a>

 Requests disconnect of collaborator connected with the provided connection id (since Amazon DCV Web Client SDK version 1.1.0).

#### Parameters:
<a name="parameters-4"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  connectionId  |  boolean  |  The id of the connection that will be disconnected.  |

#### Returns:
<a name="returns-4"></a>

 Type
 void

### enableDisplayQualityUpdates(enable) → {void}
<a name="enableDisplayQualityUpdates"></a>

 Enables or disables display quality updates for streaming areas that do not receive updates. Disabling display quality updates reduces bandwidth usage, but it also decreases the display quality.

#### Parameters:
<a name="parameters-5"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enable  |  boolean  |  To enable display quality updates, specify true. To disable display quality updates, specify false.  |

#### Returns:
<a name="returns-5"></a>

 Type
 void

### enableHighPixelDensity(enable) → {void}
<a name="enableHighPixelDensity"></a>

 Enables or disables high pixel density on the client.

#### Parameters:
<a name="parameters-5"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enable  |  boolean  |  Whether or not high pixel density should be enabled.  |

#### Returns:
<a name="returns-5"></a>

 Type
 void

### enableTimezoneRedirection(enable) → {Promise\|Promise.<{code: [TimezoneRedirectionErrorCode](dcv-module.md#TimezoneRedirectionErrorCode), message: string}>}
<a name="enableTimezoneRedirection"></a>

 Enables or disables timezone redirection. Once it is enabled, the client requests the server to make the server desktop timezone match the client timezone.

#### Parameters:
<a name="parameters-5"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enable  |  boolean  |  To enable timezone redirection, specify true. To disable timezone redirection, specify false.  |

#### Returns:
<a name="returns-5"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise.<number> \| Promise.<{code: [TimezoneRedirectionErrorCode](dcv-module.md#TimezoneRedirectionErrorCode), message: string}>

### enterRelativeMouseMode() → {void}
<a name="enterRelativeMouseMode"></a>

 Enables relative mouse mode.

#### Returns:
<a name="returns65"></a>

 Type
 void

### getConnectedDevices() → {Promise.<Array.<MediaDeviceInfo>>\|Promise.<{message: string}>}
<a name="getConnectedDevices"></a>

 Requests a list of the media devices connected to the client computer.

#### Returns:
<a name="returns-7"></a>

 If successful, it returns a Promise that resolves to an array of MediaDeviceInfo objects. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/MediaDeviceInfo. If rejected, the promise returns an error object.

 Type
 Promise.<Array.<MediaDeviceInfo>> \| Promise.<{message: string}>

### getFileExplorer() → {Promise.<[filestorage](dcv-module.md#filestorage)>\|Promise.<{code: [ChannelErrorCode](dcv-module.md#ChannelErrorCode), message: string}>}
<a name="getFileExplorer"></a>

 Gets an object to manage the Amazon DCV server's file storage.

#### Returns:
<a name="returns-8"></a>

 Promise. Resolves to the file explorer object if fulfilled, or an error object if rejected.

 Type
 Promise.<[filestorage](dcv-module.md#filestorage)> \| Promise.<{code: [ChannelErrorCode](dcv-module.md#ChannelErrorCode), message: string}>

### getMaxAllowedMonitorDimensions() {[MaxDimensionLimits](dcv-module.md#MaxDimensionLimits)}
<a name="getMaxAllowedMonitorDimensions"></a>

 Requests the display dimension limits supported from the Amazon DCV server.

#### Returns:
<a name="returns-35"></a>

 The object containing maxLargestDimension and maxSmallestDimension supported on webclient by the server.

 Type
 [MaxDimensionLimits](dcv-module.md#MaxDimensionLimits)

### getServerInfo() → {[serverInfo](dcv-module.md#serverInfo)}
<a name="getServerInfo"></a>

 Gets information about the Amazon DCV server.

#### Returns:
<a name="returns-9"></a>

 Information about the server software.

 Type
 [serverInfo](dcv-module.md#serverInfo)

### getScreenshot() → {Promise\|Promise.<{code: [ScreenshotErrorCode](dcv-module.md#ScreenshotErrorCode), message: string}>}
<a name="getScreenshot"></a>

 Retrieves the screenshot of the remote desktop in PNG format. The screenshot will be returned in the [screenshotCallback](dcv-module.md#screenshotCallback) observer. `null` will be returned instead in case of failures.

#### Returns:
<a name="returns-30"></a>

 Promise that resolves if the request is processed. If rejected we receive an error object.

 Type
 Promise \| Promise.<{code: [ScreenshotErrorCode](dcv-module.md#ScreenshotErrorCode), message: string}>

### getStats() → {[stats](dcv-module.md#stats)}
<a name="getStats"></a>

 Gets statistics about the Amazon DCV server.

#### Returns:
<a name="returns-10"></a>

 Information about the streaming statistics.

 Type
 [stats](dcv-module.md#stats)

### latchModifierKey(key, location, isDown) → {boolean}
<a name="latchModifierKey"></a>

 Sends a single keyboard `keydown` or `keyup` event for an allowed modifier.

#### Parameters:
<a name="parameters-6"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  key  |  Control \| Alt \| AltGraph \| Meta \| OS \| Shift  |  The key to send.  |
|  location  |  KeyboardEvent.location  |  The key's location. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/location.  |
|  isDown  |  boolean  |  If the key event to inject is a keydown (true) or a keyup (false).  |

#### Returns:
<a name="returns-11"></a>

 If the requested combination is valid, the function returns `true`, otherwise it returns `false`.

 Type
 boolean

### openChannel(name, authToken, callbacks, namespace) → {Promise\|Promise.<{code: [ChannelErrorCode](dcv-module.md#ChannelErrorCode), message: string}>}
<a name="openChannel"></a>

 Opens a custom data channel on the connection if it was created on the Amazon DCV Server.

#### Parameters:
<a name="parameters-7"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  name  |  string  |  The name of the channel.  |
|  authToken  |  string  |  The authentication token to use to connect to the channel.  |
|  callbacks  |  Object  |  The onMessage and onClose callbacks functions to call.  |
|  namespace  |  string  |  The namespace of the channel. Available since Amazon DCV Web Client SDK 1.2.0 and Amazon DCV Server 2022.1.  |

#### Returns:
<a name="returns-12"></a>

 Promise. If rejected we receive an error object.

 Type
 Promise \| Promise.<{code: [ChannelErrorCode](dcv-module.md#ChannelErrorCode), message: string}>

### queryFeature(featureName) → {Promise.<{enabled: boolean, remote?: string, autoCopy?: boolean, autoPaste?: boolean, serviceStatus?: string, available?: boolean}>\|Promise.<{message: string}>}
<a name="queryFeature"></a>

 Queries the status of a specific Amazon DCV server feature.

#### Parameters:
<a name="parameters-8"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  featureName  |  [feature](dcv-module.md#feature)  |  The name of the feature to query.  |

#### Returns:
<a name="returns-13"></a>

 Promise. If resolved, the function returns a `status` object that always containes an `enabled` property, and possibly also other properties. If rejected, the function returns an `error` object.

 Type
 {Promise.<{enabled: boolean, remote?: string, autoCopy?: boolean, autoPaste?: boolean, serviceStatus?: string, available?: boolean}> \| Promise.<{message: string}>

### registerKeyboardShortcuts(shortcuts) → {void}
<a name="registerKeyboardShortcuts"></a>

 Registers keyboard shortcuts.

#### Parameters:
<a name="parameters-9"></a>

<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>shortcuts</code> </td><td> Array.&lt;Object&gt; </td><td> The array of keys and mappings to register.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>sequence</code> </td><td> Array.&lt;Object&gt; </td><td> The keyboard shortcut to register.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>key</code> </td><td> KeyboardEvent.key </td><td> The value of the key pressed by the user. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key. </td></tr>
  <tr><td> <code>location</code> </td><td> KeyboardEvent.location </td><td> The array of keys to send. The location of the key on the keyboard. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/location. </td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td> <code>output</code> </td><td> Array.&lt;Object&gt; </td><td> The intended action to be performed by the shortcut.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>key</code> </td><td> KeyboardEvent.key </td><td> The value of the key pressed by the user. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key. </td></tr>
  <tr><td> <code>location</code> </td><td> KeyboardEvent.location </td><td> The array of keys to send. The location of the key on the keyboard. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/location. </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>

#### Returns:
<a name="returns-14"></a>

 Type
 void

### requestDisplayConfig(highColorAccuracy) → {Promise\|Promise.<{code: [DisplayConfigErrorCode](dcv-module.md#DisplayConfigErrorCode), message: string}>}
<a name="requestDisplayConfig"></a>

 Requests an updated display config from the Amazon DCV Server. Available since Amazon DCV Web Client SDK 1.1.0 and Amazon DCV Server 2022.0.

#### Parameters:
<a name="parameters-10"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  highColorAccuracy  |  boolean  |  Whether or not high color accuracy should be requested.  |

#### Returns:
<a name="returns-15"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise \| Promise.<{code: [DisplayConfigErrorCode](dcv-module.md#DisplayConfigErrorCode), message: string}>

### requestDisplayLayout(layout) → {Promise\|Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>}
<a name="requestDisplayLayout"></a>

 Requests an updated display layout for the connection.

#### Parameters:
<a name="parameters-11"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  layout  |  Array.<[Monitor](dcv-module.md#Monitor)>  |  The requested displays in the layout.  |

#### Returns:
<a name="returns-16"></a>

 Promise. If rejected we receive an error object.

 Type
 Promise \| Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>

### requestResolution(width, height) → {Promise\|Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>}
<a name="requestResolution"></a>

 Requests an updated display resolution from the Amazon DCV server.

#### Parameters:
<a name="parameters-12"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  width  |  number  |  The width to request in pixels. The minimum allowed value is 0.  |
|  height  |  number  |  The height to request in pixels. The minimum allowed value is 0.  |

#### Returns:
<a name="returns-17"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise \| Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>

### sendKeyboardEvent(event) → {boolean}
<a name="sendKeyboardEvent"></a>

 Sends a keyboard shortcut event. For more information about keyboard events, see [ https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent). Valid Keyboard events include: `keydown`, `keypress`, and `keyup`. For more information about these events, see [ https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent\#events](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent#events).

#### Parameters:
<a name="parameters-13"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  event  |  KeyboardEvent  |  The keyboard event to send.  |

#### Returns:
<a name="returns-18"></a>

 If the event is not valid, the function returns `false`. If the event is valid, the function returns `true`.

 Type
 boolean

### sendKeyboardShortcut(shortcut) → {void}
<a name="sendKeyboardShortcut"></a>

 Sends a keyboard shortcut. Use this function to send a full `keydown` or `keyup` sequence. For example, sending Ctrl \+ Alt \+ Del sends the `keydown` events for all the keys followed by the `keyup` events. Use this function even if you want to send a single key.

#### Parameters:
<a name="parameters-14"></a>

<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>shortcut</code> </td><td> Array.&lt;Object&gt; </td><td> The array of keys to send.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>key</code> </td><td> KeyboardEvent.key </td><td> The value of the key pressed by the user. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key. </td></tr>
  <tr><td> <code>location</code> </td><td> KeyboardEvent.location </td><td> The array of keys to send. The location of the key on the keyboard. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/location. </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>

#### Returns:
<a name="returns-19"></a>

 Type
 void

### setDisplayQuality(min, maxopt) → {void}
<a name="setDisplayQuality"></a>

 Sets the image quality to use for the connection. Valid range is `0` to `100`, with `1` being the lowest image quality and `100` being the highest image quality. Specify `0` to retain the current value.

#### Parameters:
<a name="parameters-15"></a>

|  Name  |  Type  |  Attributes  |  Description  |
| --- | --- | --- | --- |
|  min  |  number  |   |  The minimum image quality.  |
|  max  |  number  |  <optional>  |  The maximum image quality.  |

#### Returns:
<a name="returns-20"></a>

 Type
 void

### setDisplayScale(scaleRatio, displayId) → {Promise\|Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>} (DEPRECATED)
<a name="setDisplayScale"></a>

 Deprecated since version 1.3.0. There is no need to set the display scale anymore. Mouse coordinates will be managed automatically internally.

 Notifies the Amazon DCV that the display is scaled on the client side. Use this to notify the server that it needs to scale mouse events to match the client's display ratio.

#### Parameters:
<a name="parameters-16"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  scaleRatio  |  float  |  The scaling ratio to use. Must be a strictly positive number.  |
|  displayId  |  number  |  The ID of the display to scale.  |

#### Returns:
<a name="returns-21"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise \| Promise.<{code: [ResolutionErrorCode](dcv-module.md#ResolutionErrorCode), message: string}>

### setKeyboardQuirks(quirks) → {void}
<a name="setKeyboardQuirks"></a>

 Sets keyboard quirks for the client computer.

#### Parameters:
<a name="parameters-17"></a>

<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>quirks</code> </td><td> Object </td><td> The keyboard quirks to enable or disable.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>macOptionToAlt</code> </td><td> boolean </td><td> To map the Option key to Alt for macOS, specify <code>true</code>. Otherwise, specify <code>false</code>. </td></tr>
  <tr><td> <code>macCommandToControl</code> </td><td> boolean </td><td> To map the Command key to Ctrl for macOS, specify <code>true</code>. Otherwise, specify <code>false</code>. </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>

#### Returns:
<a name="returns-22"></a>

 Type
 void

### setMaxDisplayResolution(maxWidth, maxHeight) → {void}
<a name="setMaxDisplayResolution"></a>

 Sets the maximum display resolution to use for the connection.

#### Parameters:
<a name="parameters-18"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  maxWidth  |  number  |  The maximum display width in pixels. The minimum allowed value is 0.  |
|  maxHeight  |  number  |  The maximum display height in pixels. The minimum allowed value is 0.  |

#### Returns:
<a name="returns-23"></a>

 Type
 void

### setMicrophone(enable) → {Promise\|Promise.<{code: [AudioErrorCode](dcv-module.md#AudioErrorCode), message: string}>}
<a name="setMicrophone"></a>

 Enables or disables the microphone.

#### Parameters:
<a name="parameters-19"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enable  |  boolean  |  To enable the microphone, specify true. To disable the microphone, specify false.  |

#### Returns:
<a name="returns-24"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise \| Promise.<{code: [AudioErrorCode](dcv-module.md#AudioErrorCode), message: string}>

### setMinDisplayResolution(minWidth, minHeight) → {void}
<a name="setMinDisplayResolution"></a>

 Sets the minimum display resolution to use for the connection. Some applications might require a minimum display resolution. If the minimum required resolution is larger than the maximum resolution supported by the client, a resize strategy is used. Use this function carefully. The resize strategy could cause a less precise mouse and touch input system.

#### Parameters:
<a name="parameters-20"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  minWidth  |  number  |  The minimum display width in pixels. The minimum allowed value is 0.  |
|  minHeight  |  number  |  The minimum display height in pixels. The minimum allowed value is 0.  |

#### Returns:
<a name="returns-25"></a>

 Type
 void

### setUploadBandwidth(value) → {number}
<a name="setUploadBandwidth"></a>

 Sets the maxmimum bandwidth to use for uploading files to the Amazon DCV server.

#### Parameters:
<a name="parameters-21"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  value  |  number  |  The maximum bandwidth limit in kbps. Valid range is 1024 kbps to 102400 kbps.  |

#### Returns:
<a name="returns-26"></a>

 - The set bandwidth limit. `null` if the file storage feature is disabled on the server.

 Type
 number

### setVolume(volume) → {void}
<a name="setVolume"></a>

 Sets the volume level to use for audio. Valid range is 0 to 100, with 0 being the lowest volume and 100 being the highest volume.

#### Parameters:
<a name="parameters-22"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  volume  |  number  |  The volume level to use.  |

#### Returns:
<a name="returns-27"></a>

 Type
 void

### setMicrophone(enable, deviceId) → {Promise\|Promise.<{code: [AudioErrorCode](dcv-module.md#AudioErrorCode), message: string}>}
<a name="setMicrophone"></a>

 [Experimental - might change in the future] Enables or disables the microphone.

#### Parameters:
<a name="parameters-23"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enable  |  boolean  |  To enable the microphone, specify true. To disable the microphone, specify false.  |
|  deviceId  |  string  |  The device ID of the microphone. If no deviceId is provided, the default deviceId is used.  |

#### Returns:
<a name="returns-28"></a>

 Promise. If rejected, the promise returns an error object.

 Type
 Promise \| Promise.<{code: [AudioErrorCode](dcv-module.md#AudioErrorCode), message: string}>

### setWebcam(enable, deviceId) → {Promise\|Promise.<{code: [WebcamErrorCode](dcv-module.md#WebcamErrorCode), message: string}>}
<a name="setWebcam"></a>

 Enables or disables the webcam.

#### Parameters:
<a name="parameters-23"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enable  |  boolean  |  To enable the webcam, specify true. To disable the webcam, specify false.  |
|  deviceId  |  string  |  The device ID of the webcam.  |

#### Returns:
<a name="returns-28"></a>

 Promise that, if successful, resolves to the attached/detached webcam deviceId. If rejected, the promise returns an error object.

 Type
 Promise.<string> \| Promise.<{code: [WebcamErrorCode](dcv-module.md#WebcamErrorCode), message: string}>

### syncClipboards() → {boolean}
<a name="syncClipboards"></a>

 Synchronizes the local client clipboard with the remote Amazon DCV server clipboard. Autocopy must be supported by the browser.

#### Returns:
<a name="returns-29"></a>

 If the clipboards have been synchronized, the function returns `true`. If the clipboards have not been sycnhronized, or if the browser does not support autocopy, the function returns `false`.

 Type
 boolean
