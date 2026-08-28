---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksAttemptDetail.html
---

# EksAttemptDetail
<a name="API_EksAttemptDetail"></a>

An object that represents the details of a job attempt for a job attempt by an Amazon EKS container.

## Contents
<a name="API_EksAttemptDetail_Contents"></a>

 ** containers **   <a name="Batch-Type-EksAttemptDetail-containers"></a>
The details for the final status of the containers for this job attempt.
Type: Array of [EksAttemptContainerDetail](API_EksAttemptContainerDetail.md) objects
Required: No

 ** eksClusterArn **   <a name="Batch-Type-EksAttemptDetail-eksClusterArn"></a>
The Amazon Resource Name (ARN) of the Amazon EKS cluster.
Type: String
Required: No

 ** initContainers **   <a name="Batch-Type-EksAttemptDetail-initContainers"></a>
The details for the init containers.
Type: Array of [EksAttemptContainerDetail](API_EksAttemptContainerDetail.md) objects
Required: No

 ** nodeName **   <a name="Batch-Type-EksAttemptDetail-nodeName"></a>
The name of the node for this job attempt.
Type: String
Required: No

 ** podName **   <a name="Batch-Type-EksAttemptDetail-podName"></a>
The name of the pod for this job attempt.
Type: String
Required: No

 ** podNamespace **   <a name="Batch-Type-EksAttemptDetail-podNamespace"></a>
The namespace of the Amazon EKS cluster that the pod exists in.
Type: String
Required: No

 ** startedAt **   <a name="Batch-Type-EksAttemptDetail-startedAt"></a>
The Unix timestamp (in milliseconds) for when the attempt was started (when the attempt transitioned from the `STARTING` state to the `RUNNING` state).
Type: Long
Required: No

 ** statusReason **   <a name="Batch-Type-EksAttemptDetail-statusReason"></a>
A short, human-readable string to provide additional details for the current status of the job attempt.
Type: String
Required: No

 ** stoppedAt **   <a name="Batch-Type-EksAttemptDetail-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the attempt was stopped. This happens when the attempt transitioned from the `RUNNING` state to a terminal state, such as `SUCCEEDED` or `FAILED`.
Type: Long
Required: No

## See Also
<a name="API_EksAttemptDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksAttemptDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksAttemptDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksAttemptDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
