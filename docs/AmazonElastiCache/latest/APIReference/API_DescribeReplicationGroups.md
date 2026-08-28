---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.html
---

# DescribeReplicationGroups
<a name="API_DescribeReplicationGroups"></a>

Returns information about a particular replication group. If no identifier is specified, `DescribeReplicationGroups` returns information about all replication groups.

**Note**
This operation is valid for Valkey or Redis OSS only.

## Request Parameters
<a name="API_DescribeReplicationGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: minimum 20; maximum 100.
Type: Integer
Required: No

 ** ReplicationGroupId **
The identifier for the replication group to be described. This parameter is not case sensitive.
If you do not specify this parameter, information about all replication groups is returned.
Type: String
Required: No

## Response Elements
<a name="API_DescribeReplicationGroups_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

 **ReplicationGroups.ReplicationGroup.N**
A list of replication groups. Each item in the list contains detailed information about one replication group.
Type: Array of [ReplicationGroup](API_ReplicationGroup.md) objects

## Errors
<a name="API_DescribeReplicationGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

## Examples
<a name="API_DescribeReplicationGroups_Examples"></a>

### DescribeReplicationGroups
<a name="API_DescribeReplicationGroups_Example_1"></a>

This example illustrates one usage of DescribeReplicationGroups.

#### Sample Request
<a name="API_DescribeReplicationGroups_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DescribeReplicationGroups
   &MaxRecords=100
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeReplicationGroups_Example_1_Response"></a>

```
<DescribeReplicationGroupsResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <DescribeReplicationGroupsResult>
      <ReplicationGroups>
         <ReplicationGroup>
            <SnapshottingClusterId>my-redis-primary</SnapshottingClusterId>
            <MemberClusters>
               <ClusterId>my-redis-primary</ClusterId>
            </MemberClusters>
            <NodeGroups>
               <NodeGroup>
                  <NodeGroupId>0001</NodeGroupId>
                  <PrimaryEndpoint>
                     <Port>6379</Port>
                     <Address>my-repgroup.q68zge.ng.0001.use1devo.elmo-dev.amazonaws.com</Address>
                  </PrimaryEndpoint>
                  <Status>available</Status>
                  <NodeGroupMembers>
                     <NodeGroupMember>
                        <CacheClusterId>my-redis-primary</CacheClusterId>
                        <ReadEndpoint>
                           <Port>6379</Port>
                           <Address>my-redis-primary.q68zge.0001.use1devo.elmo-dev.amazonaws.com</Address>
                        </ReadEndpoint>
                        <PreferredAvailabilityZone>us-west-2c</PreferredAvailabilityZone>
                        <CacheNodeId>0001</CacheNodeId>
                        <CurrentRole>primary</CurrentRole>
                     </NodeGroupMember>
                  </NodeGroupMembers>
               </NodeGroup>
            </NodeGroups>
            <ReplicationGroupId>my-repgroup</ReplicationGroupId>
            <Status>available</Status>
            <PendingModifiedValues />
            <Description>My replication group</Description>
         </ReplicationGroup>
      </ReplicationGroups>
   </DescribeReplicationGroupsResult>
   <ResponseMetadata>
      <RequestId>144745b0-b9d3-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</DescribeReplicationGroupsResponse>
```

## See Also
<a name="API_DescribeReplicationGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeReplicationGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeReplicationGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
