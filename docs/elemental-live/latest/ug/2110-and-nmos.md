---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/2110-and-nmos.html
---

# Support for NMOS IS-04 stream discovery
<a name="2110-and-nmos"></a>

Elemental Live supports NMOS IS-04 with both SMPTE 2110 inputs and outputs.

**Note**
Currently, Elemental Live supports management of SMPTE 2110 streams using NMOS. Elemental Live doesn't support management of other types of streams.

**SMPTE 2110 with NMOS**

An NMOS solution includes an NMOS controller and an optional NMOS registry. If your solution includes a registry, you configure Elemental Live to communicate with that registry. If your solution doesn't include a registry, you must configure your NMOS controller to query Elemental Live
+ Information about the SMPTE 2110 streams, including a unique ID for each stream.
+ Information about the available *senders* and *receivers*. For a stream that Elemental Live outputs, Elemental Live is the sender. For a stream that Elemental Live ingests, it is the receiver.

**SMPTE 2110 without NMOS**

If you don't set up an NMOS solution, you still use SDP files:
+ For a SMPTE 2110 input, you must identify the server where the SDP files are stored. This can be any HTTP server. When you configure the input, you specify which SDP files contain information about the SMPTE 2110 stream.
+ For a SMPTE 2110 output, Elemental Live automatically creates the applicable SDP files. You must make these files accessible to the downstream system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
