---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.html
---

# Optimize costs for AWS Fargate tasks on Amazon ECS
<a name="optimizer-ecs-fargate"></a>

## Overview
<a name="optimizer-ecs-fargate-overview"></a>

Rightsizing AWS Fargate tasks is an important step for cost optimization. Teams often build applications with arbitrary sizing for Fargate tasks and never revisit it. This can cause overprovisioning of Fargate tasks and unnecessary spending.

## Cost benefits
<a name="optimizer-ecs-fargate-cost-benefits"></a>

Right-sizing Amazon ECS tasks on Fargate can help reduce costs for long-running tasks. If you don't review application performance metrics to right-size your tasks, you might apply the same approach that you use for EC2 instances to container sizing. This can lead to oversized Fargate tasks that increase costs for idle resources. You can use Compute Optimizer to identify right-sizing opportunities reactively. Ideally, the application owner reviews the specific application performance metrics and removes the operating system overhead to help specify the appropriate task size. For more information, see the [Move Windows applications to containers](windows-containers-main.md) section of this guide.

## Cost optimization recommendations
<a name="optimizer-ecs-fargate-rec"></a>

This section offers recommendations for using Compute Optimizer to right size your Amazon ECS on Fargate tasks.

As part of the cost-optimization process, we recommend that you do the following:
+ Enable Compute Optimizer
+ Consume Compute Optimizer results
+ Tag tasks to be right sized
+ Enable the cost allocation tag to work with AWS billing tools
+ Implement right sizing recommendations
+ Review before and after costs in Cost Explorer

### Enable Compute Optimizer
<a name="enable-9999999999999999co-.e710b7f7-f34d-575e-940b-22da277728e8"></a>

You can enable [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html#account-opt-in) at the organization or single account level in AWS Organizations. The organization-wide configuration provides ongoing reports for new and existing instances across your entire fleet for all member accounts. This enables right sizing to be a recurring activity instead of a point-in-time activity.

#### Organization level
<a name="organization-level.e8cd382e-b0e6-5b9a-8954-6d18f990ca38"></a>

For most organizations, an efficient way to use Compute Optimizer is at the organization level. This provides multi-account and multi-Region visibility into your organization and centralizes the data into one source for review. To enable this at the organization level, do the following:

1. Sign in to your [AWS Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) with a role that has the [required permissions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) and choose to opt in for all accounts within this organization. Your organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).

1. After you enable the management account, you can sign in to the account, see all other member accounts, and browse their recommendations.

|
|
| Note: It's a best practice to configure a [delegated administrator account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/delegate-administrator-account.html) for Compute Optimizer. This enables you to exercise the principle of least privilege, minimizing access to the AWS Organizations management account while still providing access to the organization-wide service. |
| --- |

#### Single account level
<a name="single-account-level.ea5f5862-5efa-51c9-85ad-e4fe7bc71a58"></a>

If you're targeting an account with high costs but don't have access to AWS Organizations, you can still enable Compute Optimizer for that account and Region. To learn about the opt-in process, see [Getting started with AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html).

|
|
| Note: The recommendations are refreshed daily and they can take up to 12 hours to generate. Keep in mind that Compute Optimizer requires 24 hours of metrics in the past 14 days to generate recommendations for Amazon ECS on Fargate. For more information, see [Requirements for Amazon ECS services on Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ecs-fargate) in the Compute Optimizer documentation. |
| --- |

Compute Optimizer automatically analyzes the following Amazon CloudWatch and Amazon ECS utilization metrics for your Amazon ECS services on Fargate:
+ `CPUUtilization` – The percentage of CPU capacity that's used in the service.
+ `MemoryUtilization` – The percentage of memory that's used in the service.

### Consume Compute Optimizer results
<a name="consume-9999999999999999co--results.30f246e4-05ff-5b19-9136-c486e1bfc3b9"></a>

Consider an example that focuses on making right sizing changes within a single account and single Region. In this example, you enable Compute Optimizer at the organization level across all accounts. Keep in mind that right sizing can be disruptive. Application owners typically perform it during a scheduled maintenance window over several weeks.

