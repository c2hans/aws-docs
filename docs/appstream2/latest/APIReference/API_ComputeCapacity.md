---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ComputeCapacity.html
---

# ComputeCapacity
<a name="API_ComputeCapacity"></a>

Describes the capacity for a fleet.

## Contents
<a name="API_ComputeCapacity_Contents"></a>

 ** DesiredInstances **   <a name="WorkSpacesApplications-Type-ComputeCapacity-DesiredInstances"></a>
The desired number of streaming instances.
Type: Integer
Required: No

 ** DesiredSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacity-DesiredSessions"></a>
The desired number of user sessions for a multi-session fleet. This is not allowed for single-session fleets.
When you create a fleet, you must set either the DesiredSessions or DesiredInstances attribute, based on the type of fleet you create. You can’t define both attributes or leave both attributes blank.
Type: Integer
Required: No

## See Also
<a name="API_ComputeCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ComputeCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ComputeCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ComputeCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
