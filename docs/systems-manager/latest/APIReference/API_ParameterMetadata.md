---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ParameterMetadata.html
---

# ParameterMetadata
<a name="API_ParameterMetadata"></a>

Metadata includes information like the Amazon Resource Name (ARN) of the last user to update the parameter and the date and time the parameter was last used.

## Contents
<a name="API_ParameterMetadata_Contents"></a>

 ** AllowedPattern **   <a name="systemsmanager-Type-ParameterMetadata-AllowedPattern"></a>
A parameter name can include only the following letters and symbols.
a-zA-Z0-9\_.-
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ARN **   <a name="systemsmanager-Type-ParameterMetadata-ARN"></a>
The Amazon Resource Name (ARN) of the parameter.
Type: String
Required: No

 ** DataType **   <a name="systemsmanager-Type-ParameterMetadata-DataType"></a>
The data type of the parameter, such as `text` or `aws:ec2:image`. The default is `text`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Description **   <a name="systemsmanager-Type-ParameterMetadata-Description"></a>
Description of the parameter actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** KeyId **   <a name="systemsmanager-Type-ParameterMetadata-KeyId"></a>
The alias of the AWS Key Management Service (AWS KMS) key used to encrypt the parameter. Applies to `SecureString` parameters only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([a-zA-Z0-9:/_-]+)$`
Required: No

 ** LastModifiedDate **   <a name="systemsmanager-Type-ParameterMetadata-LastModifiedDate"></a>
Date the parameter was last changed or updated.
Type: Timestamp
Required: No

 ** LastModifiedUser **   <a name="systemsmanager-Type-ParameterMetadata-LastModifiedUser"></a>
Amazon Resource Name (ARN) of the Amazon Web Services user who last changed the parameter.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-ParameterMetadata-Name"></a>
The parameter name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Policies **   <a name="systemsmanager-Type-ParameterMetadata-Policies"></a>
A list of policies associated with a parameter.
Type: Array of [ParameterInlinePolicy](API_ParameterInlinePolicy.md) objects
Required: No

 ** Tier **   <a name="systemsmanager-Type-ParameterMetadata-Tier"></a>
The parameter tier.
Type: String
Valid Values: `Standard | Advanced | Intelligent-Tiering`
Required: No

 ** Type **   <a name="systemsmanager-Type-ParameterMetadata-Type"></a>
The type of parameter. Valid parameter types include the following: `String`, `StringList`, and `SecureString`.
Type: String
Valid Values: `String | StringList | SecureString`
Required: No

 ** Version **   <a name="systemsmanager-Type-ParameterMetadata-Version"></a>
The parameter version.
Type: Long
Required: No

## See Also
<a name="API_ParameterMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ParameterMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ParameterMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ParameterMetadata)
