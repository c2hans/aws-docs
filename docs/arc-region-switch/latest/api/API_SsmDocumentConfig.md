---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_SsmDocumentConfig.html
---

# SsmDocumentConfig
<a name="API_SsmDocumentConfig"></a>

The Systems Manager document to run and the managed nodes to target for a single AWS Region.

## Contents
<a name="API_SsmDocumentConfig_Contents"></a>

 ** documentArn **   <a name="regionswitch-Type-SsmDocumentConfig-documentArn"></a>
The Amazon Resource Name (ARN) of the Systems Manager document to run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[a-z0-9\-]+:ssm:[a-z0-9\-]+:([0-9]{12})?:document/[a-zA-Z0-9_.\-]+`
Required: Yes

 ** targets **   <a name="regionswitch-Type-SsmDocumentConfig-targets"></a>
The target filters that Systems Manager resolves to managed nodes when the command runs. To target specific managed nodes, use the `InstanceIds` key. You can specify up to five target filters.
Type: Array of [SsmTarget](API_SsmTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-SsmDocumentConfig-crossAccountRole"></a>
The cross-account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** documentVersion **   <a name="regionswitch-Type-SsmDocumentConfig-documentVersion"></a>
The version of the Systems Manager document to run for this Region. When you omit it, Systems Manager runs the document's default version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `([$]LATEST|[$]DEFAULT|[1-9][0-9]*)`
Required: No

 ** externalId **   <a name="regionswitch-Type-SsmDocumentConfig-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** parameters **   <a name="regionswitch-Type-SsmDocumentConfig-parameters"></a>
The parameters that are passed to this Region's Systems Manager document. You set parameters for each document, so each Region can run its document with its own parameters.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `.{1,65535}`
Required: No

## See Also
<a name="API_SsmDocumentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/SsmDocumentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/SsmDocumentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/SsmDocumentConfig)
