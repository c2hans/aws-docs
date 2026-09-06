---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxClusters.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# ListKxClusters
<a name="API_ListKxClusters"></a>

Returns a list of clusters.

## Request Syntax
<a name="API_ListKxClusters_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/clusters?clusterType={{clusterType}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListKxClusters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterType](#API_ListKxClusters_RequestSyntax) **   <a name="finspace-ListKxClusters-request-uri-clusterType"></a>
Specifies the type of KDB database that is being created. The following types are available:
+ HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.
+ RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the `savedownStorageConfiguration` parameter.
+ GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.
+ GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only `SINGLE` AZ mode.
+ Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.
Valid Values: `HDB | RDB | GATEWAY | GP | TICKERPLANT`

 ** [environmentId](#API_ListKxClusters_RequestSyntax) **   <a name="finspace-ListKxClusters-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** [maxResults](#API_ListKxClusters_RequestSyntax) **   <a name="finspace-ListKxClusters-request-uri-maxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [nextToken](#API_ListKxClusters_RequestSyntax) **   <a name="finspace-ListKxClusters-request-uri-nextToken"></a>
A token that indicates where a results page should begin.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Request Body
<a name="API_ListKxClusters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListKxClusters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kxClusterSummaries": [
      {
         "availabilityZoneId": "string",
         "azMode": "string",
         "clusterDescription": "string",
         "clusterName": "string",
         "clusterType": "string",
         "createdTimestamp": number,
         "executionRole": "string",
         "initializationScript": "string",
         "lastModifiedTimestamp": number,
         "releaseLabel": "string",
         "status": "string",
         "statusReason": "string",
         "volumes": [
            {
               "volumeName": "string",
               "volumeType": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListKxClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kxClusterSummaries](#API_ListKxClusters_ResponseSyntax) **   <a name="finspace-ListKxClusters-response-kxClusterSummaries"></a>
Lists the cluster details.
Type: Array of [KxCluster](API_KxCluster.md) objects

 ** [nextToken](#API_ListKxClusters_ResponseSyntax) **   <a name="finspace-ListKxClusters-response-nextToken"></a>
A token that indicates where a results page should begin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Errors
<a name="API_ListKxClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListKxClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/ListKxClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/ListKxClusters)
