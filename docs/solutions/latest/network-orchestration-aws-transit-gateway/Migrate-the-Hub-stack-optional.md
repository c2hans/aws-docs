---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/Migrate-the-Hub-stack-optional.html
---

# Migrate the hub stack (optional)
<a name="Migrate-the-Hub-stack-optional"></a>

Follow the step-by-step instructions in this section to migrate the hub stack from earlier versions to the latest version.

## Migrate from v1 to v3
<a name="migrate-v1-to-latest"></a>

**Important**
You cannot directly update solution v1 to latest due to breaking changes in latest, including UserPoolAddOns which is not supported under the Essential pricing tier.

### Hub template
<a name="migrate-v1-hub-template"></a>

1. Download the latest version of the hub template from the link of the `network-orchestration-hub.template` [CloudFormation template](aws-cloudformation-templates.md).

1. Make the following change in UserPool Attribute Name in the hub template by removing `custom:` from the attribute name. Cognito is adding custom to the attribute so we don’t need to put it in our configuration. For more information, see [SchemaAttribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-schemaattribute.html) in the AWS CloudFormation User Guide.

   Edit the template to remove the `custom:` prefix from the Cognito User Pool attribute:

   ```
   # Change from:
   Name: custom:CognitoUserGr

   # To:
   Name: CognitoUserGr
   ```

1. Save the changes to the hub template.

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), select your user pool created by v1 hub, and navigate to **Feature plan** under settings. Select **Plus** plan instead of **Essential** plan.

1. Follow the steps provided in [Hub stack](update-the-hub-stack.md#hub-stack-update) to update the hub stack using the modified hub template.

### Spoke template
<a name="migrate-v1-spoke-template"></a>

For spoke template, follow the steps provided in [Spoke stack](update-the-spoke-stacks.md#spoke-stack-update).

## Migrate from v2 to v3
<a name="migrate-v2-to-v3"></a>

### Hub template
<a name="migrate-v2-hub-template"></a>

1. Download the latest version of the hub template from the link of the `network-orchestration-hub.template` [CloudFormation template](aws-cloudformation-templates.md).

1. Make the following change in UserPool Attribute Name in the hub template by removing `custom:` from the attribute name. Cognito is adding custom to the attribute so we don’t need to put it in our configuration.

   Edit the template to remove the `custom:` prefix from the Cognito User Pool attribute:

   ```
   # Change from:
   Name: custom:CognitoUserGr

   # To:
   Name: CognitoUserGr
   ```

1. Save the changes to the hub template.

1. Follow the steps provided in [Hub stack](update-the-hub-stack.md#hub-stack-update) to update the hub stack using the modified hub template.

### Spoke template
<a name="migrate-v2-spoke-template"></a>

For spoke template, follow the steps provided in [Spoke stack](update-the-spoke-stacks.md#spoke-stack-update).

**Note**
If you created peering attachments using solution versions before v3.0.0 and then upgraded to v3.0.0 or later, those attachments cannot be deleted by updating the tag value on the transit gateway. You will need to delete them manually.
