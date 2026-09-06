---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisioningArtifact.html
---

# DescribeProvisioningArtifact
<a name="API_DescribeProvisioningArtifact"></a>

Gets information about the specified provisioning artifact (also known as a version) for the specified product.

## Request Syntax
<a name="API_DescribeProvisioningArtifact_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "IncludeProvisioningArtifactParameters": {{boolean}},
   "ProductId": "{{string}}",
   "ProductName": "{{string}}",
   "ProvisioningArtifactId": "{{string}}",
   "ProvisioningArtifactName": "{{string}}",
   "Verbose": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeProvisioningArtifact_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IncludeProvisioningArtifactParameters](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-IncludeProvisioningArtifactParameters"></a>
Indicates if the API call response does or does not include additional details about the provisioning parameters.
Type: Boolean
Required: No

 ** [ProductId](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProductName](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-ProductName"></a>
The product name.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** [ProvisioningArtifactId](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProvisioningArtifactName](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-ProvisioningArtifactName"></a>
The provisioning artifact name.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** [Verbose](#API_DescribeProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-request-Verbose"></a>
Indicates whether a verbose level of detail is enabled.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeProvisioningArtifact_ResponseSyntax"></a>

```
{
   "Info": {
      "string" : "string"
   },
   "ProvisioningArtifactDetail": {
      "Active": boolean,
      "CreatedTime": number,
      "Description": "string",
      "Guidance": "string",
      "Id": "string",
      "Name": "string",
      "SourceRevision": "string",
      "Type": "string"
   },
   "ProvisioningArtifactParameters": [
      {
         "DefaultValue": "string",
         "Description": "string",
         "IsNoEcho": boolean,
         "ParameterConstraints": {
            "AllowedPattern": "string",
            "AllowedValues": [ "string" ],
            "ConstraintDescription": "string",
            "MaxLength": "string",
            "MaxValue": "string",
            "MinLength": "string",
            "MinValue": "string"
         },
         "ParameterKey": "string",
         "ParameterType": "string"
      }
   ],
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeProvisioningArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Info](#API_DescribeProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-response-Info"></a>
The URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format.
Type: String to string map
Map Entries: Maximum number of 100 items.

 ** [ProvisioningArtifactDetail](#API_DescribeProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-response-ProvisioningArtifactDetail"></a>
Information about the provisioning artifact.
Type: [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md) object

 ** [ProvisioningArtifactParameters](#API_DescribeProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-response-ProvisioningArtifactParameters"></a>
Information about the parameters used to provision the product.
Type: Array of [ProvisioningArtifactParameter](API_ProvisioningArtifactParameter.md) objects

 ** [Status](#API_DescribeProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-DescribeProvisioningArtifact-response-Status"></a>
The status of the current request.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors
<a name="API_DescribeProvisioningArtifact_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProvisioningArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact)
