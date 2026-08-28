---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_SoftwareSetSummary.html
---

# SoftwareSetSummary
<a name="API_SoftwareSetSummary"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Describes a software set.

## Contents
<a name="API_SoftwareSetSummary_Contents"></a>

 ** arn **   <a name="workspacesthinclient-Type-SoftwareSetSummary-arn"></a>
The Amazon Resource Name (ARN) of the software set.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+`
Required: No

 ** id **   <a name="workspacesthinclient-Type-SoftwareSetSummary-id"></a>
The ID of the software set.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** releasedAt **   <a name="workspacesthinclient-Type-SoftwareSetSummary-releasedAt"></a>
The timestamp of when the software set was released.
Type: Timestamp
Required: No

 ** supportedUntil **   <a name="workspacesthinclient-Type-SoftwareSetSummary-supportedUntil"></a>
The timestamp of the end of support for the software set.
Type: Timestamp
Required: No

 ** validationStatus **   <a name="workspacesthinclient-Type-SoftwareSetSummary-validationStatus"></a>
An option to define if the software set has been validated.
Type: String
Valid Values: `VALIDATED | NOT_VALIDATED`
Required: No

 ** version **   <a name="workspacesthinclient-Type-SoftwareSetSummary-version"></a>
The version of the software set.
Type: String
Required: No

## See Also
<a name="API_SoftwareSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/SoftwareSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/SoftwareSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/SoftwareSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
