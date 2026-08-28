---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.html
---

# Optimize costs for AWS Fargate tasks on Amazon ECS
<a name="optimizer-ecs-fargate"></a>

## Overview
<a name="optimizer-ecs-fargate-overview"></a>

Right sizing AWS Fargate tasks is an important step for cost optimization. Too often, applications are built with arbitrary sizing for Fargate tasks and never revisited. This can cause overprovisioning of Fargate tasks and unnecessary spending. This section shows you how to use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to deliver actionable recommendations so you can optimize task CPU and memory for your Amazon Elastic Container Service (Amazon ECS) services running on Fargate. Compute Optimizer also quantifies the cost impact of adopting these recommendations. This enables you to prioritize your optimization efforts based on the size of the savings opportunity. Compute Optimizer recommendations provide container-level CPU and memory configurations for downsizing tasks.

## Cost benefits
<a name="optimizer-ecs-fargate-cost-benefits"></a>

Right sizing Amazon ECS tasks on Fargate can reduce costs by 30–70 percent for long running tasks. Without reviewing application performance metrics to right size your task size, you can apply the same mindset used on EC2 compute instances to container sizing. This leads to oversized Fargate tasks that increase costs for idle resources. You can use Compute Optimizer to surface the right sizing opportunities reactively. Ideally, the application owner reviews the specific application performance metrics and removes the operating system overhead to ensure the proper task size is specified. For more information, see the [Move Windows applications to containers](windows-containers-main.md) section of this guide.

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
<a name="enable-9999999999999999co-.179eb0c7-a8a3-5c28-9efa-b2bbf2451a79"></a>

You can enable [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html#account-opt-in) at the organization or single account level in AWS Organizations. The organization-wide configuration provides ongoing reports for new and existing instances across your entire fleet for all member accounts. This enables right sizing to be a recurring activity instead of a point-in-time activity.

#### Organization level
<a name="organization-level.60eb2b86-ca85-5f69-bda6-82791b9a6a43"></a>

For most organizations, the most efficient way to use Compute Optimizer is at the organization level. This provides multi-account and multi-Region visibility into your organization and centralizes the data into one source for review. To enable this at the organization level, do the following:

1. Sign in to your [AWS Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) with a role that has the [required permissions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) and choose to opt in for all accounts within this organization. Your organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).

1. After you enable the management account, you can sign in to the account, see all other member accounts, and browse their recommendations.

|
|
| Note: It's a best practice to configure a [delegated administrator account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/delegate-administrator-account.html) for Compute Optimizer. This enables you to exercise the principle of least privilege, minimizing access to the AWS Organizations management account while still providing access to the organization-wide service. |
| --- |

#### Single account level
<a name="single-account-level.c92fa313-6443-55e4-8c55-b3a9be8d0cf5"></a>

If you're targeting an account with high costs but don't have access to AWS Organizations, you can still enable Compute Optimizer for that account and Region. To learn about the opt-in process, see [Getting started with AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html).

|
|
| Note: The recommendations are refreshed daily and they can take up to 12 hours to generate. Keep in mind that Compute Optimizer requires 24 hours of metrics in the past 14 days to generate recommendations for Amazon ECS on Fargate. For more information, see [Requirements for Amazon ECS services on Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ecs-fargate) in the Compute Optimizer documentation. |
| --- |

Compute Optimizer automatically analyzes the following Amazon CloudWatch and Amazon ECS utilization metrics for your Amazon ECS services on Fargate:
+ `CPUUtilization` – The percentage of CPU capacity that's used in the service.
+ `MemoryUtilization` – The percentage of memory that's used in the service.

### Consume Compute Optimizer results
<a name="consume-9999999999999999co--results.38cb2a7a-88da-54ee-8037-116a2ff9af5a"></a>

Consider an example that focuses on making right sizing changes within a single account and single Region. In this example, Compute Optimizer is enabled at the organization level across all accounts. Keep in mind that right sizing is a disruptive process that in most cases is carried out with precision by the application owners during a scheduled maintenance window over several weeks.

If you navigate to Compute Optimizer from within an organization's management account (as shown in the following steps), you can choose the account that you want to investigate. In this example, one task is running in a single account that's overprovisioned in `us-east-1`. The focus is on resizing to the recommended size for the Amazon ECS service.

1. Open the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/).

1. On the **Dashboard** page, filter by **Findings=Over-provisioned** to see all the Amazon ECS services on Fargate.

1. To review detailed recommendations for **Over-provisioned ECS services on Fargate**,** **scroll down and then choose **View recommendations**.

1. Choose **Export** and save the file for future use.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.html)

