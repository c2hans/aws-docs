---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ResourceToImport.html
---

# ResourceToImport
<a name="API_ResourceToImport"></a>

Describes the target resource of an import operation.

## Contents
<a name="API_ResourceToImport_Contents"></a>

 ** LogicalResourceId **
The logical ID of the target resource as specified in the template.
Type: String
Required: Yes

 ** ResourceIdentifier **  ResourceIdentifier.entry.N.key (key)  ResourceIdentifier.entry.N.value (value)
A key-value pair that identifies the target resource. The key is an identifier property (for example, `BucketName` for `AWS::S3::Bucket` resources) and the value is the actual property value (for example, `MyS3Bucket`).
Type: String to string map
Map Entries: Maximum number of 256 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** ResourceType **
The type of resource to import into your stack, such as `AWS::S3::Bucket`. For a list of supported resource types, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) in the * AWS CloudFormation User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ResourceToImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceToImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceToImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceToImport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
