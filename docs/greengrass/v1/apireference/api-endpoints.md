---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/api-endpoints.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Endpoints
<a name="api-endpoints"></a>

**Topics**
+ [/greengrass/bulk/deployments](-greengrass-bulk-deployments.md)
+ [/greengrass/bulk/deployments/BulkDeploymentId/$stop](-greengrass-bulk-deployments-bulkdeploymentid-stop.md)
+ [/greengrass/bulk/deployments/BulkDeploymentId/detailed-reports](-greengrass-bulk-deployments-bulkdeploymentid-detailed-reports.md)
+ [/greengrass/bulk/deployments/BulkDeploymentId/status](-greengrass-bulk-deployments-bulkdeploymentid-status.md)
+ [/greengrass/definition/connectors](-greengrass-definition-connectors.md)
+ [/greengrass/definition/connectors/ConnectorDefinitionId](-greengrass-definition-connectors-connectordefinitionid.md)
+ [/greengrass/definition/connectors/ConnectorDefinitionId/versions](-greengrass-definition-connectors-connectordefinitionid-versions.md)
+ [/greengrass/definition/connectors/ConnectorDefinitionId/versions/ConnectorDefinitionVersionId](-greengrass-definition-connectors-connectordefinitionid-versions-connectordefinitionversionid.md)
+ [/greengrass/definition/cores](-greengrass-definition-cores.md)
+ [/greengrass/definition/cores/CoreDefinitionId](-greengrass-definition-cores-coredefinitionid.md)
+ [/greengrass/definition/cores/CoreDefinitionId/versions](-greengrass-definition-cores-coredefinitionid-versions.md)
+ [/greengrass/definition/cores/CoreDefinitionId/versions/CoreDefinitionVersionId](-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid.md)
+ [/greengrass/definition/devices](-greengrass-definition-devices.md)
+ [/greengrass/definition/devices/DeviceDefinitionId](-greengrass-definition-devices-devicedefinitionid.md)
+ [/greengrass/definition/devices/DeviceDefinitionId/versions](-greengrass-definition-devices-devicedefinitionid-versions.md)
+ [/greengrass/definition/devices/DeviceDefinitionId/versions/DeviceDefinitionVersionId](-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid.md)
+ [/greengrass/definition/functions](-greengrass-definition-functions.md)
+ [/greengrass/definition/functions/FunctionDefinitionId](-greengrass-definition-functions-functiondefinitionid.md)
+ [/greengrass/definition/functions/FunctionDefinitionId/versions](-greengrass-definition-functions-functiondefinitionid-versions.md)
+ [/greengrass/definition/functions/FunctionDefinitionId/versions/FunctionDefinitionVersionId](-greengrass-definition-functions-functiondefinitionid-versions-functiondefinitionversionid.md)
+ [/greengrass/definition/loggers](-greengrass-definition-loggers.md)
+ [/greengrass/definition/loggers/LoggerDefinitionId](-greengrass-definition-loggers-loggerdefinitionid.md)
+ [/greengrass/definition/loggers/LoggerDefinitionId/versions](-greengrass-definition-loggers-loggerdefinitionid-versions.md)
+ [/greengrass/definition/loggers/LoggerDefinitionId/versions/LoggerDefinitionVersionId](-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid.md)
+ [/greengrass/definition/resources](-greengrass-definition-resources.md)
+ [/greengrass/definition/resources/ResourceDefinitionId](-greengrass-definition-resources-resourcedefinitionid.md)
+ [/greengrass/definition/resources/ResourceDefinitionId/versions](-greengrass-definition-resources-resourcedefinitionid-versions.md)
+ [/greengrass/definition/resources/ResourceDefinitionId/versions/ResourceDefinitionVersionId](-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid.md)
+ [/greengrass/definition/subscriptions](-greengrass-definition-subscriptions.md)
+ [/greengrass/definition/subscriptions/SubscriptionDefinitionId](-greengrass-definition-subscriptions-subscriptiondefinitionid.md)
+ [/greengrass/definition/subscriptions/SubscriptionDefinitionId/versions](-greengrass-definition-subscriptions-subscriptiondefinitionid-versions.md)
+ [/greengrass/definition/subscriptions/SubscriptionDefinitionId/versions/SubscriptionDefinitionVersionId](-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid.md)
+ [/greengrass/groups](-greengrass-groups.md)
+ [/greengrass/groups/GroupId](-greengrass-groups-groupid.md)
+ [/greengrass/groups/GroupId/certificateauthorities](-greengrass-groups-groupid-certificateauthorities.md)
+ [/greengrass/groups/GroupId/certificateauthorities/configuration/expiry](-greengrass-groups-groupid-certificateauthorities-configuration-expiry.md)
+ [/greengrass/groups/GroupId/certificateauthorities/CertificateAuthorityId](-greengrass-groups-groupid-certificateauthorities-certificateauthorityid.md)
+ [/greengrass/groups/GroupId/deployments](-greengrass-groups-groupid-deployments.md)
+ [/greengrass/groups/GroupId/deployments/$reset](-greengrass-groups-groupid-deployments-reset.md)
+ [/greengrass/groups/GroupId/deployments/DeploymentId/status](-greengrass-groups-groupid-deployments-deploymentid-status.md)
+ [/greengrass/groups/GroupId/role](-greengrass-groups-groupid-role.md)
+ [/greengrass/groups/GroupId/versions](-greengrass-groups-groupid-versions.md)
+ [/greengrass/groups/GroupId/versions/GroupVersionId](-greengrass-groups-groupid-versions-groupversionid.md)
+ [/greengrass/servicerole](-greengrass-servicerole.md)
+ [/greengrass/things/ThingName/connectivityInfo](-greengrass-things-thingname-connectivityinfo.md)
+ [/greengrass/things/ThingName/runtimeconfig](-greengrass-things-thingname-runtimeconfig.md)
+ [/greengrass/updates](-greengrass-updates.md)
+ [/tags/resource-arn](-tags-resource-arn.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
