---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ClientStat.html
---

# ClientStat
<a name="API_ClientStat"></a>

Details about clients using the deprecated resources.

## Contents
<a name="API_ClientStat_Contents"></a>

 ** lastRequestTime **   <a name="AmazonEKS-Type-ClientStat-lastRequestTime"></a>
The timestamp of the last request seen from the Kubernetes client.
Type: Timestamp
Required: No

 ** numberOfRequestsLast30Days **   <a name="AmazonEKS-Type-ClientStat-numberOfRequestsLast30Days"></a>
The number of requests from the Kubernetes client seen over the last 30 days.
Type: Integer
Required: No

 ** userAgent **   <a name="AmazonEKS-Type-ClientStat-userAgent"></a>
The user agent of the Kubernetes client using the deprecated resource.
Type: String
Required: No

## See Also
<a name="API_ClientStat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ClientStat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ClientStat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ClientStat)
