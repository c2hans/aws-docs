---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_TransportStreamProgram.html
---

# TransportStreamProgram
<a name="API_TransportStreamProgram"></a>

 The metadata of a single transport stream program.

## Contents
<a name="API_TransportStreamProgram_Contents"></a>

 ** pcrPid **   <a name="mediaconnect-Type-TransportStreamProgram-pcrPid"></a>
 The Program Clock Reference (PCR) Packet ID (PID) as it is reported in the Program Association Table.
Type: Integer
Required: Yes

 ** programNumber **   <a name="mediaconnect-Type-TransportStreamProgram-programNumber"></a>
 The program number as it is reported in the Program Association Table.
Type: Integer
Required: Yes

 ** programPid **   <a name="mediaconnect-Type-TransportStreamProgram-programPid"></a>
 The program Packet ID (PID) as it is reported in the Program Association Table.
Type: Integer
Required: Yes

 ** streams **   <a name="mediaconnect-Type-TransportStreamProgram-streams"></a>
 The list of elementary transport streams in the program. The list includes video, audio, and data streams.
Type: Array of [TransportStream](API_TransportStream.md) objects
Required: Yes

 ** programName **   <a name="mediaconnect-Type-TransportStreamProgram-programName"></a>
 The program name as it is reported in the Program Association Table.
Type: String
Required: No

## See Also
<a name="API_TransportStreamProgram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/TransportStreamProgram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/TransportStreamProgram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/TransportStreamProgram)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
