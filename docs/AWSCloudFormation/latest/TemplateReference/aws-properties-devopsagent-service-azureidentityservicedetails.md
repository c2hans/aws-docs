---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-azureidentityservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service AzureIdentityServiceDetails
<a name="aws-properties-devopsagent-service-azureidentityservicedetails"></a>

<a name="aws-properties-devopsagent-service-azureidentityservicedetails-description"></a>The `AzureIdentityServiceDetails` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-azureidentityservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-azureidentityservicedetails-syntax.json"></a>

```
{
  "[ClientId](#cfn-devopsagent-service-azureidentityservicedetails-clientid)" : {{String}},
  "[TenantId](#cfn-devopsagent-service-azureidentityservicedetails-tenantid)" : {{String}},
  "[WebIdentityRoleArn](#cfn-devopsagent-service-azureidentityservicedetails-webidentityrolearn)" : {{String}},
  "[WebIdentityTokenAudiences](#cfn-devopsagent-service-azureidentityservicedetails-webidentitytokenaudiences)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-azureidentityservicedetails-syntax.yaml"></a>

```
  [ClientId](#cfn-devopsagent-service-azureidentityservicedetails-clientid): {{String}}
  [TenantId](#cfn-devopsagent-service-azureidentityservicedetails-tenantid): {{String}}
  [WebIdentityRoleArn](#cfn-devopsagent-service-azureidentityservicedetails-webidentityrolearn): {{String}}
  [WebIdentityTokenAudiences](#cfn-devopsagent-service-azureidentityservicedetails-webidentitytokenaudiences): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-service-azureidentityservicedetails-properties"></a>

`ClientId`  <a name="cfn-devopsagent-service-azureidentityservicedetails-clientid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantId`  <a name="cfn-devopsagent-service-azureidentityservicedetails-tenantid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebIdentityRoleArn`  <a name="cfn-devopsagent-service-azureidentityservicedetails-webidentityrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebIdentityTokenAudiences`  <a name="cfn-devopsagent-service-azureidentityservicedetails-webidentitytokenaudiences"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
