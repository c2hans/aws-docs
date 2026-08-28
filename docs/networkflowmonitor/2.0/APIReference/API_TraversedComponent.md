---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TraversedComponent.html
---

# TraversedComponent
<a name="API_TraversedComponent"></a>

A section of the network that a network flow has traveled through.

## Contents
<a name="API_TraversedComponent_Contents"></a>

 ** componentArn **   <a name="networkflowmonitor-Type-TraversedComponent-componentArn"></a>
The Amazon Resource Name (ARN) of a traversed component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** componentId **   <a name="networkflowmonitor-Type-TraversedComponent-componentId"></a>
The identifier for the traversed component.
Type: String
Required: No

 ** componentType **   <a name="networkflowmonitor-Type-TraversedComponent-componentType"></a>
The type of component that was traversed.
Type: String
Required: No

 ** serviceName **   <a name="networkflowmonitor-Type-TraversedComponent-serviceName"></a>
The service name for the traversed component.
Type: String
Required: No

## See Also
<a name="API_TraversedComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/TraversedComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/TraversedComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/TraversedComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
