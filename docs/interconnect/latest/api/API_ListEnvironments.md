---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_ListEnvironments.html
---

# ListEnvironments
<a name="API_ListEnvironments"></a>

Provides the list of all [Environment](API_Environment.md) objects known to the service.

When creating a [Connection](API_Connection.md), the selected [Environment](API_Environment.md) is used to determine the partner and location the resulting connectivity provides access to.

## Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

 ** location **
Filter results to only include [Environment](API_Environment.md) objects that connect to a given location distiguisher.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
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
Filter results to only include [Environment](API_Environment.md) objects that connect to the [Provider](API_Provider.md).
Type: [Provider](API_Provider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

The following elements are returned by the service.

 ** environments **
The list of matching [Environment](API_Environment.md) objects.
Type: Array of [Environment](API_Environment.md) objects

 ** nextToken **
A pagination token for use in subsequent calls to fetch the next page of results.
Type: String

## Errors
<a name="API_ListEnvironments_Errors"></a>

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
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/ListEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/ListEnvironments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
