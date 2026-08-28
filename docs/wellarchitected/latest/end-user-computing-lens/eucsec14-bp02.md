---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp02.html
---

# EUCSEC14-BP02 Encrypt data in transit in your EUC environment
<a name="eucsec14-bp02"></a>

 Use encryption to protect data confidentiality while in transit inside your EUC environment.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-36"></a>

 Use AWS EUC streaming protocols to encrypt streaming data in transit. Amazon WorkSpaces and Amazon WorkSpaces Applications provide data encryption of pixel streaming traffic between instances and end user devices by default. Evaluate the default levels of encryption to verify that they provide sufficient protection in terms of key length and cipher suites and satisfy the requirements of the organization. For further details regarding the encryption used for Amazon AppStream, see [Data Protection in Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/data-protection.html) , and for Amazon WorkSpaces, see [Data Protection in Amazon WorkSpaces.](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
