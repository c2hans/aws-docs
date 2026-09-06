---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateLenses.html
---

# AssociateLenses
<a name="API_AssociateLenses"></a>

Associate a lens to a workload.

Up to 10 lenses can be associated with a workload in a single API operation. A maximum of 20 lenses can be associated with a workload.

**Note**
 **Disclaimer**
By accessing and/or applying custom lenses created by another AWS user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the AWS Customer Agreement.

## Request Syntax
<a name="API_AssociateLenses_RequestSyntax"></a>

```
PATCH /workloads/{{WorkloadId}}/associateLenses HTTP/1.1
Content-type: application/json

{
   "LensAliases": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AssociateLenses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [WorkloadId](#API_AssociateLenses_RequestSyntax) **   <a name="wellarchitected-AssociateLenses-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_AssociateLenses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LensAliases](#API_AssociateLenses_RequestSyntax) **   <a name="wellarchitected-AssociateLenses-request-LensAliases"></a>
List of lens aliases to associate or disassociate with a workload. Up to 10 lenses can be specified.
Identify a lens using its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_AssociateLenses_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateLenses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateLenses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_AssociateLenses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/AssociateLenses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AssociateLenses)
