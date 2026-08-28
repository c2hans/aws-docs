---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_LayerVersionsListItem.html
---

# LayerVersionsListItem
<a name="API_LayerVersionsListItem"></a>

Details about a version of an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Contents
<a name="API_LayerVersionsListItem_Contents"></a>

 ** CompatibleArchitectures **   <a name="lambda-Type-LayerVersionsListItem-CompatibleArchitectures"></a>
A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `x86_64 | arm64`
Required: No

 ** CompatibleRuntimes **   <a name="lambda-Type-LayerVersionsListItem-CompatibleRuntimes"></a>
The layer's compatible runtimes.
The following list includes deprecated runtimes. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`
Required: No

 ** CreatedDate **   <a name="lambda-Type-LayerVersionsListItem-CreatedDate"></a>
The date that the version was created, in ISO 8601 format. For example, `2018-11-27T15:10:45.123+0000`.
Type: String
Required: No

 ** Description **   <a name="lambda-Type-LayerVersionsListItem-Description"></a>
The description of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** LayerVersionArn **   <a name="lambda-Type-LayerVersionsListItem-LayerVersionArn"></a>
The ARN of the layer version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
Required: No

 ** LicenseInfo **   <a name="lambda-Type-LayerVersionsListItem-LicenseInfo"></a>
The layer's open-source license.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** Version **   <a name="lambda-Type-LayerVersionsListItem-Version"></a>
The version number.
Type: Long
Required: No

## See Also
<a name="API_LayerVersionsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/LayerVersionsListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/LayerVersionsListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/LayerVersionsListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
