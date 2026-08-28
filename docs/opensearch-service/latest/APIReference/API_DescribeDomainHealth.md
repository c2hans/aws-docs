---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainHealth.html
---

# DescribeDomainHealth
<a name="API_DescribeDomainHealth"></a>

Returns information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node.

## Request Syntax
<a name="API_DescribeDomainHealth_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/health HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainHealth_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDomainHealth_RequestSyntax) **   <a name="opensearchservice-DescribeDomainHealth-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomainHealth_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainHealth_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActiveAvailabilityZoneCount": "string",
   "AvailabilityZoneCount": "string",
   "ClusterHealth": "string",
   "DataNodeCount": "string",
   "DedicatedMaster": boolean,
   "DomainState": "string",
   "EnvironmentInformation": [
      {
         "AvailabilityZoneInformation": [
            {
               "AvailabilityZoneName": "string",
               "AvailableDataNodeCount": "string",
               "ConfiguredDataNodeCount": "string",
               "TotalShards": "string",
               "TotalUnAssignedShards": "string",
               "ZoneStatus": "string"
            }
         ]
      }
   ],
   "MasterEligibleNodeCount": "string",
   "MasterNode": "string",
   "StandByAvailabilityZoneCount": "string",
   "TotalShards": "string",
   "TotalUnAssignedShards": "string",
   "WarmNodeCount": "string"
}
```

## Response Elements
<a name="API_DescribeDomainHealth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActiveAvailabilityZoneCount](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-ActiveAvailabilityZoneCount"></a>
The number of active Availability Zones configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable`.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [AvailabilityZoneCount](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-AvailabilityZoneCount"></a>
The number of Availability Zones configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable`.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [ClusterHealth](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-ClusterHealth"></a>
The current health status of your cluster.
+  `Red` - At least one primary shard is not allocated to any node.
+  `Yellow` - All primary shards are allocated to nodes, but some replicas aren’t.
+  `Green` - All primary shards and their replicas are allocated to nodes.
+  `NotAvailable` - Unable to retrieve cluster health.
Type: String
Valid Values: `Red | Yellow | Green | NotAvailable`

 ** [DataNodeCount](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-DataNodeCount"></a>
The number of data nodes configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable`.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [DedicatedMaster](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-DedicatedMaster"></a>
A boolean that indicates if dedicated master nodes are activated for the domain.
Type: Boolean

 ** [DomainState](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-DomainState"></a>
The current state of the domain.
+  `Processing` - The domain has updates in progress.
+  `Active` - Requested changes have been processed and deployed to the domain.
Type: String
Valid Values: `Active | Processing | NotAvailable`

 ** [EnvironmentInformation](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-EnvironmentInformation"></a>
A list of `EnvironmentInfo` for the domain.
Type: Array of [EnvironmentInfo](API_EnvironmentInfo.md) objects

 ** [MasterEligibleNodeCount](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-MasterEligibleNodeCount"></a>
The number of nodes that can be elected as a master node. If dedicated master nodes is turned on, this value is the number of dedicated master nodes configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable`.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [MasterNode](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-MasterNode"></a>
Indicates whether the domain has an elected master node.
+  **Available** - The domain has an elected master node.
+  **UnAvailable** - The master node hasn't yet been elected, and a quorum to elect a new master node hasn't been reached.
Type: String
Valid Values: `Available | UnAvailable`

 ** [StandByAvailabilityZoneCount](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-StandByAvailabilityZoneCount"></a>
The number of standby Availability Zones configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable`.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [TotalShards](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-TotalShards"></a>
The total number of primary and replica shards for the domain.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [TotalUnAssignedShards](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-TotalUnAssignedShards"></a>
The total number of primary and replica shards not allocated to any of the nodes for the cluster.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

 ** [WarmNodeCount](#API_DescribeDomainHealth_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainHealth-response-WarmNodeCount"></a>
The number of warm nodes configured for the domain.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`

## Errors
<a name="API_DescribeDomainHealth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDomainHealth_Examples"></a>

### Example
<a name="API_DescribeDomainHealth_Example_1"></a>

This example illustrates one usage of DescribeDomainHealth.

#### Sample Request
<a name="API_DescribeDomainHealth_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/domain/amazonrocks/health HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.describe-domain-health
X-Amz-Date: 20240209T222820Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEEcaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240209/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=786d6e7ab6725d07b29cde81430b8e57dc2e87e4667c2879de84ab1b94dea451
```

#### Sample Response
<a name="API_DescribeDomainHealth_Example_1_Response"></a>

```
{
   "ActiveAvailabilityZoneCount":"3",
   "AvailabilityZoneCount":"3",
   "ClusterHealth":"Green",
   "DataNodeCount":"3",
   "DedicatedMaster":false,
   "DomainState":"Active",
   "EnvironmentInformation":[
      {
         "AvailabilityZoneInformation":[
            {
               "AvailabilityZoneName":"us-east-1b",
               "AvailableDataNodeCount":"1",
               "ConfiguredDataNodeCount":"1",
               "TotalShards":"6",
               "TotalUnAssignedShards":"NotAvailable",
               "ZoneStatus":"Active"
            },
            {
               "AvailabilityZoneName":"us-east-1c",
               "AvailableDataNodeCount":"1",
               "ConfiguredDataNodeCount":"1",
               "TotalShards":"7",
               "TotalUnAssignedShards":"NotAvailable",
               "ZoneStatus":"Active"
            },
            {
               "AvailabilityZoneName":"us-east-1d",
               "AvailableDataNodeCount":"1",
               "ConfiguredDataNodeCount":"1",
               "TotalShards":"6",
               "TotalUnAssignedShards":"NotAvailable",
               "ZoneStatus":"Active"
            }
         ]
      }
   ],
   "MasterEligibleNodeCount":"3",
   "MasterNode":"Available",
   "StandByAvailabilityZoneCount":"0",
   "TotalShards":"19",
   "TotalUnAssignedShards":"0",
   "WarmNodeCount":"0"
}
```

## See Also
<a name="API_DescribeDomainHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomainHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomainHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
