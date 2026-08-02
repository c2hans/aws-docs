---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DescribeSpotFleetInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeSpotFleetInstances` with a CLI
<a name="ec2_example_ec2_DescribeSpotFleetInstances_section"></a>

The following code examples show how to use `DescribeSpotFleetInstances`.

------
#### [ CLI ]

**AWS CLI**
**To describe the Spot Instances associated with a Spot fleet**
This example command lists the Spot instances associated with the specified Spot fleet.
Command:

```
aws ec2 describe-spot-fleet-instances --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}
```
Output:

```
{
  "ActiveInstances": [
      {
          "InstanceId": "i-1234567890abcdef0",
          "InstanceType": "m3.medium",
          "SpotInstanceRequestId": "sir-08b93456"
      },
      ...
  ],
  "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
}
```
+  For API details, see [DescribeSpotFleetInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the instances associated with the specified Spot fleet request.**

```
Get-EC2SpotFleetInstance -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
```
**Output:**

```
InstanceId    InstanceType    SpotInstanceRequestId
----------    ------------    ---------------------
i-f089262a    c3.large        sir-12345678
i-7e8b24a4    c3.large        sir-87654321
```
+  For API details, see [DescribeSpotFleetInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the instances associated with the specified Spot fleet request.**

```
Get-EC2SpotFleetInstance -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
```
**Output:**

```
InstanceId    InstanceType    SpotInstanceRequestId
----------    ------------    ---------------------
i-f089262a    c3.large        sir-12345678
i-7e8b24a4    c3.large        sir-87654321
```
+  For API details, see [DescribeSpotFleetInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
