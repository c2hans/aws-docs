---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignments.html
---

# ListApplicationAssignments
<a name="API_ListApplicationAssignments"></a>

Lists AWS account users that are assigned to an application.

## Request Syntax
<a name="API_ListApplicationAssignments_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplicationAssignments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_ListApplicationAssignments_RequestSyntax) **   <a name="singlesignon-ListApplicationAssignments-request-ApplicationArn"></a>
Specifies the ARN of the application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [MaxResults](#API_ListApplicationAssignments_RequestSyntax) **   <a name="singlesignon-ListApplicationAssignments-request-MaxResults"></a>
Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListApplicationAssignments_RequestSyntax) **   <a name="singlesignon-ListApplicationAssignments-request-NextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

## Response Syntax
<a name="API_ListApplicationAssignments_ResponseSyntax"></a>

```
{
   "ApplicationAssignments": [
      {
         "ApplicationArn": "string",
         "PrincipalId": "string",
         "PrincipalType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApplicationAssignments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationAssignments](#API_ListApplicationAssignments_ResponseSyntax) **   <a name="singlesignon-ListApplicationAssignments-response-ApplicationAssignments"></a>
The list of users assigned to an application.
Type: Array of [ApplicationAssignment](API_ApplicationAssignment.md) objects

 ** [NextToken](#API_ListApplicationAssignments_ResponseSyntax) **   <a name="singlesignon-ListApplicationAssignments-response-NextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

## Errors
<a name="API_ListApplicationAssignments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListApplicationAssignments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/ListApplicationAssignments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ListApplicationAssignments)
