---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/remove-addon-role.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Remove Pod Identity associations from an Amazon EKS add-on
<a name="remove-addon-role"></a>

Remove the Pod Identity associations from an Amazon EKS add-on.

1. Determine:
   +  `cluster-name` - The name of the EKS cluster to install the add-on onto.
   +  `addon-name` - The name of the Amazon EKS add-on to install.

1. Update the addon to specify an empty array of pod identity associations.

   ```
   aws eks update-addon --cluster-name <cluster-name> \
   --addon-name <addon-name> \
   --pod-identity-associations "[]"
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
