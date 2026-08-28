---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_AuthorizeCacheSecurityGroupIngress.html
---

# AuthorizeCacheSecurityGroupIngress
<a name="API_AuthorizeCacheSecurityGroupIngress"></a>

Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2, and Amazon EC2 security groups are used as the authorization mechanism.

**Note**
You cannot authorize ingress from an Amazon EC2 security group in one region to an ElastiCache cluster in another region.

## Request Parameters
<a name="API_AuthorizeCacheSecurityGroupIngress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheSecurityGroupName **
The cache security group that allows network ingress.
Type: String
Required: Yes

 ** EC2SecurityGroupName **
The Amazon EC2 security group to be authorized for ingress to the cache security group.
Type: String
Required: Yes

 ** EC2SecurityGroupOwnerId **
The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter.
Type: String
Required: Yes

## Response Elements
<a name="API_AuthorizeCacheSecurityGroupIngress_ResponseElements"></a>

The following element is returned by the service.

 ** CacheSecurityGroup **
Represents the output of one of the following operations:
+  `AuthorizeCacheSecurityGroupIngress`
+  `CreateCacheSecurityGroup`
+  `RevokeCacheSecurityGroupIngress`
Type: [CacheSecurityGroup](API_CacheSecurityGroup.md) object

## Errors
<a name="API_AuthorizeCacheSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationAlreadyExists **
The specified Amazon EC2 security group is already authorized for the specified cache security group.
HTTP Status Code: 400

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
<a name="API_AuthorizeCacheSecurityGroupIngress_Examples"></a>

### AuthorizeCacheSecurityGroupIngress
<a name="API_AuthorizeCacheSecurityGroupIngress_Example_1"></a>

This example illustrates one usage of AuthorizeCacheSecurityGroupIngress.

#### Sample Request
<a name="API_AuthorizeCacheSecurityGroupIngress_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=AuthorizeCacheSecurityGroupIngress
   &EC2SecurityGroupName=default
   &CacheSecurityGroupName=mygroup
   &EC2SecurityGroupOwnerId=1234-5678-1234
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

### Example
<a name="API_AuthorizeCacheSecurityGroupIngress_Example_2"></a>

This example illustrates one usage of AuthorizeCacheSecurityGroupIngress.

#### Sample Response
<a name="API_AuthorizeCacheSecurityGroupIngress_Example_2_Response"></a>

```
<AuthorizeCacheSecurityGroupIngressResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <AuthorizeCacheSecurityGroupIngressResult>
      <CacheSecurityGroup>
         <EC2SecurityGroups>
            <EC2SecurityGroup>
               <Status>authorizing</Status>
               <EC2SecurityGroupName>default</EC2SecurityGroupName>
               <EC2SecurityGroupOwnerId>565419523791</EC2SecurityGroupOwnerId>
            </EC2SecurityGroup>
         </EC2SecurityGroups>
         <CacheSecurityGroupName>mygroup</CacheSecurityGroupName>
         <OwnerId>123456781234</OwnerId>
         <Description>My security group</Description>
      </CacheSecurityGroup>
   </AuthorizeCacheSecurityGroupIngress>
   <ResponseMetadata>
      <RequestId>817fa999-3647-11e0-ae57-f96cfe56749c</RequestId>
   </ResponseMetadata>
</AuthorizeCacheSecurityGroupIngressResponse>
```

## See Also
<a name="API_AuthorizeCacheSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
