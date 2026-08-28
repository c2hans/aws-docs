---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTargets.html
---

# ListTargets
<a name="API_ListTargets"></a>

Returns a list of the notification rule targets for an AWS account.

## Request Syntax
<a name="API_ListTargets_RequestSyntax"></a>

```
POST /listTargets HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTargets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTargets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListTargets_RequestSyntax) **   <a name="codestarnotifications-ListTargets-request-Filters"></a>
The filters to use to return information by service or resource type. Valid filters include target type, target address, and target status.
A filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.
Type: Array of [ListTargetsFilter](API_ListTargetsFilter.md) objects
Required: No

 ** [MaxResults](#API_ListTargets_RequestSyntax) **   <a name="codestarnotifications-ListTargets-request-MaxResults"></a>
A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTargets_RequestSyntax) **   <a name="codestarnotifications-ListTargets-request-NextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Pattern: `^[\w/+=]+$`
Required: No

## Response Syntax
<a name="API_ListTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Targets": [
      {
         "TargetAddress": "string",
         "TargetStatus": "string",
         "TargetType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTargets_ResponseSyntax) **   <a name="codestarnotifications-ListTargets-response-NextToken"></a>
An enumeration token that can be used in a request to return the next batch of results.
Type: String
Pattern: `^[\w/+=]+$`

 ** [Targets](#API_ListTargets_ResponseSyntax) **   <a name="codestarnotifications-ListTargets-response-Targets"></a>
The list of notification rule targets.
Type: Array of [TargetSummary](API_TargetSummary.md) objects

## Errors
<a name="API_ListTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The value for the enumeration token used in the request to return the next batch of the results is not valid.
HTTP Status Code: 400

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/ListTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/ListTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
