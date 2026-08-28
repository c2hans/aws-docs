---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ApplicationConfig.html
---

# ApplicationConfig
<a name="API_ApplicationConfig"></a>

Configuration for an application in the imported image's application catalog. This structure defines how applications appear and launch for users.

## Contents
<a name="API_ApplicationConfig_Contents"></a>

 ** AbsoluteAppPath **   <a name="WorkSpacesApplications-Type-ApplicationConfig-AbsoluteAppPath"></a>
The absolute path to the executable file that launches the application. This is a required field that can be 1-32767 characters to support Windows extended file paths. Use escaped file path strings like "C:\\\\\\\\Windows\\\\\\\\System32\\\\\\\\notepad.exe".
Type: String
Length Constraints: Maximum length of 32767.
Required: Yes

 ** Name **   <a name="WorkSpacesApplications-Type-ApplicationConfig-Name"></a>
The name of the application. This is a required field that must be unique within the application catalog and between 1-100 characters, matching the pattern ^[a-zA-Z0-9][a-zA-Z0-9\_.-]{0,99}$.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}$`
Required: Yes

 ** AbsoluteIconPath **   <a name="WorkSpacesApplications-Type-ApplicationConfig-AbsoluteIconPath"></a>
The absolute path to the icon file for the application. This field is optional and can be 1-32767 characters. If not provided, the icon is derived from the executable. Use PNG images with proper transparency for the best user experience.
Type: String
Length Constraints: Maximum length of 32767.
Required: No

 ** AbsoluteManifestPath **   <a name="WorkSpacesApplications-Type-ApplicationConfig-AbsoluteManifestPath"></a>
The absolute path to the prewarm manifest file for this application. This field is optional and only applicable when using application-specific manifests. The path can be 1-32767 characters and should point to a text file containing file paths to prewarm.
Type: String
Length Constraints: Maximum length of 32767.
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-ApplicationConfig-DisplayName"></a>
The display name shown to users for this application. This field is optional and can be 0-100 characters, matching the pattern ^[a-zA-Z0-9][a-zA-Z0-9\_. -]{0,99}$.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_. -]{0,99}$`
Required: No

 ** LaunchParameters **   <a name="WorkSpacesApplications-Type-ApplicationConfig-LaunchParameters"></a>
The launch parameters to pass to the application executable. This field is optional and can be 0-1024 characters. Use escaped strings with the full list of required parameters, such as PowerShell script paths or command-line arguments.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[^\x00]+`
Required: No

 ** WorkingDirectory **   <a name="WorkSpacesApplications-Type-ApplicationConfig-WorkingDirectory"></a>
The working directory to use when launching the application. This field is optional and can be 0-32767 characters. Use escaped file path strings like "C:\\\\\\\\Path\\\\\\\\To\\\\\\\\Working\\\\\\\\Directory".
Type: String
Length Constraints: Maximum length of 32767.
Required: No

## See Also
<a name="API_ApplicationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ApplicationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ApplicationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ApplicationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
