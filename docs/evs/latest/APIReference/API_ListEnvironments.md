---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironments.html
---

# ListEnvironments
<a name="API_ListEnvironments"></a>

Lists the Amazon EVS environments in your AWS account in the specified AWS Region.

## Request Syntax
<a name="API_ListEnvironments_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "state": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [maxResults](#API_ListEnvironments_RequestSyntax) **   <a name="evs-ListEnvironments-request-maxResults"></a>
The maximum number of results to return. If you specify `MaxResults` in the request, the response includes information up to the limit specified.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEnvironments_RequestSyntax) **   <a name="evs-ListEnvironments-request-nextToken"></a>
A unique pagination token for each page. If `nextToken` is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Required: No

 ** [state](#API_ListEnvironments_RequestSyntax) **   <a name="evs-ListEnvironments-request-state"></a>
The state of an environment. Used to filter response results to return only environments with the specified `environmentState`.
Type: Array of strings
Valid Values: `CREATING | CREATED | DELETING | DELETED | CREATE_FAILED`
Required: No

## Response Syntax
<a name="API_ListEnvironments_ResponseSyntax"></a>

```
{
   "environmentSummaries": [
      {
         "createdAt": number,
         "environmentArn": "string",
         "environmentId": "string",
         "environmentName": "string",
         "environmentState": "string",
         "environmentStatus": "string",
         "modifiedAt": number,
         "vcfVersion": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentSummaries](#API_ListEnvironments_ResponseSyntax) **   <a name="evs-ListEnvironments-response-environmentSummaries"></a>
A list of environments with summarized environment details.
Type: Array of [EnvironmentSummary](API_EnvironmentSummary.md) objects

 ** [nextToken](#API_ListEnvironments_ResponseSyntax) **   <a name="evs-ListEnvironments-response-nextToken"></a>
A unique pagination token for next page results. Make the call again using this token to retrieve the next page.
Type: String

## Errors
<a name="API_ListEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/ListEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ListEnvironments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
