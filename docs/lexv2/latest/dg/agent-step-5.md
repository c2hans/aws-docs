---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/agent-step-5.html
---

# Step 5: Deploy Your Bot as a Web Application
<a name="agent-step-5"></a>

**To deploy your bot as a web application**

1. Download the repository at [https://github.com/awsdocs/amazon-lex-developer-guide/blob/master/example\_apps/agent\_assistance\_bot/ ](https://github.com/awsdocs/amazon-lex-developer-guide/blob/master/example_apps/agent_assistance_bot/) to your computer.

1. Navigate to the downloaded repository and open the index.html file in an editor.

1. Make the following changes.

   1. In the `AWS.config.credentials` section, enter your Region name and your identity pool ID.

   1. In the` Amazon Lex V2 runtime parameters` section, enter the bot name.

   1. Save the file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
