---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesApiCallAction.html
---

# KubernetesApiCallAction
<a name="API_KubernetesApiCallAction"></a>

Information about the Kubernetes API call action described in this finding.

## Contents
<a name="API_KubernetesApiCallAction_Contents"></a>

 ** namespace **   <a name="guardduty-Type-KubernetesApiCallAction-namespace"></a>
The name of the namespace where the Kubernetes API call action takes place.
Type: String
Required: No

 ** parameters **   <a name="guardduty-Type-KubernetesApiCallAction-parameters"></a>
Parameters related to the Kubernetes API call action.
Type: String
Required: No

 ** remoteIpDetails **   <a name="guardduty-Type-KubernetesApiCallAction-remoteIpDetails"></a>
Contains information about the remote IP address of the connection.
Type: [RemoteIpDetails](API_RemoteIpDetails.md) object
Required: No

 ** requestUri **   <a name="guardduty-Type-KubernetesApiCallAction-requestUri"></a>
The Kubernetes API request URI.
Type: String
Required: No

 ** resource **   <a name="guardduty-Type-KubernetesApiCallAction-resource"></a>
The resource component in the Kubernetes API call action.
Type: String
Required: No

 ** resourceName **   <a name="guardduty-Type-KubernetesApiCallAction-resourceName"></a>
The name of the resource in the Kubernetes API call action.
Type: String
Required: No

 ** sourceIPs **   <a name="guardduty-Type-KubernetesApiCallAction-sourceIPs"></a>
The IP of the Kubernetes API caller and the IPs of any proxies or load balancers between the caller and the API endpoint.
Type: Array of strings
Required: No

 ** statusCode **   <a name="guardduty-Type-KubernetesApiCallAction-statusCode"></a>
The resulting HTTP response code of the Kubernetes API call action.
Type: Integer
Required: No

 ** subresource **   <a name="guardduty-Type-KubernetesApiCallAction-subresource"></a>
The name of the sub-resource in the Kubernetes API call action.
Type: String
Required: No

 ** userAgent **   <a name="guardduty-Type-KubernetesApiCallAction-userAgent"></a>
The user agent of the caller of the Kubernetes API.
Type: String
Required: No

 ** verb **   <a name="guardduty-Type-KubernetesApiCallAction-verb"></a>
The Kubernetes API request HTTP verb.
Type: String
Required: No

## See Also
<a name="API_KubernetesApiCallAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesApiCallAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesApiCallAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesApiCallAction)
