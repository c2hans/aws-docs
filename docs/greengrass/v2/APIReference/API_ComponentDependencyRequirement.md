---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentDependencyRequirement.html
---

# ComponentDependencyRequirement
<a name="API_ComponentDependencyRequirement"></a>

Contains information about a component dependency for a Lambda function component.

## Contents
<a name="API_ComponentDependencyRequirement_Contents"></a>

 ** dependencyType **   <a name="greengrassv2-Type-ComponentDependencyRequirement-dependencyType"></a>
The type of this dependency. Choose from the following options:
+  `SOFT` – The component doesn't restart if the dependency changes state.
+  `HARD` – The component restarts if the dependency changes state.
Default: `HARD`
Type: String
Valid Values: `HARD | SOFT`
Required: No

 ** versionRequirement **   <a name="greengrassv2-Type-ComponentDependencyRequirement-versionRequirement"></a>
The component version requirement for the component dependency.
 AWS IoT Greengrass V2 uses semantic version constraints. For more information, see [Semantic Versioning](https://semver.org/).
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ComponentDependencyRequirement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentDependencyRequirement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentDependencyRequirement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentDependencyRequirement)
