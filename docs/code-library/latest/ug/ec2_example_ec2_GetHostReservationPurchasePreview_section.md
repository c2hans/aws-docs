---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_GetHostReservationPurchasePreview_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetHostReservationPurchasePreview` with a CLI
<a name="ec2_example_ec2_GetHostReservationPurchasePreview_section"></a>

The following code examples show how to use `GetHostReservationPurchasePreview`.

------
#### [ CLI ]

**AWS CLI**
**To get a purchase preview for a Dedicated Host Reservation**
This example provides a preview of the costs for a specified Dedicated Host Reservation for the specified Dedicated Host in your account.
Command:

```
aws ec2 get-host-reservation-purchase-preview --offering-id {{hro-03f707bf363b6b324}} --host-id-set {{h-013abcd2a00cbd123}}
```
Output:

```
{
  "TotalHourlyPrice": "1.499",
  "Purchase": [
      {
          "HourlyPrice": "1.499",
          "InstanceFamily": "m4",
          "PaymentOption": "NoUpfront",
          "HostIdSet": [
              "h-013abcd2a00cbd123"
          ],
          "UpfrontPrice": "0.000",
          "Duration": 31536000
      }
  ],
  "TotalUpfrontPrice": "0.000"
}
```
+  For API details, see [GetHostReservationPurchasePreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-host-reservation-purchase-preview.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example previews a reservation purchase with configurations that match those of your Dedicated Host h-01e23f4cd567890f1**

```
Get-EC2HostReservationPurchasePreview -OfferingId hro-0c1f23456789d0ab -HostIdSet h-01e23f4cd567890f1
```
**Output:**

```
CurrencyCode Purchase TotalHourlyPrice TotalUpfrontPrice
------------ -------- ---------------- -----------------
             {}       1.307            0.000
```
+  For API details, see [GetHostReservationPurchasePreview](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example previews a reservation purchase with configurations that match those of your Dedicated Host h-01e23f4cd567890f1**

```
Get-EC2HostReservationPurchasePreview -OfferingId hro-0c1f23456789d0ab -HostIdSet h-01e23f4cd567890f1
```
**Output:**

```
CurrencyCode Purchase TotalHourlyPrice TotalUpfrontPrice
------------ -------- ---------------- -----------------
             {}       1.307            0.000
```
+  For API details, see [GetHostReservationPurchasePreview](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
