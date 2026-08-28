---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_AuthParameter.html
---

# AuthParameter
<a name="API_AuthParameter"></a>

Information about required authentication parameters.

## Contents
<a name="API_AuthParameter_Contents"></a>

 ** connectorSuppliedValues **   <a name="appflow-Type-AuthParameter-connectorSuppliedValues"></a>
Contains default values for this authentication parameter that are supplied by the connector.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** description **   <a name="appflow-Type-AuthParameter-description"></a>
A description about the authentication parameter.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

 ** isRequired **   <a name="appflow-Type-AuthParameter-isRequired"></a>
Indicates whether this authentication parameter is required.
Type: Boolean
Required: No

 ** isSensitiveField **   <a name="appflow-Type-AuthParameter-isSensitiveField"></a>
Indicates whether this authentication parameter is a sensitive field.
Type: Boolean
Required: No

 ** key **   <a name="appflow-Type-AuthParameter-key"></a>
The authentication key required to authenticate with the connector.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** label **   <a name="appflow-Type-AuthParameter-label"></a>
Label used for authentication parameter.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `.*`
Required: No

## See Also
<a name="API_AuthParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/AuthParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/AuthParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/AuthParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
