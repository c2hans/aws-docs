---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CodeSigning.html
---

# CodeSigning
<a name="API_CodeSigning"></a>

Describes the method to use when code signing a file.

## Contents
<a name="API_CodeSigning_Contents"></a>

 ** awsSignerJobId **   <a name="iot-Type-CodeSigning-awsSignerJobId"></a>
The ID of the `AWSSignerJob` which was created to sign the file.
Type: String
Required: No

 ** customCodeSigning **   <a name="iot-Type-CodeSigning-customCodeSigning"></a>
A custom method for code signing a file.
Type: [CustomCodeSigning](API_CustomCodeSigning.md) object
Required: No

 ** startSigningJobParameter **   <a name="iot-Type-CodeSigning-startSigningJobParameter"></a>
Describes the code-signing job.
Type: [StartSigningJobParameter](API_StartSigningJobParameter.md) object
Required: No

## See Also
<a name="API_CodeSigning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CodeSigning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CodeSigning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CodeSigning)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
