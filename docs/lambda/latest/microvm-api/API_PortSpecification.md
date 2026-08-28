---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_PortSpecification.html
---

# PortSpecification
<a name="API_PortSpecification"></a>

Specifies which ports are accessible on a MicroVM. Only one of the port specification options can be set.

## Contents
<a name="API_PortSpecification_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** allPorts **   <a name="lambdamicrovm-Type-PortSpecification-allPorts"></a>
Indicates that all ports are accessible.
Type: Structure
Required: No

 ** port **   <a name="lambdamicrovm-Type-PortSpecification-port"></a>
A single port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** range **   <a name="lambdamicrovm-Type-PortSpecification-range"></a>
A range of ports.
Type: [PortRange](API_PortRange.md) object
Required: No

## See Also
<a name="API_PortSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/PortSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/PortSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/PortSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
