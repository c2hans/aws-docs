---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListVirtualClusters.html
---

# ListVirtualClusters
<a name="API_ListVirtualClusters"></a>

Lists information about the specified virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

## Request Syntax
<a name="API_ListVirtualClusters_RequestSyntax"></a>

```
GET /virtualclusters?containerProviderId={{containerProviderId}}&containerProviderType={{containerProviderType}}&createdAfter={{createdAfter}}&createdBefore={{createdBefore}}&eksAccessEntryIntegrated={{eksAccessEntryIntegrated}}&maxResults={{maxResults}}&nextToken={{nextToken}}&states={{states}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVirtualClusters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [containerProviderId](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-containerProviderId"></a>
The container provider ID of the virtual cluster.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [containerProviderType](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-containerProviderType"></a>
The container provider type of the virtual cluster. Amazon EKS is the only supported type as of now.
Valid Values: `EKS`

 ** [createdAfter](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-createdAfter"></a>
The date and time after which the virtual clusters are created.

 ** [createdBefore](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-createdBefore"></a>
The date and time before which the virtual clusters are created.

 ** [eksAccessEntryIntegrated](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-eksAccessEntryIntegrated"></a>
Optional Boolean that specifies whether the operation should return the virtual clusters that have the access entry integration enabled or disabled. If not specified, the operation returns all applicable virtual clusters.

 ** [maxResults](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-maxResults"></a>
The maximum number of virtual clusters that can be listed.

 ** [nextToken](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-nextToken"></a>
The token for the next set of virtual clusters to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [states](#API_ListVirtualClusters_RequestSyntax) **   <a name="emroneks-ListVirtualClusters-request-uri-states"></a>
The states of the requested virtual clusters.
Array Members: Maximum number of 10 items.
Valid Values: `RUNNING | TERMINATING | TERMINATED | ARRESTED`

## Request Body
<a name="API_ListVirtualClusters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVirtualClusters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "virtualClusters": [
      {
         "arn": "string",
         "containerProvider": {
            "id": "string",
            "info": { ... },
            "type": "string"
         },
         "createdAt": "string",
         "id": "string",
         "name": "string",
         "securityConfigurationId": "string",
         "state": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListVirtualClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVirtualClusters_ResponseSyntax) **   <a name="emroneks-ListVirtualClusters-response-nextToken"></a>
This output displays the token for the next set of virtual clusters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [virtualClusters](#API_ListVirtualClusters_ResponseSyntax) **   <a name="emroneks-ListVirtualClusters-response-virtualClusters"></a>
This output lists the specified virtual clusters.
Type: Array of [VirtualCluster](API_VirtualCluster.md) objects

## Errors
<a name="API_ListVirtualClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_ListVirtualClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/ListVirtualClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ListVirtualClusters)
