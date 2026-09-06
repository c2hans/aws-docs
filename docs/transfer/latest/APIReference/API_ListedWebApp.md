---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListedWebApp.html
---

# ListedWebApp
<a name="API_ListedWebApp"></a>

 a structure that contains details for the web app.

## Contents
<a name="API_ListedWebApp_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-ListedWebApp-Arn"></a>
The Amazon Resource Name (ARN) for the web app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** WebAppId **   <a name="TransferFamily-Type-ListedWebApp-WebAppId"></a>
The unique identifier for the web app.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

 ** AccessEndpoint **   <a name="TransferFamily-Type-ListedWebApp-AccessEndpoint"></a>
The `AccessEndpoint` is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** EndpointType **   <a name="TransferFamily-Type-ListedWebApp-EndpointType"></a>
The type of endpoint hosting the web app. Valid values are `PUBLIC` for publicly accessible endpoints and `VPC` for VPC-hosted endpoints.
Type: String
Valid Values: `PUBLIC | VPC`
Required: No

 ** WebAppEndpoint **   <a name="TransferFamily-Type-ListedWebApp-WebAppEndpoint"></a>
The `WebAppEndpoint` is the unique URL for your Transfer Family web app. This is the value that you use when you configure **Origins** on CloudFront.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ListedWebApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListedWebApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListedWebApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListedWebApp)
