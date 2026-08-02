---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeEnvironmentOrder.html
---

# ComputeEnvironmentOrder
<a name="API_ComputeEnvironmentOrder"></a>

The order that compute environments are tried in for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first. Compute environments must be in the `VALID` state before you can associate them with a job queue. All of the compute environments must be either EC2 (`EC2` or `SPOT`) or Fargate (`FARGATE` or `FARGATE_SPOT`); Amazon EC2 and Fargate compute environments can't be mixed.

**Note**
All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.

## Contents
<a name="API_ComputeEnvironmentOrder_Contents"></a>

 ** computeEnvironment **   <a name="Batch-Type-ComputeEnvironmentOrder-computeEnvironment"></a>
The Amazon Resource Name (ARN) of the compute environment.
Type: String
Required: Yes

 ** order **   <a name="Batch-Type-ComputeEnvironmentOrder-order"></a>
The order of the compute environment. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower `order` integer value is tried for job placement first.
Type: Integer
Required: Yes

## See Also
<a name="API_ComputeEnvironmentOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ComputeEnvironmentOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ComputeEnvironmentOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ComputeEnvironmentOrder)
