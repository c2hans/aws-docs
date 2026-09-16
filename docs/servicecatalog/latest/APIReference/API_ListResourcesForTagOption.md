---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListResourcesForTagOption.html
---

# ListResourcesForTagOption
<a name="API_ListResourcesForTagOption"></a>

Lists the resources associated with the specified TagOption.

## Request Syntax
<a name="API_ListResourcesForTagOption_RequestSyntax"></a>

```
{
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "ResourceType": "{{string}}",
   "TagOptionId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourcesForTagOption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PageSize](#API_ListResourcesForTagOption_RequestSyntax) **   <a name="servicecatalog-ListResourcesForTagOption-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListResourcesForTagOption_RequestSyntax) **   <a name="servicecatalog-ListResourcesForTagOption-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [ResourceType](#API_ListResourcesForTagOption_RequestSyntax) **   <a name="servicecatalog-ListResourcesForTagOption-request-ResourceType"></a>
The resource type.
+  `Portfolio`
+  `Product`
Type: String
Required: No

 ** [TagOptionId](#API_ListResourcesForTagOption_RequestSyntax) **   <a name="servicecatalog-ListResourcesForTagOption-request-TagOptionId"></a>
The TagOption identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_ListResourcesForTagOption_ResponseSyntax"></a>

```
{
   "PageToken": "string",
   "ResourceDetails": [
      {
         "ARN": "string",
         "CreatedTime": number,
         "Description": "string",
         "Id": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourcesForTagOption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PageToken](#API_ListResourcesForTagOption_ResponseSyntax) **   <a name="servicecatalog-ListResourcesForTagOption-response-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ResourceDetails](#API_ListResourcesForTagOption_ResponseSyntax) **   <a name="servicecatalog-ListResourcesForTagOption-response-ResourceDetails"></a>
Information about the resources.
Type: Array of [ResourceDetail](API_ResourceDetail.md) objects

## Errors
<a name="API_ListResourcesForTagOption_Errors"></a>

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
<a name="API_ListResourcesForTagOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListResourcesForTagOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListResourcesForTagOption)
