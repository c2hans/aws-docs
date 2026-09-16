---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html
---

# ListStandardsControlAssociations
<a name="API_ListStandardsControlAssociations"></a>

 Specifies whether a control is currently enabled or disabled in each enabled standard in the calling account.

This operation omits standards control associations for standard subscriptions where `StandardsControlsUpdatable` has value `NOT_READY_FOR_UPDATES`.

## Request Syntax
<a name="API_ListStandardsControlAssociations_RequestSyntax"></a>

```
GET /associations?MaxResults={{MaxResults}}&NextToken={{NextToken}}&SecurityControlId={{SecurityControlId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStandardsControlAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListStandardsControlAssociations_RequestSyntax) **   <a name="securityhub-ListStandardsControlAssociations-request-uri-MaxResults"></a>
 An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 standard and control associations. The results also include a `NextToken` parameter that you can use in a subsequent API call to get the next 25 associations. This repeats until all associations for the specified control are returned. The number of results is limited by the number of supported Security Hub CSPM standards that you've enabled in the calling account.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListStandardsControlAssociations_RequestSyntax) **   <a name="securityhub-ListStandardsControlAssociations-request-uri-NextToken"></a>
 Optional pagination parameter.

 ** [SecurityControlId](#API_ListStandardsControlAssociations_RequestSyntax) **   <a name="securityhub-ListStandardsControlAssociations-request-uri-SecurityControlId"></a>
 The identifier of the control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) that you want to determine the enablement status of in each enabled standard.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_ListStandardsControlAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStandardsControlAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "StandardsControlAssociationSummaries": [
      {
         "AssociationStatus": "string",
         "RelatedRequirements": [ "string" ],
         "SecurityControlArn": "string",
         "SecurityControlId": "string",
         "StandardsArn": "string",
         "StandardsControlDescription": "string",
         "StandardsControlTitle": "string",
         "UpdatedAt": "string",
         "UpdatedReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStandardsControlAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListStandardsControlAssociations_ResponseSyntax) **   <a name="securityhub-ListStandardsControlAssociations-response-NextToken"></a>
 A pagination parameter that's included in the response only if it was included in the request.
Type: String

 ** [StandardsControlAssociationSummaries](#API_ListStandardsControlAssociations_ResponseSyntax) **   <a name="securityhub-ListStandardsControlAssociations-response-StandardsControlAssociationSummaries"></a>
 An array that provides the enablement status and other details for each security control that applies to each enabled standard.
Type: Array of [StandardsControlAssociationSummary](API_StandardsControlAssociationSummary.md) objects

## Errors
<a name="API_ListStandardsControlAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListStandardsControlAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListStandardsControlAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListStandardsControlAssociations)
