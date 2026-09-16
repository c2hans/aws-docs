---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_ListEntitlements.html
---

# ListEntitlements
<a name="API_ListEntitlements"></a>

Lists the entitlements for a specified account access manager application. You can filter results by principal, IAM role, or account. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListEntitlements_RequestSyntax"></a>

```
POST /entitlements-list HTTP/1.1
Content-type: application/json

{
   "applicationArn": "{{string}}",
   "filter": {
      "principalRole": {
         "account": "{{string}}",
         "principal": { ... },
         "roleArn": "{{string}}"
      }
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEntitlements_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEntitlements_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationArn](#API_ListEntitlements_RequestSyntax) **   <a name="accountaccess-ListEntitlements-request-applicationArn"></a>
Specifies the ARN of the application to list entitlements for.
Type: String
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`
Required: Yes

 ** [filter](#API_ListEntitlements_RequestSyntax) **   <a name="accountaccess-ListEntitlements-request-filter"></a>
Specifies filter criteria to narrow the entitlements returned. You can filter by principal, IAM role, or account.
Type: [EntitlementFilter](API_EntitlementFilter.md) object
Required: Yes

 ** [maxResults](#API_ListEntitlements_RequestSyntax) **   <a name="accountaccess-ListEntitlements-request-maxResults"></a>
Specifies the maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEntitlements_RequestSyntax) **   <a name="accountaccess-ListEntitlements-request-nextToken"></a>
Specifies the pagination token from a previous call to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListEntitlements_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entitlements": [
      {
         "createdAt": "string",
         "entitlement": { ... },
         "entitlementId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEntitlements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entitlements](#API_ListEntitlements_ResponseSyntax) **   <a name="accountaccess-ListEntitlements-response-entitlements"></a>
The list of entitlements for the specified application.
Type: Array of [EntitlementsListMember](API_EntitlementsListMember.md) objects

 ** [nextToken](#API_ListEntitlements_ResponseSyntax) **   <a name="accountaccess-ListEntitlements-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next set of results. This value is null when there are no more results to return.
Type: String

## Errors
<a name="API_ListEntitlements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. Try your request again later.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListEntitlements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-access-2018-05-10/ListEntitlements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/ListEntitlements)
