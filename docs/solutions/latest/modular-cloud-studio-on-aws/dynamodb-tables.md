---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/dynamodb-tables.html
---

# DynamoDB Tables
<a name="dynamodb-tables"></a>

MCS uses five DynamoDB tables: [Registered Modules](#registered-modules), [External Modules](#external-modules), [Modules Mapping](#modules-mapping-table), [Enabled Modules](#enabled-modules), and [Regions](#regions-table).

## Registered Modules table
<a name="registered-modules"></a>

The Registered Modules table contains modules that are registered and can be enabled or disabled.

Attributes:
+  `registered_module_pk` - Primary key consisting of `module_name` and `region_type`.
+  `module_version` - The version of the module.
+  `category` - Can be one of the following: `Network`, `Identity`, `WorkstationManagement`, `Storage`, `Custom`, or `SpokeRegionInfrastructure`.
+  `input_parameters_hub` Systems Manager parameter inputs for the modules that exist in the hub Region.
+  `input_parameters_local` - Systems Manager parameter inputs for the modules that exist in its local Region (hub or spoke).
+  `is_external` - Boolean value indicating if the module is a Third-Party Module.
+  `module_name` - Name of the module.
+  `region_type` - Indicates whether the module can be enabled in the hub Region, a spoke Region, or both. Can be one of the following: `HUB`, `SPOKE`, or `BOTH`.
+  `servicecatalog_portfolio_id` - MCS Service Catalog portfolio.
+  `servicecatalog_product_id` - Service Catalog product of the module.
+  `status` - Can be one of the following: `REGISTERED`, `REGISTERING IN PROGRESS`, `REGISTER FAILED`, `DE-REGISTERING IN PROGRESS`, `DE-REGISTER FAILED`, or `ENABLING IN PROGRESS`.

## External Modules table
<a name="external-modules"></a>

The External Modules table contains Third-Party Modules that are registered or are available to be registered.

Attributes:
+  `module_name` - Name of the module.
+  `category` - Can be one of the following: `Network`, `Identity`, `WorkstationManagement`, `Storage`, `Custom`, or `SpokeRegionInfrastructure`.
+  `created_at` - When the module was created.
+  `display_name` - Module name to display in the UI.
+  `is_custom` - Indicates whether the module was registered post-deployment of MCS.
+  `manifest_url` - The URL for the manifest.
+  `status` - Can be one of the following: `AVAILABLE`, `REGISTERED`, `REGISTER IN PROGRESS`, `REGISTER FAILED`, `DE-REGISTER IN PROGRESS`, or `DE-REGISTER FAILED`.
+  `updated_at` - When the module was updated.
+  `registered_version` - Semantic version of the registered module. Field is empty if a module is available but not registered.

## Modules Mapping table
<a name="modules-mapping-table"></a>

The Modules Mapping table contains Systems Manager parameter paths and the registered modules that output them.

Attributes:
+  `param_name` - Systems Manager parameter path following the MCS deployment ID.
+  `infrastructure` - Boolean value indicating if the parameter is output by MCS infrastructure.
+  `module_pks` - List of registered modules that output param\_name.

## Enabled Modules table
<a name="enabled-modules"></a>

The Enabled Modules table contains modules that have been enabled.

Attributes:
+  `enabled_module_pk` - Primary key consisting of module\_name, region\_type, and module\_region.
+  `active_dependents` - List of enabled modules that are dependent on this module.
+  `category` - Can be one of the following: `Network`, `Identity`, `WorkstationManagement`, `Storage`, `Custom`, or `SpokeRegionInfrastructure`.
+  `creation_time` - Time that the module was created.
+  `deployment_uuid` - Unique ID assigned when the Service Catalog product is provisioned.
+  `input_parameters` - CloudFormation parameters.
+  `last_update_time` - Time that the module was most recently updated.
+  `module_name` - Name of the module.
+  `module_region` - Region in which the module is enabled.
+  `module_region_category` - Type of Region in which the module is enabled. Can be one of the following: `Hub` or `Spoke`.
+  `module_version` - Version of the module enabled.
+  `region_type` - Indicates whether the module can be enabled in the hub Region, a spoke Region, or both. Can be one of the following: `HUB`, `SPOKE`, or `BOTH`.
+  `servicecatalog_provisioned_product_id` - Service Catalog provisioned product ID for the module enabled.
+  `status` - Can be one of the following: `ENABLED`, `ENABLING IN PROGRESS`, `ENABLE FAILED`, `DISABLED`, `DISABLING IN PROGRESS`, or `DISABLE FAILED`.

## Regions table
<a name="regions-table"></a>

The Regions table consists of AWS Regions that can be enabled or disabled in MCS. The hub Region cannot be disabled.

Attributes:
+  `name` - AWS Region name.
+  `date_enabled` - Date that the Region was enabled.
+  `enablement_status` - Can be one of the following: `ENABLED`, `ENABLING IN PROGRESS`, `ENABLE FAILED`, `DISABLED`, `DISABLING IN PROGRESS`, or `DISABLE FAILED`.
+  `is_hub` - Boolean value indicating if the Region is the hub Region.
+  `provisioned_product_id` - Service Catalog provisioned product ID.

## Lock table
<a name="lock-table"></a>

The Lock table is a distributed locking mechanism that prevents multiple processes from executing the same critical section simultaneously.

Attributes:
+  `lock_name` - Name of the process currently being executed
+  `time_to_live` - TTL timestamp for automatic cleanup

**Note**
DynamoDB automatically deletes items where `time_to_live` date had been expired, but the deletion does not occur instantly after expiration and it can take few days until deletion.
See [Using time to live (TTL) in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) for more details
