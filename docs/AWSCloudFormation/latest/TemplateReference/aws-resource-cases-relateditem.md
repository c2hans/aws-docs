---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-relateditem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::RelatedItem
<a name="aws-resource-cases-relateditem"></a>

Creates a related item (comments, tasks, and contacts) and associates it with a case.

There's a quota for the number of fields allowed in a Custom type related item. See [Connect Customer Cases quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas).

 **Use cases**

Following are examples of related items that you may want to associate with a case:
+ Related contacts, such as calls, chats, emails tasks
+ Comments, for agent notes
+ SLAs, to capture target resolution goals
+ Cases, to capture related Connect Customer Cases
+ Files, such as policy documentation or customer-provided attachments
+ Custom related items, which provide flexibility for you to define related items that such as bookings, orders, products, notices, and more

 **Important things to know**
+ If you are associating a contact to a case by passing in `Contact` for a `type`, you must have [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) permission on the ARN of the contact that you provide in `content.contact.contactArn`.
+ A Related Item is a resource that is associated with a case. It may or may not have an external identifier linking it to an external resource (for example, a `contactArn`). All Related Items have their own internal identifier, the `relatedItemArn`. Examples of related items include `comments` and `contacts`.
+ If you provide a value for `performedBy.userArn`, you must also have [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the ARN of the user that you provide.

**Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Syntax
<a name="aws-resource-cases-relateditem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-relateditem-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::RelatedItem",
  "Properties" : {
      "[CaseId](#cfn-cases-relateditem-caseid)" : {{String}},
      "[Content](#cfn-cases-relateditem-content)" : {{RelatedItemContent}},
      "[DomainId](#cfn-cases-relateditem-domainid)" : {{String}},
      "[Tags](#cfn-cases-relateditem-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-cases-relateditem-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cases-relateditem-syntax.yaml"></a>

```
Type: AWS::Cases::RelatedItem
Properties:
  [CaseId](#cfn-cases-relateditem-caseid): {{String}}
  [Content](#cfn-cases-relateditem-content): {{
    RelatedItemContent}}
  [DomainId](#cfn-cases-relateditem-domainid): {{String}}
  [Tags](#cfn-cases-relateditem-tags): {{
    - Tag}}
  [Type](#cfn-cases-relateditem-type): {{String}}
```

## Properties
<a name="aws-resource-cases-relateditem-properties"></a>

`CaseId`  <a name="cfn-cases-relateditem-caseid"></a>
A unique identifier of the case.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Content`  <a name="cfn-cases-relateditem-content"></a>
Represents the content of a particular type of related item.
*Required*: Yes
*Type*: [RelatedItemContent](aws-properties-cases-relateditem-relateditemcontent.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainId`  <a name="cfn-cases-relateditem-domainid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cases-relateditem-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-relateditem-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cases-relateditem-type"></a>
Type of a related item.
*Required*: Yes
*Type*: String
*Allowed values*: `Contact | Comment | File | Sla | ConnectCase | Custom`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cases-relateditem-return-values"></a>

### Ref
<a name="aws-resource-cases-relateditem-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cases-relateditem-return-values-fn--getatt"></a>

####
<a name="aws-resource-cases-relateditem-return-values-fn--getatt-fn--getatt"></a>

`RelatedItemArn`  <a name="RelatedItemArn-fn::getatt"></a>
Property description not available.

`RelatedItemId`  <a name="RelatedItemId-fn::getatt"></a>
Unique identifier of a related item.
