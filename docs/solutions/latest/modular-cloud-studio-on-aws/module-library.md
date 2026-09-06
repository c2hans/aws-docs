---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/module-library.html
---

# Module Library
<a name="module-library"></a>

The Module Library serves as the central hub for managing Third-Party Modules in your MCS deployment that extend the capabilities of your cloud studio environment.

The Module Library page provides two main functions:
+  **AWS Partners modules discovery**: Import and synchronize available AWS Partners modules that can be registered with your MCS deployment. These modules are sourced from a curated list maintained in the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing).
+  **Third-Party module management**: Register Third-Party Modules. De-register modules that are no longer needed in your environment.

**Note**
Modular Cloud Studio on AWS allows you to deploy and manage a scalable, secure, and global content production infrastructure in the cloud. This includes custom modules, developed by AWS Partners or other third parties, that you can choose to use ("Third-Party Modules"). AWS does not own or otherwise have any control over Third-Party Modules.
Your use of the Third-Party Modules is governed by any terms provided to you by the Third-Party Module providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy). You are responsible for ensuring that your use of the Third-Party Modules comply with any terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Modules that you use. AWS does not make any representations, warranties, or guarantees regarding the Third-Party Modules, which are "Third-Party Content" under your agreement with AWS. Modular Cloud Studio on AWS is offered to you as "AWS Content" under your agreement with AWS.

## Synchronize AWS Partners modules
<a name="synchronize-partner-modules"></a>

The Module Library includes a **Sync partner modules** button that allows you to import the latest AWS Partners modules from the listing hosted in the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing). This ensures you have access to the most current AWS Partners modules available for registration.

**Note**
If a module is registered, it will not be updated with the latest data available in the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing) after synchronization.
If an AWS Partners module listing is removed from the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing), it will delete that module from the MCS deployment if the module is not registered.

To synchronize AWS Partners modules:

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Module Library** from the left navigation pane.

1. Click **Sync partner modules** button.

1. The system will fetch the latest AWS Partners module listings from the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing) and update the available modules in the Module Library page. This synchronization process imports new AWS Partners modules that have been added to the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing) and updates information for existing and non-registered modules.

1. During the synchronization process, modules cannot be registered.

1. Once the process has finished, the page will reflect the last date and time the AWS Partners modules were synchronized.

The synchronization process does the following:

1. Checks if the process can be triggered by looking up the [Lock DynamoDB table](dynamodb-tables.md#lock-table) and acquire the lock by inserting the lock data to the same table.

1. Fetch the latest AWS Partners modules data from the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing).

1. Execute the AWS Partners module synchronization state machine

The AWS Partners module synchronization state machine does the following:

1. Insert the module into the [External modules DynamoDB table](dynamodb-tables.md#external-modules) if a new module is found in the [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing).

1. Update the module data from the [External modules DynamoDB table](dynamodb-tables.md#external-modules) if the module already exists and the status is `AVAILABLE`.

1. Delete modules from the [External modules DynamoDB table](dynamodb-tables.md#external-modules) with `AVAILABLE` status if they are no longer hosted in [AWS Solutions GitHub repository](https://github.com/aws-solutions/modular-cloud-studio-on-aws-third-party-modules-listing).

1. Release the process lock from the [Lock DynamoDB table](dynamodb-tables.md#lock-table).

## Register a module
<a name="register-a-module"></a>

Module registration makes Third-Party Modules available for deployment in your MCS environment. You can register modules from the available AWS Partner module listings or by providing a custom module manifest URL.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Module Library** from the left navigation pane.

1. To register an available AWS Partners module, choose the module row and select **Register  *<Module Name>*  **.

1. To register a third party module, select **Register new module.**

1. Type the URL of the module’s manifest file, then select **Next**.

1. Select a module revision from the **Select Revision** dropdown menu and verify that the information is correct. Then select **Register module**.

1. Only one module can be registered at a time, and partner modules cannot be synchronized during the registration process

1. After registration is complete, the module appears in the **Module Library** with a `REGISTERED` status.

The module registration process does the following:

1. Checks if the process can be triggered by looking up the [Lock DynamoDB table](dynamodb-tables.md#lock-table) and acquire the lock by inserting the lock data to the same table.

1. Verify that a module can be registered by checking if status is `AVAILABLE`.

1. Execute the module registration state machine.

The module registration state machine does the following:

1. Validate the module can be registered by checking the status is not already `REGISTERED`

1. Inserts or updates module outputs in the [Modules Mapping DynamoDB table](dynamodb-tables.md#modules-mapping-table).

1. Creates a Service Catalog product and adds it to the MCS Service Catalog Portfolio. A stack set constraint is added to configure the Regions that the module can be deployed in.

1. Inserts or updates the module in the [External Modules DynamoDB table](dynamodb-tables.md#external-modules).

1. Inserts or updates the module in the [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules).

1. Release the process lock from the [Lock DynamoDB table](dynamodb-tables.md#lock-table).

1. In any case of failures, it updates module status to REGISTER FAILED in [External Modules DynamoDB table](dynamodb-tables.md#external-modules) and [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules).

## De-register a module
<a name="de-register-a-module"></a>

Module de-registration removes third party modules from your MCS environment, making them unavailable for deployment. This process returns the module to an available state if the module is an AWS Partners module.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Module Library** from the left navigation pane.

1. In the navigation pane, choose **Module Library**.

1. Choose the module to de-register, and select **De-register module**.

1. Select **Yes**.

The module de-registration does the following:

1. Ensure the module to be de-registered is not an internal module provided by MCS.

1. Check that the module is not enabled. Enabled modules cannot be de-registered.

1. Update module status to `DEREGISTER IN PROGRESS`.

1. Execute de-registration state machine.

The de-registration state machine does the following:

1. Removes module and outputs from the [Modules Mapping DynamoDB table](dynamodb-tables.md#modules-mapping-table).

1. Deletes the module’s Service Catalog product.

1. Deletes the module from the [External Modules DynamoDB table](dynamodb-tables.md#external-modules). If it is an AWS Partners Module, it does not get deleted and its status is updated to **Available**.

1. Deletes the module from the [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules).

1. In any case of failures, it updates module status to `DEREGISTER FAILED` in [External Modules DynamoDB table](dynamodb-tables.md#external-modules) and [Registered Modules DynamoDB table](dynamodb-tables.md#registered-modules).
