---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesActivity.html
---

# KubernetesActivity
<a name="API_KubernetesActivity"></a>

Contains details about Kubernetes activity. A record contains either `ApiCall` and `Enrichment`, or `Anomaly` and `Workload`.

## Contents
<a name="API_KubernetesActivity_Contents"></a>

 ** anomaly **   <a name="guardduty-Type-KubernetesActivity-anomaly"></a>
Details about anomalous Kubernetes behavior.
Type: [KubernetesAnomaly](API_KubernetesAnomaly.md) object
Required: No

 ** apiCall **   <a name="guardduty-Type-KubernetesActivity-apiCall"></a>
Details about a Kubernetes API call.
Type: [KubernetesApiCall](API_KubernetesApiCall.md) object
Required: No

 ** enrichment **   <a name="guardduty-Type-KubernetesActivity-enrichment"></a>
Additional context about the API call, such as geolocation information.
Type: [Enrichment](API_Enrichment.md) object
Required: No

 ** workload **   <a name="guardduty-Type-KubernetesActivity-workload"></a>
The Kubernetes workload that is associated with the anomaly.
Type: [InvestigationKubernetesWorkload](API_InvestigationKubernetesWorkload.md) object
Required: No

## See Also
<a name="API_KubernetesActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesActivity)
