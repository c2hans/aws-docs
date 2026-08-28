---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PriorityConfigurationOverride.html
---

# PriorityConfigurationOverride
<a name="API_PriorityConfigurationOverride"></a>

An alternate list of prioritized locations for use with a game session queue. When this property is included in a [StartGameSessionPlacement](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html) request, the alternate list overrides the queue's default location priorities, as defined in the queue's [PriorityConfiguration](gamelift/latest/apireference/API_PriorityConfiguration.html) setting (*LocationOrder*). The override is valid for an individual placement request only. Use this property only with queues that have a `PriorityConfiguration` setting that prioritizes `LOCATION` first.

**Note**
A priority configuration override list does not override a queue's FilterConfiguration setting, if the queue has one. Filter configurations are used to limit placements to a subset of the locations in a queue's destinations. If the override list includes a location that's not on in the `FilterConfiguration` allowed list, Amazon GameLift Servers won't attempt to place a game session there.

## Contents
<a name="API_PriorityConfigurationOverride_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LocationOrder **   <a name="gameliftservers-Type-PriorityConfigurationOverride-LocationOrder"></a>
A prioritized list of hosting locations. The list can include AWS Regions (such as `us-west-2`), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift Servers service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: Yes

 ** PlacementFallbackStrategy **   <a name="gameliftservers-Type-PriorityConfigurationOverride-PlacementFallbackStrategy"></a>
Instructions for how to proceed if placement fails in every location on the priority override list. Valid strategies include:
+  `DEFAULT_AFTER_SINGLE_PASS` -- After attempting to place a new game session in every location on the priority override list, try to place a game session in queue's other locations. This is the default behavior.
+  `NONE` -- Limit placements to locations on the priority override list only.
Type: String
Valid Values: `DEFAULT_AFTER_SINGLE_PASS | NONE`
Required: No

## See Also
<a name="API_PriorityConfigurationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PriorityConfigurationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PriorityConfigurationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PriorityConfigurationOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
