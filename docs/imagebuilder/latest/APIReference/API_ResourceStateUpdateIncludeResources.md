---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ResourceStateUpdateIncludeResources.html
---

# ResourceStateUpdateIncludeResources
<a name="API_ResourceStateUpdateIncludeResources"></a>

Specifies if the lifecycle policy should apply actions to selected resources.

## Contents
<a name="API_ResourceStateUpdateIncludeResources_Contents"></a>

 ** amis **   <a name="imagebuilder-Type-ResourceStateUpdateIncludeResources-amis"></a>
Specifies whether the lifecycle action should apply to distributed AMIs
Type: Boolean
Required: No

 ** containers **   <a name="imagebuilder-Type-ResourceStateUpdateIncludeResources-containers"></a>
Specifies whether the lifecycle action should apply to distributed containers.
Type: Boolean
Required: No

 ** snapshots **   <a name="imagebuilder-Type-ResourceStateUpdateIncludeResources-snapshots"></a>
Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.
Type: Boolean
Required: No

## See Also
<a name="API_ResourceStateUpdateIncludeResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ResourceStateUpdateIncludeResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ResourceStateUpdateIncludeResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ResourceStateUpdateIncludeResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
