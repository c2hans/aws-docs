---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DeregisterInstancesFromLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeregisterInstancesFromLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DeregisterInstancesFromLoadBalancer_section"></a>

The following code examples show how to use `DeregisterInstancesFromLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To deregister instances from a load balancer**
This example deregisters the specified instance from the specified load balancer.
Command:

```
aws elb deregister-instances-from-load-balancer --load-balancer-name {{my-load-balancer}} --instances {{i-d6f6fae3}}
```
Output:

```
{
    "Instances": [
        {
            "InstanceId": "i-207d9717"
        },
        {
            "InstanceId": "i-afefb49b"
        }
    ]
}
```
+  For API details, see [DeregisterInstancesFromLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/deregister-instances-from-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the specified EC2 instance from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBInstanceFromLoadBalancer -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBInstanceFromLoadBalancer (DeregisterInstancesFromLoadBalancer)" on Target
"Amazon.ElasticLoadBalancing.Model.Instance".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):

InstanceId
----------
i-87654321
```
+  For API details, see [DeregisterInstancesFromLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the specified EC2 instance from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBInstanceFromLoadBalancer -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBInstanceFromLoadBalancer (DeregisterInstancesFromLoadBalancer)" on Target
"Amazon.ElasticLoadBalancing.Model.Instance".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):

InstanceId
----------
i-87654321
```
+  For API details, see [DeregisterInstancesFromLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
