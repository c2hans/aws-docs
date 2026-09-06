---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateRule.html
---

# CreateRule
<a name="API_CreateRule"></a>

Creates a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.

## Request Syntax
<a name="API_CreateRule_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/rules HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "detail": { ... },
   "name": "{{string}}",
   "scope": {
      "assetType": {
         "selectionMode": "{{string}}",
         "specificAssetTypes": [ "{{string}}" ]
      },
      "dataProduct": {{boolean}},
      "project": {
         "selectionMode": "{{string}}",
         "specificProjects": [ "{{string}}" ]
      }
   },
   "target": { ... }
}
```

## URI Request Parameters
<a name="API_CreateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-uri-domainIdentifier"></a>
The ID of the domain where the rule is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-action"></a>
The action of the rule.
Type: String
Valid Values: `CREATE_LISTING_CHANGE_SET | CREATE_SUBSCRIPTION_REQUEST`
Required: Yes

 ** [clientToken](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-description"></a>
The description of the rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [detail](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-detail"></a>
The detail of the rule.
Type: [RuleDetail](API_RuleDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w -]+`
Required: Yes

 ** [scope](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-scope"></a>
The scope of the rule.
Type: [RuleScope](API_RuleScope.md) object
Required: Yes

 ** [target](#API_CreateRule_RequestSyntax) **   <a name="datazone-CreateRule-request-target"></a>
The target of the rule.
Type: [RuleTarget](API_RuleTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateRule_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "action": "string",
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "detail": { ... },
   "identifier": "string",
   "name": "string",
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
   "targetType": "string"
}
```

## Response Elements
<a name="API_CreateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [action](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-action"></a>
The action of the rule.
Type: String
Valid Values: `CREATE_LISTING_CHANGE_SET | CREATE_SUBSCRIPTION_REQUEST`

 ** [createdAt](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-createdAt"></a>
The timestamp at which the rule is created.
Type: Timestamp

 ** [createdBy](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-createdBy"></a>
The user who creates the rule.
Type: String

 ** [description](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-description"></a>
The description of the rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [detail](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-detail"></a>
The detail of the rule.
Type: [RuleDetail](API_RuleDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [identifier](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-identifier"></a>
The ID of the rule.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w -]+`

 ** [ruleType](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-ruleType"></a>
The type of the rule.
Type: String
Valid Values: `METADATA_FORM_ENFORCEMENT | GLOSSARY_TERM_ENFORCEMENT`

 ** [scope](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-scope"></a>
The scope of the rule.
Type: [RuleScope](API_RuleScope.md) object

 ** [target](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-target"></a>
The target of the rule.
Type: [RuleTarget](API_RuleTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [targetType](#API_CreateRule_ResponseSyntax) **   <a name="datazone-CreateRule-response-targetType"></a>
The target type of the rule.
Type: String
Valid Values: `DOMAIN_UNIT`

## Errors
<a name="API_CreateRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateRule)
