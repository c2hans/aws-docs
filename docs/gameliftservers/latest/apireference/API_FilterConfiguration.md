---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_FilterConfiguration.html
---

# FilterConfiguration
<a name="API_FilterConfiguration"></a>

A list of fleet locations where a game session queue can place new game sessions. You can use a filter to temporarily exclude specific locations from receiving placements. For queues that have multi-location fleets, you can use a filter configuration allow placement with some, but not all, of a fleet's locations.

## Contents
<a name="API_FilterConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllowedLocations **   <a name="gameliftservers-Type-FilterConfiguration-AllowedLocations"></a>
 A list of locations to allow game session placement in, in the form of AWS Region codes such as `us-west-2`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

## See Also
<a name="API_FilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/FilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/FilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/FilterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
