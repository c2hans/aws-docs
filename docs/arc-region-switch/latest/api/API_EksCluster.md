---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EksCluster.html
---

# EksCluster
<a name="API_EksCluster"></a>

The AWS EKS cluster execution block configuration.

## Contents
<a name="API_EksCluster_Contents"></a>

 ** clusterArn **   <a name="regionswitch-Type-EksCluster-clusterArn"></a>
The Amazon Resource Name (ARN) of an AWS EKS cluster.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:eks:[a-z0-9-]+:\d{12}:cluster/[a-zA-Z0-9][a-zA-Z0-9-_]{0,99}`
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-EksCluster-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-EksCluster-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

## See Also
<a name="API_EksCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/EksCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/EksCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/EksCluster)
