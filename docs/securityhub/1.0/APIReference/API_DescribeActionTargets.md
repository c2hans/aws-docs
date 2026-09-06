---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeActionTargets.html
---

# DescribeActionTargets
<a name="API_DescribeActionTargets"></a>

Returns a list of the custom action targets in Security Hub CSPM in your account.

## Request Syntax
<a name="API_DescribeActionTargets_RequestSyntax"></a>

```
POST /actionTargets/get HTTP/1.1
Content-type: application/json

{
   "ActionTargetArns": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeActionTargets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeActionTargets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionTargetArns](#API_DescribeActionTargets_RequestSyntax) **   <a name="securityhub-DescribeActionTargets-request-ActionTargetArns"></a>
A list of custom action target ARNs for the custom action targets to retrieve.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** [MaxResults](#API_DescribeActionTargets_RequestSyntax) **   <a name="securityhub-DescribeActionTargets-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeActionTargets_RequestSyntax) **   <a name="securityhub-DescribeActionTargets-request-NextToken"></a>
The token that is required for pagination. On your first call to the `DescribeActionTargets` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeActionTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActionTargets": [
      {
         "ActionTargetArn": "string",
         "Description": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeActionTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionTargets](#API_DescribeActionTargets_ResponseSyntax) **   <a name="securityhub-DescribeActionTargets-response-ActionTargets"></a>
A list of `ActionTarget` objects. Each object includes the `ActionTargetArn`, `Description`, and `Name` of a custom action target available in Security Hub CSPM.
Type: Array of [ActionTarget](API_ActionTarget.md) objects

 ** [NextToken](#API_DescribeActionTargets_ResponseSyntax) **   <a name="securityhub-DescribeActionTargets-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

## Errors
<a name="API_DescribeActionTargets_Errors"></a>

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
<a name="API_DescribeActionTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DescribeActionTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DescribeActionTargets)
