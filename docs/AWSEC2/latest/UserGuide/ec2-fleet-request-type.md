---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html
---

# EC2 Fleet and Spot Fleet request types
<a name="ec2-fleet-request-type"></a>

**Note**
Spot Fleet uses a legacy API with no planned investment. We recommend using EC2 Fleet or an Auto Scaling group instead. For more information, see [Which is the best fleet method to use?](which-fleet-method-to-use.md).

The request type for an EC2 Fleet or Spot Fleet determines whether the request is synchronous or asynchronous, and whether it is a one-time request for the desired target capacity or an ongoing effort to maintain the capacity over time. When configuring your fleet, you must specify the request type.

Both EC2 Fleet and Spot Fleet offer two request types: `request` and `maintain`. In addition, EC2 Fleet offers a third request type called `instant`.Fleet request types

`instant` (EC2 Fleet only)
If you configure the request type as `instant`, EC2 Fleet places a synchronous one-time request for your desired capacity. In the API response, it returns the instances that launched and provides errors for those instances that could not be launched. For more information, see [Configure an EC2 Fleet of type instant](instant-fleet.md).

`request`
If you configure the request type as `request`, the fleet places an asynchronous one-time request for your desired capacity. If capacity diminishes due to Spot interruptions, the fleet does not attempt to replenish Spot Instances, nor does it submit requests in alternative Spot capacity pools if capacity is unavailable. When creating a Spot Fleet of type `request` using the console, clear the **Maintain target capacity** checkbox.

`maintain` (default)
If you configure the request type as `maintain`, the fleet places an asynchronous request for your desired capacity, and maintains it by automatically replenishing any interrupted Spot Instances. When creating a Spot Fleet of type `maintain` using the console, select the **Maintain target capacity** checkbox

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
