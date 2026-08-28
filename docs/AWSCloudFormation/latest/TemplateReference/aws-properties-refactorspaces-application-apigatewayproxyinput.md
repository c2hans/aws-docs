---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-refactorspaces-application-apigatewayproxyinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Application ApiGatewayProxyInput
<a name="aws-properties-refactorspaces-application-apigatewayproxyinput"></a>

A wrapper object holding the Amazon API Gateway endpoint input.

## Syntax
<a name="aws-properties-refactorspaces-application-apigatewayproxyinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-refactorspaces-application-apigatewayproxyinput-syntax.json"></a>

```
{
  "[EndpointType](#cfn-refactorspaces-application-apigatewayproxyinput-endpointtype)" : {{String}},
  "[StageName](#cfn-refactorspaces-application-apigatewayproxyinput-stagename)" : {{String}}
}
```

### YAML
<a name="aws-properties-refactorspaces-application-apigatewayproxyinput-syntax.yaml"></a>

```
  [EndpointType](#cfn-refactorspaces-application-apigatewayproxyinput-endpointtype): {{String}}
  [StageName](#cfn-refactorspaces-application-apigatewayproxyinput-stagename): {{String}}
```

## Properties
<a name="aws-properties-refactorspaces-application-apigatewayproxyinput-properties"></a>

`EndpointType`  <a name="cfn-refactorspaces-application-apigatewayproxyinput-endpointtype"></a>
The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to `REGIONAL` by default.
If the value is set to `PRIVATE` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud (Amazon VPC) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint (AWS PrivateLink) availability, see [Access Refactor Spaces using an interface endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html).
*Required*: No
*Type*: String
*Allowed values*: `REGIONAL | PRIVATE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StageName`  <a name="cfn-refactorspaces-application-apigatewayproxyinput-stagename"></a>
The name of the API Gateway stage. The name defaults to `prod`.
*Required*: No
*Type*: String
*Pattern*: `^[-a-zA-Z0-9_]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
