---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LocationAttributes.html
---

# LocationAttributes
<a name="API_LocationAttributes"></a>

Details about a location in a multi-location fleet.

## Contents
<a name="API_LocationAttributes_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LocationState **   <a name="gameliftservers-Type-LocationAttributes-LocationState"></a>
A fleet location and its current life-cycle state.
Type: [LocationState](API_LocationState.md) object
Required: No

 ** StoppedActions **   <a name="gameliftservers-Type-LocationAttributes-StoppedActions"></a>
A list of fleet actions that have been suspended in the fleet location.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `AUTO_SCALING`
Required: No

 ** UpdateStatus **   <a name="gameliftservers-Type-LocationAttributes-UpdateStatus"></a>
The status of fleet activity updates to the location. The status `PENDING_UPDATE` indicates that `StopFleetActions` or `StartFleetActions` has been requested but the update has not yet been completed for the location.
Type: String
Valid Values: `PENDING_UPDATE`
Required: No

## See Also
<a name="API_LocationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LocationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LocationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LocationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
