---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/solution-overview.html
---

# Solution overview
<a name="solution-overview"></a>

AWS CodePipeline integrates with source control repositories and automatically triggers pipeline execution when code is committed. In this deployment strategy, the pipeline references an environment configuration file to select the appropriate version for each target environment. By using a centralized version-mapping configuration, the pipeline fetches the corresponding CloudFormation template versions for specific environments, providing consistent and controlled deployments across development, staging, and production.

![Centralized version-mapping configuration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/images/guide-img/4fdaca28-ded7-44f0-99b8-4fbec0ad28d6/images/efe75dfe-317a-4703-8f2e-3cd67191d50e.png)

## Code versioning and tagging
<a name="code-versioning-and-tagging"></a>

Developers commit infrastructure code to the Git repository and create semantic version tags, establishing a clear, traceable deployment baseline. a) Semantic Version Structure - - Format:` MAJOR.MINOR.PATCH` (e.g., 1.2.3) - MAJOR: Breaking changes - MINOR: New features, backward compatible - PATCH: Bug fixes, backward compatible b) Git commands for version tagging:

```
# Create and push a new version tag
git tag -a v1.0.0 -m "Initial production release"
git push origin v1.0.0
```

c) Version mapping configuration: Use a `deployment_map.json` file to manage versions across environments. This file contains environment-specific version mappings, account IDs, and Regions. The infrastructure team should configure and maintain this file. Sample `deployment_map.json` file:

```
 {
    "environments": {
        "dev": {
            "version_constraint": "= <Version_ID-1>",
            "account_id": "<Account_ID-1>",
            "region": "<region_name>"
        }
        "prod": {
            "version_constraint": "= <Version_ID-2>",
            "account_id": "<Account_ID-2>",
            "region": "<region_name>"
        }
    }
    }
```

This configuration enables you to:
+ Map specific versions to each environment
+ Maintain separate account configurations
+ Control regional deployments
+ Progressively promote changes through environments

## Automated webhook trigger
<a name="automated-webhook-trigger"></a>

To connect your GitHub repository to CodePipeline:

1. Open the CodePipeline console and navigate to your pipeline settings.

1. Generate a webhook URL and copy it.

1. In your GitHub repository, navigate to **Settings**, then **Webhooks**, then choose **Add webhook**.

1. Paste the CodePipeline webhook URL in the **Payload URL** field.

1. Set **Content type** to application/json.

1. Select **Just the push event** for the trigger.

1. Choose **Add webhook** to save.

1. Verify the connection by pushing a change to your repository and confirming that CodePipeline triggers automatically.

When implemented, each code push automatically triggers your deployment pipeline, maintaining version control and providing consistent infrastructure updates across environments.

## Version-based deployment
<a name="version-based-deployment"></a>

The Git webhook triggers an AWS CodeBuild project. CodeBuild runs the deployment process by using two key components: the version mapping configuration (`deployment_map.json`) and a deployment script (`deploy.py`). Ensure your CodeBuild project has:
+ An IAM role with permissions for CloudFormation operations
+ Cross-account deployment permissions if deploying to multiple accounts
+ Python 3.x and boto3 installed in the build environment

The deployment script performs these sequential actions:

1. Reads `deployment_map.json` to get environment configurations.

1. Extracts the current version from the CODEBUILD\_RESOLVED\_SOURCE\_VERSION environment variable.

1. Matches the version with environment constraints in deployment\_map.json.

1. Identifies the target account and AWS Region for deployment.

1. Creates or updates the CloudFormation stack in the target environment. Sample `deploy.py` file:

   ```
    import json
      import boto3
      import os

      def deploy_stack():
          # Load deployment configuration
          with open('deployment_map.json', 'r') as f:
              config = json.load(f)

          # Get current version from CodeBuild environment
          version = os.environ['CODEBUILD_RESOLVED_SOURCE_VERSION']

          for env, settings in config['environments'].items():
              if settings['version_constraint'].split()[1] == version:
                  cloudformation = boto3.client('cloudformation',
                                             region_name=settings['region'])

                  # Deploy CloudFormation stack
                  cloudformation.create_or_update_stack(
                      StackName=f'infrastructure-{env}',
                      TemplateURL='path/to/your/template.yaml',  # Ensure CloudFormation templates are in your repository
                      Parameters=[
                          {
                              'ParameterKey': 'Environment',
                              'ParameterValue': env
                          }
                      ]
                  )

                 if name == '__main__':
                   deploy_stack()
   ```

**Note**
This sample uses `create_stack`. For production use, implement logic to check whether the stack exists and call `update_stack` if it does, or use CloudFormation change sets for safer updates.

## CloudFormation stack creation
<a name="cf-nshort-stack-creation"></a>

The deployment script automatically handles stack creation through CodeBuild:
+ Each environment defined in `deployment_map.json` gets its own stack.
+ Stack names are automatically generated by using the format: infrastructure-{environment}.
+ Version control is maintained through the version\_constraint in `deployment_map.json`.
+ Stacks are created or updated based on the version tags.

Example stack names:
+ For the dev environment: `infrastructure-dev`
+ For the prod environment: `infrastructure-prod`

## Multi-account deployment
<a name="multi-account-deployment"></a>

To deploy across multiple AWS accounts, configure IAM roles in each account.

**In the administrator account (where CodeBuild runs):**

1. Create a role named `AWSCloudFormationStackSetAdministrationRole`.

1. Grant permissions for CloudFormation and StackSet management.

**In each target account:**

1. Create a role named `AWSCloudFormationStackSetExecutionRole`.

1. Configure a trust relationship with the administrator account.

1. Grant permissions for CloudFormation resource creation.

Example IAM policy for cross-account role assumption:

```
``json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": "sts:AssumeRole",
"Resource": [
"arn:aws:iam::<account-id>:role/CodeBuildCrossAccountRole"
]
}
]
}``
```

The `deployment_map.json` file handles target specification. The `deploy.py` script automatically reads target accounts and Regions from `deployment_map.json` and maps versions to specific environments. For detailed IAM role setup instructions, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the CloudFormation documentation. This is the CI/CD workflow for version-controlled CloudFormation deployments across environments:

![CI/CD workflow for version-controlled CloudFormation deployments across environments.](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/images/guide-img/4fdaca28-ded7-44f0-99b8-4fbec0ad28d6/images/1ab88171-d99f-433e-a42a-8ee31e8c112d.png)

## Hotfix deployments
<a name="hotfix-deployments"></a>

For urgent production fixes:

1. Create a hotfix branch from the production version.

1. Implement and test the change.

1. Create a specific version tag (for example, `v1.0.1-hotfix`).

1. Deploy by using an expedited approval process.

1. Monitor the deployment and verify the fix.

1. Document changes for audit purposes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
