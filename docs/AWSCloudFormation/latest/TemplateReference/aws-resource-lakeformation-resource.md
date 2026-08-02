---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lakeformation-resource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::Resource
<a name="aws-resource-lakeformation-resource"></a>

The `AWS::LakeFormation::Resource` represents the data ( buckets and folders) that is being registered with AWS Lake Formation. During a stack operation, AWS CloudFormation calls the AWS Lake Formation[https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-RegisterResource](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-RegisterResource) API operation to register the resource. To remove a `Resource` type, AWS CloudFormation calls the AWS Lake Formation[https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-DeregisterResource](https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-DeregisterResource) API operation.

## Syntax
<a name="aws-resource-lakeformation-resource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lakeformation-resource-syntax.json"></a>

```
{
  "Type" : "AWS::LakeFormation::Resource",
  "Properties" : {
      "[HybridAccessEnabled](#cfn-lakeformation-resource-hybridaccessenabled)" : {{Boolean}},
      "[ResourceArn](#cfn-lakeformation-resource-resourcearn)" : {{String}},
      "[RoleArn](#cfn-lakeformation-resource-rolearn)" : {{String}},
      "[UseServiceLinkedRole](#cfn-lakeformation-resource-useservicelinkedrole)" : {{Boolean}},
      "[WithFederation](#cfn-lakeformation-resource-withfederation)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-lakeformation-resource-syntax.yaml"></a>

```
Type: AWS::LakeFormation::Resource
Properties:
  [HybridAccessEnabled](#cfn-lakeformation-resource-hybridaccessenabled): {{Boolean}}
  [ResourceArn](#cfn-lakeformation-resource-resourcearn): {{String}}
  [RoleArn](#cfn-lakeformation-resource-rolearn): {{String}}
  [UseServiceLinkedRole](#cfn-lakeformation-resource-useservicelinkedrole): {{Boolean}}
  [WithFederation](#cfn-lakeformation-resource-withfederation): {{Boolean}}
```

## Properties
<a name="aws-resource-lakeformation-resource-properties"></a>

`HybridAccessEnabled`  <a name="cfn-lakeformation-resource-hybridaccessenabled"></a>
 Indicates whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-lakeformation-resource-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-lakeformation-resource-rolearn"></a>
The IAM role that registered a resource.
*Required*: No
*Type*: String
*Pattern*: `arn:aws:iam::[0-9]*:role/.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseServiceLinkedRole`  <a name="cfn-lakeformation-resource-useservicelinkedrole"></a>
Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WithFederation`  <a name="cfn-lakeformation-resource-withfederation"></a>
Allows Lake Formation to assume a role to access tables in a federated database.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lakeformation-resource-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-lakeformation-resource-return-values-fn--getatt"></a>

####
<a name="aws-resource-lakeformation-resource-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
An identifier for the catalog resource.
