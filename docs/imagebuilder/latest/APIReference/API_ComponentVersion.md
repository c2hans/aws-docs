---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentVersion.html
---

# ComponentVersion
<a name="API_ComponentVersion"></a>

The defining characteristics of a specific version of an AWSTOE component.

## Contents
<a name="API_ComponentVersion_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-ComponentVersion-arn"></a>
The Amazon Resource Name (ARN) of the component.
Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:

1. Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.

1. Version ARNs have only the first three nodes: <major>.<minor>.<patch>

1. Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ComponentVersion-dateCreated"></a>
The date that the component was created.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-ComponentVersion-description"></a>
The description of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-ComponentVersion-name"></a>
The name of the component.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-ComponentVersion-owner"></a>
The owner of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** platform **   <a name="imagebuilder-Type-ComponentVersion-platform"></a>
The platform of the component.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** productCodes **   <a name="imagebuilder-Type-ComponentVersion-productCodes"></a>
Contains product codes that are used for billing purposes for AWS Marketplace components.
Type: Array of [ProductCodeListItem](API_ProductCodeListItem.md) objects
Required: No

 ** status **   <a name="imagebuilder-Type-ComponentVersion-status"></a>
Describes the current status of the component version.
Type: String
Valid Values: `DEPRECATED | DISABLED | ACTIVE`
Required: No

 ** supportedOsVersions **   <a name="imagebuilder-Type-ComponentVersion-supportedOsVersions"></a>
he operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1.
Required: No

 ** type **   <a name="imagebuilder-Type-ComponentVersion-type"></a>
The type of the component denotes whether the component is used to build the image or only to test it.
Type: String
Valid Values: `BUILD | TEST`
Required: No

 ** version **   <a name="imagebuilder-Type-ComponentVersion-version"></a>
The semantic version of the component.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
 **Filtering:** With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

## See Also
<a name="API_ComponentVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentVersion)
