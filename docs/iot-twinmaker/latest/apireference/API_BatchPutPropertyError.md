---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_BatchPutPropertyError.html
---

# BatchPutPropertyError
<a name="API_BatchPutPropertyError"></a>

An error returned by the `BatchPutProperty` action.

## Contents
<a name="API_BatchPutPropertyError_Contents"></a>

 ** entry **   <a name="tm-Type-BatchPutPropertyError-entry"></a>
An object that contains information about errors returned by the `BatchPutProperty` action.
Type: [PropertyValueEntry](API_PropertyValueEntry.md) object
Required: Yes

 ** errorCode **   <a name="tm-Type-BatchPutPropertyError-errorCode"></a>
The error code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** errorMessage **   <a name="tm-Type-BatchPutPropertyError-errorMessage"></a>
The error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_BatchPutPropertyError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/BatchPutPropertyError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/BatchPutPropertyError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/BatchPutPropertyError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
