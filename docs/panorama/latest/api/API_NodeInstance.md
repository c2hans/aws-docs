---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NodeInstance.html
---

# NodeInstance
<a name="API_NodeInstance"></a>

A node instance.

## Contents
<a name="API_NodeInstance_Contents"></a>

 ** CurrentStatus **   <a name="panorama-Type-NodeInstance-CurrentStatus"></a>
The instance's current status.
Type: String
Valid Values: `RUNNING | ERROR | NOT_AVAILABLE | PAUSED`
Required: Yes

 ** NodeInstanceId **   <a name="panorama-Type-NodeInstance-NodeInstanceId"></a>
The instance's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** NodeId **   <a name="panorama-Type-NodeInstance-NodeId"></a>
The node's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: No

 ** NodeName **   <a name="panorama-Type-NodeInstance-NodeName"></a>
The instance's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** PackageName **   <a name="panorama-Type-NodeInstance-PackageName"></a>
The instance's package name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** PackagePatchVersion **   <a name="panorama-Type-NodeInstance-PackagePatchVersion"></a>
The instance's package patch version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`
Required: No

 ** PackageVersion **   <a name="panorama-Type-NodeInstance-PackageVersion"></a>
The instance's package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: No

## See Also
<a name="API_NodeInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NodeInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NodeInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NodeInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
