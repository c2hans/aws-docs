---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_ListConnections.html
---

# ListConnections
<a name="API_ListConnections"></a>

Lists all connection objects to which the caller has access.

Allows for optional filtering by the following properties:
+  `state`
+  `environmentId`
+  `provider`
+  `attach point`

Only [Connection](API_Connection.md) objects matching all filters will be returned.

## Request Parameters
<a name="API_ListConnections_RequestParameters"></a>

 ** attachPoint **
Filter results to only include [Connection](API_Connection.md) objects attached to the given [AttachPoint](API_AttachPoint.md).
Type: [AttachPoint](API_AttachPoint.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** environmentId **
Filter the results to only include [Connection](API_Connection.md) objects on the given [Environment](API_Environment.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** maxResults **
The max number of list results in a single paginated response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A pagination token from a previous paginated response indicating you wish to get the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** provider **
Filter the results to only include [Connection](API_Connection.md) objects to the given [Provider](API_Provider.md).
Type: [Provider](API_Provider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** state **
Filter the results to only include [Connection](API_Connection.md) objects in the given [Connection:state](API_Connection.md#interconnect-Type-Connection-state).
Type: String
Valid Values: `available | requested | pending | down | deleting | deleted | failed | updating`
Required: No

## Response Elements
<a name="API_ListConnections_ResponseElements"></a>

The following elements are returned by the service.

 ** connections **
The resulting list of [Connection](API_Connection.md) objects.
Type: Array of [ConnectionSummary](API_ConnectionSummary.md) objects

 ** nextToken **
A pagination token for use in subsequent calls to fetch the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The calling principal is not allowed to access the specified resource, or the resource does not exist.
HTTP Status Code: 403

 ** InterconnectClientException **
The request was denied due to incorrect client supplied parameters.
HTTP Status Code: 400

 ** InterconnectServerException **
The request resulted in an exception internal to the service.
HTTP Status Code: 500

 ** InterconnectValidationException **
The input fails to satisfy the constraints specified.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request specifies a resource that does not exist on the server.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation would result in the calling principal exceeding their allotted quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ListConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/ListConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/ListConnections)
