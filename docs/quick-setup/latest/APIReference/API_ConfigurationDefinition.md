---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationDefinition.html
---

# ConfigurationDefinition
<a name="API_ConfigurationDefinition"></a>

The definition of a Quick Setup configuration.

## Contents
<a name="API_ConfigurationDefinition_Contents"></a>

 ** Parameters **   <a name="quicksetup-Type-ConfigurationDefinition-Parameters"></a>
A list of key-value pairs containing the required parameters for the configuration type.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9+=@_\/\s-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 40960.
Required: Yes

 ** Type **   <a name="quicksetup-Type-ConfigurationDefinition-Type"></a>
The type of the Quick Setup configuration.
Type: String
Pattern: `[a-zA-Z0-9_\-.:/]{3,200}`
Required: Yes

 ** Id **   <a name="quicksetup-Type-ConfigurationDefinition-Id"></a>
The ID of the configuration definition.
Type: String
Required: No

 ** LocalDeploymentAdministrationRoleArn **   <a name="quicksetup-Type-ConfigurationDefinition-LocalDeploymentAdministrationRoleArn"></a>
The ARN of the IAM role used to administrate local configuration deployments.
Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than `AWSQuickSetupType-PatchPolicy`. A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.
Type: String
Pattern: `arn:aws(-cn|-us-gov)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+.*`
Required: No

 ** LocalDeploymentExecutionRoleName **   <a name="quicksetup-Type-ConfigurationDefinition-LocalDeploymentExecutionRoleName"></a>
The name of the IAM role used to deploy local configurations.
Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than `AWSQuickSetupType-PatchPolicy`. A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.
Type: String
Pattern: `([\w+=,.@\/-]{1,512}\/)?[\w+=,.@-]{1,64}`
Required: No

 ** TypeVersion **   <a name="quicksetup-Type-ConfigurationDefinition-TypeVersion"></a>
The version of the Quick Setup type used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ConfigurationDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ConfigurationDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ConfigurationDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ConfigurationDefinition)
