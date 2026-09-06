---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeTags.html
---

# DescribeTags
<a name="API_DescribeTags"></a>

Describes the tags associated with the specified load balancers.

## Request Parameters
<a name="API_DescribeTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **LoadBalancerNames.member.N**
The names of the load balancers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Elements
<a name="API_DescribeTags_ResponseElements"></a>

The following element is returned by the service.

 **TagDescriptions.member.N**
Information about the tags.
Type: Array of [TagDescription](API_TagDescription.md) objects

## Errors
<a name="API_DescribeTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTags_Examples"></a>

### Describe load balancer tags
<a name="API_DescribeTags_Example_1"></a>

This example describes the tags assigned to the specified load balancer.

#### Sample Request
<a name="API_DescribeTags_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTags
&LoadBalancerNames.member.1=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_1_Response"></a>

```
<DescribeTagsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeTagsResult>
    <TagDescriptions>
      <member>
        <Tags>
          <member>
            <Value>lima</Value>
            <Key>project</Key>
          </member>
          <member>
            <Value>digital-media</Value>
            <Key>department</Key>
          </member>
        </Tags>
        <LoadBalancerName>my-loadbalancer</LoadBalancerName>
      </member>
    </TagDescriptions>
  </DescribeTagsResult>
  <ResponseMetadata>
    <RequestId>07b1ecbc-1100-11e3-acaf-dd7edEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeTagsResponse>
```

## See Also
<a name="API_DescribeTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DescribeTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DescribeTags)
