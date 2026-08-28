---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-appstream.html
---

# Amazon WorkSpaces Applications and Application Auto Scaling
<a name="services-that-can-integrate-appstream"></a>

You can scale WorkSpaces Applications fleets using target tracking scaling policies, step scaling policies, and scheduled scaling.

Use the following information to help you integrate WorkSpaces Applications with Application Auto Scaling.

## Service-linked role created for WorkSpaces Applications
<a name="integrate-service-linked-role-appstream"></a>

The following service-linked role is automatically created in your AWS account when registering WorkSpaces Applications resources as scalable targets with Application Auto Scaling. This role allows Application Auto Scaling to perform supported operations within your account. For more information, see [Service-linked roles for Application Auto Scaling](application-auto-scaling-service-linked-roles.md).
+ `AWSServiceRoleForApplicationAutoScaling_AppStreamFleet`

## Service principal used by the service-linked role
<a name="integrate-service-principal-appstream"></a>

The service-linked role in the previous section can be assumed only by the service principal authorized by the trust relationships defined for the role. The service-linked role used by Application Auto Scaling grants access to the following service principal:
+ `appstream.application-autoscaling.amazonaws.com`

## Registering WorkSpaces Applications fleets as scalable targets with Application Auto Scaling
<a name="integrate-register-appstream"></a>

Application Auto Scaling requires a scalable target before you can create scaling policies or scheduled actions for an WorkSpaces Applications fleet. A scalable target is a resource that Application Auto Scaling can scale out and scale in. Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace.

If you configure auto scaling using the WorkSpaces Applications console, then WorkSpaces Applications automatically registers a scalable target for you.

If you want to configure auto scaling using the AWS CLI or one of the AWS SDKs, you can use the following options:
+ AWS CLI:

  Call the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command for an WorkSpaces Applications fleet. The following example registers the desired capacity of a fleet called `sample-fleet`, with a minimum capacity of one fleet instance and a maximum capacity of five fleet instances.

  ```
  aws application-autoscaling register-scalable-target \
     --service-namespace appstream \
     --scalable-dimension appstream:fleet:DesiredCapacity \
     --resource-id fleet/{{sample-fleet}} \
     --min-capacity {{1}} \
     --max-capacity {{5}}
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
<a name="appstream-related-resources"></a>

For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html) in the *Amazon WorkSpaces Applications Administration Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
