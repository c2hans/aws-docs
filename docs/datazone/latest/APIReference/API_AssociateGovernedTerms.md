---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssociateGovernedTerms.html
---

# AssociateGovernedTerms
<a name="API_AssociateGovernedTerms"></a>

Associates governed terms with an asset.

## Request Syntax
<a name="API_AssociateGovernedTerms_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/associate-governed-terms HTTP/1.1
Content-type: application/json

{
   "governedGlossaryTerms": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AssociateGovernedTerms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_AssociateGovernedTerms_RequestSyntax) **   <a name="datazone-AssociateGovernedTerms-request-uri-domainIdentifier"></a>
The ID of the domain where governed terms are to be associated with an asset.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_AssociateGovernedTerms_RequestSyntax) **   <a name="datazone-AssociateGovernedTerms-request-uri-entityIdentifier"></a>
The ID of the asset with which you want to associate a governed term.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityType](#API_AssociateGovernedTerms_RequestSyntax) **   <a name="datazone-AssociateGovernedTerms-request-uri-entityType"></a>
The type of the asset with which you want to associate a governed term.
Valid Values: `ASSET`
Required: Yes

## Request Body
<a name="API_AssociateGovernedTerms_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [governedGlossaryTerms](#API_AssociateGovernedTerms_RequestSyntax) **   <a name="datazone-AssociateGovernedTerms-request-governedGlossaryTerms"></a>
The glossary terms in a restricted glossary.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Response Syntax
<a name="API_AssociateGovernedTerms_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateGovernedTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateGovernedTerms_Errors"></a>

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
<a name="API_AssociateGovernedTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/AssociateGovernedTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssociateGovernedTerms)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
