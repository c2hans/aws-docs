---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListAccessControlApplications.html
---

# ListAccessControlApplications

Lists the access control applications in a Quick Sight account in the current AWS Region. You can filter the results by namespace. Quick Sight paginates the results. To retrieve additional results, use the `NextToken` parameter.

## Request Syntax
<a name="API_ListAccessControlApplications_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/access-control-applications?max-results={{MaxResults}}&namespace={{Namespace}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccessControlApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListAccessControlApplications_RequestSyntax) **   <a name="QS-ListAccessControlApplications-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListAccessControlApplications_RequestSyntax) **   <a name="QS-ListAccessControlApplications-request-uri-MaxResults"></a>
The maximum number of results to return. The default is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Namespace](#API_ListAccessControlApplications_RequestSyntax) **   <a name="QS-ListAccessControlApplications-request-uri-Namespace"></a>
The namespace to filter by. If you don't specify a namespace, access control applications in all namespaces are returned.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`

 ** [NextToken](#API_ListAccessControlApplications_RequestSyntax) **   <a name="QS-ListAccessControlApplications-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListAccessControlApplications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccessControlApplications_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccessControlApplications": [
      {
         "ApplicationId": "string",
         "Arn": "string",
         "AuthenticationType": "string",
         "CreatedTime": number,
         "Description": "string",
         "IdpAuthorizingConfiguration": {
            "IdcTrustedTokenIssuerConfiguration": {
               "IdcTrustedTokenIssuerArn": "string"
            },
            "IdpAuthorizingConfigurationSummaryDetail": { ... },
            "IdpAuthorizingType": "string"
         },
         "LastUpdatedTime": number,
         "Name": "string",
         "Namespace": "string",
         "QuickAuthenticationConfiguration": {
            "QuickAuthenticationConfigurationDetail": { ... },
            "QuickAuthenticationType": "string"
         },
         "Status": "string",
         "TenantUrl": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListAccessControlApplications_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListAccessControlApplications_ResponseSyntax) **   <a name="QS-ListAccessControlApplications-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccessControlApplications](#API_ListAccessControlApplications_ResponseSyntax) **   <a name="QS-ListAccessControlApplications-response-AccessControlApplications"></a>
A list of access control application summaries.
Type: Array of [AccessControlApplicationSummary](API_AccessControlApplicationSummary.md) objects

 ** [RequestId](#API_ListAccessControlApplications_ResponseSyntax) **   <a name="QS-ListAccessControlApplications-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [NextToken](#API_ListAccessControlApplications_ResponseSyntax) **   <a name="QS-ListAccessControlApplications-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String

## Errors
<a name="API_ListAccessControlApplications_Errors"></a>

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
<a name="API_ListAccessControlApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListAccessControlApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListAccessControlApplications)
