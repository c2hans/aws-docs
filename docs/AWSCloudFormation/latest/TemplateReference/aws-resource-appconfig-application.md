---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Application
<a name="aws-resource-appconfig-application"></a>

The `AWS::AppConfig::Application` resource creates an application. In AWS AppConfig, an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.

AWS AppConfig requires that you create resources and deploy a configuration in the following order:

1. Create an application

1. Create an environment

1. Create a configuration profile

1. Choose a pre-defined deployment strategy or create your own

1. Deploy the configuration

For more information, see [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) in the *AWS AppConfig User Guide*.

## Syntax
<a name="aws-resource-appconfig-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appconfig-application-syntax.json"></a>

```
{
  "Type" : "AWS::AppConfig::Application",
  "Properties" : {
      "[Description](#cfn-appconfig-application-description)" : {{String}},
      "[Name](#cfn-appconfig-application-name)" : {{String}},
      "[Tags](#cfn-appconfig-application-tags)" : {{[ Tags, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appconfig-application-syntax.yaml"></a>

```
Type: AWS::AppConfig::Application
Properties:
  [Description](#cfn-appconfig-application-description): {{String}}
  [Name](#cfn-appconfig-application-name): {{String}}
  [Tags](#cfn-appconfig-application-tags): {{
    - Tags}}
```

## Properties
<a name="aws-resource-appconfig-application-properties"></a>

`Description`  <a name="cfn-appconfig-application-description"></a>
A description of the application.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appconfig-application-name"></a>
A name for the application.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appconfig-application-tags"></a>
Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
*Required*: No
*Type*: [Array](aws-properties-appconfig-application-tags.md) of [Tags](aws-properties-appconfig-application-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appconfig-application-return-values"></a>

### Ref
<a name="aws-resource-appconfig-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID.

### Fn::GetAtt
<a name="aws-resource-appconfig-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-appconfig-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The application ID.

## Examples
<a name="aws-resource-appconfig-application--examples"></a>

### AWS AppConfig application example
<a name="aws-resource-appconfig-application--examples--application_example"></a>

The following example creates a simple AWS AppConfig application named MyTestApplication. An application in AWS AppConfig is a logical unit of code that provides capabilities for your customers. For example, an application can be a microservice that runs on Amazon EC2 instances, a mobile application installed by your users, a serverless application using Amazon API Gateway and AWS Lambda, or any system you run on behalf of others.

#### JSON
<a name="aws-resource-appconfig-application--examples--application_example--json"></a>

```
BasicApplication": {
    "Type": "AWS::AppConfig::Application",
    "Properties": {
      "Name": "MyTestApplication",
      "Description": "A sample test application.",
      "Tags": [
        {
          "Key": "Env",
          "Value": "test"
        }
      ]
    }
  }
}
```

#### YAML
<a name="aws-resource-appconfig-application--examples--application_example--yaml"></a>

```
BasicApplication:
    Type: AWS::AppConfig::Application
    Properties:
      Name: "MyTestApplication"
      Description: "A sample test application."
      Tags:
        - Key: Env
          Value: test
```

## See also
<a name="aws-resource-appconfig-application--seealso"></a>
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
+  [Creating an Application](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig-creating-application.html)
