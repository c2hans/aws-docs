---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerLatencyPolicy.html
---

# PlayerLatencyPolicy
<a name="API_PlayerLatencyPolicy"></a>

Sets a latency cap for individual players when placing a game session. With a latency policy in force, a game session cannot be placed in a fleet location where a player reports latency higher than the cap. Latency policies are used only with placement request that provide player latency information. Player latency policies can be stacked to gradually relax latency requirements over time.

## Contents
<a name="API_PlayerLatencyPolicy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaximumIndividualPlayerLatencyMilliseconds **   <a name="gameliftservers-Type-PlayerLatencyPolicy-MaximumIndividualPlayerLatencyMilliseconds"></a>
The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PolicyDurationSeconds **   <a name="gameliftservers-Type-PlayerLatencyPolicy-PolicyDurationSeconds"></a>
The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_PlayerLatencyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlayerLatencyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlayerLatencyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlayerLatencyPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
