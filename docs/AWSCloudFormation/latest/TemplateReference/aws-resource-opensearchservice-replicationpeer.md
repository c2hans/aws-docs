---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchservice-replicationpeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::ReplicationPeer

A domain that another domain replicates with, and the state of that relationship.

## Syntax
<a name="aws-resource-opensearchservice-replicationpeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchservice-replicationpeer-syntax.json"></a>

```json
{
  "Type" : "AWS::OpenSearchService::ReplicationPeer",
  "Properties" : {
      "[DomainName](#cfn-opensearchservice-replicationpeer-domainname)" : {{String}},
      "[PeerDomainArn](#cfn-opensearchservice-replicationpeer-peerdomainarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-opensearchservice-replicationpeer-syntax.yaml"></a>

```yaml
Type: AWS::OpenSearchService::ReplicationPeer
Properties:
  [DomainName](#cfn-opensearchservice-replicationpeer-domainname): {{String}}
  [PeerDomainArn](#cfn-opensearchservice-replicationpeer-peerdomainarn): {{String}}
```

## Properties
<a name="aws-resource-opensearchservice-replicationpeer-properties"></a>

`DomainName`  <a name="cfn-opensearchservice-replicationpeer-domainname"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9\-]+$`
*Minimum*: `3`
*Maximum*: `28`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerDomainArn`  <a name="cfn-opensearchservice-replicationpeer-peerdomainarn"></a>
The Amazon Resource Name (ARN) of the peer domain.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain/[a-z0-9\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-opensearchservice-replicationpeer-return-values"></a>

### Ref
<a name="aws-resource-opensearchservice-replicationpeer-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-opensearchservice-replicationpeer-return-values-fn--getatt"></a>

####
<a name="aws-resource-opensearchservice-replicationpeer-return-values-fn--getatt-fn--getatt"></a>

`DomainArn`  <a name="DomainArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.

`PeerRole`  <a name="PeerRole-fn::getatt"></a>
The peer's role in the relationship, either `PRIMARY` or `SECONDARY`.

`Role`  <a name="Role-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The state of the relationship:
+ `PENDING_SETUP` - replication is being established.
+ `ACTIVE` - replication is running.
+ `SWITCHING_OVER` - a planned promotion is in progress.
+ `FAILING_OVER` - an unplanned promotion is in progress.
+ `PENDING_REMOVAL` - replication is being stopped.
+ `DETACHED` - the relationship has ended.
+ `EJECTED` - a failover promoted the other domain. The former primary keeps the data it had when it was ejected and stays read-only until you remove the peer, or discard that data and pair again.
+ `FAILED` - setup or teardown could not complete. You can still remove the relationship.
A relationship that is removed successfully no longer appears in `Peers`.
