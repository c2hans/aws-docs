---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/module-enablement.html
---

# Module enablement
<a name="module-enablement"></a>

Module enablement is the core functionality of Modular Cloud Studio on AWS, allowing you to deploy and manage infrastructure components across your AWS environment. Modules are pre-configured infrastructure templates that provide specific capabilities such as networking, identity management, storage, and workstation management.

Modules can be deployed to supported Regions that are enabled and may have dependencies on other modules. For example, most modules require a Network module to be deployed first to provide the underlying VPC infrastructure. The solution automatically validates dependencies and guides you through the deployment process.

Module deployment typically involves selecting the target Region, configuring module-specific parameters, applying tags, and reviewing the configuration before deployment. The deployment process uses AWS Service Catalog to provision resources consistently and securely.

To set up a complete Modular Cloud Studio environment, follow these deployment steps in order. Note that some steps are optional depending on your specific requirements:

 [Step 1. Enable Network modules](enable-network-modules.md)

 [Step 2. Enable Identity modules](enable-identity-modules.md)

 [Step 3. Enable Leostream Broker module](enable-leostream-broker-module.md)

 [Step 4. Enable Leostream Gateway module](enable-leostream-gateway-module.md)

 [Step 5. Enable Storage modules (Optional)](enable-storage-module.md)

 [Step 6. Manual configurations](manual-configurations.md)

## Enable a module
<a name="enable-a-module"></a>

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. In the left navigation pane, choose a module category: **Network**, **Identity**, **Workstation Management**, **Storage** or **Custom**

1. Select **Deploy New Module**.

1. Select a Region from the **Select Region** dropdown menu.

1. Select a module from the **Select * <Module Category> * module** dropdown menu. Some module categories have a **Create** or **Import** option. **Create** means that new resources are created when the module is enabled. **Import** means that the resources already exist and the user will provide necessary inputs for the module.

1. Select **Next**.

1. Configure the module settings if the parameter fields are populated.

1. Select **Next**.

1. Optionally **Tag** the resources that will be deployed by the module. This allows you to assign metadata to your resources, including custom resources created by the solution. Each tag is a label consisting of a user-defined key and value pair, and you can add up to 10 tags per module. For any imported module, the tags will only be applied to resources created by MCS, and they will not be applied to imported resources originally created outside of MCS. For example, the tags won’t apply to VPC resources from the Import Amazon VPC module.

1. Select **Next**.

1. Review module settings.

1. Select **Deploy** module.

1. The module appears in **Module deployments** with an `ENABLING IN PROGRESS` status.

The Enable Module API does the following:

1. Checks if the Region is enabled.

1. Checks if the module is registered.

1. Checks if module dependencies are enabled.

1. Updates the module status to `ENABLING IN PROGRESS` in the [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules) and [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules).

1. Provisions the Service Catalog Product.

1. Updates the module `servicecatalog_provisioned_product_id` attribute in the [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules).

1. Updates the `active_dependents` attribute on module dependencies in the [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules).

1. If step 7 is successful, updates module status to `ENABLED` in the [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules). If unsuccessful, updates status to `ENABLE FAILED`.

1. Updates module status to `REGISTERED` in the [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules).

## Disable a module
<a name="disable-a-module"></a>

### Prerequisites
<a name="prerequisites-2"></a>

Before disabling a module, you must ensure that dependent modules are disabled first. The system will prevent you from disabling a module if other modules still depend on it, so you must work backwards through the dependency chain. For example, you need to disable Workstation Management modules before disabling the Identity modules they depend on.

**Important**
Verify that all important data has been properly backed up before proceeding. For storage modules, ensure data has been backed up or migrated. For workstation management modules, confirm that user data and configurations have been saved. Disabling a module will terminate all associated AWS resources, and any data stored on those resources may be permanently lost.

### Steps to disable a module
<a name="steps-to-disable-a-module"></a>

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. In left the navigation pane, choose a module category: **Network**, **Identity**, **Workstation Management**, **Storage** or **Custom**.

1. Choose a module to disable, and select **Disable**.

1. Select **OK**.

1. The module appears in **Module deployments** with a `DISABLING IN PROGRESS` status.

The Disable Module API does the following:

1. Checks if any dependent modules are enabled. If so, an error is thrown.

1. Updates the module status to `DISABLING IN PROGRESS` in the [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules) and [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules).

1. Terminates the provisioned Service Catalog product.

1. If the previous step is successful, updates the `active_dependents` attribute on module dependencies and updates module status to `DISABLED` in the [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules). If unsuccessful, updates status to `DISABLE FAILED` and doesn’t update `active_dependents` on module dependencies.

1. Updates module status to `REGISTERED` in the [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules).
