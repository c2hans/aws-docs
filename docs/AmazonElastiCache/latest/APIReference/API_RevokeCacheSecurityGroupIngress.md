---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RevokeCacheSecurityGroupIngress.html
---

# RevokeCacheSecurityGroupIngress
<a name="API_RevokeCacheSecurityGroupIngress"></a>

Revokes ingress from a cache security group. Use this operation to disallow access from an Amazon EC2 security group that had been previously authorized.

## Request Parameters
<a name="API_RevokeCacheSecurityGroupIngress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheSecurityGroupName **
The name of the cache security group to revoke ingress from.
Type: String
Required: Yes

 ** EC2SecurityGroupName **
The name of the Amazon EC2 security group to revoke access from.
Type: String
Required: Yes

 ** EC2SecurityGroupOwnerId **
The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter.
Type: String
Required: Yes

## Response Elements
<a name="API_RevokeCacheSecurityGroupIngress_ResponseElements"></a>

The following element is returned by the service.

 ** CacheSecurityGroup **
Represents the output of one of the following operations:
+  `AuthorizeCacheSecurityGroupIngress`
+  `CreateCacheSecurityGroup`
+  `RevokeCacheSecurityGroupIngress`
Type: [CacheSecurityGroup](API_CacheSecurityGroup.md) object

## Errors
<a name="API_RevokeCacheSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **
The specified Amazon EC2 security group is not authorized for the specified cache security group.
HTTP Status Code: 404

 ** CacheSecurityGroupNotFound **
The requested cache security group name does not refer to an existing cache security group.
HTTP Status Code: 404

 ** InvalidCacheSecurityGroupState **
The current state of the cache security group does not allow deletion.
HTTP Status Code: 400

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

## Examples
<a name="API_RevokeCacheSecurityGroupIngress_Examples"></a>

### RevokeCacheSecurityGroupIngress
<a name="API_RevokeCacheSecurityGroupIngress_Example_1"></a>

This example illustrates one usage of RevokeCacheSecurityGroupIngress.

#### Sample Request
<a name="API_RevokeCacheSecurityGroupIngress_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=RevokeCacheSecurityGroupIngress
   &EC2SecurityGroupName=default
   &CacheSecurityGroupName=mygroup
   &EC2SecurityGroupOwnerId=1234-5678-1234
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_RevokeCacheSecurityGroupIngress_Example_1_Response"></a>

```
<RevokeCacheSecurityGroupIngressResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
    <RevokeCacheSecurityGroupIngressResult>
        <CacheSecurityGroup>
            <EC2SecurityGroups>
                <EC2SecurityGroup>
                    <Status>revoking</Status>
                    <EC2SecurityGroupName>default</EC2SecurityGroupName>
                    <EC2SecurityGroupOwnerId>123456781234</EC2SecurityGroupOwnerId>
                </EC2SecurityGroup>
            </EC2SecurityGroups>
            <CacheSecurityGroupName>mygroup</CacheSecurityGroupName>
            <OwnerId>123456789012</OwnerId>
            <Description>My security group</Description>
        </CacheSecurityGroup>
    </RevokeCacheSecurityGroupIngressResult>
    <ResponseMetadata>
        <RequestId>02ae3699-3650-11e0-a564-8f11342c56b0</RequestId>
    </ResponseMetadata>
</RevokeCacheSecurityGroupIngressResponse>
```

## See Also
<a name="API_RevokeCacheSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
