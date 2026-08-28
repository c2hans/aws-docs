---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_ModifyLoadBalancerAttributes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyLoadBalancerAttributes` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_ModifyLoadBalancerAttributes_section"></a>

The following code examples show how to use `ModifyLoadBalancerAttributes`.

------
#### [ CLI ]

**AWS CLI**
**To modify the attributes of a load balancer**
This example modifies the `CrossZoneLoadBalancing` attribute of the specified load balancer.
Command:

```
aws elb modify-load-balancer-attributes --load-balancer-name {{my-load-balancer}} --load-balancer-attributes "{\"CrossZoneLoadBalancing\":{\"Enabled\":true}}"
```
Output:

```
{
    "LoadBalancerAttributes": {
        "CrossZoneLoadBalancing": {
            "Enabled": true
        }
    },
    "LoadBalancerName": "my-load-balancer"
}
```
This example modifies the `ConnectionDraining` attribute of the specified load balancer.
Command:

```
aws elb modify-load-balancer-attributes --load-balancer-name {{my-load-balancer}} --load-balancer-attributes "{\"ConnectionDraining\":{\"Enabled\":true,\"Timeout\":300}}"
```
Output:

```
{
    "LoadBalancerAttributes": {
        "ConnectionDraining": {
            "Enabled": true,
            "Timeout": 300
        }
    },
    "LoadBalancerName": "my-load-balancer"
}
```
+  For API details, see [ModifyLoadBalancerAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/modify-load-balancer-attributes.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables cross-zone load balancing for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer -CrossZoneLoadBalancing_Enabled $true
```
**Example 2: This example disables connection draining for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer -ConnectionDraining_Enabled $false
```
**Example 3: This example enables access logging for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer `
>> -AccessLog_Enabled $true `
>> -AccessLog_S3BucketName amzn-s3-demo-logging-bucket `
>> -AccessLog_S3BucketPrefix my-app/prod `
>> -AccessLog_EmitInterval 60
```
+  For API details, see [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables cross-zone load balancing for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer -CrossZoneLoadBalancing_Enabled $true
```
**Example 2: This example disables connection draining for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer -ConnectionDraining_Enabled $false
```
**Example 3: This example enables access logging for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer `
>> -AccessLog_Enabled $true `
>> -AccessLog_S3BucketName amzn-s3-demo-logging-bucket `
>> -AccessLog_S3BucketPrefix my-app/prod `
>> -AccessLog_EmitInterval 60
```
+  For API details, see [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
