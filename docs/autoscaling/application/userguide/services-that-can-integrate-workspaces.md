---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-workspaces.html
---

# Amazon WorkSpaces and Application Auto Scaling
<a name="services-that-can-integrate-workspaces"></a>

You can scale a pool of WorkSpaces using target tracking scaling policies, step scaling policies, and scheduled scaling.

Use the following information to help you integrate WorkSpaces with Application Auto Scaling.

## Service-linked role created for WorkSpaces
<a name="integrate-service-linked-role-workspaces"></a>

Application Auto Scaling automatically creates the service-linked role named AWSServiceRoleForApplicationAutoScaling\_WorkSpacesPool in your AWS account when you register WorkSpaces resources as scalable targets with Application Auto Scaling. For more information, see [Service-linked roles for Application Auto Scaling](application-auto-scaling-service-linked-roles.md).

This service-linked role uses the managed policy AWSApplicationAutoscalingWorkSpacesPoolPolicy. This policy grants Application Auto Scaling permissions to call Amazon WorkSpaces on your behalf. For more information, see [AWSApplicationAutoscalingWorkSpacesPoolPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingWorkSpacesPoolPolicy.html) in the *AWS Managed Policy Reference*.

## Service principal used by the service-linked role
<a name="integrate-service-principal-workspaces"></a>

The service-linked role trusts the following service principal to assume the role:
+ `workspaces.application-autoscaling.amazonaws.com`

## Registering WorkSpaces pools as scalable targets with Application Auto Scaling
<a name="integrate-register-workspaces"></a>

Application Auto Scaling requires a scalable target before you can create scaling policies or scheduled actions for WorkSpaces. A scalable target is a resource that Application Auto Scaling can scale out and scale in. Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace.

If you configure auto scaling using the WorkSpaces console, then WorkSpaces automatically registers a scalable target for you.

If you want to configure auto scaling using the AWS CLI or one of the AWS SDKs, you can use the following options:
+ AWS CLI:

  Call the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command for a pool of WorkSpaces. The following example registers the target capacity of a pool of WorkSpaces using its request ID, with a minimum capacity of two virtual desktops and a maximum capacity of ten virtual desktops.

  ```
  aws application-autoscaling register-scalable-target \
    --service-namespace workspaces \
    --resource-id workspacespool/{{wspool-abcdef012}} \
    --scalable-dimension workspaces:workspacespool:DesiredUserSessions \
    --min-capacity {{2}} \
    --max-capacity {{10}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
  }
  ```
+ AWS SDK:

  Call the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) operation and provide `ResourceId`, `ScalableDimension`, `ServiceNamespace`, `MinCapacity`, and `MaxCapacity` as parameters.

## Related resources
<a name="workspaces-related-resources"></a>

For more information, see [Auto Scaling for WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/autoscaling.html) in the *Amazon WorkSpaces Administration Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
