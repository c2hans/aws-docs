---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Standard.html
---

# Standard
<a name="API_Standard"></a>

Provides information about a specific security standard.

## Contents
<a name="API_Standard_Contents"></a>

 ** Description **   <a name="securityhub-Type-Standard-Description"></a>
A description of the standard.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnabledByDefault **   <a name="securityhub-Type-Standard-EnabledByDefault"></a>
Whether the standard is enabled by default. When Security Hub CSPM is enabled from the console, if a standard is enabled by default, the check box for that standard is selected by default.
When Security Hub CSPM is enabled using the `EnableSecurityHub` API operation, the standard is enabled by default unless `EnableDefaultStandards` is set to `false`.
Type: Boolean
Required: No

 ** Name **   <a name="securityhub-Type-Standard-Name"></a>
The name of the standard.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Provider **   <a name="securityhub-Type-Standard-Provider"></a>
The cloud provider whose resources the standard evaluates. For example, `AWS` or `Azure`.
Type: String
Valid Values: `AWS | Azure`
Required: No

 ** StandardsArn **   <a name="securityhub-Type-Standard-StandardsArn"></a>
The ARN of the standard.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StandardsManagedBy **   <a name="securityhub-Type-Standard-StandardsManagedBy"></a>
Provides details about the management of a standard.
Type: [StandardsManagedBy](API_StandardsManagedBy.md) object
Required: No

## See Also
<a name="API_Standard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Standard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Standard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Standard)
