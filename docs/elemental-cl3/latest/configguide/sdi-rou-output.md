---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/sdi-rou-output.html
---

# Step E: Complete the Router Output Mappings
<a name="sdi-rou-output"></a>

Perform this procedure on the Conductor Live node.

You must map each router output to each SDI input that you plan to use. This mapping must reflect the actual cabling from the output side of the router to the input side of the SDI card.

**To map the SDI outputs**

1. On the Conductor Live web interface, choose **Settings**, then choose **Routers**. Choose the router.

1. Choose **Map Outputs**. Complete the first line as follows and choose **Add** (\+ icon):
   + **Output**: Select an output that is one of the cabled router outputs that you plan to use. The available options have the form *Output X*, where *X* is a number that corresponds to the appropriate router output port. For example, if your cabling comes from the router's output port 20, choose **Output 20**.
**Note**
The correct number for the output is determined by the router, not by Conductor Live.
   + **Connected to**: Select the card and node that the router output is connected to. The node displays the cards that it has auto-detected.

     If you added a 4 Quadrant-4k input in [Step D: Complete the Router Input Mappings](sdi-rou-input.md) and want to map those four inputs, choose the Quadrant 4k (HD-SDI) card. This maps all four inputs to the one output.

1. Repeat the previous steps for each line to create all necessary output mappings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
