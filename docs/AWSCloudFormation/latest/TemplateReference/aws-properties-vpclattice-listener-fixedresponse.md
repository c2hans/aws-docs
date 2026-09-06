---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-listener-fixedresponse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Listener FixedResponse
<a name="aws-properties-vpclattice-listener-fixedresponse"></a>

Describes an action that returns a custom HTTP response.

## Syntax
<a name="aws-properties-vpclattice-listener-fixedresponse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-listener-fixedresponse-syntax.json"></a>

```
{
  "[StatusCode](#cfn-vpclattice-listener-fixedresponse-statuscode)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-vpclattice-listener-fixedresponse-syntax.yaml"></a>

```
  [StatusCode](#cfn-vpclattice-listener-fixedresponse-statuscode): {{Integer}}
```

## Properties
<a name="aws-properties-vpclattice-listener-fixedresponse-properties"></a>

`StatusCode`  <a name="cfn-vpclattice-listener-fixedresponse-statuscode"></a>
The HTTP response code. Only `404` and `500` status codes are supported.
*Required*: Yes
*Type*: Integer
*Minimum*: `100`
*Maximum*: `599`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
