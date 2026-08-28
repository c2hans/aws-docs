---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.deprovision.html
---

# Deprovision the address range
<a name="using-byoip.deprovision"></a>

To stop using your address range with AWS, you first must remove any accelerators that have static IP addresses that are allocated from the address pool and stop advertising your address range. After you complete those steps, you can deprovision the address range.

You must stop advertising and deprovision your address range using the CLI or Global Accelerator API operations. This functionality is not available in the AWS console.

**Step 1: Delete any associated accelerators. **To delete an accelerator using the console or using API operations, see [Delete accelerator](about-accelerators.deleting.md).

**Step 2. Stop advertising the address range.** To stop advertising the range, use the following [WithdrawByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_WithdrawByoipCidr.html) command.

```
aws globalaccelerator --region us-west-2 withdraw-byoip-cidr --cidr {{address-range}}
```

**Step 3. Deprovision the address range.** To deprovision the range, use the following [DeprovisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeprovisionByoipCidr.html) command.

```
aws globalaccelerator --region us-west-2 deprovision-byoip-cidr --cidr {{address-range}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
