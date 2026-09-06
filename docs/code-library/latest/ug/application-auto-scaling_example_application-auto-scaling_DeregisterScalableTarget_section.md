---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/application-auto-scaling_example_application-auto-scaling_DeregisterScalableTarget_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeregisterScalableTarget` with a CLI
<a name="application-auto-scaling_example_application-auto-scaling_DeregisterScalableTarget_section"></a>

The following code examples show how to use `DeregisterScalableTarget`.

------
#### [ CLI ]

**AWS CLI**
**To deregister a scalable target**
This example deregisters a scalable target for an Amazon ECS service called web-app that is running in the default cluster.
Command:

```
aws application-autoscaling deregister-scalable-target --service-namespace {{ecs}} --scalable-dimension {{ecs:service:DesiredCount}} --resource-id {{service/default/web-app}}
```
This example deregisters a scalable target for a custom resource. The custom-resource-id.txt file contains a string that identifies the Resource ID, which, for a custom resource, is the path to the custom resource through your Amazon API Gateway endpoint.
Command:

```
aws application-autoscaling deregister-scalable-target --service-namespace {{custom-resource}} --scalable-dimension {{custom-resource:ResourceType:Property}} --resource-id {{file://~/custom-resource-id.txt}}
```
Contents of custom-resource-id.txt file:

```
https://example.execute-api.us-west-2.amazonaws.com/prod/scalableTargetDimensions/1-23456789
```
+  For API details, see [DeregisterScalableTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/deregister-scalable-target.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet deregisters an Application Auto Scaling scalable target.Deregistering a scalable target deletes the scaling policies that are associated with it.**

```
Remove-AASScalableTarget -ResourceId fleet/MyFleet -ScalableDimension appstream:fleet:DesiredCapacity -ServiceNamespace AppStream
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-AASScalableTarget (DeregisterScalableTarget)" on target "fleet/MyFleet".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeregisterScalableTarget](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet deregisters an Application Auto Scaling scalable target.Deregistering a scalable target deletes the scaling policies that are associated with it.**

```
Remove-AASScalableTarget -ResourceId fleet/MyFleet -ScalableDimension appstream:fleet:DesiredCapacity -ServiceNamespace AppStream
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-AASScalableTarget (DeregisterScalableTarget)" on target "fleet/MyFleet".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeregisterScalableTarget](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
