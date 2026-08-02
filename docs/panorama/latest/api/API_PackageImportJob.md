---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_PackageImportJob.html
---

# PackageImportJob
<a name="API_PackageImportJob"></a>

A job to import a package version.

## Contents
<a name="API_PackageImportJob_Contents"></a>

 ** CreatedTime **   <a name="panorama-Type-PackageImportJob-CreatedTime"></a>
When the job was created.
Type: Timestamp
Required: No

 ** JobId **   <a name="panorama-Type-PackageImportJob-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** JobType **   <a name="panorama-Type-PackageImportJob-JobType"></a>
The job's type.
Type: String
Valid Values: `NODE_PACKAGE_VERSION | MARKETPLACE_NODE_PACKAGE_VERSION`
Required: No

 ** LastUpdatedTime **   <a name="panorama-Type-PackageImportJob-LastUpdatedTime"></a>
When the job was updated.
Type: Timestamp
Required: No

 ** Status **   <a name="panorama-Type-PackageImportJob-Status"></a>
The job's status.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED`
Required: No

 ** StatusMessage **   <a name="panorama-Type-PackageImportJob-StatusMessage"></a>
The job's status message.
Type: String
Required: No

## See Also
<a name="API_PackageImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/PackageImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/PackageImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/PackageImportJob)
