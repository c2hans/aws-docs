---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html
---

# Device
<a name="API_Device"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Describes a thin client device.

## Contents
<a name="API_Device_Contents"></a>

 ** arn **   <a name="workspacesthinclient-Type-Device-arn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+`
Required: No

 ** createdAt **   <a name="workspacesthinclient-Type-Device-createdAt"></a>
The timestamp of when the device was created.
Type: Timestamp
Required: No

 ** currentSoftwareSetId **   <a name="workspacesthinclient-Type-Device-currentSoftwareSetId"></a>
The ID of the software set currently installed on the device.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** currentSoftwareSetVersion **   <a name="workspacesthinclient-Type-Device-currentSoftwareSetVersion"></a>
The version of the software set currently installed on the device.
Type: String
Required: No

 ** desiredSoftwareSetId **   <a name="workspacesthinclient-Type-Device-desiredSoftwareSetId"></a>
The ID of the software set which the device has been set to.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** environmentId **   <a name="workspacesthinclient-Type-Device-environmentId"></a>
The ID of the environment the device is associated with.
Type: String
Pattern: `[a-z0-9]{9}`
Required: No

 ** id **   <a name="workspacesthinclient-Type-Device-id"></a>
The ID of the device.
Type: String
Pattern: `[a-zA-Z0-9]{24}`
Required: No

 ** kmsKeyArn **   <a name="workspacesthinclient-Type-Device-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[0-9]{0,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** lastConnectedAt **   <a name="workspacesthinclient-Type-Device-lastConnectedAt"></a>
The timestamp of the most recent session on the device.
Type: Timestamp
Required: No

 ** lastPostureAt **   <a name="workspacesthinclient-Type-Device-lastPostureAt"></a>
The timestamp of the most recent check-in of the device.
Type: Timestamp
Required: No

 ** model **   <a name="workspacesthinclient-Type-Device-model"></a>
The model number of the device.
Type: String
Required: No

 ** name **   <a name="workspacesthinclient-Type-Device-name"></a>
The name of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `$|^[0-9\p{IsAlphabetic}+:,.@'" -]*`
Required: No

 ** pendingSoftwareSetId **   <a name="workspacesthinclient-Type-Device-pendingSoftwareSetId"></a>
The ID of the software set that is pending to be installed on the device.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** pendingSoftwareSetVersion **   <a name="workspacesthinclient-Type-Device-pendingSoftwareSetVersion"></a>
The version of the software set that is pending to be installed on the device.
Type: String
Required: No

 ** serialNumber **   <a name="workspacesthinclient-Type-Device-serialNumber"></a>
The hardware serial number of the device.
Type: String
Required: No

 ** softwareSetComplianceStatus **   <a name="workspacesthinclient-Type-Device-softwareSetComplianceStatus"></a>
Describes if the software currently installed on the device is a supported version.
Type: String
Valid Values: `NONE | COMPLIANT | NOT_COMPLIANT`
Required: No

 ** softwareSetUpdateSchedule **   <a name="workspacesthinclient-Type-Device-softwareSetUpdateSchedule"></a>
An option to define if software updates should be applied within a maintenance window.
Type: String
Valid Values: `USE_MAINTENANCE_WINDOW | APPLY_IMMEDIATELY`
Required: No

 ** softwareSetUpdateStatus **   <a name="workspacesthinclient-Type-Device-softwareSetUpdateStatus"></a>
Describes if the device has a supported version of software installed.
Type: String
Valid Values: `AVAILABLE | IN_PROGRESS | UP_TO_DATE`
Required: No

 ** status **   <a name="workspacesthinclient-Type-Device-status"></a>
The status of the device.
Type: String
Valid Values: `REGISTERED | DEREGISTERING | DEREGISTERED | ARCHIVED`
Required: No

 ** tags **   <a name="workspacesthinclient-Type-Device-tags"></a>
The tag keys and optional values for the resource.
Type: String to string map
Required: No

 ** updatedAt **   <a name="workspacesthinclient-Type-Device-updatedAt"></a>
The timestamp of when the device was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/Device)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