To see recommendations from Compute Optimizer, do the following:

1. In the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/), go the **Export recommendations** page.

1. For **S3 bucket destination**, choose your S3 bucket.

1. In the **Export filters** section, for **Resource type**, choose **ECS services on Fargate**.

1. On the **Recommendations for ECS services on Fargate** page, drill into one of the ECS services on Fargate and see the CPU and memory recommendations from Compute Optimizer. For example, review the recommendations in the **Compare current settings with recommend task size** and **Compare current settings with recommended container size** sections.

To get the list of ECS services for Fargate that you need to right size, do the following:

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Buckets**, and then choose the bucket where you exported your results.

1. On the **Objects** tab, select your object and choose **Download**.

1. In your downloaded results, filter the finding column to show only **OVER\_PROVISIONED** Amazon ECS services on Fargate. This shows the Amazon ECS services that you plan to target for right sizing.

1. Store the task definitions in a text editor for use later.

### Right sizing tag tasks
<a name="right-sizing-tag-tasks.ae94e30a-6fc2-5d9a-b194-d4406fb44bac"></a>

Tagging your workloads is a powerful tool for organizing your resources in AWS. You can use tags to gain fine-grain visibility into costs and enable chargeback. There are many methods and strategies for adding tags to AWS resources to handle chargeback and automation. For more information, see the AWS Whitepaper [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). The following example uses [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home) to tag all the tasks that are part of any Amazon ECS service within the target account and AWS Region.

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
<a name="enable-the-cost-allocation-tag-to-work-with-9999999999999999aws--billing-tools.3a087579-7e20-5a40-8889-26e86881e7d0"></a>

We recommend activating the user-defined cost allocation tag. This enables the **Rightsizing **tag to be recognized and filterable in the AWS billing tools (for example, AWS Cost Explorer and AWS Cost and Usage Report). If you don't enable this, the tag filtering option and data won't be available. For information about using cost allocation tags, see [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the AWS Billing and Cost Management documentation.

After waiting for 24 hours, you can see the tag in Cost Explorer before implementing right sizing recommendations in the next section. To do this, search for the **Rightsizing** tag in Cost Explorer.

### Implement right sizing recommendations
<a name="implement-right-sizing-recommendations.30ec0a97-8796-55c6-8f41-dc62a78b923d"></a>

Compute Optimizer will provide either task or container size recommendations. To implement right sizing recommendations, do the following.

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

For advanced operators, you could use CloudShell to update the Amazon ECS service. For example:

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
<a name="review-before-and-after-costs.2bf1fc79-de8c-59a5-8e54-99486b5ffe95"></a>

After you have right sized your resources, you can use Cost Explorer to show before and after costs by using the **Rightsizing** tag. Recall that you can use [resource tags](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) to track costs. By using several layers of tags, you can achieve granular visibility into your costs. In the example covered in this guide, the **Rightsizing** tag is used to apply a generic tag to all targeted instances. Then, a **team** tag is used to further organize resources. The next step is to introduce application tags to further show the cost impact for operating a specific application.

Consider an example of the cost reduction that can be achieved by using the **Rightsizing** tag for a single account level. In this example, operating costs go from $30.26 per day to $7.56 per day. Assuming 744 hours per month, the annual cost before right sizing is $11,044.9. After right sizing, the annual cost drops to $2,759.4. This translates to a 75 percent decrease in compute costs for this account. Imagine the impact of this across a large organization.

Before embarking on your right sizing journey, consider the following:
+ AWS offers many options for cost reduction. This includes [AWS OLA](https://aws.amazon.com/optimization-and-licensing-assessment/), where AWS reviews your on-premises instances prior to moving to AWS. The AWS OLA also provides you with right-sizing recommendations and licensing guidance.
+ Complete all of your right sizing before purchasing [Savings Plans](https://aws.amazon.com/savingsplans/). This can help you avoid over purchases on your Savings Plans commitment.

## Next steps
<a name="optimizer-ecs-fargate-next-steps"></a>

We recommend the following next steps:

1. Review your existing landscape and consider converting Amazon EBS gp2 volumes to gp3 volumes.

1. Review [Savings Plans](https://aws.amazon.com/savingsplans/).

## Additional resources
<a name="optimizer-ecs-fargate-resources"></a>
+ [Getting started with Compute Optimizer](https://aws.amazon.com/compute-optimizer/getting-started/) (AWS documentation)
+ [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) (AWS Whitepapers)
+ [Windows Containers on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/1de8014a-d598-4cb5-a119-801576492564/en-US) (AWS Workshop Studio)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
