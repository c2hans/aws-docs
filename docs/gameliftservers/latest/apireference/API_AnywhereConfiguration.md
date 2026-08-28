---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AnywhereConfiguration.html
---

# AnywhereConfiguration
<a name="API_AnywhereConfiguration"></a>

Amazon GameLift Servers configuration options for your Anywhere fleets.

## Contents
<a name="API_AnywhereConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Cost **   <a name="gameliftservers-Type-AnywhereConfiguration-Cost"></a>
The cost to run your fleet per hour. Amazon GameLift Servers uses the provided cost of your fleet to balance usage in queues. For more information about queues, see [Setting up queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html) in the *Amazon GameLift Servers Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `^\d{1,5}(?:\.\d{1,5})?$`
Required: Yes

## See Also
<a name="API_AnywhereConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/AnywhereConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/AnywhereConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/AnywhereConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
