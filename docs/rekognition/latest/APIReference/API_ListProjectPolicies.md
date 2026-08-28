---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListProjectPolicies.html
---

# ListProjectPolicies
<a name="API_ListProjectPolicies"></a>

**Note**
This operation applies only to Amazon Rekognition Custom Labels.

Gets a list of the project policies attached to a project.

To attach a project policy to a project, call [PutProjectPolicy](API_PutProjectPolicy.md). To remove a project policy from a project, call [DeleteProjectPolicy](API_DeleteProjectPolicy.md).

This operation requires permissions to perform the `rekognition:ListProjectPolicies` action.

## Request Syntax
<a name="API_ListProjectPolicies_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProjectArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProjectPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListProjectPolicies_RequestSyntax) **   <a name="rekognition-ListProjectPolicies-request-MaxResults"></a>
The maximum number of results to return per paginated call. The largest value you can specify is 5. If you specify a value greater than 5, a ValidationException error occurs. The default value is 5.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [NextToken](#API_ListProjectPolicies_RequestSyntax) **   <a name="rekognition-ListProjectPolicies-request-NextToken"></a>
If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [ProjectArn](#API_ListProjectPolicies_RequestSyntax) **   <a name="rekognition-ListProjectPolicies-request-ProjectArn"></a>
The ARN of the project for which you want to list the project policies.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

## Response Syntax
<a name="API_ListProjectPolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProjectPolicies": [
      {
         "CreationTimestamp": number,
         "LastUpdatedTimestamp": number,
         "PolicyDocument": "string",
         "PolicyName": "string",
         "PolicyRevisionId": "string",
         "ProjectArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProjectPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProjectPolicies_ResponseSyntax) **   <a name="rekognition-ListProjectPolicies-response-NextToken"></a>
If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of project policies.
Type: String
Length Constraints: Maximum length of 1024.

 ** [ProjectPolicies](#API_ListProjectPolicies_ResponseSyntax) **   <a name="rekognition-ListProjectPolicies-response-ProjectPolicies"></a>
A list of project policies attached to the project.
Type: Array of [ProjectPolicy](API_ProjectPolicy.md) objects

## Errors
<a name="API_ListProjectPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidPaginationTokenException **
Pagination token in the request is not valid.
HTTP Status Code: 400

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_ListProjectPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListProjectPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ListProjectPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
