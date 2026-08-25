---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateVirtualCluster.html
---

# CreateVirtualCluster
<a name="API_CreateVirtualCluster"></a>

Creates a virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, update, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

## Request Syntax
<a name="API_CreateVirtualCluster_RequestSyntax"></a>

```
POST /virtualclusters HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "containerProvider": {
      "id": "{{string}}",
      "info": { ... },
      "type": "{{string}}"
   },
   "name": "{{string}}",
   "schedulerConfiguration": {
      "maxConcurrentJobRuns": {{number}},
      "maxInQueueJobRuns": {{number}}
   },
   "securityConfigurationId": "{{string}}",
   "sessionEnabled": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateVirtualCluster_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVirtualCluster_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-clientToken"></a>
The client token of the virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [containerProvider](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-containerProvider"></a>
The container provider of the virtual cluster.
Type: [ContainerProvider](API_ContainerProvider.md) object
Required: Yes

 ** [name](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-name"></a>
The specified name of the virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [schedulerConfiguration](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-schedulerConfiguration"></a>
The scheduler configuration (concurrency and queue limits) to apply to the virtual cluster at creation time. When omitted, no limits are applied.
Type: [SchedulerConfiguration](API_SchedulerConfiguration.md) object
Required: No

 ** [securityConfigurationId](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-securityConfigurationId"></a>
The ID of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** [sessionEnabled](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-sessionEnabled"></a>
Indicates whether the virtual cluster has session support enabled.
Type: Boolean
Required: No

 ** [tags](#API_CreateVirtualCluster_RequestSyntax) **   <a name="emroneks-CreateVirtualCluster-request-tags"></a>
The tags assigned to the virtual cluster.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_CreateVirtualCluster_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateVirtualCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateVirtualCluster_ResponseSyntax) **   <a name="emroneks-CreateVirtualCluster-response-arn"></a>
This output contains the ARN of virtual cluster.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+$`

 ** [id](#API_CreateVirtualCluster_ResponseSyntax) **   <a name="emroneks-CreateVirtualCluster-response-id"></a>
This output contains the virtual cluster ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [name](#API_CreateVirtualCluster_ResponseSyntax) **   <a name="emroneks-CreateVirtualCluster-response-name"></a>
This output contains the name of the virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`

## Errors
<a name="API_CreateVirtualCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EKSRequestThrottledException **
The request exceeded the Amazon EKS API operation limits.
HTTP Status Code: 429

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_CreateVirtualCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/CreateVirtualCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/CreateVirtualCluster)
