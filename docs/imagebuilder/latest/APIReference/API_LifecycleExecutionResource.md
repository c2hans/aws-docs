---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecutionResource.html
---

# LifecycleExecutionResource
<a name="API_LifecycleExecutionResource"></a>

Contains details for a resource that the runtime instance of the lifecycle policy identified for action.

## Contents
<a name="API_LifecycleExecutionResource_Contents"></a>

 ** accountId **   <a name="imagebuilder-Type-LifecycleExecutionResource-accountId"></a>
The account that owns the impacted resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** action **   <a name="imagebuilder-Type-LifecycleExecutionResource-action"></a>
The action to take for the identified resource.
Type: [LifecycleExecutionResourceAction](API_LifecycleExecutionResourceAction.md) object
Required: No

 ** endTime **   <a name="imagebuilder-Type-LifecycleExecutionResource-endTime"></a>
The ending timestamp from the lifecycle action that was applied to the resource.
Type: Timestamp
Required: No

 ** imageUris **   <a name="imagebuilder-Type-LifecycleExecutionResource-imageUris"></a>
For an impacted container image, this identifies a list of URIs for associated container images distributed to ECR repositories.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** region **   <a name="imagebuilder-Type-LifecycleExecutionResource-region"></a>
The AWS Region where the lifecycle execution resource is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** resourceId **   <a name="imagebuilder-Type-LifecycleExecutionResource-resourceId"></a>
Identifies the impacted resource. The resource ID depends on the type of resource, as follows.
+ Image Builder image resources: Amazon Resource Name (ARN)
+ Distributed AMIs: AMI ID
+ Container images distributed to an ECR repository: image URI or SHA Digest
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** snapshots **   <a name="imagebuilder-Type-LifecycleExecutionResource-snapshots"></a>
A list of associated resource snapshots for the impacted resource if it’s an AMI.
Type: Array of [LifecycleExecutionSnapshotResource](API_LifecycleExecutionSnapshotResource.md) objects
Required: No

 ** startTime **   <a name="imagebuilder-Type-LifecycleExecutionResource-startTime"></a>
The starting timestamp from the lifecycle action that was applied to the resource.
Type: Timestamp
Required: No

 ** state **   <a name="imagebuilder-Type-LifecycleExecutionResource-state"></a>
The runtime state of the lifecycle action for this resource.
Type: [LifecycleExecutionResourceState](API_LifecycleExecutionResourceState.md) object
Required: No

## See Also
<a name="API_LifecycleExecutionResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecycleExecutionResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecycleExecutionResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecycleExecutionResource)
