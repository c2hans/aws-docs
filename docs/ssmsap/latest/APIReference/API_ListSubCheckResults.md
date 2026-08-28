---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListSubCheckResults.html
---

# ListSubCheckResults
<a name="API_ListSubCheckResults"></a>

Lists the sub-check results of a specified configuration check operation.

## Request Syntax
<a name="API_ListSubCheckResults_RequestSyntax"></a>

```
POST /list-sub-check-results HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OperationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSubCheckResults_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSubCheckResults_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSubCheckResults_RequestSyntax) **   <a name="ssmsap-ListSubCheckResults-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListSubCheckResults_RequestSyntax) **   <a name="ssmsap-ListSubCheckResults-request-NextToken"></a>
The token for the next page of results.
Type: String
Pattern: `.{16,2048}`
Required: No

 ** [OperationId](#API_ListSubCheckResults_RequestSyntax) **   <a name="ssmsap-ListSubCheckResults-request-OperationId"></a>
The ID of the configuration check operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: Yes

## Response Syntax
<a name="API_ListSubCheckResults_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SubCheckResults": [
      {
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "References": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListSubCheckResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSubCheckResults_ResponseSyntax) **   <a name="ssmsap-ListSubCheckResults-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Pattern: `.{16,2048}`

 ** [SubCheckResults](#API_ListSubCheckResults_ResponseSyntax) **   <a name="ssmsap-ListSubCheckResults-response-SubCheckResults"></a>
The sub-check results of a configuration check operation.
Type: Array of [SubCheckResult](API_SubCheckResult.md) objects

## Errors
<a name="API_ListSubCheckResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListSubCheckResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/ListSubCheckResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ListSubCheckResults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
