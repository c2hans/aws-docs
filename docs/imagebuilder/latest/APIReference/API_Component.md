---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Component.html
---

# Component
<a name="API_Component"></a>

A detailed view of a component.

## Contents
<a name="API_Component_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-Component-arn"></a>
The Amazon Resource Name (ARN) of the component.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** changeDescription **   <a name="imagebuilder-Type-Component-changeDescription"></a>
Describes what change has been made in this version of the component, or what makes this version different from other versions of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** data **   <a name="imagebuilder-Type-Component-data"></a>
Component data contains the YAML document content for the component.
Type: String
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-Component-dateCreated"></a>
The date that Image Builder created the component.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-Component-description"></a>
The description of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** encrypted **   <a name="imagebuilder-Type-Component-encrypted"></a>
Indicates whether the component data is encrypted at rest. Image Builder encrypts all component data at rest, so this value is always `true`. This field is retained for backward compatibility.
Type: Boolean
Required: No

 ** kmsKeyId **   <a name="imagebuilder-Type-Component-kmsKeyId"></a>
The KMS key identifier used to encrypt the component. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-Component-name"></a>
The name of the component.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** obfuscate **   <a name="imagebuilder-Type-Component-obfuscate"></a>
Indicates whether component source is hidden from view in the console, and from component detail results for API, CLI, or SDK operations.
Type: Boolean
Required: No

 ** owner **   <a name="imagebuilder-Type-Component-owner"></a>
The owner of the component. The value is your account ID for components that you own, the sharing account's ID for shared components, or `Amazon`, `ThirdParty`, or `AWSMarketplace`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** parameters **   <a name="imagebuilder-Type-Component-parameters"></a>
Contains parameter details for each of the parameters that the component document defined for the component.
Type: Array of [ComponentParameterDetail](API_ComponentParameterDetail.md) objects
Required: No

 ** platform **   <a name="imagebuilder-Type-Component-platform"></a>
The operating system platform of the component.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** productCodes **   <a name="imagebuilder-Type-Component-productCodes"></a>
Contains product codes that are used for billing purposes for AWS Marketplace components.
Type: Array of [ProductCodeListItem](API_ProductCodeListItem.md) objects
Required: No

 ** publisher **   <a name="imagebuilder-Type-Component-publisher"></a>
Contains the name of the publisher if this is a third-party component. Otherwise, this property is empty.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** state **   <a name="imagebuilder-Type-Component-state"></a>
Describes the current status of the component.
Type: [ComponentState](API_ComponentState.md) object
Required: No

 ** supportedOsVersions **   <a name="imagebuilder-Type-Component-supportedOsVersions"></a>
The operating system (OS) version supported by the component. If the OS information is available, Image Builder performs a prefix match against the base image OS version during image recipe creation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1.
Required: No

 ** tags **   <a name="imagebuilder-Type-Component-tags"></a>
The tags that apply to the component.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** type **   <a name="imagebuilder-Type-Component-type"></a>
The component type specifies whether Image Builder uses the component to build the image or only to test it.
Type: String
Valid Values: `BUILD | TEST`
Required: No

 ** version **   <a name="imagebuilder-Type-Component-version"></a>
The version of the component.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

## See Also
<a name="API_Component_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Component)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Component)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Component)
