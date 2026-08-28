---
source_url: https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStateEntry.html
---

# UpdateRoutingControlStateEntry
<a name="API_UpdateRoutingControlStateEntry"></a>

A routing control state entry.

## Contents
<a name="API_UpdateRoutingControlStateEntry_Contents"></a>

 ** RoutingControlArn **   <a name="r53recovery-Type-UpdateRoutingControlStateEntry-RoutingControlArn"></a>
The Amazon Resource Name (ARN) for a routing control state entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Za-z0-9:.\/_-]*$`
Required: Yes

 ** RoutingControlState **   <a name="r53recovery-Type-UpdateRoutingControlStateEntry-RoutingControlState"></a>
The routing control state in a set of routing control state entries.
Type: String
Valid Values: `On | Off`
Required: Yes

## See Also
<a name="API_UpdateRoutingControlStateEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStateEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStateEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStateEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query routing-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
