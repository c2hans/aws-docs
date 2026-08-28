---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_CancelCapacityReservation_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CancelCapacityReservation` with a CLI
<a name="ec2_example_ec2_CancelCapacityReservation_section"></a>

The following code examples show how to use `CancelCapacityReservation`.

------
#### [ CLI ]

**AWS CLI**
**To cancel a capacity reservation**
The following `cancel-capacity-reservation` example cancels the specified capacity reservation.

```
aws ec2 cancel-capacity-reservation \
    --capacity-reservation-id {{cr-1234abcd56EXAMPLE}}
```
Output:

```
{
    "Return": true
}
```
For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.
+  For API details, see [CancelCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example cancels the capacity reservation cr-0c1f2345db6f7cdba**

```
Remove-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2CapacityReservation (CancelCapacityReservation)" on target "cr-0c1f2345db6f7cdba".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
True
```
+  For API details, see [CancelCapacityReservation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example cancels the capacity reservation cr-0c1f2345db6f7cdba**

```
Remove-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2CapacityReservation (CancelCapacityReservation)" on target "cr-0c1f2345db6f7cdba".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
True
```
+  For API details, see [CancelCapacityReservation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
