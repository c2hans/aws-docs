---
source_url: https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsEphemeralStorage.html
---

# EcsEphemeralStorage
<a name="API_EcsEphemeralStorage"></a>

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see [Fargate task storage](https://docs.aws.amazon.com/AmazonECS/latest/userguide/using_data_volumes.html) in the *Amazon ECS User Guide for Fargate*.

**Note**
This parameter is only supported for tasks hosted on Fargate using Linux platform version `1.4.0` or later. This parameter is not supported for Windows containers on Fargate.

## Contents
<a name="API_EcsEphemeralStorage_Contents"></a>

 ** sizeInGiB **   <a name="eventbridge-Type-EcsEphemeralStorage-sizeInGiB"></a>
The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.
Type: Integer
Valid Range: Minimum value of 21. Maximum value of 200.
Required: Yes

## See Also
<a name="API_EcsEphemeralStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/EcsEphemeralStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/EcsEphemeralStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/EcsEphemeralStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge Pipes. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
