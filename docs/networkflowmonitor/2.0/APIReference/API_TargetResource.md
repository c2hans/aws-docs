---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TargetResource.html
---

# TargetResource
<a name="API_TargetResource"></a>

A target resource in a scope. The resource is identified by a Region and an account, defined by a target identifier. A target identifier is made up of a target ID (currently always an account ID) and a target type (currently always `ACCOUNT`).

## Contents
<a name="API_TargetResource_Contents"></a>

 ** region **   <a name="networkflowmonitor-Type-TargetResource-region"></a>
The AWS Region for the scope.
Type: String
Required: Yes

 ** targetIdentifier **   <a name="networkflowmonitor-Type-TargetResource-targetIdentifier"></a>
A target identifier is a pair of identifying information for a scope. A target identifier is made up of a targetID (currently always an account ID) and a targetType (currently always an account).
Type: [TargetIdentifier](API_TargetIdentifier.md) object
Required: Yes

## See Also
<a name="API_TargetResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/TargetResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/TargetResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/TargetResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
