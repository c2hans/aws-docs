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

<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Required </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>dcv</code> </td><td> Object </td><td> Yes </td><td> The object defining the properties necessary to establish the connection to the Amazon DCV Server, setting the log level and the URL from where to load the Amazon DCV Web Client SDK assets and access the DCV resources.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Required </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>sessionId</code> </td><td> String </td><td> Yes </td><td> The Amazon DCV session ID. </td></tr>
  <tr><td> <code>authToken</code> </td><td> String </td><td> Yes </td><td> The authentication token to use when connecting to the server. </td></tr>
  <tr><td> <code>serverUrl</code> </td><td> String </td><td> Yes </td><td> The host name and port of the running Amazon DCV server in the following format: https://dcv_host_address:port. For example: https://my-dcv-server:8443. </td></tr>
  <tr><td> <code>baseUrl</code> </td><td> String </td><td> Yes </td><td> The absolute or relative URL from which to load SDK files. </td></tr>
  <tr><td> <code>resourceBaseUrl</code> </td><td> String </td><td> No (default: <code>""</code>) </td><td> The absolute or relative URL from which to access DCV resources. </td></tr>
  <tr><td> <code>onDisconnect</code> </td><td> function </td><td> No (default: <code>() =&gt; {}</code>) </td><td> The callback function invoked when disconnecting from the Amazon DCV server, and the connection is closed. </td></tr>
  <tr><td> <code>logLevel</code> </td><td> <a href="dcv-module.md#LogLevel">LogLevel</a> </td><td> No (default: <code>LogLevel.INFO</code>) </td><td> The log level to use in the viewer. </td></tr>
  <tr><td> <code>observers</code> </td><td> Object </td><td> No (default: {}) </td><td> The object to include httpExtraHeadersCallback and httpExtraSearchParamsCallback to define their implementation.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Required </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <a href="dcv-module.md#httpExtraSearchParamsCallback">httpExtraSearchParams</a> </td><td> function </td><td> No (default: <code>() =&gt; {}</code>) </td><td> The callback function to be called to inject custom query parameters into URLs during authentication and connection establishment. </td></tr>
  <tr><td> <a href="dcv-module.md#httpExtraHeadersCallback">httpExtraHeaders</a> </td><td> function </td><td> No (default: <code>() =&gt; {}</code>) </td><td> The callback function to be called to add custom headers to the HTTP request during connection establishment. </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>

##### uiConfig
<a name="uiConfig-prop"></a>

<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Required </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>uiConfig</code> </td><td> Object </td><td> No (default: <code>{}</code>) </td><td> The object defining the properties to configure whether the toolbar is visible and whether to display the fullscreen and multimonitor buttons on it.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Required </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>toolbar</code> </td><td> Object </td><td> No (default: <code>{}</code>) </td><td> The Object defining the configuration options for the toolbar.
<table>
<thead>
  <tr><th> Name </th><th> Type </th><th> Required </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> <code>visible</code> </td><td> Boolean </td><td> No (default: <code>true</code>) </td><td> The option to define whether to show or hide the toolbar. </td></tr>
  <tr><td> <code>fullscreenButton</code> </td><td> Boolean </td><td> No (default: <code>true</code>) </td><td> The option to define whether to show or hide the fullscreen button on the toolbar. </td></tr>
  <tr><td> <code>multimonitorButton</code> </td><td> Boolean </td><td> No (default: <code>true</code>) </td><td> The option to define whether to show or hide the multimonitor button on the toolbar. </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>
