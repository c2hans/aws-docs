---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetEnabledStandards.html
---

# GetEnabledStandards
<a name="API_GetEnabledStandards"></a>

Returns a list of the standards that are currently enabled.

## Request Syntax
<a name="API_GetEnabledStandards_RequestSyntax"></a>

```
POST /standards/get HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Providers": [ "{{string}}" ],
   "StandardsSubscriptionArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetEnabledStandards_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEnabledStandards_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetEnabledStandards_RequestSyntax) **   <a name="securityhub-GetEnabledStandards-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetEnabledStandards_RequestSyntax) **   <a name="securityhub-GetEnabledStandards-request-NextToken"></a>
The token that is required for pagination. On your first call to the `GetEnabledStandards` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.
Type: String
Required: No

 ** [Providers](#API_GetEnabledStandards_RequestSyntax) **   <a name="securityhub-GetEnabledStandards-request-Providers"></a>
A list of cloud providers to filter the enabled standards by. For example, specify `Azure` to return only enabled standards that evaluate Azure resources.
Type: Array of strings
Valid Values: `AWS | Azure`
Required: No

 ** [StandardsSubscriptionArns](#API_GetEnabledStandards_RequestSyntax) **   <a name="securityhub-GetEnabledStandards-request-StandardsSubscriptionArns"></a>
The list of the standards subscription ARNs for the standards to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_GetEnabledStandards_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "StandardsSubscriptions": [
      {
         "Provider": "string",
         "StandardsArn": "string",
         "StandardsControlsUpdatable": "string",
         "StandardsInput": {
            "string" : "string"
         },
         "StandardsStatus": "string",
         "StandardsStatusReason": {
            "StatusReasonCode": "string"
         },
         "StandardsSubscriptionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEnabledStandards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetEnabledStandards_ResponseSyntax) **   <a name="securityhub-GetEnabledStandards-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

 ** [StandardsSubscriptions](#API_GetEnabledStandards_ResponseSyntax) **   <a name="securityhub-GetEnabledStandards-response-StandardsSubscriptions"></a>
The list of `StandardsSubscriptions` objects that include information about the enabled standards.
Type: Array of [StandardsSubscription](API_StandardsSubscription.md) objects

## Errors
<a name="API_GetEnabledStandards_Errors"></a>

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
<a name="API_GetEnabledStandards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetEnabledStandards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetEnabledStandards)
