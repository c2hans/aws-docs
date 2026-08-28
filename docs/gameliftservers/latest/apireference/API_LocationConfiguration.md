---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LocationConfiguration.html
---

# LocationConfiguration
<a name="API_LocationConfiguration"></a>

A remote location where a multi-location fleet can deploy game servers for game hosting.

## Contents
<a name="API_LocationConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Location **   <a name="gameliftservers-Type-LocationConfiguration-Location"></a>
An AWS Region code, such as `us-west-2`. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: Yes

## See Also
<a name="API_LocationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LocationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LocationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LocationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
