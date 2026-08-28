---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneOperationSummary.html
---

# LandingZoneOperationSummary
<a name="API_LandingZoneOperationSummary"></a>

Returns a summary of information about a landing zone operation.

## Contents
<a name="API_LandingZoneOperationSummary_Contents"></a>

 ** operationIdentifier **   <a name="controltower-Type-LandingZoneOperationSummary-operationIdentifier"></a>
The `operationIdentifier` of the landing zone operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** operationType **   <a name="controltower-Type-LandingZoneOperationSummary-operationType"></a>
The type of the landing zone operation.
Type: String
Valid Values: `DELETE | CREATE | UPDATE | RESET`
Required: No

 ** status **   <a name="controltower-Type-LandingZoneOperationSummary-status"></a>
The status of the landing zone operation.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

## See Also
<a name="API_LandingZoneOperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/LandingZoneOperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/LandingZoneOperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/LandingZoneOperationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
