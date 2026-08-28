---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_TypeConfigurationIdentifier.html
---

# TypeConfigurationIdentifier
<a name="API_TypeConfigurationIdentifier"></a>

Identifying information for the configuration of a CloudFormation extension.

## Contents
<a name="API_TypeConfigurationIdentifier_Contents"></a>

 ** Type **
The type of extension.
Type: String
Valid Values: `RESOURCE | MODULE | HOOK`
Required: No

 ** TypeArn **
The ARN for the extension, in this account and Region.
For public extensions, this will be the ARN assigned when you call the [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) API operation in this account and Region.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`
Required: No

 ** TypeConfigurationAlias **
The alias specified for this configuration, if one was specified when the configuration was set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9]{1,256}$`
Required: No

 ** TypeConfigurationArn **
The ARN for the configuration, in this account and Region.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type-configuration/.+`
Required: No

 ** TypeName **
The name of the extension type to which this configuration applies.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 204.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`
Required: No

## See Also
<a name="API_TypeConfigurationIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeConfigurationIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeConfigurationIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeConfigurationIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
