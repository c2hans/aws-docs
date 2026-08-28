---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/closing-a-case.html
---

# Closing a case
<a name="closing-a-case"></a>

 For AWS supported cases, choose **Close Case** on the case details page to permanently close the case at any status. A case typically reaches the status **Ready to Close** before it is permanently closed. If you close a case prematurely at any other status than **Ready to Close**, you are requesting that AWS Security Incident Response engineers will stop working on this AWS supported case.

 If your incident response team is the responder, select **Action/Close Case** on the case details page.

**Note**
 The "Ready to Close" status signifies that a case can be permanently closed and that there is no additional work to be done on a case.

 A case cannot be re-opened again after it has been permanently closed. All information will be available read-only. To prevent accidental closure, you will be asked to confirm that you want to close the case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
