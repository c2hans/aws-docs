---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandardsControls.html
---

# DescribeStandardsControls
<a name="API_DescribeStandardsControls"></a>

Returns a list of security standards controls.

For each control, the results include information about whether it is currently enabled, the severity, and a link to remediation information.

This operation returns an empty list for standard subscriptions where `StandardsControlsUpdatable` has value `NOT_READY_FOR_UPDATES`.

## Request Syntax
<a name="API_DescribeStandardsControls_RequestSyntax"></a>

```
GET /standards/controls/{{StandardsSubscriptionArn+}}?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeStandardsControls_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_DescribeStandardsControls_RequestSyntax) **   <a name="securityhub-DescribeStandardsControls-request-uri-MaxResults"></a>
The maximum number of security standard controls to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_DescribeStandardsControls_RequestSyntax) **   <a name="securityhub-DescribeStandardsControls-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `DescribeStandardsControls` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

 ** [StandardsSubscriptionArn](#API_DescribeStandardsControls_RequestSyntax) **   <a name="securityhub-DescribeStandardsControls-request-uri-StandardsSubscriptionArn"></a>
The ARN of a resource that represents your subscription to a supported standard. To get the subscription ARNs of the standards you have enabled, use the `GetEnabledStandards` operation.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DescribeStandardsControls_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeStandardsControls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Controls": [
      {
         "ControlId": "string",
         "ControlStatus": "string",
         "ControlStatusUpdatedAt": "string",
         "Description": "string",
         "DisabledReason": "string",
         "RelatedRequirements": [ "string" ],
         "RemediationUrl": "string",
         "SeverityRating": "string",
         "StandardsControlArn": "string",
         "Title": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeStandardsControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Controls](#API_DescribeStandardsControls_ResponseSyntax) **   <a name="securityhub-DescribeStandardsControls-response-Controls"></a>
A list of security standards controls.
Type: Array of [StandardsControl](API_StandardsControl.md) objects

 ** [NextToken](#API_DescribeStandardsControls_ResponseSyntax) **   <a name="securityhub-DescribeStandardsControls-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

## Errors
<a name="API_DescribeStandardsControls_Errors"></a>

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_DescribeStandardsControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DescribeStandardsControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DescribeStandardsControls)
