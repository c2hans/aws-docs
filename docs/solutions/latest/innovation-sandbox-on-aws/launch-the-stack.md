---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/launch-the-stack.html
---

# Launch the stacks
<a name="launch-the-stack"></a>

You must gather deployment parameter details before deploying the stacks. For details, refer to [Prerequisites](prerequisites.md).

 **Time to deploy:** Approximately 60 minutes

You must deploy these four stacks for the Innovation Sandbox solution in the following order. Failing to do so will result in deployment failures.

1.  [Step 1: Deploy the `AccountPool` stack](step1-deploy-accountpool-stack.md)

1.  [Step 2: Deploy the `IDC` stack](step2-deploy-idc-stack.md)

1.  [Step 3: Deploy the `Data` stack](step3-deploy-data-stack.md)

1.  [Step 4: Deploy the `Compute` stack](step4-deploy-compute-stack.md)

**Important**
Before you deploy the **Data** stack ([Step 3 of Launch the stacks](step3-deploy-data-stack.md)), you must have completed [Create a SAML 2.0 application](create-saml-app.md) and copied its metadata URL — you supply it as the `SamlMetadataUrl` parameter when you deploy the Data stack. After all stacks are deployed, return to [Update the SAML application configuration](update-saml-app-config.md) to replace the placeholder ACS URL and audience with the Data stack outputs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
