---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_JobLogEventData.html
---

# JobLogEventData
<a name="API_JobLogEventData"></a>

Metadata associated with a Job log.

## Contents
<a name="API_JobLogEventData_Contents"></a>

 ** attemptCount **   <a name="drs-Type-JobLogEventData-attemptCount"></a>
Retries for this operation.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 9.
Required: No

 ** conversionProperties **   <a name="drs-Type-JobLogEventData-conversionProperties"></a>
Properties of a conversion job
Type: [ConversionProperties](API_ConversionProperties.md) object
Required: No

 ** conversionServerID **   <a name="drs-Type-JobLogEventData-conversionServerID"></a>
The ID of a conversion server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** eventResourceData **   <a name="drs-Type-JobLogEventData-eventResourceData"></a>
Properties of resource related to a job event.
Type: [EventResourceData](API_EventResourceData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maxAttemptsCount **   <a name="drs-Type-JobLogEventData-maxAttemptsCount"></a>
The maximum number of retries that will be attempted if this operation failed.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 9.
Required: No

 ** rawError **   <a name="drs-Type-JobLogEventData-rawError"></a>
A string representing a job error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** sourceServerID **   <a name="drs-Type-JobLogEventData-sourceServerID"></a>
The ID of a Source Server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** targetInstanceID **   <a name="drs-Type-JobLogEventData-targetInstanceID"></a>
The ID of a Recovery Instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

## See Also
<a name="API_JobLogEventData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/JobLogEventData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/JobLogEventData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/JobLogEventData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
