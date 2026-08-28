---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PriorityConfiguration.html
---

# PriorityConfiguration
<a name="API_PriorityConfiguration"></a>

Custom prioritization settings to use with a game session queue. Prioritization settings determine how the queue selects a game hosting resource to start a new game session. This configuration replaces the default prioritization process for queues.

By default, a queue makes game session placements based on the following criteria:
+ When a game session request does not include player latency data, Amazon GameLift Servers places game sessions based on the following priorities: (1) the queue's default destination order, and (2) for multi-location fleets, an alphabetic list of locations.
+ When a game session request includes player latency data, Amazon GameLift Servers re-orders the queue's destinations to make placements where the average player latency is lowest. It reorders based the following priorities: (1) the lowest average latency across all players, (2) the lowest hosting cost, (3) the queue's default destination order, and (4) for multi-location fleets, an alphabetic list of locations.

## Contents
<a name="API_PriorityConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LocationOrder **   <a name="gameliftservers-Type-PriorityConfiguration-LocationOrder"></a>
The prioritization order to use for fleet locations, when the `PriorityOrder` property includes `LOCATION`. Locations can include AWS Region codes (such as `us-west-2`), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift Servers service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** PriorityOrder **   <a name="gameliftservers-Type-PriorityConfiguration-PriorityOrder"></a>
A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once.
+  `LATENCY` -- Amazon GameLift Servers prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request.
+  `COST` -- Amazon GameLift Servers prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destination's location, instance type, and fleet type (Spot or On-Demand).
+  `DESTINATION` -- Amazon GameLift Servers prioritizes based on the list order of destinations in the queue configuration.
+  `LOCATION` -- Amazon GameLift Servers prioritizes based on the provided order of locations, as defined in `LocationOrder`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `LATENCY | COST | DESTINATION | LOCATION`
Required: No

## See Also
<a name="API_PriorityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PriorityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PriorityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PriorityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
