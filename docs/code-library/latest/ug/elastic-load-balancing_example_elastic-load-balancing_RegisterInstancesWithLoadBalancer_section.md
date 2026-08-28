---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_RegisterInstancesWithLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RegisterInstancesWithLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_RegisterInstancesWithLoadBalancer_section"></a>

The following code examples show how to use `RegisterInstancesWithLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To register instances with a load balancer**
This example registers the specified instance with the specified load balancer.
Command:

```
aws elb register-instances-with-load-balancer --load-balancer-name {{my-load-balancer}} --instances {{i-d6f6fae3}}
```
Output:

```
{
   "Instances": [
       {
           "InstanceId": "i-d6f6fae3"
       },
       {
           "InstanceId": "i-207d9717"
       },
       {
           "InstanceId": "i-afefb49b"
       }
   ]
}
```
+  For API details, see [RegisterInstancesWithLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/register-instances-with-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example registers the specified EC2 instance with the specified load balancer.**

```
Register-ELBInstanceWithLoadBalancer -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Output:**

```
InstanceId
----------
i-12345678
i-87654321
```
+  For API details, see [RegisterInstancesWithLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example registers the specified EC2 instance with the specified load balancer.**

```
Register-ELBInstanceWithLoadBalancer -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Output:**

```
InstanceId
----------
i-12345678
i-87654321
```
+  For API details, see [RegisterInstancesWithLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
