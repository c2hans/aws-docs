---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html
---

# DCV module
<a name="dcv-module"></a>

A module that implements the client side of the DCV protocol.

**Topics**
+ [Methods](#methods)
+ [Members](#members)
+ [Type and callback definitions](#type-definitions)

## Methods
<a name="methods"></a>

**Topics**
+ [authenticate(authParams) → {[Authentication](authentication-class.md)}](#authenticate)
+ [connect(config) → {Promise.<[Connection](connection-class.md)>\|Promise.<{code: [ConnectionErrorCode](#ConnectionErrorCode), message: string}>}](#connect)
+ [setLogHandler(handler) → {void}](#setLogHandler)
+ [setLogLevel(level) → {void}](#setLogLevel)

### authenticate(authParams) → {[Authentication](authentication-class.md)}
<a name="authenticate"></a>

 Starts the authentication process for the specified Amazon DCV server endpoint.

#### Parameters:
<a name="parameters"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  url  |  string  |  The host name and port of the running Amazon DCV server in the following format: https://dcv\_host\_address:port. For example: https://my-dcv-server:8443.  |
|  authenticationToken  |  string  |  The authentication token to use for authentication.  |
|  callbacks  |  [authenticationCallbacks](#authenticationCallbacks)  |  The callbacks that are available to be called during the authentication process.  |

#### Returns:
<a name="returns"></a>

 - The Authentication object.

 Type
 [Authentication](authentication-class.md)

### connect(config) → {Promise.<[Connection](connection-class.md)>\|Promise.<{code: [ConnectionErrorCode](#ConnectionErrorCode), message: string}>}
<a name="connect"></a>

 Connects to the specified Amazon DCV server endpoint. If connection succeeds, it returns a Connection object. If connection fails, it returns an error object.

#### Parameters:
<a name="parameters-1"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  config  |  [ConnectionConfig](#ConnectionConfig)  |  The ConnectionConfig object.  |

#### Returns:
<a name="returns-1"></a>

 - A Connection object, or an error object.

 Type
 Promise.<[Connection](connection-class.md)> \| Promise.<{code: [ConnectionErrorCode](#ConnectionErrorCode), message: string}>

### setLogHandler(handler) → {void}
<a name="setLogHandler"></a>

 Sets a custom log handler function. When overriding the default log handler, the original log entry position will be lost when debugging with the browser console.

#### Parameters:
<a name="parameters-2"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  handler  |  function  |  The custom log handler function. The handler function contains level (number), levelName (string), domain (string), and message (string).  |

#### Returns:
<a name="returns-2"></a>

 Type
 void

### setLogLevel(level) → {void}
<a name="setLogLevel"></a>

 Sets the log level. This is required only if the default log handler is used.

#### Parameters:
<a name="parameters-3"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  level  |  [LogLevel](#LogLevel)  |  The log level to use.  |

#### Returns:
<a name="returns-3"></a>

 Type
 void

## Members
<a name="members"></a>

**Topics**
+ [(constant) AudioError :[AudioErrorCode](#AudioErrorCode)](#AudioError)
+ [(constant) AuthenticationError :[AuthenticationErrorCode](#AuthenticationErrorCode)](#AuthenticationError)
+ [(constant) ChannelError :[ChannelErrorCode](#ChannelErrorCode)](#ChannelError)
+ [(constant) ClosingReasonError :[ClosingReasonErrorCode](#ClosingReasonErrorCode)](#ClosingReasonError)
+ [(constant) ConnectionError :[ConnectionErrorCode](#ConnectionErrorCode)](#ConnectionError)
+ [(constant) CustomChannelError :[CustomChannelErrorCode](#CustomChannelErrorCode)](#CustomChannelError)
+ [(constant) DisplayConfigError :[DisplayConfigErrorCode](#DisplayConfigErrorCode)](#DisplayConfigError)
+ [(constant) FileStorageError :[FileStorageErrorCode](#FileStorageErrorCode)](#FileStorageError)
+ [(constant) LogLevel :[LogLevel](#LogLevel)](#LogLevel_)
+ [(constant) MultiMonitorError :[MultiMonitorErrorCode](#MultiMonitorErrorCode)](#MultiMonitorError)
+ [(constant) ResolutionError :[ResolutionErrorCode](#ResolutionErrorCode)](#ResolutionError)
+ [(constant) TimezoneRedirectionError :[TimezoneRedirectionErrorCode](#TimezoneRedirectionErrorCode)](#TimezoneRedirectionError)
+ [(constant) TimezoneRedirectionSetting :[TimezoneRedirectionSettingCode](#TimezoneRedirectionSettingCode)](#TimezoneRedirectionSetting)
+ [(constant) TimezoneRedirectionStatus :[TimezoneRedirectionStatusCode](#TimezoneRedirectionStatusCode)](#TimezoneRedirectionStatus)
+ [(constant) version](#version)
+ [(constant) ScreenshotError :[ScreenshotErrorCode](#ScreenshotErrorCode)](#ScreenshotError)
+ [(constant) WebcamError :[WebcamErrorCode](#WebcamErrorCode)](#WebcamError)

### (constant) AudioError :[AudioErrorCode](#AudioErrorCode)
<a name="AudioError"></a>

 The AudioError codes enum.

#### Type:
<a name="type"></a>
+  [AudioErrorCode](#AudioErrorCode)

### (constant) AuthenticationError :[AuthenticationErrorCode](#AuthenticationErrorCode)
<a name="AuthenticationError"></a>

 The AuthenticationError codes enum.

#### Type:
<a name="type-1"></a>
+  [AuthenticationErrorCode](#AuthenticationErrorCode)

### (constant) ChannelError :[ChannelErrorCode](#ChannelErrorCode)
<a name="ChannelError"></a>

 The ChannelError codes enum.

#### Type:
<a name="type-2"></a>
+  [ChannelErrorCode](#ChannelErrorCode)

### (constant) ClosingReasonError :[ClosingReasonErrorCode](#ClosingReasonErrorCode)
<a name="ClosingReasonError"></a>

 The ClosingReasonError codes enum.

#### Type:
<a name="type-3"></a>
+  [ClosingReasonErrorCode](#ClosingReasonErrorCode)

### (constant) ConnectionError :[ConnectionErrorCode](#ConnectionErrorCode)
<a name="ConnectionError"></a>

 The ConnectionError codes enum.

#### Type:
<a name="type-4"></a>
+  [ConnectionErrorCode](#ConnectionErrorCode)

### (constant) CustomChannelError :[CustomChannelErrorCode](#CustomChannelErrorCode)
<a name="CustomChannelError"></a>

 The CustomChannelError codes enum.

#### Type:
<a name="type-5"></a>
+  [CustomChannelErrorCode](#CustomChannelErrorCode)

### (constant) DisplayConfigError :[DisplayConfigErrorCode](#DisplayConfigErrorCode)
<a name="DisplayConfigError"></a>

 The DisplayConfigError codes enum.

#### Type:
<a name="type-8"></a>
+  [DisplayConfigErrorCode](#DisplayConfigErrorCode)

### (constant) FileStorageError :[FileStorageErrorCode](#FileStorageErrorCode)
<a name="FileStorageError"></a>

 The FileStorageError codes enum.

#### Type:
<a name="type-6"></a>
+  [FileStorageErrorCode](#FileStorageErrorCode)

### (constant) LogLevel :[LogLevel](#LogLevel)
<a name="LogLevel_"></a>

 The available SDK log levels.

#### Type:
<a name="type-31"></a>
+  [LogLevel](#LogLevel)

### (constant) MultiMonitorError :[MultiMonitorErrorCode](#MultiMonitorErrorCode)
<a name="MultiMonitorError"></a>

 The MultiMonitorError codes enum.

#### Type:
<a name="type-7"></a>
+  [MultiMonitorErrorCode](#MultiMonitorErrorCode)

### (constant) ResolutionError :[ResolutionErrorCode](#ResolutionErrorCode)
<a name="ResolutionError"></a>

 The ResolutionError codes enum.

#### Type:
<a name="w2aac14b9c13c25b5"></a>
+  [ResolutionErrorCode](#ResolutionErrorCode)

### (constant) TimezoneRedirectionError :[TimezoneRedirectionErrorCode](#TimezoneRedirectionErrorCode)
<a name="TimezoneRedirectionError"></a>

 The TimezoneRedirectionError codes enum.

#### Type:
<a name="w2aac14b9c13c27b5"></a>
+  [TimezoneRedirectionErrorCode](#TimezoneRedirectionErrorCode)

### (constant) TimezoneRedirectionSetting :[TimezoneRedirectionSettingCode](#TimezoneRedirectionSettingCode)
<a name="TimezoneRedirectionSetting"></a>

 The TimezoneRedirectionSetting codes enum.

#### Type:
<a name="w2aac14b9c13c29b5"></a>
+  [TimezoneRedirectionSettingCode](#TimezoneRedirectionSettingCode)

### (constant) TimezoneRedirectionStatus :[TimezoneRedirectionStatusCode](#TimezoneRedirectionStatusCode)
<a name="TimezoneRedirectionStatus"></a>

 The TimezoneRedirectionStatus codes enum.

#### Type:
<a name="w2aac14b9c13c31b5"></a>
+  [TimezoneRedirectionStatusCode](#TimezoneRedirectionStatusCode)

### (constant) version
<a name="version"></a>

 The Amazon DCV version with major, minor, patch, revision, extended, and versionStr.

#### Properties:
<a name="properties"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  major  |  integer  |  The major version number.  |
|  minor  |  integer  |  The minor version number.  |
|  patch  |  integer  |  The patch version number.  |
|  revision  |  integer  |  The revision number.  |
|  extended  |  string  |  The extended string.  |
|  versionStr  |  string  |  A concatenation of the major, minor, patch, and revision numbers in the form major.minor.patch\+build.revision.  |

### (constant) ScreenshotError :[ScreenshotErrorCode](#ScreenshotErrorCode)
<a name="ScreenshotError"></a>

 The ScreenshotError codes enum.

#### Type:
<a name="type-34"></a>
+  [ScreenshotErrorCode](#ScreenshotErrorCode)

### (constant) WebcamError :[WebcamErrorCode](#WebcamErrorCode)
<a name="WebcamError"></a>

 The WebcamError codes enum.

#### Type:
<a name="type-9"></a>
+  [WebcamErrorCode](#WebcamErrorCode)

## Type and callback definitions
<a name="type-definitions"></a>

**Topics**
+ [AudioErrorCode](#AudioErrorCode)
+ [authenticationCallbacks](#authenticationCallbacks)
+ [AuthenticationErrorCode](#AuthenticationErrorCode)
+ [authErrorCallback(authentication, error)](#authErrorCallback)
+ [authPromptCredentialsCallback(authentication, challenge)](#authPromptCredentialsCallback)
+ [authSuccessCallback(authentication, authenticationData)](#authSuccessCallback)
+ [Channel](#Channel)
+ [ChannelErrorCode](#ChannelErrorCode)
+ [clipboardEventCallback(event)](#clipboardEventCallback)
+ [ClosingReasonErrorCode](#ClosingReasonErrorCode)
+ [Colorspace](#Colorspace)
+ [connectionCallbacks](#connectionCallbacks)
+ [ConnectionConfig](#ConnectionConfig)
+ [ConnectionErrorCode](#ConnectionErrorCode)
+ [createDirectory(path)](#createDirectory)
+ [CustomChannelErrorCode](#CustomChannelErrorCode)
+ [dataChannelCallback(info)](#dataChannelCallback)
+ [deleteFile(path)](#deleteFile)
+ [deviceChangeEventCallback()](#deviceChangeEventCallback)
+ [disconnectCallback(reason)](#disconnectCallback)
+ [displayAvailabilityCallback(status, displayId)](#displayAvailabilityCallback)
+ [DisplayConfigErrorCode](#DisplayConfigErrorCode)
+ [displayLayoutCallback(serverWidth, serverHeight, heads)](#displayLayoutCallback)
+ [feature](#feature)
+ [featuresUpdateCallback(featuresList)](#featuresUpdateCallback)
+ [fileDownloadCallback(fileResource)](#fileDownloadCallback)
+ [filePrintedCallback(printResource)](#filePrintedCallback)
+ [filestorage](#filestorage)
+ [filestorageEnabledCallback(enabled)](#filestorageEnabledCallback)
+ [FileStorageErrorCode](#FileStorageErrorCode)
+ [firstFrameCallback(resizeEnabled, relativeMouseModeEnabled, displayId)](#firstFrameCallback)
+ [idleWarningNotificationCallback(disconnectionDateTime)](#idleWarningNotificationCallback)
+ [collaboratorListCallback(collaborators)](#collaboratorListCallback)
+ [licenseNotificationCallback(notification)](#licenseNotificationCallback)
+ [list(path)](#list)
+ [LogLevel](#LogLevel)
+ [MaxDimensionLimits](#MaxDimensionLimits)
+ [Monitor](#Monitor)
+ [MultiMonitorErrorCode](#MultiMonitorErrorCode)
+ [qualityIndicatorStateCallback(state)](#qualityIndicatorStateCallback)
+ [renameDirectory(src, dest)](#renameDirectory)
+ [renameFile(src, dest)](#renameFile)
+ [ResolutionErrorCode](#ResolutionErrorCode)
+ [retrieveFile(path)](#retrieveFile)
+ [screenshotCallback(screenshot)](#screenshotCallback)
+ [ScreenshotErrorCode](#ScreenshotErrorCode)
+ [serverInfo](#serverInfo)
+ [stats](#stats)
+ [storeFile(file, dir)](#storeFile)
+ [TimezoneRedirectionErrorCode](#TimezoneRedirectionErrorCode)
+ [TimezoneRedirectionSettingCode](#TimezoneRedirectionSettingCode)
+ [TimezoneRedirectionStatusCode](#TimezoneRedirectionStatusCode)
+ [WebcamErrorCode](#WebcamErrorCode)
+ [httpExtraSearchParamsCallback(method, url, body)](#httpExtraSearchParamsCallback)
+ [httpExtraHeadersCallback(method, url, body)](#httpExtraHeadersCallback)

### AudioErrorCode
<a name="AudioErrorCode"></a>

 The AudioError code enums available in the DCV module
+  `SETTING_AUDIO_FAILED`
+  `CHANNEL_NOT_AVAILABLE`

#### Type:
<a name="type-10"></a>
+  number

### authenticationCallbacks
<a name="authenticationCallbacks"></a>

 Authentication callbacks

#### Type:
<a name="type-11"></a>
+  Object

#### Properties:
<a name="properties-1"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  promptCredentials  |  [authPromptCredentialsCallback](#authPromptCredentialsCallback)  |  The callback function to be called when the user is challenged for credentials.  |
|  error  |  [authErrorCallback](#authErrorCallback)  |  The callback function to be called when authentication fails.  |
|  success  |  [authSuccessCallback](#authSuccessCallback)  |  The callback function to be called when authentication succeeds.  |
|  httpExtraSearchParamsCallback  |  [httpExtraSearchParamsCallback](#httpExtraSearchParamsCallback)  |  The callback function to be called in the authenticate method to inject custom query parameters into the authentication URL before initiating the request. It can also be used in the connect method to customize the URL that's used when establishing a WebSocket connection to the DCV server.  |

### AuthenticationErrorCode
<a name="AuthenticationErrorCode"></a>

 The AuthenticationError code enums available in the DCV module
+  `INVALID_MESSAGE`
+  `UNKNOWN_AUTH_MODE`
+  `SESSION_NOT_AVAILABLE`
+  `NO_SESSIONS`
+  `WRONG_CREDENTIALS`
+  `SASL_CHALLENGE`
+  `SASL_AUTH_MECHANISM`
+  `FAILED_COMMUNICATION`
+  `AUTHENTICATION_REJECTED`
+  `GENERIC_ERROR`
+  `WRONG_CREDENTIALS_FORMAT`
+  `WRONG_CREDENTIALS_TYPE`
+  `UNREQUESTED_CREDENTIALS`
+  `MISSING_CREDENTIAL`

#### Type:
<a name="type-12"></a>
+  number

### authErrorCallback(authentication, error)
<a name="authErrorCallback"></a>

 The callback function to be called when authentication fails.

#### Parameters:
<a name="parameters-4"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  authentication  |  [Authentication](authentication-class.md)  |  The Authentication object.  |
|  error  |  Object  |  The error object raised by the authentication process. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  code  |  [AuthenticationErrorCode](#AuthenticationErrorCode)  |  The error code.  |
|  message  |  string  |  The error message.  |

### authPromptCredentialsCallback(authentication, challenge)
<a name="authPromptCredentialsCallback"></a>

 The callback function to be called when the user is challenged for credentials. The user must answer the challenge by providing the requested credentials.

#### Parameters:
<a name="parameters-5"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  authentication  |  [Authentication](authentication-class.md)  |  The Authentication object.  |
|  challenge  |  Object  |  The challenge. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  requiredCredentials  |  Array.<Object>  |  An array of requested credential objects. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  name  |  string  |  The name of the requested credential.  |
|  type  |  string  |  The type of the requested credential.  |

### authSuccessCallback(authentication, authenticationData)
<a name="authSuccessCallback"></a>

 The callback function to be called when authentication succeeds.

#### Parameters:
<a name="parameters-6"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  authentication  |  [Authentication](authentication-class.md)  |  The Authentication object.  |
|  authenticationData  |  Array.<Object>  |  An array of objects that include Amazon DCV session IDs and authentication tokens. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  sessionId  |  string  |  The Amazon DCV session ID.  |
|  authToken  |  string  |  The authentication token for the Amazon DCV session.  |

### Channel
<a name="Channel"></a>

 The available channels that can be specified.

#### Type:
<a name="type-13"></a>
+  "clipboard" \| "display" \| "input" \| "audio" \| "filestorage"

### ChannelErrorCode
<a name="ChannelErrorCode"></a>

 The ChannelError code enums available in the DCV module
+  `ALREADY_OPEN`
+  `INITIALIZATION_FAILED`
+  `REJECTED`

#### Type:
<a name="type-14"></a>
+  number

### clipboardEventCallback(event)
<a name="clipboardEventCallback"></a>

 The callback function to be called when a `clipboardEvent` is generated.

#### Parameters:
<a name="parameters-7"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Attributes  |  Description  |
| --- | --- | --- | --- |
|  event  |  Object  |  Information about the clipboard event. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  name  |  established \| copy \| paste \| dataSizeAlert \| autoCopyDone \| newDataAvailable \| autoPasteDone \| remoteError \| pasteAvailableData  |   |  Always present. The name of the event.  |
|  clipboardData  |  Object \| string  |   |  The data in the clipboard.  |
|  autoCopy  |  boolean  |  <optional>  |  Indicates whether automatic copying from the session clipboard to the local client clipboard is enabled.  |
|  maxDataSize  |  number  |  <optional>  |  The maximum amount of data that can be placed in the clipboard.  |
|  error  |  string  |  <optional>  |  Error information if applicable.  |

### ClosingReasonErrorCode
<a name="ClosingReasonErrorCode"></a>

 The ClosingReasonError code enums available in the DCV module
+  `TRANSPORT_ERROR`
+  `NO_ERROR`
+  `GENERIC_ERROR`
+  `INTERNAL_SERVER_ERROR`
+  `PROTOCOL_ERROR`
+  `AUTHORIZATION_DENIED`
+  `AUTHORIZATION_REVOKED`
+  `ACCESS_REJECTED`
+  `IDLE_TIMEOUT_EXPIRED`
+  `DISCONNECT_BY_OWNER`
+  `DISCONNECT_BY_USER`
+  `EVICTED`
+  `EXTERNAL_PROTOCOL_CONNECTION_EVICTED`
+  `DISCONNECTION_REQUESTED`

#### Type:
<a name="type-15"></a>
+  number

### Colorspace
<a name="Colorspace"></a>

 The available colorspaces that can be specified.

#### Type:
<a name="type-16"></a>
+  "RGB" \| "YUV\_REC601" \| "YUV\_REC709"

### connectionCallbacks
<a name="connectionCallbacks"></a>

 The callbacks that are available to be called in the event of a connection error.

#### Type:
<a name="type-17"></a>
+  Object

#### Properties:
<a name="properties-7"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  disconnect  |  [disconnectCallback](#disconnectCallback)  |  The callback function to be called when the connection ends.  |
|  displayLayout  |  [displayLayoutCallback](#displayLayoutCallback)  |  The callback function to be called when the display layout or resolution is changed.  |
|  displayAvailability  |  [displayAvailabilityCallback](#displayAvailabilityCallback)  |  The callback function to be called when a display's availability changes.  |
|  firstFrame  |  [firstFrameCallback](#firstFrameCallback)  |  The callback function to be called when the first frame is received from the Amazon DCV server.  |
|  filePrinted  |  [filePrintedCallback](#filePrintedCallback)  |  The callback function to be called when a file is printed on the Amazon DCV server.  |
|  fileDownload  |  [fileDownloadCallback](#fileDownloadCallback)  |  The callback function to be called when a file is ready to be downloaded from the Amazon DCV server.  |
|  dataChannel  |  [dataChannelCallback](#dataChannelCallback)  |  The callback function to be called when the Amazon DCV server sends a notification about the availability of a data channel.  |
|  licenseNotification  |  [licenseNotificationCallback](#licenseNotificationCallback)  |  The callback function to be called when the Amazon DCV server sends a notification about the license state.  |
|  idleWarningNotification  |  [idleWarningNotificationCallback](#idleWarningNotificationCallback)  |  The callback function to be called when the Amazon DCV server sends an idle timeout warning.  |
|  collaboratorList  |  [collaboratorListCallback](#collaboratorListCallback)  |  The callback function to be called when the Amazon DCV server sends the list of collaborators (since Amazon DCV Web Client SDK version 1.1.0).  |
|  qualityIndicatorState  |  [qualityIndicatorStateCallback](#qualityIndicatorStateCallback)  |  The callback function to be called when the connection quality indicator changes state.  |
|  filestorageEnabled  |  [filestorageEnabledCallback](#filestorageEnabledCallback)  |  The callback function to be called when file storage is enabled or disabled.  |
|  featuresUpdate  |  [featuresUpdateCallback](#featuresUpdateCallback)  |  The callback function to be called when a feature's status changes.  |
|  clipboardEvent  |  [clipboardEventCallback](#clipboardEventCallback)  |  The callback function to be called when a clipboardEvent is generated.  |
|  deviceChangeEvent  |  [deviceChangeEventCallback](#deviceChangeEventCallback)  |  The callback function to be called when an deviceChange event is triggered.  |
|  screenshot  |  [screenshotCallback](#screenshotCallback)  |  The callback function to be called when a screenshot is available.  |
|  httpExtraSearchParamsCallback  |  [httpExtraSearchParamsCallback](#httpExtraSearchParamsCallback)  |  The callback function to be called to customize the URL when establishing a WebSocket connection to the Amazon DCV server. Note that this callback can also be used with the authenticate method to dynamically append query parameters to the authentication URL before the SDK sends the request.  |
|  httpExtraHeadersCallback  |  [httpExtraHeadersCallback](#httpExtraHeadersCallback)  |  The callback function to be called to add custom headers to the HTTP request during connection establishment.  |

### ConnectionConfig
<a name="ConnectionConfig"></a>

 The configuration for a Amazon DCV connection.

#### Type:
<a name="type-18"></a>
+  Object

#### Properties:
<a name="properties-8"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  url  |  string  |  The host name and port of the running Amazon DCV server in the following format: https://dcv\_host\_address:port. For example: https://my-dcv-server:8443.  |
|  sessionId  |  string  |  The Amazon DCV session ID.  |
|  authToken  |  string  |  The authentication token to use when connecting to the server.  |
|  baseUrl  |  string  |  The absolute or relative URL from which to load SDK files.  |
|  resourceBaseUrl  |  string  |  The absolute or relative URL from which to access DCV resources.  |
|  enabledChannels  |  Array.<[Channel](#Channel)>  |  Indicates the list of channels that can be enabled. If not specified or an empty array is provided, it defaults to all the available channels.  |
|  losslessColorspace  |  [Colorspace](#Colorspace)  |  Indicates the colorspace that will be used. If not specified, it defaults to "RGB".  |
|  divId  |  string  |  The ID of the div object in the HTML DOM where SDK should create the canvas with the remote stream.  |
|  volumeLevel  |  integer  |  The preferred volume level. The valid range is 0 to 100.  |
|  clipboardAutoSync  |  boolean  |  Indicates whether automatic copying from the Amazon DCV session clipboard to the local client clipboard is enabled for compatible web browsers.  |
|  dynamicAudioTuning  |  boolean  |  Indicates whether to dynamically tune the audio based on the Amazon DCV server audio settings when a connection is established.  |
|  clientHiDpiScaling  |  boolean  |  Indicates whether to scale the canvas based on the client's DPI.  |
|  highColorAccuracy  |  boolean  |  Indicates whether high color accuracy should be used if available. If not specified, it defaults to false.  |
|  enableWebCodecs  |  Boolean  |  Indicates whether WebCodecs should be used if available. Defaults to false if not specified.  |
|  observers  |  [connectionCallbacks](#connectionCallbacks)  |  The callback functions to call for events that are related to the connection.  |
|  callbacks  |  [connectionCallbacks](#connectionCallbacks)  |  The same as the observers property, but each callback includes the [Connection](connection-class.md) object as the first parameter.  |

### ConnectionErrorCode
<a name="ConnectionErrorCode"></a>

 The ConnectionError code enums available in the DCV module
+  `ALREADY_OPEN`
+  `INVALID_CONFIG`
+  `INITIALIZATION_FAILED`
+  `REJECTED`
+  `MAIN_CHANNEL_ALREADY_OPEN`
+  `GENERIC_ERROR` (since DCV Server 2021.0)
+  `INTERNAL_SERVER_ERROR` (since DCV Server 2021.0)
+  `AUTHENTICATION_FAILED` (since DCV Server 2021.0)
+  `PROTOCOL_ERROR` (since DCV Server 2021.0)
+  `INVALID_SESSION_ID` (since DCV Server 2021.0)
+  `INVALID_CONNECTION_ID` (since DCV Server 2021.0)
+  `CONNECTION_LIMIT_REACHED` (since DCV Server 2021.0)
+  `SERVER_UNREACHABLE` (since DCV Server 2022.1)
+  `GATEWAY_BUSY`
+  `UNSUPPORTED_CREDENTIAL` (since DCV Server 2022.2)
+  `TRANSPORT_ERROR`

#### Type:
<a name="type-19"></a>
+  number

### createDirectory(path)
<a name="createDirectory"></a>

#### Parameters:
<a name="parameters-8"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  path  |  string  |  The absolute path on the server where we want to create a directory. It should also include the name of the target directory.  |

### CustomChannelErrorCode
<a name="CustomChannelErrorCode"></a>

 The CustomChannelError code enums available in the DCV module
+  `TRANSPORT_ERROR`

#### Type:
<a name="type-20"></a>
+  number

### dataChannelCallback(info)
<a name="dataChannelCallback"></a>

 The callback function to be called when the Amazon DCV server sends a notification about the availability of a data channel.

#### Parameters:
<a name="parameters-9"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  info  |  Object  |  Information about the data channel. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  name  |  string  |  The name of the data channel.  |
|  token  |  string  |  The authentication token for the data channel.  |

### deleteFile(path)
<a name="deleteFile"></a>

#### Parameters:
<a name="parameters-10"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  path  |  string  |  The absolute path on the server identifying the file we want to delete.  |

### deviceChangeEventCallback()
<a name="deviceChangeEventCallback"></a>

 The callback function to be called when an `deviceChange` event is triggered.

### disconnectCallback(reason)
<a name="disconnectCallback"></a>

 The callback function to be called when the connection ends.

#### Parameters:
<a name="parameters-11"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  reason  |  Object  |  The reason for the disconnection. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  code  |  number  |  The reason code.  |
|  message  |  string  |  The reason message.  |

### displayAvailabilityCallback(status, displayId)
<a name="displayAvailabilityCallback"></a>

 The callback function to be called when a display's availability changes.

#### Parameters:
<a name="parameters-12"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  status  |  Object  |  The status of the display. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  displayId  |  number  |  The identifier for the display.  |
|  enabled  |  boolean  |  Indicates if the display is enabled.  |
|  closed  |  boolean  |  Indicates if the display is closed.  |

### DisplayConfigErrorCode
<a name="DisplayConfigErrorCode"></a>

 The DisplayConfigError code enums available in the DCV module
+  `INVALID_ARGUMENT`
+  `UNSUPPORTED_OPERATION`
+  `NO_CHANNEL`

#### Type:
<a name="type-32"></a>
+  number

### displayLayoutCallback(serverWidth, serverHeight, heads)
<a name="displayLayoutCallback"></a>

 The callback function to be called when the display layout or resolution is changed.

#### Parameters:
<a name="parameters-13"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  serverWidth  |  number  |  The width (in pixels) of the primary display.  |
|  serverHeight  |  number  |  The height (in pixels) of the primary display.  |
|  heads  |  Array.<[Monitor](#Monitor)>  |  The display heads supported by the Amazon DCV server.  |

### feature
<a name="feature"></a>

 The feature values.
+  `display` - Indicates the availability of a single-display video stream.
+  `display-multi` - Indicates the availability of a multi-display video stream.
+  `high-color-accuracy` - Indicates the availability of high color accuracy (since Amazon DCV Web Client SDK version 1.1.0).
+  `mouse` - Indicates the availability of mouse functionality.
+  `keyboard` - Indicates the availability of keyboard functionality.
+  `keyboard-sas` - Indicates the availability of SAS sequence (Control \+ Alt \+ Delete) functionality.
+  `relative-mouse` - Indicates the availability of relative mouse mode.
+  `clipboard-copy` - Indicates the availability of clipboard copy functionality from Amazon DCV server to the client.
+  `clipboard-paste` - Indicates the availability of clipboard paste functionality from the client to the Amazon DCV server.
+  `audio-in` - Indicates the availability of audio input functionality using the microphone.
+  `audio-out` - Indicates the availability of audio playback functionality.
+  `webcam` - Indicates the availability of webcam streaming functionality.
+  `file-download` - Indicates availability of file download functionality from the Amazon DCV server to the client.
+  `file-upload` - Indicates availability of file upload functionality from the client to the Amazon DCV server.
+  `timezone-redirection` - Indicates the availability of timezone redirection functionality (since Amazon DCV Web Client SDK version 1.3.0).

#### Type:
<a name="type-21"></a>
+  string

### featuresUpdateCallback(featuresList)
<a name="featuresUpdateCallback"></a>

 The callback function to be called when a feature's status changes.

#### Parameters:
<a name="parameters-14"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  featuresList  |  Array.<[feature](#feature)>  |  An array of features that have changed.  |

### fileDownloadCallback(fileResource)
<a name="fileDownloadCallback"></a>

 The callback function to be called when a file is ready to be downloaded from the Amazon DCV server.

#### Parameters:
<a name="parameters-15"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  fileResource  |  Object  |  Information about the file that is ready for download. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  id  |  string  |  The identifier for the file.  |
|  url  |  string  |  The URL to use to download the file.  |
|  domain  |  string  |  The resource domain.  |
|  token  |  string  |  The authentication token to use to download the file. The token is also included in the URL.  |

### filePrintedCallback(printResource)
<a name="filePrintedCallback"></a>

 The callback function to be called when a file is printed on the Amazon DCV server.

#### Parameters:
<a name="parameters-16"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  printResource  |  Object  |  Information about the printed file. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  id  |  string  |  The identifier for the printed file.  |
|  url  |  string  |  The URL to use to download the printed file.  |
|  domain  |  string  |  The resource domain. In this case, printer.  |
|  token  |  string  |  The authentication token to use to download the printed file. The token is also included in the URL.  |

### filestorage
<a name="filestorage"></a>

 Object that allows for exploring and performing actions on the file system.

#### Type:
<a name="type-22"></a>
+  Object

#### Properties:
<a name="properties-14"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  list  |  [list](#list)  |  Function that allows to list the items (files and directories) present at the supplied path on the server.  |
|  createDirectory  |  [createDirectory](#createDirectory)  |  Function that allows to create a directory at the specified path on the server.  |
|  retrieveFile  |  [retrieveFile](#retrieveFile)  |  Function that allows to locally download a file at the specified path on the server.  |
|  deleteFile  |  [deleteFile](#deleteFile)  |  Function that allows to delete a file at the specified path on the server.  |
|  renameFile  |  [renameFile](#renameFile)  |  Function that allows to rename a file from the specified source path to the specified destination path.  |
|  renameDirectory  |  [renameDirectory](#renameDirectory)  |  Function that allows to rename a directory from the specified source path to the absolute destination path.  |
|  storeFile  |  [storeFile](#storeFile)  |  Function that allows to upload a local file to the supplied path on the server.  |

### filestorageEnabledCallback(enabled)
<a name="filestorageEnabledCallback"></a>

 The callback function to be called when file storage is enabled. Lazy channel on Internet Explorer 11 only.

#### Parameters:
<a name="parameters-17"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  enabled  |  boolean  |  Indicates whether file storage is enabled.  |

### FileStorageErrorCode
<a name="FileStorageErrorCode"></a>

 The FileStorageError code enums available in the DCV module
+  `CANCELLED`
+  `ABORTED`
+  `INVALID_ARGUMENT`
+  `NOT_IMPLEMENTED`
+  `ERROR`
+  `ALREADY_EXIST`
+  `NOT_FOUND`

#### Type:
<a name="type-23"></a>
+  number

### firstFrameCallback(resizeEnabled, relativeMouseModeEnabled, displayId)
<a name="firstFrameCallback"></a>

 The callback function to be called when the first frame is received from the Amazon DCV server. Emitted for each display.

#### Parameters:
<a name="parameters-18"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  resizeEnabled  |  boolean  |  Indicates whether the server supports resizing the client display layout.  |
|  relativeMouseModeEnabled  |  boolean  |  Indicates whether the server supports relative mouse mode.  |
|  displayId  |  number  |  The identifier for the display.  |

### idleWarningNotificationCallback(disconnectionDateTime)
<a name="idleWarningNotificationCallback"></a>

 The callback function to be called when the Amazon DCV server sends an idle timeout warning.

#### Parameters:
<a name="parameters-19"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  disconnectionDateTime  |  Date  |  The date and time of the disconnection.  |

### collaboratorListCallback(collaborators)
<a name="collaboratorListCallback"></a>

 The callback function to be called when the Amazon DCV server sends the list of collaborators.

#### Parameters:
<a name="parameters-20"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  collaborators  |  Array.<Object>  |  A list of objects containing information on collaborators. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  username  |  string  |  The username of the collaborator.  |
|  owner  |  boolean  |  Indicates whether the collaborator is the session owner.  |
|  connectionId  |  number  |  Indicates the ID assigned by the server to the connection.  |

### licenseNotificationCallback(notification)
<a name="licenseNotificationCallback"></a>

 The callback function to be called when the Amazon DCV server sends a notification about the license state.

#### Parameters:
<a name="parameters-21"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  notification  |  Object  |  The notification. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  product  |  string  |  The DCV product.  |
|  status  |  string  |  The status of the license.  |
|  message  |  string  |  A message.  |
|  leftDays  |  number  |  The number of days before the license expires.  |
|  isDemo  |  boolean  |  Indicates if the license is a demo license.  |
|  numUnlicensed  |  number  |  The number of unlicensed connections.  |
|  licensingMode  |  string  |  The licensing mode.  |
|  documentationUrl  |  string  |  The URL for the documentation.  |

### list(path)
<a name="list"></a>

#### Parameters:
<a name="parameters-22"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  path  |  string  |  The absolute path on the server of which we want to list the content.  |

### LogLevel
<a name="LogLevel"></a>

 The available SDK log levels.

#### Type:
<a name="type-24"></a>
+  TRACE \| DEBUG \| INFO \| WARN \| ERROR \| SILENT

### MaxDimensionLimits
<a name="MaxDimensionLimits"></a>

#### Type:
<a name="type-35"></a>
+  Object

#### Properties:
<a name="properties-35"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  maxLargestDimension  |  number  |  The maximum size for the largest dimension supported on webclient by the server.  |
|  maxSmallestDimension  |  number  |  The maximum size for the smallest dimension supported on webclient by the server.  |

### Monitor
<a name="Monitor"></a>

#### Type:
<a name="type-25"></a>
+  Object

#### Properties:
<a name="properties-16"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  name  |  string  |  The name of the display head.  |
|  rect  |  Object  |  Information about the display head. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  primary  |  boolean  |  Indicates whether the display head is the primary display head. This is determined from the remote operating system if available.  |
|  dpi  |  number  |  The DPI of the display head.  |
|  x  |  number  |  The initial x coordinate for the display head.  |
|  y  |  number  |  The initial y coordinate for the display head.  |
|  width  |  number  |  The width (in pixels) of the display head.  |
|  height  |  number  |  The height (in pixels) of the display head.  |

### MultiMonitorErrorCode
<a name="MultiMonitorErrorCode"></a>

 The MultiMonitorError code enums available in the DCV module
+  `NO_DISPLAY_CHANNEL`
+  `MAX_DISPLAY_NUMBER_REACHED`
+  `INVALID_ARGUMENT`
+  `DISPLAY_NOT_OPENED_BY_SERVER`
+  `REQUEST_TIMEOUT`
+  `GENERIC_ERROR`
+  `NO_ERROR`

#### Type:
<a name="type-26"></a>
+  number

### qualityIndicatorStateCallback(state)
<a name="qualityIndicatorStateCallback"></a>

 The callback function to be called when the connection quality indicator changes state.

#### Parameters:
<a name="parameters-23"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  state  |  Array.<Object>  |  Information about the connection quality. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  name  |  string  |  The name of the indicator.  |
|  status  |  NORMAL \| WARNING \| CRITICAL  |  Description of the status.  |
|  changed  |  boolean  |  Indicates whether the status changed.  |

### renameDirectory(src, dest)
<a name="renameDirectory"></a>

#### Parameters:
<a name="parameters-24"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  src  |  string  |  The absolute source path on the server identifying the directory we want to rename.  |
|  dest  |  string  |  The absolute destination path on the server specifying the target path and directory name.  |

### renameFile(src, dest)
<a name="renameFile"></a>

#### Parameters:
<a name="parameters-25"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  src  |  string  |  The absolute source path on the server identifying the file we want to rename.  |
|  dest  |  string  |  The absolute destination path on the server specifying the target path and file name.  |

### ResolutionErrorCode
<a name="ResolutionErrorCode"></a>

 The ResolutionError code enums available in the DCV module
+  `INVALID_ARGUMENT`
+  `NO_CHANNEL`
+  `NOT_IMPLEMENTED`

#### Type:
<a name="type-27"></a>
+  number

### retrieveFile(path)
<a name="retrieveFile"></a>

#### Parameters:
<a name="parameters-26"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  path  |  string  |  The absolute path on the server identifying the file we want to download locally.  |

### screenshotCallback(screenshot)
<a name="screenshotCallback"></a>

 The callback function to be called when a screenshot is available.

#### Parameters:
<a name="parameters-27"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  screenshot  |  byte[]  |  Screenshot buffer in PNG format, or null if screenshot retrieval failed.  |

### ScreenshotErrorCode
<a name="ScreenshotErrorCode"></a>

 The ScreenshotError code enums available in the DCV module
+  `NO_CHANNEL`
+  `GENERIC_ERROR`

#### Type:
<a name="type-33"></a>
+  number

### serverInfo
<a name="serverInfo"></a>

#### Type:
<a name="type-28"></a>
+  Object

#### Properties:
<a name="properties-19"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  name  |  string  |  The name of the software.  |
|  version  |  Object  |  The software version number. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-module.html)  |
|  os  |  string  |  The OS.  |
|  arch  |  string  |  The architecture.  |
|  hostname  |  string  |  The hostname.  |
|  major  |  number  |  The major version number.  |
|  minor  |  number  |  The minor version number.  |
|  revision  |  number  |  The revision version number.  |

### stats
<a name="stats"></a>

#### Type:
<a name="type-29"></a>
+  Object

#### Properties:
<a name="properties-21"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  fps  |  number  |  The current frames per second.  |
|  traffic  |  number  |  The current traffic in bit/s.  |
|  peakTraffic  |  number  |  The peak of traffic in bit/s since the connection was established.  |
|  latency  |  number  |  The current latency in ms.  |
|  currentChannels  |  number  |  The number of channels that have been opened since the connection was established.  |
|  openedChannels  |  number  |  The number of currently opened channels.  |
|  channelErrors  |  number  |  The number of channels which have reported an error.  |

### storeFile(file, dir)
<a name="storeFile"></a>

#### Parameters:
<a name="parameters-28"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  file  |  File  |  The file object (for more information see https://developer.mozilla.org/en-US/docs/Web/API/File) we want to upload to the server.  |
|  dir  |  string  |  The absolute path on the server where we want to upload the file.  |

### TimezoneRedirectionErrorCode
<a name="TimezoneRedirectionErrorCode"></a>

 The TimezoneRedirectionError code enums available in the DCV module
+  `INVALID_ARGUMENT`
+  `NO_CHANNEL`
+  `USER_CANNOT_CHANGE`

#### Type:
<a name="w2aac14b9c17d103b7"></a>
+  number

### TimezoneRedirectionSettingCode
<a name="TimezoneRedirectionSettingCode"></a>

 The TimezoneRedirectionSetting code enums available in the DCV module
+  `ALWAYS_OFF`
+  `ALWAYS_ON`
+  `CLIENT_DECIDES`

#### Type:
<a name="w2aac14b9c17d105b7"></a>
+  number

### TimezoneRedirectionStatusCode
<a name="TimezoneRedirectionStatusCode"></a>

 The TimezoneRedirectionStatus code enums available in the DCV module
+  `SUCCESS`
+  `PERMISSION_ERROR`
+  `GENERIC_ERROR`

#### Type:
<a name="w2aac14b9c17d107b7"></a>
+  number

### WebcamErrorCode
<a name="WebcamErrorCode"></a>

 The WebcamError code enums available in the DCV module
+  `SETTING_WEBCAM_FAILED`
+  `CHANNEL_NOT_AVAILABLE`

#### Type:
<a name="type-30"></a>
+  number

### httpExtraSearchParamsCallback(method, url, body)
<a name="httpExtraSearchParamsCallback"></a>

 The callback function to be called to inject custom query parameters into URLs during authentication and connection establishment. This enables advanced integration scenarios, including the ability to append custom query parameters and add AWS Signature Version 4 (SigV4) signed values to secure and authorize connections through external systems.

This callback is also used to customize the URL that's used when establishing a WebSocket connection to the Amazon DCV server.

#### Parameters:
<a name="parameters-29"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  method  |  string  |  The HTTP method being used for the request.  |
|  url  |  string  |  The URL that will be used for the request.  |
|  body  |  string  |  The request body content.  |

#### Returns:
<a name="returns-30"></a>

 `URLSearchParams` object containing the custom query parameters to be appended to the URL.

 Type
 URLSearchParams

### httpExtraHeadersCallback(method, url, body)
<a name="httpExtraHeadersCallback"></a>

 The callback function to be called to insert custom headers (such as `Authorization`) to the HTTP request during connection establishment.

#### Parameters:
<a name="parameters-31"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  method  |  string  |  The HTTP method being used for the request.  |
|  url  |  string  |  The URL that will be used for the request.  |
|  body  |  string  |  The request body content.  |

#### Returns:
<a name="returns-32"></a>

 Object containing key-value pairs representing the custom headers to be added to the HTTP request.

 Type
 Object
