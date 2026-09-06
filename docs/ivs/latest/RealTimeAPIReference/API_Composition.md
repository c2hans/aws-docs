---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Composition.html
---

# Composition
<a name="API_Composition"></a>

Object specifying a Composition resource.

## Contents
<a name="API_Composition_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-Composition-arn"></a>
ARN of the Composition resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:composition/[a-zA-Z0-9-]+`
Required: Yes

 ** destinations **   <a name="ivsrealtimeeapireference-Type-Composition-destinations"></a>
Array of Destination objects. A Composition can contain either one destination (`channel` or `s3`) or two (one `channel` and one `s3`).
Type: Array of [Destination](API_Destination.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** layout **   <a name="ivsrealtimeeapireference-Type-Composition-layout"></a>
Layout object to configure composition parameters.
Type: [LayoutConfiguration](API_LayoutConfiguration.md) object
Required: Yes

 ** stageArn **   <a name="ivsrealtimeeapireference-Type-Composition-stageArn"></a>
ARN of the stage used as input
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** state **   <a name="ivsrealtimeeapireference-Type-Composition-state"></a>
State of the Composition.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | FAILED | STOPPED`
Required: Yes

 ** endTime **   <a name="ivsrealtimeeapireference-Type-Composition-endTime"></a>
UTC time of the Composition end. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** startTime **   <a name="ivsrealtimeeapireference-Type-Composition-startTime"></a>
UTC time of the Composition start. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** tags **   <a name="ivsrealtimeeapireference-Type-Composition-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Composition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/Composition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/Composition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/Composition)
