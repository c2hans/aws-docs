---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-systemsmanagersap-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SystemsManagerSAP::Application
<a name="aws-resource-systemsmanagersap-application"></a>

An SAP application registered with AWS Systems Manager for SAP.

## Syntax
<a name="aws-resource-systemsmanagersap-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-systemsmanagersap-application-syntax.json"></a>

```
{
  "Type" : "AWS::SystemsManagerSAP::Application",
  "Properties" : {
      "[ApplicationId](#cfn-systemsmanagersap-application-applicationid)" : {{String}},
      "[ApplicationType](#cfn-systemsmanagersap-application-applicationtype)" : {{String}},
      "[ComponentsInfo](#cfn-systemsmanagersap-application-componentsinfo)" : {{[ ComponentInfo, ... ]}},
      "[Credentials](#cfn-systemsmanagersap-application-credentials)" : {{[ Credential, ... ]}},
      "[DatabaseArn](#cfn-systemsmanagersap-application-databasearn)" : {{String}},
      "[Instances](#cfn-systemsmanagersap-application-instances)" : {{[ String, ... ]}},
      "[SapInstanceNumber](#cfn-systemsmanagersap-application-sapinstancenumber)" : {{String}},
      "[Sid](#cfn-systemsmanagersap-application-sid)" : {{String}},
      "[Tags](#cfn-systemsmanagersap-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-systemsmanagersap-application-syntax.yaml"></a>

```
Type: AWS::SystemsManagerSAP::Application
Properties:
  [ApplicationId](#cfn-systemsmanagersap-application-applicationid): {{String}}
  [ApplicationType](#cfn-systemsmanagersap-application-applicationtype): {{String}}
  [ComponentsInfo](#cfn-systemsmanagersap-application-componentsinfo): {{
    - ComponentInfo}}
  [Credentials](#cfn-systemsmanagersap-application-credentials): {{
    - Credential}}
  [DatabaseArn](#cfn-systemsmanagersap-application-databasearn): {{String}}
  [Instances](#cfn-systemsmanagersap-application-instances): {{
    - String}}
  [SapInstanceNumber](#cfn-systemsmanagersap-application-sapinstancenumber): {{String}}
  [Sid](#cfn-systemsmanagersap-application-sid): {{String}}
  [Tags](#cfn-systemsmanagersap-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-systemsmanagersap-application-properties"></a>

`ApplicationId`  <a name="cfn-systemsmanagersap-application-applicationid"></a>
The ID of the application.
*Required*: Yes
*Type*: String
*Pattern*: `[\w\d\.-]{1,60}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationType`  <a name="cfn-systemsmanagersap-application-applicationtype"></a>
The type of the application.
*Required*: Yes
*Type*: String
*Allowed values*: `HANA | SAP_ABAP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentsInfo`  <a name="cfn-systemsmanagersap-application-componentsinfo"></a>
Property description not available.
*Required*: No
*Type*: Array of [ComponentInfo](aws-properties-systemsmanagersap-application-componentinfo.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Credentials`  <a name="cfn-systemsmanagersap-application-credentials"></a>
The credentials of the SAP application.
*Required*: No
*Type*: Array of [Credential](aws-properties-systemsmanagersap-application-credential.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseArn`  <a name="cfn-systemsmanagersap-application-databasearn"></a>
The Amazon Resource Name (ARN) of the database.
*Required*: No
*Type*: String
*Pattern*: `^arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Instances`  <a name="cfn-systemsmanagersap-application-instances"></a>
The Amazon EC2 instances on which your SAP application is running.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SapInstanceNumber`  <a name="cfn-systemsmanagersap-application-sapinstancenumber"></a>
The SAP instance number of the application.
*Required*: No
*Type*: String
*Pattern*: `[0-9]{2}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Sid`  <a name="cfn-systemsmanagersap-application-sid"></a>
The System ID of the application.
*Required*: No
*Type*: String
*Pattern*: `[A-Z][A-Z0-9]{2}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-systemsmanagersap-application-tags"></a>
The tags on the application.
*Required*: No
*Type*: Array of [Tag](aws-properties-systemsmanagersap-application-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-systemsmanagersap-application-return-values"></a>

### Ref
<a name="aws-resource-systemsmanagersap-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

### Fn::GetAtt
<a name="aws-resource-systemsmanagersap-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-systemsmanagersap-application-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name of the SAP application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
