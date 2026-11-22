---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetprotection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::RecordSetProtection

The `AWS::Route53::RecordSetProtection` resource specifies a protection for a record set in a hosted zone. A protection covers every record set that has the specified name and type, including record sets that have a `SetIdentifier`. While the protection exists, Route 53 refuses changes to those record sets and refuses to create additional record sets with that name and type, for example a weighted record set that has a new `SetIdentifier`.

The record set must exist before you create the protection. In the protection, add a [DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-dependson.html) that names the `AWS::Route53::RecordSet`, so that CloudFormation creates the record set first.

## Syntax
<a name="aws-resource-route53-recordsetprotection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-recordsetprotection-syntax.json"></a>

```json
{
  "Type" : "AWS::Route53::RecordSetProtection",
  "Properties" : {
      "[Comment](#cfn-route53-recordsetprotection-comment)" : {{String}},
      "[HostedZoneId](#cfn-route53-recordsetprotection-hostedzoneid)" : {{String}},
      "[RecordName](#cfn-route53-recordsetprotection-recordname)" : {{String}},
      "[RecordType](#cfn-route53-recordsetprotection-recordtype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53-recordsetprotection-syntax.yaml"></a>

```yaml
Type: AWS::Route53::RecordSetProtection
Properties:
  [Comment](#cfn-route53-recordsetprotection-comment): {{String}}
  [HostedZoneId](#cfn-route53-recordsetprotection-hostedzoneid): {{String}}
  [RecordName](#cfn-route53-recordsetprotection-recordname): {{String}}
  [RecordType](#cfn-route53-recordsetprotection-recordtype): {{String}}
```

## Properties
<a name="aws-resource-route53-recordsetprotection-properties"></a>

`Comment`  <a name="cfn-route53-recordsetprotection-comment"></a>
A comment that describes the protection. Route 53 includes the comment in the error that it returns when it refuses a change to the protected record set.
Changing `Comment` replaces the protection. CloudFormation deletes the existing protection before it creates the new one, so the record set is unprotected during the replacement.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostedZoneId`  <a name="cfn-route53-recordsetprotection-hostedzoneid"></a>
The ID of the hosted zone that contains the record set to protect, for example, `Z0123456789ABCDEFGHIJ`. You can also specify the ID with the `/hostedzone/` prefix.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `44`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordName`  <a name="cfn-route53-recordsetprotection-recordname"></a>
The name of the record set to protect, for example, `www.example.com`. The name must match the `Name` of an existing record set in the hosted zone. Route 53 treats the name as case-insensitive, and the trailing dot is optional.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordType`  <a name="cfn-route53-recordsetprotection-recordtype"></a>
The DNS record type of the record set to protect, for example, `A`. The type must match the `Type` of an existing record set that has the name in `RecordName`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53-recordsetprotection-return-values"></a>

### Ref
<a name="aws-resource-route53-recordsetprotection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the primary identifier of the protection: the `HostedZoneId`, `RecordName`, and `RecordType` values, separated by a pipe (`|`). The record name is lowercase and has no trailing dot, and the record type is uppercase.

For example, `{ "Ref": "MyRecordSetProtection" }` could return the value `Z0123456789ABCDEFGHIJ|www.example.com|A`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Remarks
<a name="aws-resource-route53-recordsetprotection--remarks"></a>

 *Stack updates that change a protected record set*

Use separate stack updates to change a record set and to add or remove its protection:
+ To change a protected record set, first remove the protection in one stack update, then change the record set in a second stack update. If one update does both, CloudFormation changes the record set first and deletes the removed protection only in the cleanup phase at the end of the update. The protection still exists when CloudFormation changes the record set, so the change fails with a `ResourceConflict` error.
+ To protect a record set that's already in the stack, add the protection in a stack update that doesn't change the record set. For example, suppose that one update changes the record set's TTL and adds the protection, and another resource in that update fails. During the rollback, CloudFormation reverts the record set first and deletes the new protection only in the rollback cleanup phase. The revert fails with a `ResourceConflict` error, and the stack status becomes `UPDATE_ROLLBACK_FAILED`. A `DependsOn` attribute doesn't change this order.

 *Deleting a protected record set*

Deleting an `AWS::Route53::RecordSet` fails with a `ResourceConflict` error while a protection exists for it. For example, if the protection has a `DeletionPolicy` of `Retain`, deleting the stack or removing the protection from the template leaves the protection in Route 53, so CloudFormation can't delete the record set. The same applies to a protection that you created outside CloudFormation. Delete the protection first.

 *Recovering from UPDATE\_ROLLBACK\_FAILED*

If a protection blocks the rollback of a record set and the stack status is `UPDATE_ROLLBACK_FAILED`, delete the protection by using the Route 53 `DeleteResourceRecordSetProtections` API action. Then continue the rollback by using [ContinueUpdateRollback](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ContinueUpdateRollback.html). CloudFormation reverts the record set, and in the rollback cleanup phase it treats the protection that you deleted as already deleted. The stack returns to its previous template, without the protection. To add the protection again, use a stack update that doesn't change the record set.

 *Managing an existing protection*

To manage a protection that already exists, import it into the stack. Use the `HostedZoneId`, `RecordName`, and `RecordType` values as the identifier. For more information about importing resources, see [Import AWS resources into a CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources.html) in the *AWS CloudFormation User Guide*.

## Examples
<a name="aws-resource-route53-recordsetprotection--examples"></a>

### Protect a record set
<a name="aws-resource-route53-recordsetprotection--examples--Protect_a_record_set"></a>

The following example creates a hosted zone, an `A` record set, and a protection for that record set in a new stack. The protection has a `DependsOn` attribute so that CloudFormation creates the record set first. You can create a new record set and its protection together because, if the stack rolls back, CloudFormation deletes the protection before the record set. To protect a record set that's already in a stack, add the protection in a stack update that doesn't change the record set.

#### JSON
<a name="aws-resource-route53-recordsetprotection--examples--Protect_a_record_set--json"></a>

```json
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MyHostedZone": {
            "Type": "AWS::Route53::HostedZone",
            "Properties": {
                "Name": "example.com"
            }
        },
        "MyRecordSet": {
            "Type": "AWS::Route53::RecordSet",
            "Properties": {
                "HostedZoneId": {
                    "Ref": "MyHostedZone"
                },
                "Name": "www.example.com",
                "Type": "A",
                "TTL": "300",
                "ResourceRecords": [
                    "198.51.100.1"
                ]
            }
        },
        "MyRecordSetProtection": {
            "Type": "AWS::Route53::RecordSetProtection",
            "DependsOn": "MyRecordSet",
            "Properties": {
                "HostedZoneId": {
                    "Ref": "MyHostedZone"
                },
                "RecordName": "www.example.com",
                "RecordType": "A",
                "Comment": "Managed by CloudFormation. Remove the protection before you change this record set."
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-route53-recordsetprotection--examples--Protect_a_record_set--yaml"></a>

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyHostedZone:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: example.com
  MyRecordSet:
    Type: AWS::Route53::RecordSet
    Properties:
      HostedZoneId:
        Ref: MyHostedZone
      Name: www.example.com
      Type: A
      TTL: '300'
      ResourceRecords:
        - 198.51.100.1
  MyRecordSetProtection:
    Type: AWS::Route53::RecordSetProtection
    DependsOn: MyRecordSet
    Properties:
      HostedZoneId:
        Ref: MyHostedZone
      RecordName: www.example.com
      RecordType: A
      Comment: Managed by CloudFormation. Remove the protection before you change this record set.
```
