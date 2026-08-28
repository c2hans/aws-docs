---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CompositionSummary.html
---

# CompositionSummary
<a name="API_CompositionSummary"></a>

Summary information about a Composition.

## Contents
<a name="API_CompositionSummary_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-arn"></a>
ARN of the Composition resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:composition/[a-zA-Z0-9-]+`
Required: Yes

 ** destinations **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-destinations"></a>
Array of Destination objects.
Type: Array of [DestinationSummary](API_DestinationSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** stageArn **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-stageArn"></a>
ARN of the attached stage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** state **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-state"></a>
State of the Composition resource.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | FAILED | STOPPED`
Required: Yes

 ** endTime **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-endTime"></a>
UTC time of the Composition end. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** startTime **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-startTime"></a>
UTC time of the Composition start. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** tags **   <a name="ivsrealtimeeapireference-Type-CompositionSummary-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CompositionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CompositionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CompositionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CompositionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
