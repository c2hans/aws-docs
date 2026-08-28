---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_UpdateVirtualCluster.html
---

# UpdateVirtualCluster
<a name="API_UpdateVirtualCluster"></a>

Updates a virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, update, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

## Request Syntax
<a name="API_UpdateVirtualCluster_RequestSyntax"></a>

```
PATCH /virtualclusters/{{virtualClusterId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "schedulerConfiguration": {
      "maxConcurrentJobRuns": {{number}},
      "maxInQueueJobRuns": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateVirtualCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [virtualClusterId](#API_UpdateVirtualCluster_RequestSyntax) **   <a name="emroneks-UpdateVirtualCluster-request-uri-id"></a>
The ID of the virtual cluster to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_UpdateVirtualCluster_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateVirtualCluster_RequestSyntax) **   <a name="emroneks-UpdateVirtualCluster-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [schedulerConfiguration](#API_UpdateVirtualCluster_RequestSyntax) **   <a name="emroneks-UpdateVirtualCluster-request-schedulerConfiguration"></a>
The scheduler configuration to apply to the virtual cluster. The new configuration fully replaces the existing one. If you omit a field, the corresponding limit is removed.
Type: [SchedulerConfiguration](API_SchedulerConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateVirtualCluster_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "virtualCluster": {
      "arn": "string",
      "containerProvider": {
         "id": "string",
         "info": { ... },
         "type": "string"
      },
      "createdAt": "string",
      "id": "string",
      "name": "string",
      "schedulerConfiguration": {
         "maxConcurrentJobRuns": number,
         "maxInQueueJobRuns": number
      },
      "schedulerStatus": {
         "currentConcurrentJobRuns": number,
         "currentInQueueJobRuns": number
      },
      "securityConfigurationId": "string",
      "sessionEnabled": boolean,
      "state": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateVirtualCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualCluster](#API_UpdateVirtualCluster_ResponseSyntax) **   <a name="emroneks-UpdateVirtualCluster-response-virtualCluster"></a>
The updated virtual cluster.
Type: [VirtualCluster](API_VirtualCluster.md) object

## Errors
<a name="API_UpdateVirtualCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateVirtualCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/UpdateVirtualCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/UpdateVirtualCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
