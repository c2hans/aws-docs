---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribePortfolioShareStatus.html
---

# DescribePortfolioShareStatus
<a name="API_DescribePortfolioShareStatus"></a>

Gets the status of the specified portfolio share operation. This API can only be called by the management account in the organization or by a delegated admin.

## Request Syntax
<a name="API_DescribePortfolioShareStatus_RequestSyntax"></a>

```
{
   "PortfolioShareToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePortfolioShareStatus_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PortfolioShareToken](#API_DescribePortfolioShareStatus_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShareStatus-request-PortfolioShareToken"></a>
The token for the portfolio share operation. This token is returned either by CreatePortfolioShare or by DeletePortfolioShare.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribePortfolioShareStatus_ResponseSyntax"></a>

```
{
   "OrganizationNodeValue": "string",
   "PortfolioId": "string",
   "PortfolioShareToken": "string",
   "ShareDetails": {
      "ShareErrors": [
         {
            "Accounts": [ "string" ],
            "Error": "string",
            "Message": "string"
         }
      ],
      "SuccessfulShares": [ "string" ]
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribePortfolioShareStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OrganizationNodeValue](#API_DescribePortfolioShareStatus_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShareStatus-response-OrganizationNodeValue"></a>
Organization node identifier. It can be either account id, organizational unit id or organization id.
Type: String
Pattern: `(^[0-9]{12}$)|(^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32})|(^o-[a-z0-9]{10,32}$)|(^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}$)|(^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)`

 ** [PortfolioId](#API_DescribePortfolioShareStatus_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShareStatus-response-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

 ** [PortfolioShareToken](#API_DescribePortfolioShareStatus_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShareStatus-response-PortfolioShareToken"></a>
The token for the portfolio share operation. For example, `share-6v24abcdefghi`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

 ** [ShareDetails](#API_DescribePortfolioShareStatus_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShareStatus-response-ShareDetails"></a>
Information about the portfolio share operation.
Type: [ShareDetails](API_ShareDetails.md) object

 ** [Status](#API_DescribePortfolioShareStatus_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShareStatus-response-Status"></a>
Status of the portfolio share operation.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`

## Errors
<a name="API_DescribePortfolioShareStatus_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePortfolioShareStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus)
