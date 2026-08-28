---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheSubnetGroups.html
---

# DescribeCacheSubnetGroups
<a name="API_DescribeCacheSubnetGroups"></a>

Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group. This is applicable only when you have ElastiCache in VPC setup. All ElastiCache clusters now launch in VPC by default.

## Request Parameters
<a name="API_DescribeCacheSubnetGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheSubnetGroupName **
The name of the cache subnet group to return details for.
Type: String
Required: No

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

## Response Elements
<a name="API_DescribeCacheSubnetGroups_ResponseElements"></a>

The following elements are returned by the service.

 **CacheSubnetGroups.CacheSubnetGroup.N**
A list of cache subnet groups. Each element in the list contains detailed information about one group.
Type: Array of [CacheSubnetGroup](API_CacheSubnetGroup.md) objects

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

## Errors
<a name="API_DescribeCacheSubnetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheSubnetGroupNotFoundFault **
The requested cache subnet group name does not refer to an existing cache subnet group.
HTTP Status Code: 400

## Examples
<a name="API_DescribeCacheSubnetGroups_Examples"></a>

### DescribeCacheSubnetGroups
<a name="API_DescribeCacheSubnetGroups_Example_1"></a>

Some of the output has been omitted for brevity.

#### Sample Request
<a name="API_DescribeCacheSubnetGroups_Example_1_Request"></a>

```
https://elasticache.amazonaws.com/
   ?Action=DescribeCacheSubnetGroups
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeCacheSubnetGroups_Example_1_Response"></a>

```
<DescribeCacheSubnetGroupsResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
        <DescribeCacheSubnetGroupsResult>
            <CacheSubnetGroups>
                <CacheSubnetGroup>
                    <VpcId>990524496922</VpcId>
                    <CacheSubnetGroupDescription>description</CacheSubnetGroupDescription>
                    <CacheSubnetGroupName>subnet_grp1</CacheSubnetGroupName>
                    <Subnets>
                        <Subnet>
                            <SubnetStatus>Active</SubnetStatus>
                            <SubnetIdentifier>subnet-7c5b4115</SubnetIdentifier>
                            <SubnetAvailabilityZone>
                                <Name>us-west-2c</Name>
                            </SubnetAvailabilityZone>
                        </Subnet>
                        <Subnet>
                            <SubnetStatus>Active</SubnetStatus>
                            <SubnetIdentifier>subnet-7b5b4112</SubnetIdentifier>
                            <SubnetAvailabilityZone>
                                <Name>us-west-2b</Name>
                            </SubnetAvailabilityZone>
                        </Subnet>
                        <Subnet>
                            <SubnetStatus>Active</SubnetStatus>
                            <SubnetIdentifier>subnet-3ea6bd57</SubnetIdentifier>
                            <SubnetAvailabilityZone>
                                <Name>us-west-2c</Name>
                            </SubnetAvailabilityZone>
                        </Subnet>
                    </Subnets>
                </CacheSubnetGroup>

 (...output omitted...)

            </CacheSubnetGroups>
        </DescribeCacheSubnetGroupsResult>
        <ResponseMetadata>
            <RequestId>31d0faee-229b-11e1-81f1-df3a2a803dad</RequestId>
        </ResponseMetadata>
    </DescribeCacheSubnetGroupsResponse>
```

## See Also
<a name="API_DescribeCacheSubnetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeCacheSubnetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeCacheSubnetGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
