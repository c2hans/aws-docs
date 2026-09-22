---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicy.html
---

# LifecyclePolicy
<a name="API_LifecyclePolicy"></a>

Defines a lifecycle policy resource: its identity, status, execution role, resource type, rules, resource selection, timestamps, and tags.

## Contents
<a name="API_LifecyclePolicy_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-LifecyclePolicy-arn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy resource.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-LifecyclePolicy-dateCreated"></a>
The timestamp when Image Builder created the lifecycle policy resource.
Type: Timestamp
Required: No

 ** dateLastRun **   <a name="imagebuilder-Type-LifecyclePolicy-dateLastRun"></a>
The timestamp for the last time Image Builder ran the lifecycle policy.
Type: Timestamp
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-LifecyclePolicy-dateUpdated"></a>
The timestamp when Image Builder updated the lifecycle policy resource.
Type: Timestamp
Required: No

 ** description **   <a name="imagebuilder-Type-LifecyclePolicy-description"></a>
Optional description for the lifecycle policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** executionRole **   <a name="imagebuilder-Type-LifecyclePolicy-executionRole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to run the lifecycle policy. This is a custom role that you create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** name **   <a name="imagebuilder-Type-LifecyclePolicy-name"></a>
The name of the lifecycle policy.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** policyDetails **   <a name="imagebuilder-Type-LifecyclePolicy-policyDetails"></a>
The list of rules for the lifecycle policy. Each rule pairs an action with a filter and optional exclusion rules. A policy can contain at most one rule per action type.
Type: Array of [LifecyclePolicyDetail](API_LifecyclePolicyDetail.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** resourceSelection **   <a name="imagebuilder-Type-LifecyclePolicy-resourceSelection"></a>
Resource selection criteria used to run the lifecycle policy.
Type: [LifecyclePolicyResourceSelection](API_LifecyclePolicyResourceSelection.md) object
Required: No

 ** resourceType **   <a name="imagebuilder-Type-LifecyclePolicy-resourceType"></a>
The type of resources the lifecycle policy targets.
Type: String
Valid Values: `AMI_IMAGE | CONTAINER_IMAGE`
Required: No

 ** status **   <a name="imagebuilder-Type-LifecyclePolicy-status"></a>
Indicates whether the lifecycle policy resource is enabled. Only enabled policies run on their schedule. Disabling or deleting a policy removes its schedule and cancels any in-flight lifecycle execution.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** tags **   <a name="imagebuilder-Type-LifecyclePolicy-tags"></a>
To help manage your lifecycle policy resources, you can assign your own metadata to each resource in the form of tags. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicy)
