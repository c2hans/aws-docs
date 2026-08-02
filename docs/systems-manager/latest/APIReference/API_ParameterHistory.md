---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ParameterHistory.html
---

# ParameterHistory
<a name="API_ParameterHistory"></a>

Information about parameter usage.

## Contents
<a name="API_ParameterHistory_Contents"></a>

 ** AllowedPattern **   <a name="systemsmanager-Type-ParameterHistory-AllowedPattern"></a>
Parameter names can include the following letters and symbols.
a-zA-Z0-9\_.-
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DataType **   <a name="systemsmanager-Type-ParameterHistory-DataType"></a>
The data type of the parameter, such as `text` or `aws:ec2:image`. The default is `text`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Description **   <a name="systemsmanager-Type-ParameterHistory-Description"></a>
Information about the parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** KeyId **   <a name="systemsmanager-Type-ParameterHistory-KeyId"></a>
The alias of the AWS Key Management Service (AWS KMS) key used to encrypt the parameter. Applies to `SecureString` parameters only
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([a-zA-Z0-9:/_-]+)$`
Required: No

 ** Labels **   <a name="systemsmanager-Type-ParameterHistory-Labels"></a>
Labels assigned to the parameter version.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** LastModifiedDate **   <a name="systemsmanager-Type-ParameterHistory-LastModifiedDate"></a>
Date the parameter was last changed or updated.
Type: Timestamp
Required: No

 ** LastModifiedUser **   <a name="systemsmanager-Type-ParameterHistory-LastModifiedUser"></a>
Amazon Resource Name (ARN) of the Amazon Web Services user who last changed the parameter.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-ParameterHistory-Name"></a>
The name of the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Policies **   <a name="systemsmanager-Type-ParameterHistory-Policies"></a>
Information about the policies assigned to a parameter.
 [Assigning parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the * AWS Systems Manager User Guide*.
Type: Array of [ParameterInlinePolicy](API_ParameterInlinePolicy.md) objects
Required: No

 ** Tier **   <a name="systemsmanager-Type-ParameterHistory-Tier"></a>
The parameter tier.
Type: String
Valid Values: `Standard | Advanced | Intelligent-Tiering`
Required: No

 ** Type **   <a name="systemsmanager-Type-ParameterHistory-Type"></a>
The type of parameter used.
Type: String
Valid Values: `String | StringList | SecureString`
Required: No

 ** Value **   <a name="systemsmanager-Type-ParameterHistory-Value"></a>
The parameter value.
Type: String
Required: No

 ** Version **   <a name="systemsmanager-Type-ParameterHistory-Version"></a>
The parameter version.
Type: Long
Required: No

## See Also
<a name="API_ParameterHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ParameterHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ParameterHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ParameterHistory)
