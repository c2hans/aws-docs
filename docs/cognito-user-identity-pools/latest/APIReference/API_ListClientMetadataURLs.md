---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListClientMetadataURLs.html
---

# ListClientMetadataURLs

Lists the client ID metadata document URLs that Amazon Cognito has received for a Client ID Metadata Document (CIMD) policy, with the cache state of each URL.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_ListClientMetadataURLs_RequestSyntax"></a>

```
{
   "CIMDPolicyId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClientMetadataURLs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CIMDPolicyId](#API_ListClientMetadataURLs_RequestSyntax) **   <a name="CognitoUserPools-ListClientMetadataURLs-request-CIMDPolicyId"></a>
The ID of the CIMD policy whose client metadata document URLs you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** [MaxResults](#API_ListClientMetadataURLs_RequestSyntax) **   <a name="CognitoUserPools-ListClientMetadataURLs-request-MaxResults"></a>
The maximum number of URLs that you want Amazon Cognito to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

 ** [NextToken](#API_ListClientMetadataURLs_RequestSyntax) **   <a name="CognitoUserPools-ListClientMetadataURLs-request-NextToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`
Required: No

 ** [UserPoolId](#API_ListClientMetadataURLs_RequestSyntax) **   <a name="CognitoUserPools-ListClientMetadataURLs-request-UserPoolId"></a>
The ID of the user pool that contains the CIMD policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_ListClientMetadataURLs_ResponseSyntax"></a>

```
{
   "ClientMetadataURLs": [
      {
         "CachedDate": number,
         "ExpirationDate": number,
         "URL": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClientMetadataURLs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientMetadataURLs](#API_ListClientMetadataURLs_ResponseSyntax) **   <a name="CognitoUserPools-ListClientMetadataURLs-response-ClientMetadataURLs"></a>
The client metadata document URLs for the CIMD policy, with the cache state of each URL.
Type: Array of [ClientMetadataURLType](API_ClientMetadataURLType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.

 ** [NextToken](#API_ListClientMetadataURLs_ResponseSyntax) **   <a name="CognitoUserPools-ListClientMetadataURLs-response-NextToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`

## Errors
<a name="API_ListClientMetadataURLs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## See Also
<a name="API_ListClientMetadataURLs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListClientMetadataURLs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListClientMetadataURLs)
