---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesApiCall.html
---

# KubernetesApiCall
<a name="API_KubernetesApiCall"></a>

Contains details about a Kubernetes API call.

## Contents
<a name="API_KubernetesApiCall_Contents"></a>

 ** clusterName **   <a name="guardduty-Type-KubernetesApiCall-clusterName"></a>
The name of the cluster.
Type: String
Required: No

 ** eventCount **   <a name="guardduty-Type-KubernetesApiCall-eventCount"></a>
The number of matching API calls.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** namespace **   <a name="guardduty-Type-KubernetesApiCall-namespace"></a>
The Kubernetes namespace of the resource.
Type: String
Required: No

 ** requestUri **   <a name="guardduty-Type-KubernetesApiCall-requestUri"></a>
The URI of the request.
Type: String
Required: No

 ** resourceName **   <a name="guardduty-Type-KubernetesApiCall-resourceName"></a>
The name of the Kubernetes resource.
Type: String
Required: No

 ** resourceType **   <a name="guardduty-Type-KubernetesApiCall-resourceType"></a>
The type of the Kubernetes resource.
Type: String
Required: No

 ** sourceIPs **   <a name="guardduty-Type-KubernetesApiCall-sourceIPs"></a>
The source IP addresses of the API call.
Type: String
Required: No

 ** statusCode **   <a name="guardduty-Type-KubernetesApiCall-statusCode"></a>
The status code of the API call.
Type: Integer
Required: No

 ** userAgent **   <a name="guardduty-Type-KubernetesApiCall-userAgent"></a>
The user agent of the caller.
Type: String
Required: No

 ** userGroups **   <a name="guardduty-Type-KubernetesApiCall-userGroups"></a>
The Kubernetes groups of the caller.
Type: String
Required: No

 ** userId **   <a name="guardduty-Type-KubernetesApiCall-userId"></a>
The ID of the caller.
Type: String
Required: No

 ** username **   <a name="guardduty-Type-KubernetesApiCall-username"></a>
The Kubernetes user name of the caller.
Type: String
Required: No

 ** verb **   <a name="guardduty-Type-KubernetesApiCall-verb"></a>
The Kubernetes API verb, such as `get` or `create`.
Type: String
Required: No

## See Also
<a name="API_KubernetesApiCall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesApiCall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesApiCall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesApiCall)
