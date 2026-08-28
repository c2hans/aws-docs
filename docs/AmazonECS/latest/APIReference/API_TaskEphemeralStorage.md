---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskEphemeralStorage.html
---

# TaskEphemeralStorage
<a name="API_TaskEphemeralStorage"></a>

The amount of ephemeral storage to allocate for the task.

## Contents
<a name="API_TaskEphemeralStorage_Contents"></a>

 ** kmsKeyId **   <a name="ECS-Type-TaskEphemeralStorage-kmsKeyId"></a>
Specify an AWS Key Management Service key ID to encrypt the ephemeral storage for the task.
Type: String
Required: No

 ** sizeInGiB **   <a name="ECS-Type-TaskEphemeralStorage-sizeInGiB"></a>
The total amount, in GiB, of the ephemeral storage to set for the task. The minimum supported value is `20` GiB and the maximum supported value is `200` GiB.
Type: Integer
Required: No

## See Also
<a name="API_TaskEphemeralStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskEphemeralStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskEphemeralStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskEphemeralStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
