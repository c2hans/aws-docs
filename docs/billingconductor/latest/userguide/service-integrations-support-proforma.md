---
source_url: https://docs.aws.amazon.com/billingconductor/latest/userguide/service-integrations-support-proforma.html
---

# AWS services that support pro forma-based billing view costs
<a name="service-integrations-support-proforma"></a>

The following Cloud Financial Management services and their features support pro forma costs.

<table>
<thead>
  <tr><th>Service and features</th><th colspan="3">Support level by AWS account type</th></tr>
</thead>
<tbody>
  <tr><td></td><td>Payer (management account)</td><td>Primary account</td><td>Linked (member account)</td></tr>
  <tr><td>AWS Cost and Usage Report</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Split cost allocation</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>AWS Billing</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Dashboard</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Billing details</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Download CSV</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>AWS Cost Explorer</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Forecasting</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Save reports</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Rightsizing recommendations</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Cost anomaly monitors</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Savings Plans recommendations</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Savings Plans utilization reports</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Savings Plans coverage reports</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Reservation recommendations</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Reservation utilization reports</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Reservation coverage reports</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>AWS Budgets </td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Budget reports</td><td>No</td><td>Yes</td><td>Yes</td></tr>
</tbody>
</table>

For services and features that don't support pro forma costs, AWS accounts will see costs at billable rates, which match the AWS invoice.

## Related information
<a name="related-information-proforma-costs"></a>

To manage linked account access to billable refunds, credits, and discounts, see the **AWS Cost Explorer** section on the **Preferences** page in the [Cost Management Console](https://console.aws.amazon.com/cost-management/home#/settings).

If you don't want your IAM entities to see specific billable rates for these services and features, you can use IAM policies to deny access. For an example IAM policy, see [Denying AWS Billing and Cost Explorer access to services and features that don't support pro forma costs](security_iam_id-based-policy-examples.md#deny-access-proforma-costs).

You can also customize your IAM policies to allow or deny specific permissions. For a granular list of IAM actions for Billing and Cost Management, see the following topics:
+ [Migrating access control for AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/migrate-granularaccess-whatis.html) in the *AWS Cost Management User Guide*
+ [Migrating access control for AWS Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-granularaccess-whatis.html) and in the *AWS Billing User Guide*
