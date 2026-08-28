---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-hyperpod-update-using-api-cli-sdk.html
---

# Update a SageMaker HyperPod cluster on training plans using the SageMaker API, or AWS CLI
<a name="use-training-plan-for-hyperpod-update-using-api-cli-sdk"></a>

You can add, update, or remove a training plan by updating the instance group of an existing cluster using the `update-cluster` AWS CLI command. The following sample illustrates how to update a SageMaker HyperPod cluster and provide an instance group with a new training plan.

```
# Update a cluster
aws sagemaker update-cluster \
  --cluster-name {{cluster-name}} \
  --instance-groups '[ \
        { \
            "InstanceCount": {{1}},\
            "InstanceGroupName": "{{controller-nodes}}",\
            "InstanceType": "{{ml.t3.xlarge}}",\
            "LifeCycleConfig": {"SourceS3Uri": {{source_s3_uri}}, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::{{customer_account_id}}:role/{{execution_role}}",\
            "ThreadsPerCore": {{1}},\
        },\
        { \
            "InstanceCount": {{2}}, \
            "InstanceGroupName": "{{worker-nodes}}",\
            "InstanceType": "{{p4d.24xlarge}}",\
            "LifeCycleConfig": {"SourceS3Uri": {{source_s3_uri}}, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::{{customer_account_id}}}:role/{{execution_role}}}",\
            "ThreadsPerCore": {{1}},\
            "TrainingPlanArn": {{training_plan_arn}},\
        },\
        {\
            "InstanceCount": {{1}},\
            "InstanceGroupName": "{{worker-nodes-2}}",\
            "InstanceType": "{{p4d.24xlarge}}",\
            "LifeCycleConfig": {"SourceS3Uri": {{source_s3_uri}}, "OnCreate": "on_create.sh"},\
            "ExecutionRole": "arn:aws:iam::{{customer_account_id}}:role/{{execution_role}}",\
            "ThreadsPerCore": {{1}},\
            "TrainingPlanArn": {{training_plan_arn}},\
        }\
    ]'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
