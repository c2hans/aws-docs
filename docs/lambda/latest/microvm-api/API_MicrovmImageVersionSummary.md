---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_MicrovmImageVersionSummary.html
---

# MicrovmImageVersionSummary
<a name="API_MicrovmImageVersionSummary"></a>

Contains summary information about a version of a MicroVM image.

## Contents
<a name="API_MicrovmImageVersionSummary_Contents"></a>

 ** baseImageArn **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-baseImageArn"></a>
The ARN of the base MicroVM image used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** buildRoleArn **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-buildRoleArn"></a>
The ARN of the IAM build role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** codeArtifact **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-codeArtifact"></a>
The code artifact for this version.
Type: [CodeArtifact](API_CodeArtifact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-createdAt"></a>
The timestamp when the version was created.
Type: Timestamp
Required: Yes

 ** imageArn **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** imageVersion **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-imageVersion"></a>
The version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** state **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-state"></a>
The current state of the version.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESSFUL | FAILED | DELETING | DELETED | DELETE_FAILED`
Required: Yes

 ** status **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-status"></a>
The availability status of the version: ACTIVE (can be used by RunMicrovm) or INACTIVE (blocked from launching new MicroVMs).
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** additionalOsCapabilities **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-additionalOsCapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
Type: Array of strings
Valid Values: `ALL`
Required: No

 ** baseImageVersion **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-baseImageVersion"></a>
The specific version of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

 ** cpuConfigurations **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-cpuConfigurations"></a>
The list of supported CPU configurations for the MicroVM.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects
Required: No

 ** description **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-description"></a>
The description of the version.
Type: String
Required: No

 ** egressNetworkConnectors **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-egressNetworkConnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** environmentVariables **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-environmentVariables"></a>
Environment variables set in the MicroVM runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** hooks **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
Type: [Hooks](API_Hooks.md) object
Required: No

 ** logging **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-logging"></a>
The logging configuration for this version.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** resources **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-resources"></a>
The resource requirements for the MicroVM.
Type: Array of [Resources](API_Resources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** stateReason **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-stateReason"></a>
The reason for the current state. For example, one or more builds failed.
Type: String
Required: No

 ** tags **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-tags"></a>
Key-value pairs associated with the version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** updatedAt **   <a name="lambdamicrovm-Type-MicrovmImageVersionSummary-updatedAt"></a>
The timestamp when the version was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_MicrovmImageVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/MicrovmImageVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/MicrovmImageVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/MicrovmImageVersionSummary)
