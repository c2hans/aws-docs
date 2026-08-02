---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-viewer.html
---

# Amazon DCV Web UI SDK
<a name="dcv-viewer"></a>

 A JavaScript React component library, currently exporting a single React component called `DCVViewer` which connects to the Amazon DCV Server and renders the toolbar to interact with the remote stream.

**Topics**
+ [Components](#Components)

## Components
<a name="Components"></a>

**Topics**
+ [DCVViewer](#DCVViewer)

### DCVViewer
<a name="DCVViewer"></a>

 The React component rendering the toolbar with all of its functionalities useful to interact with the remote stream.

#### Properties:
<a name="properties"></a>

**Topics**
+ [dcv](#dcv-prop)
+ [uiConfig](#uiConfig-prop)

##### dcv
<a name="dcv-prop"></a>

|  Name  |  Type  |  Required  |  Description  |
| --- | --- | --- | --- |
|  Name  |  Type  |  Required  |  Description  |
| --- | --- | --- | --- |
|  Name  |  Type  |  Required  |  Description  |
| --- | --- | --- | --- |
|  dcv  |  Object  |  Yes  |  The object defining the properties necessary to establish the connection to the Amazon DCV Server, setting the log level and the URL from where to load the Amazon DCV Web Client SDK assets and access the DCV resources. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-viewer.html)  |
|  sessionId  |  String  |  Yes  |  The Amazon DCV session ID.  |
|  authToken  |  String  |  Yes  |  The authentication token to use when connecting to the server.  |
|  serverUrl  |  String  |  Yes  |  The host name and port of the running Amazon DCV server in the following format: https://dcv\_host\_address:port. For example: https://my-dcv-server:8443.  |
|  baseUrl  |  String  |  Yes  |  The absolute or relative URL from which to load SDK files.  |
|  resourceBaseUrl  |  String  |  No (default: "")  |  The absolute or relative URL from which to access DCV resources.  |
|  onDisconnect  |  function  |  No (default: () => {})  |  The callback function invoked when disconnecting from the Amazon DCV server, and the connection is closed.  |
|  logLevel  |  [LogLevel](dcv-module.md#LogLevel)  |  No (default: LogLevel.INFO)  |  The log level to use in the viewer.  |
|  observers  |  Object  |  No (default: {})  |  The object to include httpExtraHeadersCallback and httpExtraSearchParamsCallback to define their implementation. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-viewer.html)  |
|  [httpExtraSearchParams](dcv-module.md#httpExtraSearchParamsCallback)  |  function  |  No (default: () => {})  |  The callback function to be called to inject custom query parameters into URLs during authentication and connection establishment.  |
|  [httpExtraHeaders](dcv-module.md#httpExtraHeadersCallback)  |  function  |  No (default: () => {})  |  The callback function to be called to add custom headers to the HTTP request during connection establishment.  |

##### uiConfig
<a name="uiConfig-prop"></a>

|  Name  |  Type  |  Required  |  Description  |
| --- | --- | --- | --- |
|  Name  |  Type  |  Required  |  Description  |
| --- | --- | --- | --- |
|  Name  |  Type  |  Required  |  Description  |
| --- | --- | --- | --- |
|  uiConfig  |  Object  |  No (default: {})  |  The object defining the properties to configure whether the toolbar is visible and whether to display the fullscreen and multimonitor buttons on it. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-viewer.html)  |
|  toolbar  |  Object  |  No (default: {})  |  The Object defining the configuration options for the toolbar. [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-viewer.html)  |
|  visible  |  Boolean  |  No (default: true)  |  The option to define whether to show or hide the toolbar.  |
|  fullscreenButton  |  Boolean  |  No (default: true)  |  The option to define whether to show or hide the fullscreen button on the toolbar.  |
|  multimonitorButton  |  Boolean  |  No (default: true)  |  The option to define whether to show or hide the multimonitor button on the toolbar.  |
