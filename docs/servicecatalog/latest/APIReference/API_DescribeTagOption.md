---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeTagOption.html
---

# DescribeTagOption
<a name="API_DescribeTagOption"></a>

Gets information about the specified TagOption.

## Request Syntax
<a name="API_DescribeTagOption_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTagOption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Id](#API_DescribeTagOption_RequestSyntax) **   <a name="servicecatalog-DescribeTagOption-request-Id"></a>
The TagOption identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_DescribeTagOption_ResponseSyntax"></a>

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
<a name="API_DescribeTagOption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TagOptionDetail](#API_DescribeTagOption_ResponseSyntax) **   <a name="servicecatalog-DescribeTagOption-response-TagOptionDetail"></a>
Information about the TagOption.
Type: [TagOptionDetail](API_TagOptionDetail.md) object

## Errors
<a name="API_DescribeTagOption_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** TagOptionNotMigratedException **
An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the AWS Management Console to perform the migration process before retrying the operation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTagOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeTagOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeTagOption)
