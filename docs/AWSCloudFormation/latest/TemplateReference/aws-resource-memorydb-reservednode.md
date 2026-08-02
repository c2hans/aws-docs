---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-memorydb-reservednode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::ReservedNode
<a name="aws-resource-memorydb-reservednode"></a>

Represents the output of a `PurchaseReservedNodesOffering` operation.

## Syntax
<a name="aws-resource-memorydb-reservednode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-memorydb-reservednode-syntax.json"></a>

```
{
  "Type" : "AWS::MemoryDB::ReservedNode"
}
```

### YAML
<a name="aws-resource-memorydb-reservednode-syntax.yaml"></a>

```
Type: AWS::MemoryDB::ReservedNode
```

## Return values
<a name="aws-resource-memorydb-reservednode-return-values"></a>

### Ref
<a name="aws-resource-memorydb-reservednode-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-memorydb-reservednode-return-values-fn--getatt"></a>

####
<a name="aws-resource-memorydb-reservednode-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the reserved node.

`Duration`  <a name="Duration-fn::getatt"></a>
The duration of the reservation in seconds.

`FixedPrice`  <a name="FixedPrice-fn::getatt"></a>
The fixed price charged for this reserved node.

`NodeCount`  <a name="NodeCount-fn::getatt"></a>
The number of nodes that have been reserved.

`NodeType`  <a name="NodeType-fn::getatt"></a>
The node type for the reserved nodes.

`OfferingType`  <a name="OfferingType-fn::getatt"></a>
The offering type of this reserved node.

`RecurringCharges`  <a name="RecurringCharges-fn::getatt"></a>
The recurring price charged to run this reserved node.

`ReservationId`  <a name="ReservationId-fn::getatt"></a>
A customer-specified identifier to track this reservation.

`ReservedNodesOfferingId`  <a name="ReservedNodesOfferingId-fn::getatt"></a>
The ID of the reserved node offering to purchase.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time the reservation started.

`State`  <a name="State-fn::getatt"></a>
The state of the reserved node.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.
