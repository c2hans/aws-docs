---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-cd-app.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Create a CodeDeploy Application
<a name="gui-ex-create-cd-app"></a>

The CodeDeploy application is simply a name or container used by AWS CodeDeploy to ensure that the correct revision, deployment configuration, and deployment group are referenced during a deployment. The deployment configuration, in this case, is the WordPress bundle that you previously created.

REQUIRED DATA:
+ `VpcId`: The VPC that you are using, this should be the same as the previously used VPC.
+ `CodeDeployApplicationName`: Must be unique in the account. Look at the CodeDeploy Console to check for existing application names.

1. Create the CodeDeploy Application for WordPress

   On the **Create RFC** page, select the category **Deployment**, subcategory **Applications**, item **CodeDeploy application** and operation **Create** from the RFC CT pick list. Choose **Basic** and set the values as shown. Click **Submit** when finished.

   ```
   Subject:                      CD-WP-App-RFC
   CodeDeployApplicationName:    {{WordPress}}
   VpcId:                        {{VPC_ID}}
   Name:                         WP-CD-App
   ```

1. Click **Submit** when finished.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
