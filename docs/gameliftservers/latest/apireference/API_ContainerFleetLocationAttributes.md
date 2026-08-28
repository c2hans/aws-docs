---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerFleetLocationAttributes.html
---

# ContainerFleetLocationAttributes
<a name="API_ContainerFleetLocationAttributes"></a>

Details about a location in a multi-location container fleet.

## Contents
<a name="API_ContainerFleetLocationAttributes_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Location **   <a name="gameliftservers-Type-ContainerFleetLocationAttributes-Location"></a>
A location identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** PlayerGatewayStatus **   <a name="gameliftservers-Type-ContainerFleetLocationAttributes-PlayerGatewayStatus"></a>
The current status of player gateway in this location for this container fleet. Note, even if a container fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+  `ENABLED` -- Player gateway is available for this container fleet location.
+  `DISABLED` -- Player gateway is not available for this container fleet location.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** Status **   <a name="gameliftservers-Type-ContainerFleetLocationAttributes-Status"></a>
The status of fleet activity in the location.
+  `PENDING` -- A new container fleet has been requested.
+  `CREATING` -- A new container fleet resource is being created.
+  `CREATED` -- A new container fleet resource has been created. No fleet instances have been deployed.
+  `ACTIVATING` -- New container fleet instances are being deployed.
+  `ACTIVE` -- The container fleet has been deployed and is ready to host game sessions.
+  `UPDATING` -- Updates to the container fleet is being updated. A deployment is in progress.
+  `EXPIRED` -- The container fleet has been expired. The fleet is scaled down to zero instances and cannot host new game sessions.
Type: String
Valid Values: `PENDING | CREATING | CREATED | ACTIVATING | ACTIVE | UPDATING | DELETING`
Required: No

## See Also
<a name="API_ContainerFleetLocationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerFleetLocationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerFleetLocationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerFleetLocationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
