---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-warm-pools-aws-cli.html
---

# Examples for creating and managing warm pools with the AWS CLI
<a name="examples-warm-pools-aws-cli"></a>

You can create and manage warm pools using the AWS Management Console, AWS Command Line Interface (AWS CLI), or SDKs.

The following examples show you how to create and manage warm pools using the AWS CLI.

**Topics**
+ [Example 1: Keep instances in the `Stopped` state](#warm-pool-configuration-ex1)
+ [Example 2: Keep instances in the `Running` state](#warm-pool-configuration-ex2)
+ [Example 3: Keep instances in the `Hibernated` state](#warm-pool-configuration-ex3)
+ [Example 4: Return instances to the warm pool when scaling in](#warm-pool-configuration-ex4)
+ [Example 5: Specify the minimum number of instances in the warm pool](#warm-pool-configuration-ex5)
+ [Example 6: Define the warm pool size using a custom specification](#warm-pool-configuration-ex6)
+ [Example 7: Define an absolute warm pool size](#warm-pool-configuration-ex7)
+ [Example 8: Delete a warm pool](#delete-warm-pool-cli)

## Example 1: Keep instances in the `Stopped` state
<a name="warm-pool-configuration-ex1"></a>

The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool that keeps instances in a `Stopped` state.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state Stopped
```

## Example 2: Keep instances in the `Running` state
<a name="warm-pool-configuration-ex2"></a>

The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool that keeps instances in a `Running` state instead of a `Stopped` state.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state Running
```

## Example 3: Keep instances in the `Hibernated` state
<a name="warm-pool-configuration-ex3"></a>

The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool that keeps instances in a `Hibernated` state instead of a `Stopped` state. This lets you stop instances without deleting their memory contents (RAM).

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state Hibernated
```

## Example 4: Return instances to the warm pool when scaling in
<a name="warm-pool-configuration-ex4"></a>

The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool that keeps instances in a `Stopped` state and includes the `--instance-reuse-policy` option. The instance reuse policy value `'{"ReuseOnScaleIn": true}'` tells Amazon EC2 Auto Scaling to return instances to the warm pool when your Auto Scaling group scales in.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state {{Stopped}} --instance-reuse-policy '{"ReuseOnScaleIn": true}'
```

## Example 5: Specify the minimum number of instances in the warm pool
<a name="warm-pool-configuration-ex5"></a>

The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool that maintains a minimum of 4 instances, so that there are at least 4 instances available to handle traffic spikes.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state {{Stopped}} --min-size {{4}}
```

## Example 6: Define the warm pool size using a custom specification
<a name="warm-pool-configuration-ex6"></a>

By default, Amazon EC2 Auto Scaling manages the size of your warm pool as the difference between the maximum and desired capacity of the Auto Scaling group. However, you can manage the size of the warm pool independently from the group's maximum capacity by using the `--max-group-prepared-capacity` option.

The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool and sets the maximum number of instances that can exist concurrently in both the warm pool and Auto Scaling group. If the group has a desired capacity of 800, the warm pool will initially have a size of 100 as it initializes after running this command.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state {{Stopped}} --max-group-prepared-capacity {{900}}
```

To maintain a minimum number of instances in the warm pool, include the `--min-size` option with the command, as follows.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state {{Stopped}} --max-group-prepared-capacity {{900}} --min-size {{25}}
```

## Example 7: Define an absolute warm pool size
<a name="warm-pool-configuration-ex7"></a>

If you set the same values for the `--max-group-prepared-capacity` and `--min-size` options, the warm pool has an absolute size. The following [put-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html) example creates a warm pool that maintains a constant warm pool size of 10 instances.

```
aws autoscaling put-warm-pool --auto-scaling-group-name {{my-asg}} /
  --pool-state {{Stopped}} --min-size {{10}} --max-group-prepared-capacity {{10}}
```

## Example 8: Delete a warm pool
<a name="delete-warm-pool-cli"></a>

Use the following [delete-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-warm-pool.html) command to delete a warm pool.

```
aws autoscaling delete-warm-pool --auto-scaling-group-name {{my-asg}}
```

If there are instances in the warm pool, or if scaling activities are in progress, use the [delete-warm-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-warm-pool.html) command with the `--force-delete` option. This option also terminates the Amazon EC2 instances and any outstanding lifecycle actions.

```
aws autoscaling delete-warm-pool --auto-scaling-group-name {{my-asg}} --force-delete
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
