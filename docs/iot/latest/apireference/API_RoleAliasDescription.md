---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RoleAliasDescription.html
---

# RoleAliasDescription
<a name="API_RoleAliasDescription"></a>

Role alias description.

## Contents
<a name="API_RoleAliasDescription_Contents"></a>

 ** creationDate **   <a name="iot-Type-RoleAliasDescription-creationDate"></a>
The UNIX timestamp of when the role alias was created.
Type: Timestamp
Required: No

 ** credentialDurationSeconds **   <a name="iot-Type-RoleAliasDescription-credentialDurationSeconds"></a>
The number of seconds for which the credential is valid.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

 ** lastModifiedDate **   <a name="iot-Type-RoleAliasDescription-lastModifiedDate"></a>
The UNIX timestamp of when the role alias was last modified.
Type: Timestamp
Required: No

 ** owner **   <a name="iot-Type-RoleAliasDescription-owner"></a>
The role alias owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** roleAlias **   <a name="iot-Type-RoleAliasDescription-roleAlias"></a>
The role alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: No

 ** roleAliasArn **   <a name="iot-Type-RoleAliasDescription-roleAliasArn"></a>
The ARN of the role alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** roleArn **   <a name="iot-Type-RoleAliasDescription-roleArn"></a>
The role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_RoleAliasDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RoleAliasDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RoleAliasDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RoleAliasDescription)
