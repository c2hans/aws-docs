---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LocationState.html
---

# LocationState
<a name="API_LocationState"></a>

A fleet location and its life-cycle state. A location state object might be used to describe a fleet's remote location or home Region. Life-cycle state tracks the progress of launching the first instance in a new location and preparing it for game hosting, and then removing all instances and deleting the location from the fleet.
+  **NEW** -- A new fleet location has been defined and desired instances is set to 1.
+  **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift Servers is setting up the new fleet location, creating new instances with the game build or Realtime script and starting server processes.
+  **ACTIVE** -- Hosts can now accept game sessions.
+  **ERROR** -- An error occurred when downloading, validating, building, or activating the fleet location.
+  **DELETING** -- Hosts are responding to a delete fleet location request.
+  **TERMINATED** -- The fleet location no longer exists.
+  **NOT\_FOUND** -- The fleet location was not found. This could be because the custom location was removed or not created.

## Contents
<a name="API_LocationState_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Location **   <a name="gameliftservers-Type-LocationState-Location"></a>
The fleet location, expressed as an AWS Region code such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** PlayerGatewayStatus **   <a name="gameliftservers-Type-LocationState-PlayerGatewayStatus"></a>
The current status of player gateway in this location for this fleet. Note, even if a fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+  `ENABLED` -- Player gateway is available for this fleet location.
+  `DISABLED` -- Player gateway is not available for this fleet location.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** Status **   <a name="gameliftservers-Type-LocationState-Status"></a>
The life-cycle status of a fleet location.
Type: String
Valid Values: `NEW | DOWNLOADING | VALIDATING | BUILDING | ACTIVATING | ACTIVE | DELETING | ERROR | TERMINATED | NOT_FOUND`
Required: No

## See Also
<a name="API_LocationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LocationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LocationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LocationState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
