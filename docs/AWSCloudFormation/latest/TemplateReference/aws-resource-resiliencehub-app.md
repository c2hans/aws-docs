---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehub-app.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::App
<a name="aws-resource-resiliencehub-app"></a>

Creates an AWS Resilience Hub application. An AWS Resilience Hub application is a collection of AWS resources structured to prevent and recover AWS application disruptions. To describe a AWS Resilience Hub application, you provide an application name, resources from one or more AWS CloudFormation stacks, AWS Resource Groups, Terraform state files, AppRegistry applications, and an appropriate resiliency policy. In addition, you can also add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters as optional resources. For more information about the number of resources supported per application, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html#limits_resiliencehub).

After you create an AWS Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).

## Syntax
<a name="aws-resource-resiliencehub-app-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehub-app-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHub::App",
  "Properties" : {
      "[AppAssessmentSchedule](#cfn-resiliencehub-app-appassessmentschedule)" : {{String}},
      "[AppTemplateBody](#cfn-resiliencehub-app-apptemplatebody)" : {{String}},
      "[Description](#cfn-resiliencehub-app-description)" : {{String}},
      "[EventSubscriptions](#cfn-resiliencehub-app-eventsubscriptions)" : {{[ EventSubscription, ... ]}},
      "[Name](#cfn-resiliencehub-app-name)" : {{String}},
      "[PermissionModel](#cfn-resiliencehub-app-permissionmodel)" : {{PermissionModel}},
      "[ResiliencyPolicyArn](#cfn-resiliencehub-app-resiliencypolicyarn)" : {{String}},
      "[ResourceMappings](#cfn-resiliencehub-app-resourcemappings)" : {{[ ResourceMapping, ... ]}},
      "[Tags](#cfn-resiliencehub-app-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehub-app-syntax.yaml"></a>

```
Type: AWS::ResilienceHub::App
Properties:
  [AppAssessmentSchedule](#cfn-resiliencehub-app-appassessmentschedule): {{String}}
  [AppTemplateBody](#cfn-resiliencehub-app-apptemplatebody): {{String}}
  [Description](#cfn-resiliencehub-app-description): {{String}}
  [EventSubscriptions](#cfn-resiliencehub-app-eventsubscriptions): {{
    - EventSubscription}}
  [Name](#cfn-resiliencehub-app-name): {{String}}
  [PermissionModel](#cfn-resiliencehub-app-permissionmodel): {{
    PermissionModel}}
  [ResiliencyPolicyArn](#cfn-resiliencehub-app-resiliencypolicyarn): {{String}}
  [ResourceMappings](#cfn-resiliencehub-app-resourcemappings): {{
    - ResourceMapping}}
  [Tags](#cfn-resiliencehub-app-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-resiliencehub-app-properties"></a>

`AppAssessmentSchedule`  <a name="cfn-resiliencehub-app-appassessmentschedule"></a>
Assessment execution schedule with 'Daily' or 'Disabled' values.
*Required*: No
*Type*: String
*Allowed values*: `Disabled | Daily`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppTemplateBody`  <a name="cfn-resiliencehub-app-apptemplatebody"></a>
A JSON string that provides information about your application structure. To learn more about the `appTemplateBody` template, see the sample template in [Sample appTemplateBody template](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PutDraftAppVersionTemplate.html#API_PutDraftAppVersionTemplate_Examples).
The `appTemplateBody` JSON string has the following structure:
+  ** `resources` **

  The list of logical resources that needs to be included in the AWS Resilience Hub application.

  Type: Array
**Note**
Don't add the resources that you want to exclude.

  Each `resources` array item includes the following fields:
  +  * `logicalResourceId` *

    The logical identifier of the resource.

    Type: Object

    Each `logicalResourceId` object includes the following fields:
    +  `identifier`

      Identifier of the resource.

      Type: String
    +  `logicalStackName`

      Name of the AWS CloudFormation stack this resource belongs to.

      Type: String
    +  `resourceGroupName`

      Name of the resource group this resource belongs to.

      Type: String
    +  `terraformSourceName`

      Name of the Terraform S3 state file this resource belongs to.

      Type: String
    +  `eksSourceName`

      Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
**Note**
This parameter accepts values in "eks-cluster/namespace" format.

      Type: String
  +  * `type` *

    The type of resource.

    Type: string
  +  * `name` *

    Name of the resource.

    Type: String
  +  `additionalInfo`

    Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
**Note**
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
+  ** `appComponents` **

  The list of Application Components (AppComponent) that this resource belongs to. If an AppComponent is not part of the AWS Resilience Hub application, it will be added.

  Type: Array

  Each `appComponents` array item includes the following fields:
  +  `name`

    Name of the AppComponent.

    Type: String
  +  `type`

    The type of AppComponent. For more information about the types of AppComponent, see [Grouping resources in an AppComponent](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html).

    Type: String
  +  `resourceNames`

    The list of included resources that are assigned to the AppComponent.

    Type: Array of strings
  +  `additionalInfo`

    Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
**Note**
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
+  ** `excludedResources` **

  The list of logical resource identifiers to be excluded from the application.

  Type: Array
**Note**
Don't add the resources that you want to include.

  Each `excludedResources` array item includes the following fields:
  +  * `logicalResourceIds` *

    The logical identifier of the resource.

    Type: Object
**Note**
You can configure only one of the following fields:
 `logicalStackName`
 `resourceGroupName`
 `terraformSourceName`
 `eksSourceName`

    Each `logicalResourceIds` object includes the following fields:
    +  `identifier`

      The identifier of the resource.

      Type: String
    +  `logicalStackName`

      Name of the AWS CloudFormation stack this resource belongs to.

      Type: String
    +  `resourceGroupName`

      Name of the resource group this resource belongs to.

      Type: String
    +  `terraformSourceName`

      Name of the Terraform S3 state file this resource belongs to.

      Type: String
    +  `eksSourceName`

      Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
**Note**
This parameter accepts values in "eks-cluster/namespace" format.

      Type: String
+  ** `version` **

  The AWS Resilience Hub application version.
+  `additionalInfo`

  Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
**Note**
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\s:,-\.'\/{}\[\]:"]+$`
*Minimum*: `0`
*Maximum*: `409600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-resiliencehub-app-description"></a>
Optional description for an application.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventSubscriptions`  <a name="cfn-resiliencehub-app-eventsubscriptions"></a>
The list of events you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for **Drift detected** and **Scheduled assessment failure** events.
*Required*: No
*Type*: Array of [EventSubscription](aws-properties-resiliencehub-app-eventsubscription.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-resiliencehub-app-name"></a>
Name for the application.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PermissionModel`  <a name="cfn-resiliencehub-app-permissionmodel"></a>
Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
*Required*: No
*Type*: [PermissionModel](aws-properties-resiliencehub-app-permissionmodel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResiliencyPolicyArn`  <a name="cfn-resiliencehub-app-resiliencypolicyarn"></a>
The Amazon Resource Name (ARN) of the resiliency policy.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceMappings`  <a name="cfn-resiliencehub-app-resourcemappings"></a>
An array of `ResourceMapping` objects.
*Required*: Yes
*Type*: Array of [ResourceMapping](aws-properties-resiliencehub-app-resourcemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-resiliencehub-app-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,128}`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-resiliencehub-app-return-values"></a>

### Ref
<a name="aws-resource-resiliencehub-app-return-values-ref"></a>

The returned Amazon Resource Name (ARN) for the applcation.

### Fn::GetAtt
<a name="aws-resource-resiliencehub-app-return-values-fn--getatt"></a>

The Amazon Resource Name (ARN) for the applcation.

####
<a name="aws-resource-resiliencehub-app-return-values-fn--getatt-fn--getatt"></a>

`AppArn`  <a name="AppArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the applcation.

`DriftStatus`  <a name="DriftStatus-fn::getatt"></a>
Indicates if compliance drifts (deviations) were detected while running an assessment for your application.

## Examples
<a name="aws-resource-resiliencehub-app--examples"></a>

The following examples show how to create an application in AWS Resilience Hub.

### Creating an application
<a name="aws-resource-resiliencehub-app--examples--Creating_an_application"></a>

#### YAML
<a name="aws-resource-resiliencehub-app--examples--Creating_an_application--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  Type: AWS::ResilienceHub::App
  Properties:
    Name: test
    Description: ResilienceHub TestApp
    Tags:
      TagKey1: someValue
    AppTemplateBody: '{"resources":[{"logicalResourceId":{"identifier":"LAMBDA","logicalStackName":null,"resourceGroupName":null},"type":"AWS::lambda::Function","name":"lambda"}],"appComponents":[{"id":"compute","name":"compute","type":"AWS::ResilienceHub::ComputeAppComponent","resourceNames":["lambda"]},{"id":"appcommon","name":"appcommon","type":"AWS::ResilienceHub::AppCommonAppComponent","resourceNames":null}],"excludedResources":{"logicalResourceIds":[]},"version":2.0}'
    ResourceMappings:
      - ResourceName: lambda
        MappingType: Resource
        PhysicalResourceId:
          Type: Arn
          Identifier: arn:aws:lambda:us-west-2:123456789012:function:functionName
```

#### JSON
<a name="aws-resource-resiliencehub-app--examples--Creating_an_application--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09T00:00:00.000Z",
    "Resources": {
        "Type": "AWS::ResilienceHub::App",
        "Properties": {
            "Name": "test",
            "Description": "ResilienceHub TestApp",
            "Tags": {
                "TagKey1": "someValue"
            },
            "AppTemplateBody": "{\"resources\":[{\"logicalResourceId\":{\"identifier\":\"LAMBDA\",\"logicalStackName\":null,\"resourceGroupName\":null},\"type\":\"AWS::lambda::Function\",\"name\":\"lambda\"}],\"appComponents\":[{\"id\":\"compute\",\"name\":\"compute\",\"type\":\"AWS::ResilienceHub::ComputeAppComponent\",\"resourceNames\":[\"lambda\"]},{\"id\":\"appcommon\",\"name\":\"appcommon\",\"type\":\"AWS::ResilienceHub::AppCommonAppComponent\",\"resourceNames\":null}],\"excludedResources\":{\"logicalResourceIds\":[]},\"version\":2.0}",
            "ResourceMappings": [
                {
                    "ResourceName": "lambda",
                    "MappingType": "Resource",
                    "PhysicalResourceId": {
                        "Type": "Arn",
                        "Identifier": "arn:aws:lambda:us-west-2:123456789012:function:functionName"
                    }
                }
            ]
        }
    }
}
```
