---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListSubCheckRuleResults.html
---

# ListSubCheckRuleResults
<a name="API_ListSubCheckRuleResults"></a>

Lists the rules of a specified sub-check belonging to a configuration check operation.

## Request Syntax
<a name="API_ListSubCheckRuleResults_RequestSyntax"></a>

```
POST /list-sub-check-rule-results HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubCheckResultId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSubCheckRuleResults_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSubCheckRuleResults_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSubCheckRuleResults_RequestSyntax) **   <a name="ssmsap-ListSubCheckRuleResults-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListSubCheckRuleResults_RequestSyntax) **   <a name="ssmsap-ListSubCheckRuleResults-request-NextToken"></a>
The token for the next page of results.
Type: String
Pattern: `.{16,2048}`
Required: No

 ** [SubCheckResultId](#API_ListSubCheckRuleResults_RequestSyntax) **   <a name="ssmsap-ListSubCheckRuleResults-request-SubCheckResultId"></a>
The ID of the sub check result.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: Yes

## Response Syntax
<a name="API_ListSubCheckRuleResults_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RuleResults": [
      {
         "Description": "string",
         "Id": "string",
         "Message": "string",
         "Metadata": {
            "string" : "string"
         },
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSubCheckRuleResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSubCheckRuleResults_ResponseSyntax) **   <a name="ssmsap-ListSubCheckRuleResults-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Pattern: `.{16,2048}`

 ** [RuleResults](#API_ListSubCheckRuleResults_ResponseSyntax) **   <a name="ssmsap-ListSubCheckRuleResults-response-RuleResults"></a>
The rule results of a sub-check belonging to a configuration check operation.
Type: Array of [RuleResult](API_RuleResult.md) objects

## Errors
<a name="API_ListSubCheckRuleResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListSubCheckRuleResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/ListSubCheckRuleResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ListSubCheckRuleResults)
