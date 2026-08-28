---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListComplianceStatus.html
---

# ListComplianceStatus
<a name="API_ListComplianceStatus"></a>

Returns an array of `PolicyComplianceStatus` objects. Use `PolicyComplianceStatus` to get a summary of which member accounts are protected by the specified policy.

## Request Syntax
<a name="API_ListComplianceStatus_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PolicyId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListComplianceStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListComplianceStatus_RequestSyntax) **   <a name="fms-ListComplianceStatus-request-MaxResults"></a>
Specifies the number of `PolicyComplianceStatus` objects that you want Firewall Manager to return for this request. If you have more `PolicyComplianceStatus` objects than the number that you specify for `MaxResults`, the response includes a `NextToken` value that you can use to get another batch of `PolicyComplianceStatus` objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListComplianceStatus_RequestSyntax) **   <a name="fms-ListComplianceStatus-request-NextToken"></a>
If you specify a value for `MaxResults` and you have more `PolicyComplianceStatus` objects than the number that you specify for `MaxResults`, AWS Firewall Manager returns a `NextToken` value in the response that allows you to list another group of `PolicyComplianceStatus` objects. For the second and subsequent `ListComplianceStatus` requests, specify the value of `NextToken` from the previous response to get information about another batch of `PolicyComplianceStatus` objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [PolicyId](#API_ListComplianceStatus_RequestSyntax) **   <a name="fms-ListComplianceStatus-request-PolicyId"></a>
The ID of the AWS Firewall Manager policy that you want the details for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

## Response Syntax
<a name="API_ListComplianceStatus_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PolicyComplianceStatusList": [
      {
         "EvaluationResults": [
            {
               "ComplianceStatus": "string",
               "EvaluationLimitExceeded": boolean,
               "ViolatorCount": number
            }
         ],
         "IssueInfoMap": {
            "string" : "string"
         },
         "LastUpdated": number,
         "MemberAccount": "string",
         "PolicyId": "string",
         "PolicyName": "string",
         "PolicyOwner": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListComplianceStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListComplianceStatus_ResponseSyntax) **   <a name="fms-ListComplianceStatus-response-NextToken"></a>
If you have more `PolicyComplianceStatus` objects than the number that you specified for `MaxResults` in the request, the response includes a `NextToken` value. To list more `PolicyComplianceStatus` objects, submit another `ListComplianceStatus` request, and specify the `NextToken` value from the response in the `NextToken` value in the next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [PolicyComplianceStatusList](#API_ListComplianceStatus_ResponseSyntax) **   <a name="fms-ListComplianceStatus-response-PolicyComplianceStatusList"></a>
An array of `PolicyComplianceStatus` objects.
Type: Array of [PolicyComplianceStatus](API_PolicyComplianceStatus.md) objects

## Errors
<a name="API_ListComplianceStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListComplianceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListComplianceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListComplianceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
