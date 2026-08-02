---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html
---

# Environment
<a name="API_Environment"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Describes an environment.

## Contents
<a name="API_Environment_Contents"></a>

 ** activationCode **   <a name="workspacesthinclient-Type-Environment-activationCode"></a>
The activation code to register a device to the environment.
Type: String
Pattern: `[a-z]{2}[a-z0-9]{6}`
Required: No

 ** arn **   <a name="workspacesthinclient-Type-Environment-arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+`
Required: No

 ** createdAt **   <a name="workspacesthinclient-Type-Environment-createdAt"></a>
The timestamp of when the environment was created.
Type: Timestamp
Required: No

 ** desiredSoftwareSetId **   <a name="workspacesthinclient-Type-Environment-desiredSoftwareSetId"></a>
The ID of the software set to apply.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** desktopArn **   <a name="workspacesthinclient-Type-Environment-desktopArn"></a>
The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or WorkSpaces Applications.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+`
Required: No

 ** desktopEndpoint **   <a name="workspacesthinclient-Type-Environment-desktopEndpoint"></a>
The URL for the identity provider login (only for environments that use WorkSpaces Applications).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,32}(:[0-9]{1,5})?(\/.*)?`
Required: No

 ** desktopType **   <a name="workspacesthinclient-Type-Environment-desktopType"></a>
The type of streaming desktop for the environment.
Type: String
Valid Values: `workspaces | appstream | workspaces-web`
Required: No

 ** deviceCreationTags **   <a name="workspacesthinclient-Type-Environment-deviceCreationTags"></a>
The tag keys and optional values for the newly created devices for this environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Required: No

 ** id **   <a name="workspacesthinclient-Type-Environment-id"></a>
The ID of the environment.
Type: String
Pattern: `[a-z0-9]{9}`
Required: No

 ** kmsKeyArn **   <a name="workspacesthinclient-Type-Environment-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[0-9]{0,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** maintenanceWindow **   <a name="workspacesthinclient-Type-Environment-maintenanceWindow"></a>
A specification for a time window to apply software updates.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** name **   <a name="workspacesthinclient-Type-Environment-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `$|^[0-9\p{IsAlphabetic}+:,.@'" -][0-9\p{IsAlphabetic}+=:,.@'" -]*`
Required: No

 ** pendingSoftwareSetId **   <a name="workspacesthinclient-Type-Environment-pendingSoftwareSetId"></a>
The ID of the software set that is pending to be installed.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** pendingSoftwareSetVersion **   <a name="workspacesthinclient-Type-Environment-pendingSoftwareSetVersion"></a>
The version of the software set that is pending to be installed.
Type: String
Required: No

 ** registeredDevicesCount **   <a name="workspacesthinclient-Type-Environment-registeredDevicesCount"></a>
The number of devices registered to the environment.
Type: Integer
Required: No

 ** softwareSetComplianceStatus **   <a name="workspacesthinclient-Type-Environment-softwareSetComplianceStatus"></a>
Describes if the software currently installed on all devices in the environment is a supported version.
Type: String
Valid Values: `NO_REGISTERED_DEVICES | COMPLIANT | NOT_COMPLIANT`
Required: No

 ** softwareSetUpdateMode **   <a name="workspacesthinclient-Type-Environment-softwareSetUpdateMode"></a>
An option to define which software updates to apply.
Type: String
Valid Values: `USE_LATEST | USE_DESIRED`
Required: No

 ** softwareSetUpdateSchedule **   <a name="workspacesthinclient-Type-Environment-softwareSetUpdateSchedule"></a>
An option to define if software updates should be applied within a maintenance window.
Type: String
Valid Values: `USE_MAINTENANCE_WINDOW | APPLY_IMMEDIATELY`
Required: No

 ** tags **   <a name="workspacesthinclient-Type-Environment-tags"></a>
The tag keys and optional values for the resource.
Type: String to string map
Required: No

 ** updatedAt **   <a name="workspacesthinclient-Type-Environment-updatedAt"></a>
The timestamp of when the device was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/Environment)
