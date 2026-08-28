---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListEntities.html
---

# ListEntities
<a name="API_ListEntities"></a>

Returns the available entities supported by the connection type.

## Request Syntax
<a name="API_ListEntities_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ConnectionName": "{{string}}",
   "DataStoreApiVersion": "{{string}}",
   "NextToken": "{{string}}",
   "ParentEntityName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEntities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListEntities_RequestSyntax) **   <a name="Glue-ListEntities-request-CatalogId"></a>
The catalog ID of the catalog that contains the connection. This can be null, By default, the AWS Account ID is the catalog ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionName](#API_ListEntities_RequestSyntax) **   <a name="Glue-ListEntities-request-ConnectionName"></a>
A name for the connection that has required credentials to query any connection type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataStoreApiVersion](#API_ListEntities_RequestSyntax) **   <a name="Glue-ListEntities-request-DataStoreApiVersion"></a>
The API version of the SaaS connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9.-]*`
Required: No

 ** [NextToken](#API_ListEntities_RequestSyntax) **   <a name="Glue-ListEntities-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`
Required: No

 ** [ParentEntityName](#API_ListEntities_RequestSyntax) **   <a name="Glue-ListEntities-request-ParentEntityName"></a>
Name of the parent entity for which you want to list the children. This parameter takes a fully-qualified path of the entity in order to list the child entities.
Type: String
Required: No

## Response Syntax
<a name="API_ListEntities_ResponseSyntax"></a>

```
{
   "Entities": [
      {
         "Category": "string",
         "CustomProperties": {
            "string" : "string"
         },
         "Description": "string",
         "EntityName": "string",
         "IsParentEntity": boolean,
         "Label": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEntities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_ListEntities_ResponseSyntax) **   <a name="Glue-ListEntities-response-Entities"></a>
A list of `Entity` objects.
Type: Array of [Entity](API_Entity.md) objects

 ** [NextToken](#API_ListEntities_ResponseSyntax) **   <a name="Glue-ListEntities-response-NextToken"></a>
A continuation token, present if the current segment is not the last.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`

## Errors
<a name="API_ListEntities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** FederationSourceException **
A federation source failed.
 ** FederationSourceErrorCode **
The error code of the problem.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListEntities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListEntities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListEntities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListEntities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListEntities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListEntities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListEntities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListEntities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
