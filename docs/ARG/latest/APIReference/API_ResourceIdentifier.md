---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ResourceIdentifier.html
---

# ResourceIdentifier
<a name="API_ResourceIdentifier"></a>

A structure that contains the ARN of a resource and its resource type.

## Contents
<a name="API_ResourceIdentifier_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceArn **   <a name="ARG-Type-ResourceIdentifier-ResourceArn"></a>
The Amazon resource name (ARN) of a resource.
Type: String
Pattern: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`
Required: No

 ** ResourceType **   <a name="ARG-Type-ResourceIdentifier-ResourceType"></a>
The resource type of a resource, such as `AWS::EC2::Instance`.
Type: String
Pattern: `AWS::[a-zA-Z0-9]+::\w+`
Required: No

## See Also
<a name="API_ResourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ResourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ResourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ResourceIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
