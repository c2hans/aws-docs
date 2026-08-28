---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsguru-resourcecollection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsGuru::ResourceCollection
<a name="aws-resource-devopsguru-resourcecollection"></a>

 A collection of AWS resources supported by DevOps Guru. The one type of AWS resource collection supported is AWS CloudFormation stacks. DevOps Guru can be configured to analyze only the AWS resources that are defined in the stacks.

## Syntax
<a name="aws-resource-devopsguru-resourcecollection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsguru-resourcecollection-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsGuru::ResourceCollection",
  "Properties" : {
      "[ResourceCollectionFilter](#cfn-devopsguru-resourcecollection-resourcecollectionfilter)" : {{ResourceCollectionFilter}}
    }
}
```

### YAML
<a name="aws-resource-devopsguru-resourcecollection-syntax.yaml"></a>

```
Type: AWS::DevOpsGuru::ResourceCollection
Properties:
  [ResourceCollectionFilter](#cfn-devopsguru-resourcecollection-resourcecollectionfilter): {{
    ResourceCollectionFilter}}
```

## Properties
<a name="aws-resource-devopsguru-resourcecollection-properties"></a>

`ResourceCollectionFilter`  <a name="cfn-devopsguru-resourcecollection-resourcecollectionfilter"></a>
 Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.
*Required*: Yes
*Type*: [ResourceCollectionFilter](aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devopsguru-resourcecollection-return-values"></a>

### Ref
<a name="aws-resource-devopsguru-resourcecollection-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns Amazon Resource Name (ARN) of the `ResourceCollection`. For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsguru-resourcecollection-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values. For more information about using `Fn::GetAtt`, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsguru-resourcecollection-return-values-fn--getatt-fn--getatt"></a>

`ResourceCollectionType`  <a name="ResourceCollectionType-fn::getatt"></a>
The type of AWS resource collections to return. The one valid value is `CLOUD_FORMATION` for AWS CloudFormation stacks.

## Examples
<a name="aws-resource-devopsguru-resourcecollection--examples"></a>

**Topics**
+ [Create a resource collection using two CloudFormation stacks](#aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_using_two_CloudFormation_stacks)
+ [Create a resource collection with all CloudFormation stacks in your account](#aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_with_all_CloudFormation_stacks_in_your_account)
+ [Monitor DevOps Guru resources using tags](#aws-resource-devopsguru-resourcecollection--examples--Monitor_DevOps_Guru_resources_using_tags)

### Create a resource collection using two CloudFormation stacks
<a name="aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_using_two_CloudFormation_stacks"></a>

#### JSON
<a name="aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_using_two_CloudFormation_stacks--json"></a>

```
{
  "Resources": {
    "MyResourceCollection": {
      "Type": "AWS::DevOpsGuru::ResourceCollection",
      "Properties": {
        "ResourceCollectionFilter": {
          "CloudFormation": {
            "StackNames": [
              "StackA",
              "StackB"
            ]
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_using_two_CloudFormation_stacks--yaml"></a>

```
Resources:
  MyResourceCollection:
    Type: AWS::DevOpsGuru::ResourceCollection
    Properties:
      ResourceCollectionFilter:
        CloudFormation:
          StackNames:
          - StackA
          - StackB
```

### Create a resource collection with all CloudFormation stacks in your account
<a name="aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_with_all_CloudFormation_stacks_in_your_account"></a>

#### JSON
<a name="aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_with_all_CloudFormation_stacks_in_your_account--json"></a>

```
{
  "Resources": {
    "MyResourceCollection": {
      "Type": "AWS::DevOpsGuru::ResourceCollection",
      "Properties": {
        "ResourceCollectionFilter": {
          "CloudFormation": {
            "StackNames": [
              "*"
            ]
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-devopsguru-resourcecollection--examples--Create_a_resource_collection_with_all_CloudFormation_stacks_in_your_account--yaml"></a>

```
Resources:
  MyResourceCollection:
    Type: AWS::DevOpsGuru::ResourceCollection
    Properties:
      ResourceCollectionFilter:
        CloudFormation:
          StackNames:
          - "*"
```

### Monitor DevOps Guru resources using tags
<a name="aws-resource-devopsguru-resourcecollection--examples--Monitor_DevOps_Guru_resources_using_tags"></a>

#### JSON
<a name="aws-resource-devopsguru-resourcecollection--examples--Monitor_DevOps_Guru_resources_using_tags--json"></a>

```
{
"DevOpsGuruResourceCollection": {
  "Type": "AWS::DevOpsGuru::ResourceCollection",
  "Condition": "DevOpsGuruEnable",
  "Properties": {
    "ResourceCollectionFilter": {
      "Tags": [{
        "AppBoundaryKey": "devops-guru-workshop",
        "TagValues": [
          "devops-guru-serverless",
          "devops-guru-aurora"
          ]
        }]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-devopsguru-resourcecollection--examples--Monitor_DevOps_Guru_resources_using_tags--yaml"></a>

```
DevOpsGuruResourceCollection:
    Type: AWS::DevOpsGuru::ResourceCollection
    Condition: DevOpsGuruEnable
    Properties:
      ResourceCollectionFilter:
        Tags:
          - AppBoundaryKey: devops-guru-workshop
            TagValues:
              - devops-guru-serverless
	      - devops-guru-aurora
```

#### JSON
<a name="aws-resource-devopsguru-resourcecollection--examples--Monitor_DevOps_Guru_resources_using_tags--json"></a>

```
{
 "DevOpsGuruResourceCollection": {
    "Type": "AWS::DevOpsGuru::ResourceCollection",
    "Condition": "DevOpsGuruEnable",
    "Properties": {
      "ResourceCollectionFilter": {
        "Tags": [
          {
            "AppBoundaryKey": "devops-guru-workshop",
            "TagValues": [
              "*"
            ]
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-devopsguru-resourcecollection--examples--Monitor_DevOps_Guru_resources_using_tags--yaml"></a>

```
DevOpsGuruResourceCollection:
    Type: AWS::DevOpsGuru::ResourceCollection
    Condition: DevOpsGuruEnable
    Properties:
      ResourceCollectionFilter:
        Tags:
          - AppBoundaryKey: devops-guru-workshop
            TagValues:
              - "*"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
