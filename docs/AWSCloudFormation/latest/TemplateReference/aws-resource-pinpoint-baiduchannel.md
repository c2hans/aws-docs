---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pinpoint-baiduchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::BaiduChannel
<a name="aws-resource-pinpoint-baiduchannel"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the Baidu channel to send notifications to the Baidu Cloud Push notification service. Before you can use Amazon Pinpoint to send notifications to the Baidu Cloud Push service, you have to enable the Baidu channel for an Amazon Pinpoint application.

The BaiduChannel resource represents the status and authentication settings of the Baidu channel for an application.

## Syntax
<a name="aws-resource-pinpoint-baiduchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pinpoint-baiduchannel-syntax.json"></a>

```
{
  "Type" : "AWS::Pinpoint::BaiduChannel",
  "Properties" : {
      "[ApiKey](#cfn-pinpoint-baiduchannel-apikey)" : {{String}},
      "[ApplicationId](#cfn-pinpoint-baiduchannel-applicationid)" : {{String}},
      "[Enabled](#cfn-pinpoint-baiduchannel-enabled)" : {{Boolean}},
      "[SecretKey](#cfn-pinpoint-baiduchannel-secretkey)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pinpoint-baiduchannel-syntax.yaml"></a>

```
Type: AWS::Pinpoint::BaiduChannel
Properties:
  [ApiKey](#cfn-pinpoint-baiduchannel-apikey): {{String}}
  [ApplicationId](#cfn-pinpoint-baiduchannel-applicationid): {{String}}
  [Enabled](#cfn-pinpoint-baiduchannel-enabled): {{Boolean}}
  [SecretKey](#cfn-pinpoint-baiduchannel-secretkey): {{String}}
```

## Properties
<a name="aws-resource-pinpoint-baiduchannel-properties"></a>

`ApiKey`  <a name="cfn-pinpoint-baiduchannel-apikey"></a>
The API key that you received from the Baidu Cloud Push service to communicate with the service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-pinpoint-baiduchannel-applicationid"></a>
The unique identifier for the Amazon Pinpoint application that you're configuring the Baidu channel for.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Enabled`  <a name="cfn-pinpoint-baiduchannel-enabled"></a>
Specifies whether to enable the Baidu channel for the application.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretKey`  <a name="cfn-pinpoint-baiduchannel-secretkey"></a>
The secret key that you received from the Baidu Cloud Push service to communicate with the service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pinpoint-baiduchannel-return-values"></a>

### Ref
<a name="aws-resource-pinpoint-baiduchannel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier (`ApplicationId`) for the Amazon Pinpoint application that the channel is associated with.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-pinpoint-baiduchannel-return-values-fn--getatt"></a>

####
<a name="aws-resource-pinpoint-baiduchannel-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
(Deprecated) An identifier for the Baidu channel. This property is retained only for backward compatibility.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
