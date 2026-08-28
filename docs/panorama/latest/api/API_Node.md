---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_Node.html
---

# Node
<a name="API_Node"></a>

An application node that represents a camera stream, a model, code, or output.

## Contents
<a name="API_Node_Contents"></a>

 ** Category **   <a name="panorama-Type-Node-Category"></a>
The node's category.
Type: String
Valid Values: `BUSINESS_LOGIC | ML_MODEL | MEDIA_SOURCE | MEDIA_SINK`
Required: Yes

 ** CreatedTime **   <a name="panorama-Type-Node-CreatedTime"></a>
When the node was created.
Type: Timestamp
Required: Yes

 ** Name **   <a name="panorama-Type-Node-Name"></a>
The node's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** NodeId **   <a name="panorama-Type-Node-NodeId"></a>
The node's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** PackageId **   <a name="panorama-Type-Node-PackageId"></a>
The node's package ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`
Required: Yes

 ** PackageName **   <a name="panorama-Type-Node-PackageName"></a>
The node's package name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** PackageVersion **   <a name="panorama-Type-Node-PackageVersion"></a>
The node's package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: Yes

 ** PatchVersion **   <a name="panorama-Type-Node-PatchVersion"></a>
The node's patch version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`
Required: Yes

 ** Description **   <a name="panorama-Type-Node-Description"></a>
The node's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** OwnerAccount **   <a name="panorama-Type-Node-OwnerAccount"></a>
The account ID of the node's owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9a-z\_]+`
Required: No

 ** PackageArn **   <a name="panorama-Type-Node-PackageArn"></a>
The node's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/Node)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
