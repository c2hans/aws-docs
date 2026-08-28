---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-verifiedaccessendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint
<a name="aws-resource-ec2-verifiedaccessendpoint"></a>

An AWS Verified Access endpoint specifies the application that AWS Verified Access provides access to. It must be attached to an AWS Verified Access group. An AWS Verified Access endpoint must also have an attached access policy before you attached it to a group.

## Syntax
<a name="aws-resource-ec2-verifiedaccessendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-verifiedaccessendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VerifiedAccessEndpoint",
  "Properties" : {
      "[ApplicationDomain](#cfn-ec2-verifiedaccessendpoint-applicationdomain)" : {{String}},
      "[AttachmentType](#cfn-ec2-verifiedaccessendpoint-attachmenttype)" : {{String}},
      "[CidrOptions](#cfn-ec2-verifiedaccessendpoint-cidroptions)" : {{CidrOptions}},
      "[Description](#cfn-ec2-verifiedaccessendpoint-description)" : {{String}},
      "[DomainCertificateArn](#cfn-ec2-verifiedaccessendpoint-domaincertificatearn)" : {{String}},
      "[EndpointDomainPrefix](#cfn-ec2-verifiedaccessendpoint-endpointdomainprefix)" : {{String}},
      "[EndpointType](#cfn-ec2-verifiedaccessendpoint-endpointtype)" : {{String}},
      "[LoadBalancerOptions](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions)" : {{LoadBalancerOptions}},
      "[NetworkInterfaceOptions](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions)" : {{NetworkInterfaceOptions}},
      "[PolicyDocument](#cfn-ec2-verifiedaccessendpoint-policydocument)" : {{String}},
      "[PolicyEnabled](#cfn-ec2-verifiedaccessendpoint-policyenabled)" : {{Boolean}},
      "[RdsOptions](#cfn-ec2-verifiedaccessendpoint-rdsoptions)" : {{RdsOptions}},
      "[SecurityGroupIds](#cfn-ec2-verifiedaccessendpoint-securitygroupids)" : {{[ String, ... ]}},
      "[SseSpecification](#cfn-ec2-verifiedaccessendpoint-ssespecification)" : {{SseSpecification}},
      "[Tags](#cfn-ec2-verifiedaccessendpoint-tags)" : {{[ Tag, ... ]}},
      "[VerifiedAccessGroupId](#cfn-ec2-verifiedaccessendpoint-verifiedaccessgroupid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-verifiedaccessendpoint-syntax.yaml"></a>

```
Type: AWS::EC2::VerifiedAccessEndpoint
Properties:
  [ApplicationDomain](#cfn-ec2-verifiedaccessendpoint-applicationdomain): {{String}}
  [AttachmentType](#cfn-ec2-verifiedaccessendpoint-attachmenttype): {{String}}
  [CidrOptions](#cfn-ec2-verifiedaccessendpoint-cidroptions): {{
    CidrOptions}}
  [Description](#cfn-ec2-verifiedaccessendpoint-description): {{String}}
  [DomainCertificateArn](#cfn-ec2-verifiedaccessendpoint-domaincertificatearn): {{String}}
  [EndpointDomainPrefix](#cfn-ec2-verifiedaccessendpoint-endpointdomainprefix): {{String}}
  [EndpointType](#cfn-ec2-verifiedaccessendpoint-endpointtype): {{String}}
  [LoadBalancerOptions](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions): {{
    LoadBalancerOptions}}
  [NetworkInterfaceOptions](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions): {{
    NetworkInterfaceOptions}}
  [PolicyDocument](#cfn-ec2-verifiedaccessendpoint-policydocument): {{String}}
  [PolicyEnabled](#cfn-ec2-verifiedaccessendpoint-policyenabled): {{Boolean}}
  [RdsOptions](#cfn-ec2-verifiedaccessendpoint-rdsoptions): {{
    RdsOptions}}
  [SecurityGroupIds](#cfn-ec2-verifiedaccessendpoint-securitygroupids): {{
    - String}}
  [SseSpecification](#cfn-ec2-verifiedaccessendpoint-ssespecification): {{
    SseSpecification}}
  [Tags](#cfn-ec2-verifiedaccessendpoint-tags): {{
    - Tag}}
  [VerifiedAccessGroupId](#cfn-ec2-verifiedaccessendpoint-verifiedaccessgroupid): {{String}}
```

## Properties
<a name="aws-resource-ec2-verifiedaccessendpoint-properties"></a>

`ApplicationDomain`  <a name="cfn-ec2-verifiedaccessendpoint-applicationdomain"></a>
The DNS name for users to reach your application.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AttachmentType`  <a name="cfn-ec2-verifiedaccessendpoint-attachmenttype"></a>
The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
*Required*: Yes
*Type*: String
*Allowed values*: `vpc`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CidrOptions`  <a name="cfn-ec2-verifiedaccessendpoint-cidroptions"></a>
The options for a CIDR endpoint.
*Required*: No
*Type*: [CidrOptions](aws-properties-ec2-verifiedaccessendpoint-cidroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ec2-verifiedaccessendpoint-description"></a>
A description for the AWS Verified Access endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainCertificateArn`  <a name="cfn-ec2-verifiedaccessendpoint-domaincertificatearn"></a>
The ARN of a public TLS/SSL certificate imported into or created with ACM.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointDomainPrefix`  <a name="cfn-ec2-verifiedaccessendpoint-endpointdomainprefix"></a>
A custom identifier that is prepended to the DNS name that is generated for the endpoint.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointType`  <a name="cfn-ec2-verifiedaccessendpoint-endpointtype"></a>
The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
*Required*: Yes
*Type*: String
*Allowed values*: `load-balancer | network-interface | rds | cidr`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoadBalancerOptions`  <a name="cfn-ec2-verifiedaccessendpoint-loadbalanceroptions"></a>
The load balancer details if creating the AWS Verified Access endpoint as `load-balancer`type.
*Required*: No
*Type*: [LoadBalancerOptions](aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceOptions`  <a name="cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions"></a>
The options for network-interface type endpoint.
*Required*: No
*Type*: [NetworkInterfaceOptions](aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDocument`  <a name="cfn-ec2-verifiedaccessendpoint-policydocument"></a>
The Verified Access policy document.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyEnabled`  <a name="cfn-ec2-verifiedaccessendpoint-policyenabled"></a>
The status of the Verified Access policy.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RdsOptions`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions"></a>
The options for an RDS endpoint.
*Required*: No
*Type*: [RdsOptions](aws-properties-ec2-verifiedaccessendpoint-rdsoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-ec2-verifiedaccessendpoint-securitygroupids"></a>
The IDs of the security groups for the endpoint.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SseSpecification`  <a name="cfn-ec2-verifiedaccessendpoint-ssespecification"></a>
 The options for additional server side encryption.
*Required*: No
*Type*: [SseSpecification](aws-properties-ec2-verifiedaccessendpoint-ssespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-verifiedaccessendpoint-tags"></a>
The tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-verifiedaccessendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerifiedAccessGroupId`  <a name="cfn-ec2-verifiedaccessendpoint-verifiedaccessgroupid"></a>
The ID of the AWS Verified Access group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-verifiedaccessendpoint-return-values"></a>

### Ref
<a name="aws-resource-ec2-verifiedaccessendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Verified Access endpoint.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-verifiedaccessendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-verifiedaccessendpoint-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time.

`DeviceValidationDomain`  <a name="DeviceValidationDomain-fn::getatt"></a>
Use this to construct the redirect URI to add to your OIDC provider's allow list.

`EndpointDomain`  <a name="EndpointDomain-fn::getatt"></a>
The DNS name generated for the endpoint.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The last updated time.

`Status`  <a name="Status-fn::getatt"></a>
The endpoint status.

`VerifiedAccessEndpointId`  <a name="VerifiedAccessEndpointId-fn::getatt"></a>
The ID of the Verified Access endpoint.

`VerifiedAccessInstanceId`  <a name="VerifiedAccessInstanceId-fn::getatt"></a>
The instance identifier.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
