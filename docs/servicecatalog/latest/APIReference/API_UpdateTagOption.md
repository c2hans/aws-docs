---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateTagOption.html
---

# UpdateTagOption
<a name="API_UpdateTagOption"></a>

Updates the specified TagOption.

## Request Syntax
<a name="API_UpdateTagOption_RequestSyntax"></a>

```
{
   "Active": {{boolean}},
   "Id": "{{string}}",
   "Value": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTagOption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Active](#API_UpdateTagOption_RequestSyntax) **   <a name="servicecatalog-UpdateTagOption-request-Active"></a>
The updated active state.
Type: Boolean
Required: No

 ** [Id](#API_UpdateTagOption_RequestSyntax) **   <a name="servicecatalog-UpdateTagOption-request-Id"></a>
The TagOption identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Value](#API_UpdateTagOption_RequestSyntax) **   <a name="servicecatalog-UpdateTagOption-request-Value"></a>
The updated value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_UpdateTagOption_ResponseSyntax"></a>

```
{
   "TagOptionDetail": {
      "Active": boolean,
      "Id": "string",
      "Key": "string",
      "Owner": "string",
      "Value": "string"
   }
}
```

## Response Elements
<a name="API_UpdateTagOption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TagOptionDetail](#API_UpdateTagOption_ResponseSyntax) **   <a name="servicecatalog-UpdateTagOption-response-TagOptionDetail"></a>
Information about the TagOption.
Type: [TagOptionDetail](API_TagOptionDetail.md) object

## Errors
<a name="API_UpdateTagOption_Errors"></a>

 ** DuplicateResourceException **
The specified resource is a duplicate.
HTTP Status Code: 400

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** TagOptionNotMigratedException **
An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the AWS Management Console to perform the migration process before retrying the operation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTagOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdateTagOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateTagOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
