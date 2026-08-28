---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedWebApp.html
---

# DescribedWebApp
<a name="API_DescribedWebApp"></a>

A structure that describes the parameters for the web app, as identified by the `WebAppId`.

## Contents
<a name="API_DescribedWebApp_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedWebApp-Arn"></a>
The Amazon Resource Name (ARN) of the web app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** WebAppId **   <a name="TransferFamily-Type-DescribedWebApp-WebAppId"></a>
The unique identifier for the web app.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

 ** AccessEndpoint **   <a name="TransferFamily-Type-DescribedWebApp-AccessEndpoint"></a>
The `AccessEndpoint` is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** DescribedEndpointDetails **   <a name="TransferFamily-Type-DescribedWebApp-DescribedEndpointDetails"></a>
The endpoint configuration details for the web app, including VPC settings if the endpoint is hosted within a VPC.
Type: [DescribedWebAppEndpointDetails](API_DescribedWebAppEndpointDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** DescribedIdentityProviderDetails **   <a name="TransferFamily-Type-DescribedWebApp-DescribedIdentityProviderDetails"></a>
A structure that contains the details for the identity provider used by the web app.
Type: [DescribedWebAppIdentityProviderDetails](API_DescribedWebAppIdentityProviderDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** EndpointType **   <a name="TransferFamily-Type-DescribedWebApp-EndpointType"></a>
The type of endpoint hosting the web app. Valid values are `PUBLIC` for publicly accessible endpoints and `VPC` for VPC-hosted endpoints that provide network isolation.
Type: String
Valid Values: `PUBLIC | VPC`
Required: No

 ** Tags **   <a name="TransferFamily-Type-DescribedWebApp-Tags"></a>
Key-value pairs that can be used to group and search for web apps. Tags are metadata attached to web apps for any purpose.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** WebAppEndpoint **   <a name="TransferFamily-Type-DescribedWebApp-WebAppEndpoint"></a>
The `WebAppEndpoint` is the unique URL for your Transfer Family web app. This is the value that you use when you configure **Origins** on CloudFront.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** WebAppEndpointPolicy **   <a name="TransferFamily-Type-DescribedWebApp-WebAppEndpointPolicy"></a>
 Setting for the type of endpoint policy for the web app. The default value is `STANDARD`.
If your web app was created in an AWS GovCloud (US) Region, the value of this parameter can be `FIPS`, which indicates the web app endpoint is FIPS-compliant.
Type: String
Valid Values: `FIPS | STANDARD`
Required: No

 ** WebAppUnits **   <a name="TransferFamily-Type-DescribedWebApp-WebAppUnits"></a>
A union that contains the value for number of concurrent connections or the user sessions on your web app.
Type: [WebAppUnits](API_WebAppUnits.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_DescribedWebApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedWebApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedWebApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedWebApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
