---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/extension-manifest.html
---

# Extension manifest
<a name="extension-manifest"></a>

Manifest files are JSON files in the format described below. Ensure that all special characters are properly escaped with a reverse backslash. A `.json` extension is required for the manifest file.

```
{
"name": "MyExtension",
"description": "My extension longer description",
"path": "C:\\Program Files\\My Company\\My Product\\bin\\myextension.exe",
"start_on_server": true,
"start_on_client": true,
"virtual_channel_namespace": "com.company.product",
"userdata": "parameters to the extension"
}
```
+ **name** – The name for the extension that will appear in DCV logs.
+ **description** – A textual description of the extension that appears in the user interface (About dialog box).
+ **path** – The complete path to the extension executable, escaping backslashes if necessary. It is important to use the correct path notation depending on the operating system. This would be `c:\\path\\to.exe` in Windows and ` /path/to/executable` in Linux and macOS.
+ **start\_on\_server** and **start\_on\_client** – Indicates whether an extension defined by the manifest should be run on the server or client or both.
+ **virtual\_channel\_namespace** – This attribute specifies the namespace for virtual channels created by this extension. Although different vendors may create virtual channels with the same name, they should be in separate namespaces. Namespace 'dcv' is reserved, so it shouldn't be used.
+ **userdata** – Amazon DCV ignores this attribute, but the extension can access it via `GetManifestRequest`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