If you navigate to Compute Optimizer from within an organization's management account (as shown in the following steps), you can choose the account that you want to investigate. In this example, one task is running in a single account that's overprovisioned in `us-east-1`. The focus is on resizing to the recommended size for the Amazon ECS service.

1. Open the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/).

1. On the **Dashboard** page, filter by **Findings=Over-provisioned** to see all the Amazon ECS services on Fargate.

1. To review detailed recommendations for **Over-provisioned ECS services on Fargate**,** **scroll down and then choose **View recommendations**.

1. Choose **Export** and save the file for future use.

<table>
<tbody>
</tbody>
</table>

To see recommendations from Compute Optimizer, do the following:

1. In the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/), go to the **Export recommendations** page.

1. For **S3 bucket destination**, choose your S3 bucket.

1. In the **Export filters** section, for **Resource type**, choose **ECS services on Fargate**.

1. On the **Recommendations for ECS services on Fargate** page, drill into one of the ECS services on Fargate and see the CPU and memory recommendations from Compute Optimizer. For example, review the recommendations in the **Compare current settings with recommend task size** and **Compare current settings with recommended container size** sections.

To get the list of Amazon ECS services for Fargate that you need to right size, do the following:

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Buckets**, and then choose the bucket where you exported your results.

1. On the **Objects** tab, select your object and choose **Download**.

1. In your downloaded results, filter the finding column to show only **OVER\_PROVISIONED** Amazon ECS services on Fargate. This shows the Amazon ECS services that you plan to target for right sizing.

1. Store the task definitions in a text editor for use later.

### Tag tasks to be right sized
<a name="tag-tasks-to-be-right-sized.2ffa13da-b5f8-5052-aa4c-748f8be79998"></a>

Tagging your workloads helps you organize your resources in AWS. You can use tags to gain fine-grained visibility into costs and enable chargeback. There are many methods and strategies for adding tags to AWS resources to handle chargeback and automation. For more information, see the AWS Whitepaper [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). The following example uses [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home) to tag all the tasks that are part of any Amazon ECS service within the target account and AWS Region.

```
#!/bin/bash
# Set variables
TAG_KEY="rightsizing"
TAG_VALUE="enabled"
# Get a list of ECS Clusters
ClustersArns=$( w secs list-clusters –query 'clusterArns' –output text)
for ClustersArn in $ClustersArns; do
 ServiceArns=$( w secs list-services –cluster $ClustersArn –query 'serviceArns' –output text)
 for ServiceArn in $ServiceArns; do
  TasksArns=$( w secs list-tasks –cluster $ClustersArn –service-name $ServiceArn –query 'taskArns' –output text)
  for TasksArn in $TasksArns; do
    w secs tag-resource –resource-arn $TasksArn –tags key=$TAG_KEY,value=$TAG_VALUE
  done
 done
done
```

