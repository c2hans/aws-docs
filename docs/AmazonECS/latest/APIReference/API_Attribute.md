---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Attribute.html
---

# Attribute
<a name="API_Attribute"></a>

An attribute is a name-value pair that's associated with an Amazon ECS object. Use attributes to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see [Attributes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_Attribute_Contents"></a>

 ** name **   <a name="ECS-Type-Attribute-name"></a>
The name of the attribute. The `name` must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (\_), forward slashes (/), back slashes (\\), or periods (.).
Type: String
Required: Yes

 ** targetId **   <a name="ECS-Type-Attribute-targetId"></a>
The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
Type: String
Required: No

 ** targetType **   <a name="ECS-Type-Attribute-targetType"></a>
The type of the target to attach the attribute with. This parameter is required if you use the short form ID for a resource instead of the full ARN.
Type: String
Valid Values: `container-instance`
Required: No

 ** value **   <a name="ECS-Type-Attribute-value"></a>
The value of the attribute. The `value` must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (\_), periods (.), at signs (@), forward slashes (/), back slashes (\\), colons (:), or spaces. The value can't start or end with a space.
Type: String
Required: No

## See Also
<a name="API_Attribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Attribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Attribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Attribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
