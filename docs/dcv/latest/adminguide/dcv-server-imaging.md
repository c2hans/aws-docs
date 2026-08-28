---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-imaging.html
---

# Amazon DCV server imaging
<a name="dcv-server-imaging"></a>

Counters in this set provide information about the subsystems responsible for screen grabbing, encoding and delivery.

Counters in this set are divided in two groups:
+ For those in the first group, Amazon DCV collects one value for each session and publishes it in the `$session_name` instance.
+ For those in the second group, Amazon DCV collects one value for each encoder in each session. There are three active encoders:
  + one full-frame encoder
  + one tile-based encoder
  + one lossless encoder

  These counters are published in the `$session_name:$encoder_name` instances.

| Counter name | Description | Unit | Instance |
| --- | --- | --- | --- |
| Grabbed Frames/sec | Captured frame rate in frames per second | Count/second | session |
| Grabbed Frames | Total number of captured frames since the session started | Count | session |
| Sent Frames/sec | Rate of screen frames sent per second to the connected client | Count/second | session |
| Dropped Frames/sec | Rate of screen frames that were not sent to the connected client per second | Count/second | session |
| Display Latency ms | Average time in milliseconds between frame capture and presentation | Milliseconds | session |
| Available Bandwidth bits/sec | Estimated bandwidth available in the connection, in bits per second | Bits/second | session |
| Encoded Frames/sec | Rate of screen frames encoded per second | Count/second | session:encoder |
| Encoding Time ms | Average time, in milliseconds, used for encoding one sceeen frame | Milliseconds | session:encoder |
| Encoding Time per Megapixel ms | Average time, in milliseconds, used to encode one million pixels | Milliseconds | session:encoder |
| Frame Quality % | Average frame compression quality, expressed as a percentage | Percent | session:encoder |
| Frame Compression Ratio % | Average frame compression ratio, defined as the ratio between the frame size, in bytes, and the size of the compressed frame | Percent | session:encoder |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
