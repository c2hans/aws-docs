---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListenerCertificates.html
---

# DescribeListenerCertificates
<a name="API_DescribeListenerCertificates"></a>

Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.

If the default certificate is also in the certificate list, it appears twice in the results (once with `IsDefault` set to true and once with `IsDefault` set to false).

For more information, see [SSL certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html) in the *Application Load Balancers Guide* or [Server certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html) in the *Network Load Balancers Guide*.

## Request Parameters
<a name="API_DescribeListenerCertificates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ListenerArn **
The Amazon Resource Names (ARN) of the listener.
Type: String
Required: Yes

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

## Response Elements
<a name="API_DescribeListenerCertificates_ResponseElements"></a>

The following elements are returned by the service.

 **Certificates.member.N**
Information about the certificates.
Type: Array of [Certificate](API_Certificate.md) objects

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

## Errors
<a name="API_DescribeListenerCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeListenerCertificates_Examples"></a>

### Describe the certificate list for a listener
<a name="API_DescribeListenerCertificates_Example_1"></a>

This example describes the certificate list for the specified listener.

#### Sample Request
<a name="API_DescribeListenerCertificates_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeListenerCertificates
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeListenerCertificates_Example_1_Response"></a>

```
<DescribeListenerCertificatesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeListenerCertificatesResult>
    <Certificates>
      <member>
        <CertificateArn>arn:aws:acm:us-west-2:123456789012:certificate/1bf70a25-6914-495a-92f8-e27feEXAMPLE</CertificateArn>
        <IsDefault>true</IsDefault>
      </member>
      <member>
        <CertificateArn>arn:aws:acm:us-west-2:123456789012:certificate/68c11a12-39de-44dd-b329-fe64aEXAMPLE</CertificateArn>
        <IsDefault>false</IsDefault>
      </member>
      <member>
        <CertificateArn>arn:aws:acm:us-west-2:123456789012:certificate/1bf70a25-6914-495a-92f8-e27feEXAMPLE</CertificateArn>
        <IsDefault>false</IsDefault>
      </member>
    </Certificates>
  </DescribeListenerCertificatesResult>
  <ResponseMetadata>
    <RequestId>18e470d3-f39c-11e5-a53c-67205c0d10fd</RequestId>
  </ResponseMetadata>
</DescribeListenerCertificatesResponse>
```

## See Also
<a name="API_DescribeListenerCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
