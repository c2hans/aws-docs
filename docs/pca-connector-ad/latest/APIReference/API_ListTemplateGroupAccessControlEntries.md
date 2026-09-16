---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTemplateGroupAccessControlEntries.html
---

# ListTemplateGroupAccessControlEntries
<a name="API_ListTemplateGroupAccessControlEntries"></a>

Lists group access control entries you created.

## Request Syntax
<a name="API_ListTemplateGroupAccessControlEntries_RequestSyntax"></a>

```
GET /templates/{{TemplateArn}}/accessControlEntries?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTemplateGroupAccessControlEntries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListTemplateGroupAccessControlEntries_RequestSyntax) **   <a name="PcaConnectorAd-ListTemplateGroupAccessControlEntries-request-uri-MaxResults"></a>
Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the `NextToken` element is sent in the response. Use this `NextToken` value in a subsequent request to retrieve additional items.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListTemplateGroupAccessControlEntries_RequestSyntax) **   <a name="PcaConnectorAd-ListTemplateGroupAccessControlEntries-request-uri-NextToken"></a>
Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the `NextToken` parameter from the response you just received.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`

 ** [TemplateArn](#API_ListTemplateGroupAccessControlEntries_RequestSyntax) **   <a name="PcaConnectorAd-ListTemplateGroupAccessControlEntries-request-uri-TemplateArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html).
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/template\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_ListTemplateGroupAccessControlEntries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTemplateGroupAccessControlEntries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessControlEntries": [
      {
         "AccessRights": {
            "AutoEnroll": "string",
            "Enroll": "string"
         },
         "CreatedAt": number,
         "GroupDisplayName": "string",
         "GroupSecurityIdentifier": "string",
         "TemplateArn": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListTemplateGroupAccessControlEntries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessControlEntries](#API_ListTemplateGroupAccessControlEntries_ResponseSyntax) **   <a name="PcaConnectorAd-ListTemplateGroupAccessControlEntries-response-AccessControlEntries"></a>
An access control entry grants or denies permission to an Active Directory group to enroll certificates for a template.
Type: Array of [AccessControlEntrySummary](API_AccessControlEntrySummary.md) objects

 ** [NextToken](#API_ListTemplateGroupAccessControlEntries_ResponseSyntax) **   <a name="PcaConnectorAd-ListTemplateGroupAccessControlEntries-response-NextToken"></a>
Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the `NextToken` parameter from the response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`

## Errors
<a name="API_ListTemplateGroupAccessControlEntries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be one of `Connector`, `Template`, `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or `DirectoryRegistration`.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** QuotaCode **
The code associated with the quota.
 ** ServiceCode **
Identifies the originating service.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid.
 ** Reason **
The reason for the validation error. This won't be return for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListTemplateGroupAccessControlEntries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/ListTemplateGroupAccessControlEntries)
