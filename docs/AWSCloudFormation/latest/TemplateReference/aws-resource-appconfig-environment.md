---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Environment
<a name="aws-resource-appconfig-environment"></a>

The `AWS::AppConfig::Environment` resource creates an environment, which is a logical deployment group of AWS AppConfig targets, such as applications in a `Beta` or `Production` environment. You define one or more environments for each AWS AppConfig application. You can also define environments for application subcomponents such as the `Web`, `Mobile` and `Back-end` components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

AWS AppConfig requires that you create resources and deploy a configuration in the following order:

1. Create an application

1. Create an environment

1. Create a configuration profile

1. Choose a pre-defined deployment strategy or create your own

1. Deploy the configuration

For more information, see [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) in the *AWS AppConfig User Guide*.

## Syntax
<a name="aws-resource-appconfig-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appconfig-environment-syntax.json"></a>

```
{
  "Type" : "AWS::AppConfig::Environment",
  "Properties" : {
      "[ApplicationId](#cfn-appconfig-environment-applicationid)" : {{String}},
      "[DeletionProtectionCheck](#cfn-appconfig-environment-deletionprotectioncheck)" : {{String}},
      "[Description](#cfn-appconfig-environment-description)" : {{String}},
      "[Monitors](#cfn-appconfig-environment-monitors)" : {{[ Monitor, ... ]}},
      "[Name](#cfn-appconfig-environment-name)" : {{String}},
      "[Tags](#cfn-appconfig-environment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appconfig-environment-syntax.yaml"></a>

```
Type: AWS::AppConfig::Environment
Properties:
  [ApplicationId](#cfn-appconfig-environment-applicationid): {{String}}
  [DeletionProtectionCheck](#cfn-appconfig-environment-deletionprotectioncheck): {{String}}
  [Description](#cfn-appconfig-environment-description): {{String}}
  [Monitors](#cfn-appconfig-environment-monitors): {{
    - Monitor}}
  [Name](#cfn-appconfig-environment-name): {{String}}
  [Tags](#cfn-appconfig-environment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-appconfig-environment-properties"></a>

`ApplicationId`  <a name="cfn-appconfig-environment-applicationid"></a>
The ID or name of the application.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9]{4,7}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeletionProtectionCheck`  <a name="cfn-appconfig-environment-deletionprotectioncheck"></a>
A parameter to configure deletion protection. Deletion protection prevents a user from deleting an environment if your application called either [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html) in the environment during the specified interval.
This parameter supports the following values:
+ `BYPASS`: Instructs AWS AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it.
+ `APPLY`: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. `APPLY` also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks.
+ `ACCOUNT_DEFAULT`: The default setting, which instructs AWS AppConfig to implement the deletion protection value specified in the `UpdateAccountSettings` API.
*Required*: No
*Type*: String
*Allowed values*: `ACCOUNT_DEFAULT | APPLY | BYPASS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appconfig-environment-description"></a>
A description of the environment.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monitors`  <a name="cfn-appconfig-environment-monitors"></a>
Amazon CloudWatch alarms to monitor during the deployment process.
*Required*: No
*Type*: Array of [Monitor](aws-properties-appconfig-environment-monitor.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appconfig-environment-name"></a>
A name for the environment.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appconfig-environment-tags"></a>
Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
*Required*: No
*Type*: Array of [Tag](aws-properties-appconfig-environment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appconfig-environment-return-values"></a>

### Ref
<a name="aws-resource-appconfig-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the environment ID.

### Fn::GetAtt
<a name="aws-resource-appconfig-environment-return-values-fn--getatt"></a>

####
<a name="aws-resource-appconfig-environment-return-values-fn--getatt-fn--getatt"></a>

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The environment ID.

## Examples
<a name="aws-resource-appconfig-environment--examples"></a>

### AWS AppConfig environment example
<a name="aws-resource-appconfig-environment--examples--environment_example"></a>

The following example creates an AWS AppConfig environment named MyTestEnvironment. An environment is a logical deployment group of AWS AppConfig targets, such as applications in a Beta or Production environment. You can also define environments for application subcomponents such as the Web, Mobile, and Back-end components for your application.

#### JSON
<a name="aws-resource-appconfig-environment--examples--environment_example--json"></a>

```
Resources": {
    "BasicEnvironment": {
      "Type": "AWS::AppConfig::Environment",
      "DependsOn": "DependentApplication",
      "Properties": {
        "ApplicationId": null,
        "Name": "MyTestEnvironment",
        "Description": "My test environment",
        "Tags": [
          {
            "Key": "Env",
            "Value": "test"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-appconfig-environment--examples--environment_example--yaml"></a>

```
Resources:
  BasicEnvironment:
    Type: AWS::AppConfig::Environment
    Properties:
      ApplicationId: !Ref DependentApplication
      Name: "MyTestEnvironment"
      Description: "My test environment"
      Tags:
        - Key: Env
          Value: test
```

## See also
<a name="aws-resource-appconfig-environment--seealso"></a>
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
+  [Creating an environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig-creating-environment.html)
