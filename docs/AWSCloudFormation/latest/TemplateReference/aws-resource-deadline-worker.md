---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-worker.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Worker
<a name="aws-resource-deadline-worker"></a>

Creates a worker. A worker tells your instance how much processing power (vCPU), and memory (GiB) you’ll need to assemble the digital assets held within a particular instance. You can specify certain instance types to use, or let the worker know which instances types to exclude.

Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to `CreateWorker` before the field updates, you might exceed your fleet's maximum worker count. For example, if your `maxWorkerCount` is 10 and you currently have 9 workers, making two quick `CreateWorker` calls might successfully create 2 workers instead of 1, resulting in 11 total workers.

## Syntax
<a name="aws-resource-deadline-worker-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-worker-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Worker",
  "Properties" : {
      "[FarmId](#cfn-deadline-worker-farmid)" : {{String}},
      "[FleetId](#cfn-deadline-worker-fleetid)" : {{String}},
      "[HostProperties](#cfn-deadline-worker-hostproperties)" : {{HostPropertiesRequest}},
      "[Tags](#cfn-deadline-worker-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-deadline-worker-syntax.yaml"></a>

```
Type: AWS::Deadline::Worker
Properties:
  [FarmId](#cfn-deadline-worker-farmid): {{String}}
  [FleetId](#cfn-deadline-worker-fleetid): {{String}}
  [HostProperties](#cfn-deadline-worker-hostproperties): {{
    HostPropertiesRequest}}
  [Tags](#cfn-deadline-worker-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-deadline-worker-properties"></a>

`FarmId`  <a name="cfn-deadline-worker-farmid"></a>
The farm ID.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FleetId`  <a name="cfn-deadline-worker-fleetid"></a>
The fleet ID.
*Required*: Yes
*Type*: String
*Pattern*: `^fleet-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostProperties`  <a name="cfn-deadline-worker-hostproperties"></a>
The host properties of the worker.
*Required*: No
*Type*: [HostPropertiesRequest](aws-properties-deadline-worker-hostpropertiesrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-deadline-worker-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-deadline-worker-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-worker-return-values"></a>

### Ref
<a name="aws-resource-deadline-worker-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-deadline-worker-return-values-fn--getatt"></a>

####
<a name="aws-resource-deadline-worker-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the resource was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The user or system that created this resource.

`Status`  <a name="Status-fn::getatt"></a>
The status of the worker.

`WorkerId`  <a name="WorkerId-fn::getatt"></a>
The worker ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
