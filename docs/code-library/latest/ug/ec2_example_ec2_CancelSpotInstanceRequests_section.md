---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_CancelSpotInstanceRequests_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CancelSpotInstanceRequests` with a CLI
<a name="ec2_example_ec2_CancelSpotInstanceRequests_section"></a>

The following code examples show how to use `CancelSpotInstanceRequests`.

------
#### [ CLI ]

**AWS CLI**
**To cancel Spot Instance requests**
This example command cancels a Spot Instance request.
Command:

```
aws ec2 cancel-spot-instance-requests --spot-instance-request-ids {{sir-08b93456}}
```
Output:

```
{
    "CancelledSpotInstanceRequests": [
        {
            "State": "cancelled",
            "SpotInstanceRequestId": "sir-08b93456"
        }
    ]
}
```
+  For API details, see [CancelSpotInstanceRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-instance-requests.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example cancels the specified Spot instance request.**

```
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678
```
**Output:**

```
SpotInstanceRequestId    State
---------------------    -----
sir-12345678             cancelled
```
+  For API details, see [CancelSpotInstanceRequests](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example cancels the specified Spot instance request.**

```
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678
```
**Output:**

```
SpotInstanceRequestId    State
---------------------    -----
sir-12345678             cancelled
```
+  For API details, see [CancelSpotInstanceRequests](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
