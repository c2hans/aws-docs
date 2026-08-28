---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListIdentityProviders.html
---

# ListIdentityProviders
<a name="API_ListIdentityProviders"></a>

Lists the Active Directory identity providers for user-based subscriptions.

## Request Syntax
<a name="API_ListIdentityProviders_RequestSyntax"></a>

```
POST /identity-provider/ListIdentityProviders HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Attribute": "{{string}}",
         "Operation": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListIdentityProviders_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListIdentityProviders_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListIdentityProviders_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListIdentityProviders-request-Filters"></a>
You can use the following filters to streamline results:
+ Product
+ DirectoryId
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListIdentityProviders_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListIdentityProviders-request-MaxResults"></a>
The maximum number of results to return from a single request.
Type: Integer
Required: No

 ** [NextToken](#API_ListIdentityProviders_RequestSyntax) **   <a name="licensemanagerusersubscriptions-ListIdentityProviders-request-NextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Required: No

## Response Syntax
<a name="API_ListIdentityProviders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IdentityProviderSummaries": [
      {
         "FailureMessage": "string",
         "IdentityProvider": { ... },
         "IdentityProviderArn": "string",
         "OwnerAccountId": "string",
         "Product": "string",
         "Settings": {
            "SecurityGroupId": "string",
            "Subnets": [ "string" ]
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIdentityProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProviderSummaries](#API_ListIdentityProviders_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-ListIdentityProviders-response-IdentityProviderSummaries"></a>
An array of `IdentityProviderSummary` resources that contain details about the Active Directory identity providers that meet the request criteria.
Type: Array of [IdentityProviderSummary](API_IdentityProviderSummary.md) objects

 ** [NextToken](#API_ListIdentityProviders_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-ListIdentityProviders-response-NextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String

## Errors
<a name="API_ListIdentityProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
HTTP Status Code: 500

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request failed because a service quota is exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
HTTP Status Code: 400

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListIdentityProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/ListIdentityProviders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
