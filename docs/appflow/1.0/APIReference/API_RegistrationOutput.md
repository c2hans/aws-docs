---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_RegistrationOutput.html
---

# RegistrationOutput
<a name="API_RegistrationOutput"></a>

Describes the status of an attempt from Amazon AppFlow to register a resource.

When you run a flow that you've configured to use a metadata catalog, Amazon AppFlow registers a metadata table and data partitions with that catalog. This operation provides the status of that registration attempt. The operation also indicates how many related resources Amazon AppFlow created or updated.

## Contents
<a name="API_RegistrationOutput_Contents"></a>

 ** message **   <a name="appflow-Type-RegistrationOutput-message"></a>
Explains the status of the registration attempt from Amazon AppFlow. If the attempt fails, the message explains why.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

 ** result **   <a name="appflow-Type-RegistrationOutput-result"></a>
Indicates the number of resources that Amazon AppFlow created or updated. Possible resources include metadata tables and data partitions.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

 ** status **   <a name="appflow-Type-RegistrationOutput-status"></a>
Indicates the status of the registration attempt from Amazon AppFlow.
Type: String
Valid Values: `InProgress | Successful | Error | CancelStarted | Canceled`
Required: No

## See Also
<a name="API_RegistrationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/RegistrationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/RegistrationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/RegistrationOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
