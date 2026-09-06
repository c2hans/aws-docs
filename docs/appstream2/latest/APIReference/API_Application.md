---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Application.html
---

# Application
<a name="API_Application"></a>

Describes an application in the application catalog.

## Contents
<a name="API_Application_Contents"></a>

 ** AppBlockArn **   <a name="WorkSpacesApplications-Type-Application-AppBlockArn"></a>
The app block ARN of the application.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** Arn **   <a name="WorkSpacesApplications-Type-Application-Arn"></a>
The ARN of the application.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-Application-CreatedTime"></a>
The time at which the application was created within the app block.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-Application-Description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-Application-DisplayName"></a>
The application name to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Enabled **   <a name="WorkSpacesApplications-Type-Application-Enabled"></a>
If there is a problem, the application can be disabled after image creation.
Type: Boolean
Required: No

 ** IconS3Location **   <a name="WorkSpacesApplications-Type-Application-IconS3Location"></a>
The S3 location of the application icon.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** IconURL **   <a name="WorkSpacesApplications-Type-Application-IconURL"></a>
The URL for the application icon. This URL might be time-limited.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** InstanceFamilies **   <a name="WorkSpacesApplications-Type-Application-InstanceFamilies"></a>
The instance families for the application.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** LaunchParameters **   <a name="WorkSpacesApplications-Type-Application-LaunchParameters"></a>
The arguments that are passed to the application at launch.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** LaunchPath **   <a name="WorkSpacesApplications-Type-Application-LaunchPath"></a>
The path to the application executable in the instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Metadata **   <a name="WorkSpacesApplications-Type-Application-Metadata"></a>
Additional attributes that describe the application.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: No

 ** Name **   <a name="WorkSpacesApplications-Type-Application-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Platforms **   <a name="WorkSpacesApplications-Type-Application-Platforms"></a>
The platforms on which the application can run.
Type: Array of strings
Array Members: Maximum number of 4 items.
Valid Values: `WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | WINDOWS_11 | AMAZON_LINUX2 | RHEL8 | ROCKY_LINUX8 | UBUNTU_PRO_2404`
Required: No

 ** WorkingDirectory **   <a name="WorkSpacesApplications-Type-Application-WorkingDirectory"></a>
The working directory for the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Application)
