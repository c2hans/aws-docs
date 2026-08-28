---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

 You can uninstall the Secure Media Delivery at the Edge on AWS solution from the AWS Management Console or by using the AWS Command Line Interface.

 Before you perform the steps to uninstall the Secure Media Delivery at the Edge solution, ensure you disassociate all the components created by the solution with the resources that are operated externally. In particular, review the configuration in:
+  AWS WAF web ACL which includes the rule group for session revocation. Remove the corresponding rule from the web ACL list.
+  CloudFront distributions’ cache behaviors protected by secure tokens provided by this solution. Remove the association between all the viewer request triggers and function used to validate the token. You can see all the distributions and cache behaviors which use the function by navigating in CloudFront console to **Functions** page, selecting token validation function and switching to **Publish** tab which details all associations for this function.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  On the **Stacks** page, select this solution’s installation stack.

1.  Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

 Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
aws cloudformation delete-stack --stack-name [Stack Name]
```

## Using CDK toolkit
<a name="using-cdk-toolkit"></a>

 If you deployed the solution through CDK, depending on if you activated the Auto Session Revocation module, one or two stacks will be deployed in the region, named:
+  **[Stack name]** – deploys components from Base and API module
+  **[Stack name]AutoSessionRevocation –** includes components used in the Auto Session Revocation workflow

 To remove both of the stacks run the following command from the project folder:

```
npx cdk destroy –-all
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
