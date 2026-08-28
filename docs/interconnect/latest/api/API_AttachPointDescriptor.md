---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_AttachPointDescriptor.html
---

# AttachPointDescriptor
<a name="API_AttachPointDescriptor"></a>

Describes a possible Attach Point for a Connection.

## Contents
<a name="API_AttachPointDescriptor_Contents"></a>

 ** identifier **   <a name="interconnect-Type-AttachPointDescriptor-identifier"></a>
The identifier for the specific type of the AttachPoint.
Type: String
Required: Yes

 ** name **   <a name="interconnect-Type-AttachPointDescriptor-name"></a>
The descriptive name of the identifier attach point.
Type: String
Required: Yes

 ** type **   <a name="interconnect-Type-AttachPointDescriptor-type"></a>
The type of identifier for the AttachPoint, which will dictate the syntax of the identifier.
Current types include:
+ ARN
+ DirectConnect Gateway
Type: String
Valid Values: `DirectConnectGateway`
Required: Yes

## See Also
<a name="API_AttachPointDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/AttachPointDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/AttachPointDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/AttachPointDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