The following code example shows how to enable [tag propagation](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html#ECS-UpdateService-request-propagateTags) to all Amazon ECS services.

```
#!/bin/bash
# Set variables
TAG_KEY="rightsizing"
TAG_VALUE="enabled"
# Get a list of ECS Clusters
ClustersArns=$(aws ecs list-clusters --query 'clusterArns' --output text)
for ClustersArn in $ClustersArns; do
 ServiceArns=$(aws ecs list-services --cluster $ClustersArn --query 'serviceArns' --output text)
 for ServiceArn in $ServiceArns; do
  aws ecs update-service --cluster $ClustersArn --service $ServiceArn --propagate-tags SERVICE &>/dev/null
  aws ecs tag-resource --resource-arn $ServiceArn --tags key=$TAG_KEY,value=$TAG_VALUE
 done
done
```

### Enable the cost allocation tag to work with AWS billing tools
<a name="enable-the-cost-allocation-tag-to-work-with-9999999999999999aws--billing-tools.8c6543e5-6281-5622-89dd-0ff2ecf52142"></a>

We recommend activating the user-defined cost allocation tag. This enables the **Rightsizing **tag to be recognized and filterable in the AWS billing tools (for example, AWS Cost Explorer and AWS Cost and Usage Report). If you don't enable this, the tag filtering option and data won't be available. For information about using cost allocation tags, see [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the AWS Billing and Cost Management documentation.

After waiting for 24 hours, you can see the tag in Cost Explorer before implementing right sizing recommendations in the next section. To do this, search for the **Rightsizing** tag in Cost Explorer.

### Implement right sizing recommendations
<a name="implement-right-sizing-recommendations.8376ad61-3973-5be6-9ec4-2354283d378d"></a>

Compute Optimizer provides either task or container size recommendations. To implement right sizing recommendations, do the following:

1. Open the [Amazon ECS console](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, choose the Region that contains your task definition.

1. In the navigation pane, choose **Task definitions**.

1. On the **Task definitions** page, choose the task, and then choose **Create new revision**.

1. On the **Create new task definition revision** page, make changes. To update the container size recommendation, update `cpu` and `memory` under the **containerDefinitions** block in your [ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size). For example:

   ```
   "containerDefinitions": [
   	{
   		"name": "your-container-name",
   		"image": "your-image",
   		"cpu": 1024,
   		"memory": 2048,
   	}
   ],
   ```

1. Verify the information, and then choose **Create**.

To update the Amazon ECS service, do the following:

1. Open the [Amazon ECS console](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, select the cluster.

1. On the **Cluster overview** page, select the service, and then choose **Update**.

1. For **Task definition**, choose the task definition family and revision to use.

If you prefer to use the command line, you can use CloudShell to update the Amazon ECS service. For example:

```
bash
#!/bin/bash
# Set variables
ClustersName="workshop-cluster"
ServiceName="lab7-fargate-service"
TaskDefinition="lab7-fargate-demo:3"
# update the service
aws ecs update-service --cluster $ClustersName --service $ServiceName --task-definition $TaskDefinition
```

### Review before and after costs
<a name="review-before-and-after-costs.c68f848d-03c8-5bfc-b32d-9a3da475409d"></a>

After you have right sized your resources, you can use Cost Explorer to show before and after costs by using the **Rightsizing** tag. Recall that you can use [resource tags](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) to track costs. By using several layers of tags, you can achieve granular visibility into your costs. In the example covered in this guide, the **Rightsizing** tag is used to apply a generic tag to all targeted instances. Then, a **team** tag is used to further organize resources. The next step is to introduce application tags to further show the cost impact for operating a specific application.

Consider an example of the cost reduction that you can measure by using the **Rightsizing** tag for a single account. In this example, operating costs go from $30.26 per day to $7.56 per day. The annual cost before right sizing is $11,044.90. After right sizing, the annual cost drops to $2,759.40. This translates to a 75 percent decrease in compute costs for this account. Actual savings vary based on your workloads and usage.

Before you start right sizing, consider the following:
+ AWS offers many options for cost reduction, including the [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/). With AWS OLA, AWS reviews your on-premises instances before you move to AWS. AWS OLA also provides right sizing recommendations and licensing guidance.
+ Complete all of your right sizing before you purchase [Savings Plans](https://aws.amazon.com/savingsplans/). This can help you avoid overpurchasing on your Savings Plans commitment.

## Next steps
<a name="optimizer-ecs-fargate-next-steps"></a>

We recommend the following next steps:

1. Review your existing volumes and consider converting [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) gp2 volumes to gp3 volumes.

1. Review [Savings Plans](https://aws.amazon.com/savingsplans/).

## Additional resources
<a name="optimizer-ecs-fargate-resources"></a>
+ [Getting started with Compute Optimizer](https://aws.amazon.com/compute-optimizer/getting-started/) (AWS documentation)
+ [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) (AWS Whitepapers)
+ [Windows Containers on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/1de8014a-d598-4cb5-a119-801576492564/en-US) (AWS Workshop Studio)
