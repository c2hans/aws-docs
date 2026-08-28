---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-sdi-rou.html
---

# Add SDI video routers
<a name="config-wrkr-lv-cg-sdi-rou"></a>

If your deployment includes SDI video inputs that pass through a router, provide information about your router configuration on the AWS Elemental Live node.

**Warning**
If you forget to configure the router, everything looks acceptable on the event or profile, but when you run the event, you receive a no input detected error.

**Topics**
+ [Step A: Get ready](sdi-rou-ready.md)
+ [Step B: Create the router](sdi-rou-create.md)
+ [Step C: Complete the input mappings](sdi-rou-input.md)
+ [Step D: Complete the output mappings](sdi-rou-output.md)
+ [Step E: Use the router inputs](sdi-rou-using.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
