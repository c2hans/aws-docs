---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-change-tenancy.html
---

# Change the tenancy of an EC2 instance
<a name="dedicated-change-tenancy"></a>

You can change the tenancy of a stopped instance after launch. The changes that you make take effect the next time the instance starts.

Alternatively, you can change the tenancy of your virtual private cloud (VPC). For more information, see [Change the instance tenancy of a VPC](change-tenancy-vpc.md).

**Limitations**
+ You can't change the tenancy of an instance using the AWS Management Console.
+ The instance must be in the `stopped` state.
+ The operating system details of your instance—and whether SQL Server is installed—affect what conversions are supported. For more information about the tenancy conversion paths available to your instance, see [Tenancy conversion](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-tenancy.html) in the *License Manager User Guide*.
+ For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of `host`. You can't change the tenancy from `host` to `dedicated` or `default`. Attempting to make one of these unsupported tenancy changes results in an `InvalidRequest` error code.

------
#### [ AWS CLI ]

**To modify the tenancy value of an instance**
Use the [ modify-instance-placement](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-placement.html) command.

```
aws ec2 modify-instance-placement \
    --instance-id {{i-1234567890abcdef0}} \
    --tenancy {{dedicated}}
```

------
#### [ PowerShell ]

**To modify the tenancy value of an instance**
Use the [ Edit-EC2InstancePlacement](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstancePlacement.html) cmdlet.

```
Edit-EC2InstancePlacement `
    -InstanceId {{i-1234567890abcdef0}} `
    -Tenancy {{Dedicated}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
