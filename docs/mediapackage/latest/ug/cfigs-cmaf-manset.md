---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-cmaf-manset.html
---

# Manifest settings fields
<a name="cfigs-cmaf-manset"></a>

Specify the format of the manifest that AWS Elemental MediaPackage delivers from an asset that uses this packaging configuration.

1. (Optional) For **Manifest name**, enter a short string that will be appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, *index*.

1. (Optional) In stream sets with a single video track, select **Include IFrame-only streams** to include an additional I-frame only stream along with the other tracks in the manifest. MediaPackage inserts `EXT-I-FRAMES-ONLY` tags in the manifest, and then compiles and includes an I-frames only playlist in the stream. This playlist enables player functionality like fast forward and rewind.

1. (Optional) Select **Repeat EXT-X-KEY** if you want the service to repeat the key before every segment of the manifest. By default, the key is written just once, after the header and before the segments. If you select **Repeat EXT-X-KEY**, the manifest is written as header, key, segment, key, segment, key, and so on, with every segment preceded by the key. Set this according to the needs of the player. Selecting this option might result in an increase in client requests to the DRM server.

1. (Optional) For **Program date/time interval**, enter the interval at which MediaPackage should insert the `EXT-X-PROGRAM-DATE-TIME` tags in the manifest.

   The `EXT-X-PROGRAM-DATE-TIME` tag synchronizes the stream to the wall clock, enabling functionality like viewer seek in the playback timeline and time display on the player.

1. (Optional) For **Ad markers**, choose how ad markers are included in the packaged content.

   Choose from the following:
   + **None** – Omit all SCTE-35 ad markers from the output.
   + **Passthrough** – Copy the SCTE-35 ad markers directly from the input HLS input stream to the output.
   + **SCTE-35 Enhanced** – Generate ad markers and blackout tags based on the SCTE-35 input messages from the input stream.

1. (Optional) Select **Include encoder configuration in segments**, for MediaPackage to place your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
