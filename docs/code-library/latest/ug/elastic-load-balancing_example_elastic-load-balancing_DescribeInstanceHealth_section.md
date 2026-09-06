---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DescribeInstanceHealth_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeInstanceHealth` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DescribeInstanceHealth_section"></a>

The following code examples show how to use `DescribeInstanceHealth`.

------
#### [ CLI ]

**AWS CLI**
**To describe the health of the instances for a load balancer**
This example describes the health of the instances for the specified load balancer.
Command:

```
aws elb describe-instance-health --load-balancer-name {{my-load-balancer}}
```
Output:

```
{
  "InstanceStates": [
      {
          "InstanceId": "i-207d9717",
          "ReasonCode": "N/A",
          "State": "InService",
          "Description": "N/A"
      },
      {
          "InstanceId": "i-afefb49b",
          "ReasonCode": "N/A",
          "State": "InService",
          "Description": "N/A"
      }
  ]
}
```
**To describe the health of an instance for a load balancer**
This example describes the health of the specified instance for the specified load balancer.
Command:

```
aws elb describe-instance-health --load-balancer-name {{my-load-balancer}} --instances {{i-7299c809}}
```
The following is an example response for an instance that is registering.
Output:

```
{
  "InstanceStates": [
      {
          "InstanceId": "i-7299c809",
          "ReasonCode": "ELB",
          "State": "OutOfService",
          "Description": "Instance registration is still in progress."
    }
  ]
}
```
The following is an example response for an unhealthy instance.
Output:

```
{
  "InstanceStates": [
      {
          "InstanceId": "i-7299c809",
          "ReasonCode": "Instance",
          "State": "OutOfService",
          "Description": "Instance has failed at least the UnhealthyThreshold number of health checks consecutively."
      }
  ]
}
```
+  For API details, see [DescribeInstanceHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-instance-health.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the state of the instances registered with the specified load balancer.**

```
Get-ELBInstanceHealth -LoadBalancerName my-load-balancer
```
**Output:**

```
Description                   InstanceId                    ReasonCode                    State
-----------                   ----------                    ----------                    -----
N/A                           i-87654321                    N/A                           InService
Instance has failed at lea... i-12345678                    Instance                      OutOfService
```
**Example 2: This example describes the state of the specified instance registered with the specified load balancer.**

```
Get-ELBInstanceHealth -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Example 3: This example displays the complete description of the state of the specified instance.**

```
(Get-ELBInstanceHealth -LoadBalancerName my-load-balancer -Instance i-12345678).Description
```
**Output:**

```
Instance has failed at least the UnhealthyThreshold number of health checks consecutively.
```
+  For API details, see [DescribeInstanceHealth](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the state of the instances registered with the specified load balancer.**

```
Get-ELBInstanceHealth -LoadBalancerName my-load-balancer
```
**Output:**

```
Description                   InstanceId                    ReasonCode                    State
-----------                   ----------                    ----------                    -----
N/A                           i-87654321                    N/A                           InService
Instance has failed at lea... i-12345678                    Instance                      OutOfService
```
**Example 2: This example describes the state of the specified instance registered with the specified load balancer.**

```
Get-ELBInstanceHealth -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Example 3: This example displays the complete description of the state of the specified instance.**

```
(Get-ELBInstanceHealth -LoadBalancerName my-load-balancer -Instance i-12345678).Description
```
**Output:**

```
Instance has failed at least the UnhealthyThreshold number of health checks consecutively.
```
+  For API details, see [DescribeInstanceHealth](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
