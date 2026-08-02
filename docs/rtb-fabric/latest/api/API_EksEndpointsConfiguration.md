---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_EksEndpointsConfiguration.html
---

# EksEndpointsConfiguration
<a name="API_EksEndpointsConfiguration"></a>

Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.

## Contents
<a name="API_EksEndpointsConfiguration_Contents"></a>

 ** clusterApiServerCaCertificateChain **   <a name="rtbfabric-Type-EksEndpointsConfiguration-clusterApiServerCaCertificateChain"></a>
The CA certificate chain of the cluster API server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2097152.
Required: Yes

 ** clusterApiServerEndpointUri **   <a name="rtbfabric-Type-EksEndpointsConfiguration-clusterApiServerEndpointUri"></a>
The URI of the cluster API server endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(https|http)://(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(?:\.(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?))+`
Required: Yes

 ** clusterName **   <a name="rtbfabric-Type-EksEndpointsConfiguration-clusterName"></a>
The name of the cluster.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 63.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]`
Required: Yes

 ** endpointsResourceName **   <a name="rtbfabric-Type-EksEndpointsConfiguration-endpointsResourceName"></a>
The name of the endpoint resource.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 63.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]`
Required: Yes

 ** endpointsResourceNamespace **   <a name="rtbfabric-Type-EksEndpointsConfiguration-endpointsResourceNamespace"></a>
The namespace of the endpoint resource.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 63.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]`
Required: Yes

 ** roleArn **   <a name="rtbfabric-Type-EksEndpointsConfiguration-roleArn"></a>
The role ARN for the cluster.
Type: String
Pattern: `arn:aws:iam::[0-9]{12}:role/.{1,2048}`
Required: Yes

## See Also
<a name="API_EksEndpointsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/EksEndpointsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/EksEndpointsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/EksEndpointsConfiguration)
