---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/deployment-process-overview.html
---

# Deployment process overview
<a name="deployment-process-overview"></a>

Before you launch the automated deployment, review the architecture, components, and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the Cloud Migration Factory on AWS solution into your account.

 **Time to deploy:** Approximately 20 minutes

**Note**
If you deploy this solution to AWS Regions other than US East (N. Virginia), the Migration Factory CloudFront URL may take longer to become available. During this time, you will receive an **Access Denied** message when accessing the web interface.

 [Step 1: Choose your deployment option](choose-deployment-option.md)

 [Step 2: Launch the Stack](launch-the-stack.md)

 [Step 3: Launch the target account stack in the target AWS account](launch-target-account-stack.md)

 [Step 4: Create the first user](create-first-user.md)

 [Step 5: (Optional) Deploy private web console static content](deploy-private-web-console.md)

 [Step 6: Update the factory schema](update-factory-schema.md)

 [Step 7: Configure a migration automation server](configure-migration-automation-server.md)

 [Step 8: Test the solution using the automation scripts](test-solution-automation-scripts.md)

 [Step 9: Configure Wave Planning Manager](configure-wave-planning-manager.md)

 [Step 10: (Optional) Build a migration tracker dashboard](build-migration-tracker-dashboard.md)

 [Step 11: (Optional) Configure additional identity providers in Amazon Cognito](configure-cognito-identity-providers.md)

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the solution. For more information, see the [Anonymized data collection](anonymized-data-collection.md) section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
