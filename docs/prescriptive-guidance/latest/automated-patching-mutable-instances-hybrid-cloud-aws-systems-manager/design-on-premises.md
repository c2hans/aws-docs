---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-mutable-instances-hybrid-cloud-aws-systems-manager/design-on-premises.html
---

# Patching solution design for on-premises instances in a hybrid cloud environment
<a name="design-on-premises"></a>

You can also extend the solution described in this guide to patch on-premises server instances in a hybrid cloud environment.

The standard patching process for on-premises instances consists of two steps:
+ You configure your on-premises servers to be managed by Systems Manager. For the details of this process, see [Setting up Systems Manager for hybrid environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html) in the Systems Manager documentation.
+ You configure the appropriate **Patch Group** and **Maintenance Window** tags for these on-premises managed instances by using the AWS Command Line Interface (AWS CLI) [add-tags-to-resource command](https://docs.aws.amazon.com/cli/latest/reference/ssm/add-tags-to-resource.html).

However, this approach requires either the application team or the cloud team to manually run the AWS CLI commands whenever they want to perform changes to the patch groups or maintenance windows.

## Automated process
<a name="on-premises-auto-process"></a>

The following illustration describes an alternate approach to patching on-premises instances that uses the Systems Manager custom inventory option. This process is an extension of the automated patching solution that we described earlier for mutable Amazon EC2 instances.

![Reference architecture and workflow for patching on-premises Amazon EC2 instances.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-mutable-instances-hybrid-cloud-aws-systems-manager/images/guide-img/9c36bc8c-880d-42f7-8b76-ddf8e3d52477/images/a9a0af8c-b23c-4d0d-8743-a3f0732ae568.png)

1. Instead of using tags, Systems Manager captures the patch information (patch groups and maintenance windows) from the on-premises managed instances through a custom inventory collection.

   ```
   Sample custom inventory JSON file
   {
       "SchemaVersion": "1.0",
       "TypeName": "Custom:PatchInformation",
       "Content": {
           "Patch Group": "<APP-PROD>",
           "Maintenance Window": "XXX"
       }
   }
   ```

1. The Lambda `automate-patch` function runs every day, collects the patch group and maintenance window information from the on-premises server custom inventory, and creates the **Patch Group** and **Maintenance Window** tags on the managed instances.

1. The Lambda `automate-patch` function then creates or updates the appropriate patch groups and maintenance windows, associates the patch groups with the patch baselines, configures the patch scans, and deploys the patching task, based on the custom inventory that was gathered. Optionally, the `automate-patch` function also creates events in CloudWatch Events to notify users of impending patches.

1. Based on the maintenance windows, the events send patch notifications to the application teams with the details of the impending patching operation.

1. Patch Manager performs system patching based on the defined schedule and the patch groups.

1. A resource data sync in Systems Manager Inventory gathers the patching details and publishes them to an Amazon S3 bucket.

1. Patch compliance reporting and dashboards are built in Quick from the Amazon S3 bucket information.

## Architectural considerations and limitations
<a name="on-premises-considerations"></a>

As discussed in the previous sections, there are two approaches to patching on-premises instances: through custom inventory or by using tags. Here are the advantages and disadvantages of each approach.

### Option 1. Use custom inventory for patch information
<a name="option-1.-use-custom-inventory-for-patch-information.51a4639a-ef1c-5eb4-afce-6c1fd9986e99"></a>
+ Application teams working with on-premises servers configure the patch information in the custom inventory file, and Systems Manager picks that information.
+ The custom inventory patch information is then used to create the patch tasks.

Pros:
+ Much simpler to configure because it involves only a file update.

Cons:
+ The changes to the patch configuration are limited to the inventory collection schedule.

### Option 2. Use tags for on-premises managed instances
<a name="option-2.-use-tags-for-on-premises-managed-instances.0017e434-7509-5570-9094-e4f18ee5859a"></a>
+ Application teams working with on-premises servers create **Patch Group** and **Maintenance Window** tags by using AWS CLI with the appropriate patch information.
+ The tag information is used to create the patch tasks.

Pros:
+ Consistent approach across AWS and on premises to drive patching standardization and automation.

Cons:
+ Application teams working with on-premises instances have to learn and use AWS CLI to create or update the tags.
