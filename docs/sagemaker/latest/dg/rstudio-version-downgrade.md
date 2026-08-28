---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio-version-downgrade.html
---

# Downgrade to a previous version
<a name="rstudio-version-downgrade"></a>

You can manually downgrade the version of your existing RStudio application to the `2024.04.2+764.pro1` version.

**To downgrade to a previous version**

1. Delete the `RStudioServerPro` application that's associated with your existing domain. For information about how to find your domain ID, see [View domains](domain-view.md).

   ```
   aws sagemaker delete-app \
       --domain-id {{domainId}} \
       --user-profile-name domain-shared \
       --app-type RStudioServerPro \
       --app-name default
   ```

1. Pass the corresponding `2024.04.2+764.pro1` ARN for your Region as part of the `update-domain` command. For a list of all available ARNs, see [Versioning](rstudio-version.md#rstudio-version-new). You must also pass an execution role ARN for the domain that provides permissions to update the domain.

   ```
   aws sagemaker update-domain \
       --region {{region}} \
       --domain-id {{domainId}} \
       --domain-settings-for-update "{\"RStudioServerProDomainSettingsForUpdate\":{\"DefaultResourceSpec\": {\"SageMakerImageArn\": \"{{arn-for-2024.04.2+764.pro1-version}}\", \"InstanceType\": \"system\"}, \"DomainExecutionRoleArn\": \"{{execution-role-arn}}\"}}"
   ```

1. Create a new `RStudioServerPro` application in the existing domain. The RStudio version defaults to `2024.04.2+764.pro1`.

   ```
   aws sagemaker create-app \
       --domain-id {{domainId}} \
       --user-profile-name domain-shared \
       --app-type RStudioServerPro \
       --app-name default
   ```

Your `RStudioServerPro` application is now downgraded to version `2024.04.2+764.pro1`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
