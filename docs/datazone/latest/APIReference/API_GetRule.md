---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetRule.html
---

# GetRule
<a name="API_GetRule"></a>

Gets the details of a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.

## Request Syntax
<a name="API_GetRule_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/rules/{{identifier}}?revision={{revision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetRule_RequestSyntax) **   <a name="datazone-GetRule-request-uri-domainIdentifier"></a>
The ID of the domain where the `GetRule` action is to be invoked.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetRule_RequestSyntax) **   <a name="datazone-GetRule-request-uri-identifier"></a>
The ID of the rule.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [revision](#API_GetRule_RequestSyntax) **   <a name="datazone-GetRule-request-uri-revision"></a>
The revision of the rule.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_GetRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": "string",
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "detail": { ... },
   "identifier": "string",
   "lastUpdatedBy": "string",
   "name": "string",
   "revision": "string",
   "ruleType": "string",
   "scope": {
      "assetType": {
         "selectionMode": "string",
         "specificAssetTypes": [ "string" ]
      },
      "dataProduct": boolean,
      "project": {
         "selectionMode": "string",
         "specificProjects": [ "string" ]
      }
   },
   "target": { ... },
   "targetType": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-action"></a>
The action of the rule.
Type: String
Valid Values: `CREATE_LISTING_CHANGE_SET | CREATE_SUBSCRIPTION_REQUEST`

 ** [createdAt](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-createdAt"></a>
The timestamp at which the rule was created.
Type: Timestamp

 ** [createdBy](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-createdBy"></a>
The user who created the rule.
Type: String

 ** [description](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-description"></a>
The description of the rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [detail](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-detail"></a>
The detail of the rule.
Type: [RuleDetail](API_RuleDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [identifier](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-identifier"></a>
The ID of the rule.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedBy](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-lastUpdatedBy"></a>
The timestamp at which the rule was last updated.
Type: String

 ** [name](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w -]+`

 ** [revision](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-revision"></a>
The revision of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ruleType](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-ruleType"></a>
The type of the rule.
Type: String
Valid Values: `METADATA_FORM_ENFORCEMENT | GLOSSARY_TERM_ENFORCEMENT`

 ** [scope](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-scope"></a>
The scope of the rule.
Type: [RuleScope](API_RuleScope.md) object

 ** [target](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-target"></a>
The target of the rule.
Type: [RuleTarget](API_RuleTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [targetType](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-targetType"></a>
The target type of the rule.
Type: String
Valid Values: `DOMAIN_UNIT`

 ** [updatedAt](#API_GetRule_ResponseSyntax) **   <a name="datazone-GetRule-response-updatedAt"></a>
The timestamp at which the rule was last updated.
Type: Timestamp

## Errors
<a name="API_GetRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetRule)
