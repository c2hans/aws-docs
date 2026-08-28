---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CapacityAssignmentConfiguration.html
---

# CapacityAssignmentConfiguration
<a name="API_CapacityAssignmentConfiguration"></a>

Assigns Athena workgroups (and hence their queries) to capacity reservations. A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.

## Contents
<a name="API_CapacityAssignmentConfiguration_Contents"></a>

 ** CapacityAssignments **   <a name="athena-Type-CapacityAssignmentConfiguration-CapacityAssignments"></a>
The list of assignments that make up the capacity assignment configuration.
Type: Array of [CapacityAssignment](API_CapacityAssignment.md) objects
Required: No

 ** CapacityReservationName **   <a name="athena-Type-CapacityAssignmentConfiguration-CapacityReservationName"></a>
The name of the reservation that the capacity assignment configuration is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9._-]+`
Required: No

## See Also
<a name="API_CapacityAssignmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CapacityAssignmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CapacityAssignmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CapacityAssignmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
