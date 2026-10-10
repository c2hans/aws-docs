---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredgithubservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredGitHubServiceDetails
<a name="aws-properties-devopsagent-service-registeredgithubservicedetails"></a>

<a name="aws-properties-devopsagent-service-registeredgithubservicedetails-description"></a>The `RegisteredGitHubServiceDetails` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-registeredgithubservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredgithubservicedetails-syntax.json"></a>

```
{
  "[AppVariant](#cfn-devopsagent-service-registeredgithubservicedetails-appvariant)" : {{String}},
  "[AuthMode](#cfn-devopsagent-service-registeredgithubservicedetails-authmode)" : {{String}},
  "[HostingType](#cfn-devopsagent-service-registeredgithubservicedetails-hostingtype)" : {{String}},
  "[Owner](#cfn-devopsagent-service-registeredgithubservicedetails-owner)" : {{String}},
  "[OwnerType](#cfn-devopsagent-service-registeredgithubservicedetails-ownertype)" : {{String}},
  "[TargetUrl](#cfn-devopsagent-service-registeredgithubservicedetails-targeturl)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredgithubservicedetails-syntax.yaml"></a>

```
  [AppVariant](#cfn-devopsagent-service-registeredgithubservicedetails-appvariant): {{String}}
  [AuthMode](#cfn-devopsagent-service-registeredgithubservicedetails-authmode): {{String}}
  [HostingType](#cfn-devopsagent-service-registeredgithubservicedetails-hostingtype): {{String}}
  [Owner](#cfn-devopsagent-service-registeredgithubservicedetails-owner): {{String}}
  [OwnerType](#cfn-devopsagent-service-registeredgithubservicedetails-ownertype): {{String}}
  [TargetUrl](#cfn-devopsagent-service-registeredgithubservicedetails-targeturl): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredgithubservicedetails-properties"></a>

`AppVariant`  <a name="cfn-devopsagent-service-registeredgithubservicedetails-appvariant"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `READ_ONLY | READ_WRITE | CUSTOM_APP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthMode`  <a name="cfn-devopsagent-service-registeredgithubservicedetails-authmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `app | pat`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostingType`  <a name="cfn-devopsagent-service-registeredgithubservicedetails-hostingtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `SAAS | SELF_MANAGED | DEDICATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Owner`  <a name="cfn-devopsagent-service-registeredgithubservicedetails-owner"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerType`  <a name="cfn-devopsagent-service-registeredgithubservicedetails-ownertype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `organization | user`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetUrl`  <a name="cfn-devopsagent-service-registeredgithubservicedetails-targeturl"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
