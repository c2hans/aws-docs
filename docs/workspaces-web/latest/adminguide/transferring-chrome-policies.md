---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/transferring-chrome-policies.html
---

# Transferring Chrome policies
<a name="transferring-chrome-policies"></a>

In case you already have Chrome policies set up to allow or block specific domains, we recommend that you transfer them to the Web Content Filtering feature.

The Web Content Filtering feature will detect any URLAllow or URLBlock policies that apply to a WorkSpaces Secure Browser session and will signal it in the AWS Console.

To transfer the Chrome policies for URLAllowlist and / or URLBlocklist:
+ In your AWS Console, under URL Filtering, click **Review Chrome Policies** (if you do not see the Review Chrome Policies button, this means not Chrome policies currently applies for URL Allow or URLBlock)
+ Under the overlay, review the Chrome policies
+ Click **Transfer**

The Chrome policies will be removed from the JSON Editor under Policy Settings and new URLs will be automatically added to the Web Content Filtering feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
