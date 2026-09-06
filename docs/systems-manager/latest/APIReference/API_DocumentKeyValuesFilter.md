---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentKeyValuesFilter.html
---

# DocumentKeyValuesFilter
<a name="API_DocumentKeyValuesFilter"></a>

One or more filters. Use a filter to return a more specific list of documents.

For keys, you can specify one or more tags that have been applied to a document.

You can also use AWS-provided keys, some of which have specific allowed values. These keys and their associated values are as follows:

DocumentType
+  `ApplicationConfiguration`
+  `ApplicationConfigurationSchema`
+  `Automation`
+  `ChangeCalendar`
+  `Command`
+  `Package`
+  `Policy`
+  `Session`

Owner
Note that only one `Owner` can be specified in a request. For example: `Key=Owner,Values=Self`.
+  `Amazon`
+  `Private`
+  `Public`
+  `Self`
+  `ThirdParty`

PlatformTypes
+  `Linux`
+  `Windows`

 `Name` is another AWS-provided key. If you use `Name` as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with `Te`, run the following command:

 `aws ssm list-documents --filters Key=Name,Values=Te`

You can also use the `TargetType` AWS-provided key. For a list of valid resource type values that can be used with this key, see [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the * AWS CloudFormation User Guide*.

If you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.

To specify a custom key-value pair, use the format `Key=tag:tagName,Values=valueName`.

For example, if you created a key called region and are using the AWS CLI to call the `list-documents` command:

 `aws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self`

## Contents
<a name="API_DocumentKeyValuesFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-DocumentKeyValuesFilter-Key"></a>
The name of the filter key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Values **   <a name="systemsmanager-Type-DocumentKeyValuesFilter-Values"></a>
The value for the filter key.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_DocumentKeyValuesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentKeyValuesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentKeyValuesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentKeyValuesFilter)
