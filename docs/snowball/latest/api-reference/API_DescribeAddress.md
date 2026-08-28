---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddress.html
---

# DescribeAddress
<a name="API_DescribeAddress"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Takes an `AddressId` and returns specific details about that address in the form of an `Address` object.

## Request Syntax
<a name="API_DescribeAddress_RequestSyntax"></a>

```
{
   "AddressId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAddress_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressId](#API_DescribeAddress_RequestSyntax) **   <a name="Snowball-DescribeAddress-request-AddressId"></a>
The automatically generated ID for a specific address.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeAddress_ResponseSyntax"></a>

```
{
   "Address": {
      "AddressId": "string",
      "City": "string",
      "Company": "string",
      "Country": "string",
      "IsRestricted": boolean,
      "Landmark": "string",
      "Name": "string",
      "PhoneNumber": "string",
      "PostalCode": "string",
      "PrefectureOrDistrict": "string",
      "StateOrProvince": "string",
      "Street1": "string",
      "Street2": "string",
      "Street3": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Address](#API_DescribeAddress_ResponseSyntax) **   <a name="Snowball-DescribeAddress-response-Address"></a>
The address that you want the Snow device(s) associated with a specific job to be shipped to.
Type: [Address](API_Address.md) object

## Errors
<a name="API_DescribeAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/DescribeAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/DescribeAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
