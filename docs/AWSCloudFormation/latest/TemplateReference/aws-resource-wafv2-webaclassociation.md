---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafv2-webaclassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACLAssociation
<a name="aws-resource-wafv2-webaclassociation"></a>

**Note**
This is the latest version of ** AWS WAF **, named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the [AWS WAF developer guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).

Use a web ACL association to define an association between a web ACL and a regional application resource, to protect the resource. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AWS AppSync GraphQL API, an Amazon Cognito user pool, an AWS App Runner service, an AWS Amplify application, or an AWS Verified Access instance.

For Amazon CloudFront, don't use this resource. Instead, use your CloudFront distribution configuration. To associate a web ACL with a distribution, provide the Amazon Resource Name (ARN) of the [AWS::WAFv2::WebACL](aws-resource-wafv2-webacl.md) to your CloudFront distribution configuration. To disassociate a web ACL, provide an empty ARN. For information, see [AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html).

 **Required permissions for customer-managed IAM policies**

This call requires permissions that are specific to the protected resource type. For details, see [Permissions for AssociateWebACL](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL) in the *AWS WAF Developer Guide*.

 **Temporary inconsistencies during updates**

When you create or change a web ACL or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:
+ After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable.
+ After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.
+ After you change a rule action setting, you might see the old action in some places and the new action in others.
+ After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

## Syntax
<a name="aws-resource-wafv2-webaclassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wafv2-webaclassociation-syntax.json"></a>

```
{
  "Type" : "AWS::WAFv2::WebACLAssociation",
  "Properties" : {
      "[ResourceArn](#cfn-wafv2-webaclassociation-resourcearn)" : {{String}},
      "[WebACLArn](#cfn-wafv2-webaclassociation-webaclarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wafv2-webaclassociation-syntax.yaml"></a>

```
Type: AWS::WAFv2::WebACLAssociation
Properties:
  [ResourceArn](#cfn-wafv2-webaclassociation-resourcearn): {{String}}
  [WebACLArn](#cfn-wafv2-webaclassociation-webaclarn): {{String}}
```

## Properties
<a name="aws-resource-wafv2-webaclassociation-properties"></a>

`ResourceArn`  <a name="cfn-wafv2-webaclassociation-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource to associate with the web ACL.
The ARN must be in one of the following formats:
+ For an Application Load Balancer: `arn:partition:elasticloadbalancing:region:account-id:loadbalancer/app/load-balancer-name/load-balancer-id`
+ For an Amazon API Gateway REST API: `arn:partition:apigateway:region::/restapis/api-id/stages/stage-name`
+ For an AWS AppSync GraphQL API: `arn:partition:appsync:region:account-id:apis/GraphQLApiId`
+ For an Amazon Cognito user pool: `arn:partition:cognito-idp:region:account-id:userpool/user-pool-id`
+ For an AWS App Runner service: `arn:partition:apprunner:region:account-id:service/apprunner-service-name/apprunner-service-id`
+ For an AWS Verified Access instance: `arn:partition:ec2:region:account-id:verified-access-instance/instance-id`
+ For an AWS Amplify instance: `arn:partition:amplify:region:account-id:apps/app-id`
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WebACLArn`  <a name="cfn-wafv2-webaclassociation-webaclarn"></a>
The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wafv2-webaclassociation-return-values"></a>

### Ref
<a name="aws-resource-wafv2-webaclassociation-return-values-ref"></a>

The `Ref` for the resource, containing the resource name, physical ID, and scope, formatted as follows: `name|id|scope`.

For example: `my-webacl-name|1234a1a-a1b1-12a1-abcd-a123b123456|REGIONAL`.

## Examples
<a name="aws-resource-wafv2-webaclassociation--examples"></a>

### Create a web ACL association
<a name="aws-resource-wafv2-webaclassociation--examples--Create_a_web_ACL_association"></a>

The following shows an example web ACL association specification.

#### YAML
<a name="aws-resource-wafv2-webaclassociation--examples--Create_a_web_ACL_association--yaml"></a>

```
  SampleWebACLAssociation:
    Type: 'AWS::WAFv2::WebACLAssociation'
    Properties:
      WebACLArn: ExampleARNForWebACL
      ResourceArn: ExampleARNForRegionalResource
```

#### JSON
<a name="aws-resource-wafv2-webaclassociation--examples--Create_a_web_ACL_association--json"></a>

```
  "SampleWebACLAssociation": {
    "Type": "AWS::WAFv2::WebACLAssociation",
    "Properties": {
      "WebACLArn": "WebACLArn",
      "ResourceArn": "APIGatewayOrALBArn"
    }
  }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
