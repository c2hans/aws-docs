---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_LifecyclePolicy.html
---

# LifecyclePolicy
<a name="API_LifecyclePolicy"></a>

Describes a policy used by lifecycle management that specifies when to transition files into and out of storage classes. For more information, see [Managing file system storage](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html).

**Note**
When using the `put-lifecycle-configuration` CLI command or the `PutLifecycleConfiguration` API action, Amazon EFS requires that each `LifecyclePolicy` object have only a single transition. This means that in a request body, `LifecyclePolicies` must be structured as an array of `LifecyclePolicy` objects, one object for each transition. For more information, see the request examples in [PutLifecycleConfiguration](API_PutLifecycleConfiguration.md).

## Contents
<a name="API_LifecyclePolicy_Contents"></a>

 ** TransitionToArchive **   <a name="efs-Type-LifecyclePolicy-TransitionToArchive"></a>
The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
Type: String
Valid Values: `AFTER_1_DAY | AFTER_7_DAYS | AFTER_14_DAYS | AFTER_30_DAYS | AFTER_60_DAYS | AFTER_90_DAYS | AFTER_180_DAYS | AFTER_270_DAYS | AFTER_365_DAYS`
Required: No

 ** TransitionToIA **   <a name="efs-Type-LifecyclePolicy-TransitionToIA"></a>
The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory don't count as file access events.
Type: String
Valid Values: `AFTER_7_DAYS | AFTER_14_DAYS | AFTER_30_DAYS | AFTER_60_DAYS | AFTER_90_DAYS | AFTER_1_DAY | AFTER_180_DAYS | AFTER_270_DAYS | AFTER_365_DAYS`
Required: No

 ** TransitionToPrimaryStorageClass **   <a name="efs-Type-LifecyclePolicy-TransitionToPrimaryStorageClass"></a>
Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
Type: String
Valid Values: `AFTER_1_ACCESS`
Required: No

## See Also
<a name="API_LifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/LifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/LifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/LifecyclePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
