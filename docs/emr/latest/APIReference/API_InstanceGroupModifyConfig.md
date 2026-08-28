---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceGroupModifyConfig.html
---

# InstanceGroupModifyConfig
<a name="API_InstanceGroupModifyConfig"></a>

Modify the size or configurations of an instance group.

## Contents
<a name="API_InstanceGroupModifyConfig_Contents"></a>

 ** InstanceGroupId **   <a name="EMR-Type-InstanceGroupModifyConfig-InstanceGroupId"></a>
Unique ID of the instance group to modify.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Configurations **   <a name="EMR-Type-InstanceGroupModifyConfig-Configurations"></a>
A list of new or modified configurations to apply for an instance group.
Type: Array of [Configuration](API_Configuration.md) objects
Required: No

 ** EC2InstanceIdsToTerminate **   <a name="EMR-Type-InstanceGroupModifyConfig-EC2InstanceIdsToTerminate"></a>
The Amazon EC2 InstanceIds to terminate. After you terminate the instances, the instance group will not return to its original requested size.
Type: Array of strings
Required: No

 ** InstanceCount **   <a name="EMR-Type-InstanceGroupModifyConfig-InstanceCount"></a>
Target size for the instance group.
Type: Integer
Required: No

 ** ReconfigurationType **   <a name="EMR-Type-InstanceGroupModifyConfig-ReconfigurationType"></a>
Type of reconfiguration requested. Valid values are MERGE and OVERWRITE.
Type: String
Valid Values: `OVERWRITE | MERGE`
Required: No

 ** ShrinkPolicy **   <a name="EMR-Type-InstanceGroupModifyConfig-ShrinkPolicy"></a>
Policy for customizing shrink operations.
Type: [ShrinkPolicy](API_ShrinkPolicy.md) object
Required: No

## See Also
<a name="API_InstanceGroupModifyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroupModifyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroupModifyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroupModifyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
