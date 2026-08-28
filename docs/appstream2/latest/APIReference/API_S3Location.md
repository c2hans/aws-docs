---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

Describes the S3 location.

## Contents
<a name="API_S3Location_Contents"></a>

 ** S3Bucket **   <a name="WorkSpacesApplications-Type-S3Location-S3Bucket"></a>
The S3 bucket of the S3 object.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[0-9a-z\.\-]*(?<!\.)$`
Required: Yes

 ** S3Key **   <a name="WorkSpacesApplications-Type-S3Location-S3Key"></a>
The S3 key of the S3 object.
This is required when used for the following:
+ IconS3Location (Actions: CreateApplication and UpdateApplication)
+ SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)
+ ScriptDetails (Actions: CreateAppBlock)
+ SourceS3Location when creating an app block with `CUSTOM` PackagingType (Actions: CreateAppBlock)
+ SourceS3Location when creating an app block with `APPSTREAM2` PackagingType, and using an existing application package (VHD file). In this case, `S3Key` refers to the VHD file. If a new application package is required, then `S3Key` is not required. (Actions: CreateAppBlock)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/S3Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
