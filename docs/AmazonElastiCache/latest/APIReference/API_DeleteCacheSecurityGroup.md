---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteCacheSecurityGroup.html
---

# DeleteCacheSecurityGroup
<a name="API_DeleteCacheSecurityGroup"></a>

Deletes a cache security group.

**Note**
You cannot delete a cache security group if it is associated with any clusters.

## Request Parameters
<a name="API_DeleteCacheSecurityGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheSecurityGroupName **
The name of the cache security group to delete.
You cannot delete the default security group.
Type: String
Required: Yes

## Errors
<a name="API_DeleteCacheSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DeleteCacheSecurityGroup_Examples"></a>

### DeleteCacheSecurityGroup
<a name="API_DeleteCacheSecurityGroup_Example_1"></a>

This example illustrates one usage of DeleteCacheSecurityGroup.

#### Sample Request
<a name="API_DeleteCacheSecurityGroup_Example_1_Request"></a>

```
   https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteCacheSecurityGroup
   &CacheSecurityGroupName=mycachesecuritygroup3
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DeleteCacheSecurityGroup_Example_1_Response"></a>

```
<DeleteCacheSecurityGroupResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
    <ResponseMetadata>
        <RequestId>c130cfb7-3650-11e0-ae57-f96cfe56749c</RequestId>
    </ResponseMetadata>
</DeleteCacheSecurityGroupResponse>
```

## See Also
<a name="API_DeleteCacheSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteCacheSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteCacheSecurityGroup)
