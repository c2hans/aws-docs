---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html
---

# Billing for interrupted Spot Instances
<a name="billing-for-interrupted-spot-instances"></a>

When a Spot Instance is interrupted, you're charged for instance and EBS volume usage, and you might incur other charges, as follows.

## Instance usage
<a name="billing-for-interrupted-spot-instances-instance-usage"></a>

- ** If **you** stop or terminate the Spot Instance  **
  - **Operating system:** Windows and Linux (excluding SUSE) / **Interrupted in the first hour:** Charged for the seconds used / **Interrupted in any hour after the first hour:** Charged for the seconds used
  - **Operating system:** SUSE / **Interrupted in the first hour:** Charged for the full hour even if you used a partial hour / **Interrupted in any hour after the first hour:** Charged for the full hours used, and charged a full hour for the interrupted partial hour

- ** If the **Amazon EC2** interrupts the Spot Instance **
  - **Operating system:** Windows and Linux (excluding SUSE) / **Interrupted in the first hour:** No charge / **Interrupted in any hour after the first hour:** Charged for the seconds used
  - **Operating system:** SUSE / **Interrupted in the first hour:** No charge / **Interrupted in any hour after the first hour:** Charged for the full hours used, but no charge for the interrupted partial hour

## EBS volume usage
<a name="billing-for-interrupted-spot-instances-ebs-usage"></a>

While an interrupted Spot Instance is stopped, you are charged only for the EBS volumes, which are preserved.

With EC2 Fleet and Spot Fleet, if you have many stopped instances, you can exceed the limit on the number of EBS volumes for your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
