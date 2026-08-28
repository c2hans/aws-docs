---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediastore-container.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaStore::Container
<a name="aws-resource-mediastore-container"></a>

The AWS::MediaStore::Container resource specifies a storage container to hold objects. A container is similar to a bucket in Amazon S3.

When you create a container using CloudFormation, the template manages data for five API actions: creating a container, setting access logging, updating the default container policy, adding a cross-origin resource sharing (CORS) policy, and adding an object lifecycle policy.

## Syntax
<a name="aws-resource-mediastore-container-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediastore-container-syntax.json"></a>

```
{
  "Type" : "AWS::MediaStore::Container",
  "Properties" : {
      "[AccessLoggingEnabled](#cfn-mediastore-container-accessloggingenabled)" : {{Boolean}},
      "[ContainerName](#cfn-mediastore-container-containername)" : {{String}},
      "[CorsPolicy](#cfn-mediastore-container-corspolicy)" : {{[ CorsRule, ... ]}},
      "[LifecyclePolicy](#cfn-mediastore-container-lifecyclepolicy)" : {{String}},
      "[MetricPolicy](#cfn-mediastore-container-metricpolicy)" : {{MetricPolicy}},
      "[Policy](#cfn-mediastore-container-policy)" : {{String}},
      "[Tags](#cfn-mediastore-container-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediastore-container-syntax.yaml"></a>

```
Type: AWS::MediaStore::Container
Properties:
  [AccessLoggingEnabled](#cfn-mediastore-container-accessloggingenabled): {{Boolean}}
  [ContainerName](#cfn-mediastore-container-containername): {{String}}
  [CorsPolicy](#cfn-mediastore-container-corspolicy): {{
    - CorsRule}}
  [LifecyclePolicy](#cfn-mediastore-container-lifecyclepolicy): {{String}}
  [MetricPolicy](#cfn-mediastore-container-metricpolicy): {{
    MetricPolicy}}
  [Policy](#cfn-mediastore-container-policy): {{String}}
  [Tags](#cfn-mediastore-container-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediastore-container-properties"></a>

`AccessLoggingEnabled`  <a name="cfn-mediastore-container-accessloggingenabled"></a>
The state of access logging on the container. This value is `false` by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to `true`, indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerName`  <a name="cfn-mediastore-container-containername"></a>
The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named `movies` in every region, as long as you don’t have an existing container with that name.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CorsPolicy`  <a name="cfn-mediastore-container-corspolicy"></a>
End of support notice: On November 13, 2025, AWS will discontinue support for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the AWS Elemental MediaStore console or AWS Elemental MediaStore resources. For more information, visit this [blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/).
Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability.
To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
To learn more about CORS, see [Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html).
*Required*: No
*Type*: Array of [CorsRule](aws-properties-mediastore-container-corsrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecyclePolicy`  <a name="cfn-mediastore-container-lifecyclepolicy"></a>
End of support notice: On November 13, 2025, AWS will discontinue support for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the AWS Elemental MediaStore console or AWS Elemental MediaStore resources. For more information, visit this [blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/).
Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect.
For information about how to construct an object lifecycle policy, see [Components of an Object Lifecycle Policy](https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricPolicy`  <a name="cfn-mediastore-container-metricpolicy"></a>
The metric policy that is associated with the container. A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include rules to define groups of objects that you want MediaStore to send object-level metrics for.
To view examples of how to construct a metric policy for your use case, see [Example Metric Policies](https://docs.aws.amazon.com/mediastore/latest/ug/policies-metric-examples.html).
*Required*: No
*Type*: [MetricPolicy](aws-properties-mediastore-container-metricpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policy`  <a name="cfn-mediastore-container-policy"></a>
Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/iam/).
For this release of the REST API, you can create only one policy for a container. If you enter `PutContainerPolicy` twice, the second command modifies the existing policy.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediastore-container-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediastore-container-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediastore-container-return-values"></a>

### Ref
<a name="aws-resource-mediastore-container-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the container.

For example: `{ "Ref": "myContainer" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediastore-container-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediastore-container-return-values-fn--getatt-fn--getatt"></a>

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
