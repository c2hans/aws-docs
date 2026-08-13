---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListApprovalPolicies.html
---

# ListApprovalPolicies
<a name="API_ListApprovalPolicies"></a>

Lists all approval policies in the specified Quick Sight account. The results are paginated. If the response includes a `NextToken` value, pass it in a subsequent call to retrieve the next set of results.

## Request Syntax
<a name="API_ListApprovalPolicies_RequestSyntax"></a>

```
GET /governance/approvalworkflows/policies?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApprovalPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListApprovalPolicies_RequestSyntax) **   <a name="QS-ListApprovalPolicies-request-uri-MaxResults"></a>
The maximum number of results to return in a single call. If you don't specify a value, the service returns a default number of results. Use the `NextToken` value in the response to retrieve additional results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListApprovalPolicies_RequestSyntax) **   <a name="QS-ListApprovalPolicies-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Request Body
<a name="API_ListApprovalPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApprovalPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Policies": [
      {
         "Actions": [ "string" ],
         "ApplicableTo": {
            "GroupArns": [ "string" ],
            "Type": "string"
         },
         "ApprovalGroups": [ "string" ],
         "AssetTypes": [ "string" ],
         "CreatedAt": number,
         "Description": "string",
         "Name": "string",
         "PolicyArn": "string",
         "PolicyId": "string",
         "UpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListApprovalPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policies](#API_ListApprovalPolicies_ResponseSyntax) **   <a name="QS-ListApprovalPolicies-response-Policies"></a>
The list of approval policies.
Type: Array of [ApprovalPolicy](API_ApprovalPolicy.md) objects

 ** [NextToken](#API_ListApprovalPolicies_ResponseSyntax) **   <a name="QS-ListApprovalPolicies-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_ListApprovalPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListApprovalPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListApprovalPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListApprovalPolicies)
