---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/upgrading-from-v1.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Upgrading the SDK for JavaScript from Version 1
<a name="upgrading-from-v1"></a>

The following notes help you upgrade the SDK for JavaScript from version 1 to version 2.

## Automatic Conversion of Base64 and Timestamp Types on Input/Output
<a name="upgrading-from-v1-base64-timestamp-conversion"></a>

The SDK now automatically encodes and decodes base64-encoded values, as well as timestamp values, on the user's behalf. This change affects any operation where base64 or timestamp values were sent by a request or returned in a response that allows for base64-encoded values.

User code that previously converted base64 is no longer required. Values encoded as base64 are now returned as buffer objects from server responses and can also be passed as buffer input. For example, the following version 1 `SQS.sendMessage` parameters:

```
var params = {
   MessageBody: '{{Some Message}}',
   MessageAttributes: {
      attrName: {
         DataType: 'Binary',
         BinaryValue: new Buffer('{{example text}}').toString('base64')
      }
   }
};
```

Can be rewritten as follows.

```
var params = {
   MessageBody: '{{Some Message}}',
   MessageAttributes: {
      attrName: {
         DataType: 'Binary',
         BinaryValue: '{{example text}}'
      }
   }
};
```

Here is how the message is read.

```
sqs.receiveMessage(params, function(err, data) {
  // buf is <Buffer 65 78 61 6d 70 6c 65 20 74 65 78 74>
  var buf = data.Messages[0].MessageAttributes.attrName.BinaryValue;
  console.log(buf.toString()); // "example text"
});
```

## Moved response.data.RequestId to response.requestId
<a name="upgrading-from-v1-response-requestid"></a>

The SDK now stores request IDs for all services in a consistent place on the `response` object, rather than inside the `response.data` property. This improves consistency across services that expose request IDs in different ways. This is also a breaking change that renames the `response.data.RequestId` property to `response.requestId` (`this.requestId` inside a callback function).

In your code, change the following:

```
svc.operation(params, function (err, data) {
  console.log('Request ID:', data.RequestId);
});
```

To the following:

```
svc.operation(params, function () {
  console.log('Request ID:', this.requestId);
});
```

## Exposed Wrapper Elements
<a name="upgrading-from-v1-exposed-wrapper-elements"></a>

If you use `AWS.ElastiCache`, `AWS.RDS`, or `AWS.Redshift`, you must access the response through the top-level output property in the response for some operations.

For example, the `RDS.describeEngineDefaultParameters` method used to return the following.

```
{ Parameters: [ ... ] }
```

It now returns the following.

```
{ EngineDefaults: { Parameters: [ ... ] } }
```

The list of affected operations for each service are shown in the following table.

| Client Class | Operations |
| --- | --- |
| `AWS.ElastiCache` | `authorizeCacheSecurityGroupIngress`<br />`createCacheCluster`<br />`createCacheParameterGroup`<br />`createCacheSecurityGroup`<br />`createCacheSubnetGroup`<br />`createReplicationGroup`<br />`deleteCacheCluster`<br />`deleteReplicationGroup`<br />`describeEngineDefaultParameters`<br />`modifyCacheCluster`<br />`modifyCacheSubnetGroup`<br />`modifyReplicationGroup`<br />`purchaseReservedCacheNodesOffering`<br />`rebootCacheCluster`<br />`revokeCacheSecurityGroupIngress` |
| `AWS.RDS` | `addSourceIdentifierToSubscription`<br />`authorizeDBSecurityGroupIngress`<br />`copyDBSnapshot` `createDBInstance`<br />`createDBInstanceReadReplica`<br />`createDBParameterGroup`<br />`createDBSecurityGroup`<br />`createDBSnapshot`<br />`createDBSubnetGroup`<br />`createEventSubscription`<br />`createOptionGroup`<br />`deleteDBInstance`<br />`deleteDBSnapshot`<br />`deleteEventSubscription`<br />`describeEngineDefaultParameters`<br />`modifyDBInstance`<br />`modifyDBSubnetGroup`<br />`modifyEventSubscription`<br />`modifyOptionGroup`<br />`promoteReadReplica`<br />`purchaseReservedDBInstancesOffering`<br />`rebootDBInstance`<br />`removeSourceIdentifierFromSubscription`<br />`restoreDBInstanceFromDBSnapshot`<br />`restoreDBInstanceToPointInTime`<br />`revokeDBSecurityGroupIngress` |
| `AWS.Redshift` | `authorizeClusterSecurityGroupIngress`<br />`authorizeSnapshotAccess`<br />`copyClusterSnapshot`<br />`createCluster`<br />`createClusterParameterGroup`<br />`createClusterSecurityGroup`<br />`createClusterSnapshot`<br />`createClusterSubnetGroup`<br />`createEventSubscription`<br />`createHsmClientCertificate`<br />`createHsmConfiguration`<br />`deleteCluster`<br />`deleteClusterSnapshot`<br />`describeDefaultClusterParameters`<br />`disableSnapshotCopy`<br />`enableSnapshotCopy`<br />`modifyCluster`<br />`modifyClusterSubnetGroup`<br />`modifyEventSubscription`<br />`modifySnapshotCopyRetentionPeriod`<br />`purchaseReservedNodeOffering`<br />`rebootCluster`<br />`restoreFromClusterSnapshot`<br />`revokeClusterSecurityGroupIngress`<br />`revokeSnapshotAccess`<br />`rotateEncryptionKey` |

## Dropped Client Properties
<a name="upgrading-from-v1-dropped-client-properties"></a>

The `.Client` and `.client` properties have been removed from service objects. If you use the `.Client` property on a service class or a `.client` property on a service object instance, remove these properties from your code.

The following code used with version 1 of the SDK for JavaScript:

```
var sts = new AWS.STS.Client();
// or
var sts = new AWS.STS();

sts.client.operation(...);
```

Should be changed to the following code.

```
var sts = new AWS.STS();
sts.operation(...)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for JavaScript SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
