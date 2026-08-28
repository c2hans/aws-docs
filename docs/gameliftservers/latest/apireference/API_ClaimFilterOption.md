---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ClaimFilterOption.html
---

# ClaimFilterOption
<a name="API_ClaimFilterOption"></a>

 Filters which game servers may be claimed when calling `ClaimGameServer`.

## Contents
<a name="API_ClaimFilterOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InstanceStatuses **   <a name="gameliftservers-Type-ClaimFilterOption-InstanceStatuses"></a>
List of instance statuses that game servers may be claimed on. If provided, the list must contain the `ACTIVE` status.
Type: Array of strings
Valid Values: `ACTIVE | DRAINING`
Required: No

## See Also
<a name="API_ClaimFilterOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ClaimFilterOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ClaimFilterOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ClaimFilterOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
