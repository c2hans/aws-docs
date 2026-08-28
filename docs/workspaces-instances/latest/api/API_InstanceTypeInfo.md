---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceTypeInfo.html
---

# InstanceTypeInfo
<a name="API_InstanceTypeInfo"></a>

Provides details about a specific WorkSpace Instance type.

## Contents
<a name="API_InstanceTypeInfo_Contents"></a>

 ** InstanceType **   <a name="workspacesinstances-Type-InstanceTypeInfo-InstanceType"></a>
Unique identifier for the WorkSpace Instance type.
Type: String
Pattern: `([a-z0-9-]+)\.([a-z0-9]+)`
Required: No

 ** SupportedInstanceConfigurations **   <a name="workspacesinstances-Type-InstanceTypeInfo-SupportedInstanceConfigurations"></a>
Lists all valid combinations of tenancy, platform type, and billing mode supported for the specific WorkSpace Instance type. Contains the complete set of configuration options available for this instance type.
Type: Array of [SupportedInstanceConfiguration](API_SupportedInstanceConfiguration.md) objects
Required: No

## See Also
<a name="API_InstanceTypeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/InstanceTypeInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/InstanceTypeInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/InstanceTypeInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
